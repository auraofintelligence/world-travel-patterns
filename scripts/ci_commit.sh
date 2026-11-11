#!/usr/bin/env bash
# Commit step shared by the scheduled GitHub Actions.
#
#   bash scripts/ci_commit.sh "Daily feeds" data/feeds
#
# Other lanes (Claude, Codex, Grok, Luke) push to main all day, so this step:
#   1. commits the job's own data paths plus every generated file (queue, site/data, sitemap.xml, llms.txt);
#   2. rebases onto the newest main (on a clash inside the same lines, the job's fresh data wins);
#   3. regenerates the generated files on top of everyone's data, so they never go stale;
#   4. validates, pushes, and retries up to four times if main moved again.
set -euo pipefail
msg="$1"; shift
GEN=(queue site/data sitemap.xml llms.txt)

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

git add -- "$@" "${GEN[@]}"
if git diff --cached --quiet; then
  echo "Nothing changed."
  exit 0
fi
git commit -q -m "$msg"

for attempt in 1 2 3 4; do
  git fetch -q origin main
  if git rebase -q --autostash -X theirs origin/main; then
    python scripts/due.py > /dev/null
    python scripts/build_site.py > /dev/null
    git add -- "${GEN[@]}"
    git diff --cached --quiet || git commit -q --amend --no-edit
    python scripts/validate.py
    if git push -q origin HEAD:main; then
      echo "Pushed on attempt $attempt."
      exit 0
    fi
  else
    git rebase --abort || true
  fi
  sleep $((attempt * 20))
done
echo "::error::Could not push after 4 attempts."
exit 1
