/* World Travel Patterns website. Reads the repo's own data; never reads private/. */
(() => {
  "use strict";

  const PAGES = [
    ["index.html", "Home", "home"],
    ["places.html", "Places", "places"],
    ["patterns.html", "Patterns", "patterns"],
    ["upcoming.html", "Upcoming", "upcoming"],
    ["advisories.html", "Advisories", "advisories"],
    ["queue.html", "Queue", "queue"],
    ["how.html", "How it works", "how"],
    ["site-map.html", "Site map", "site-map"],
  ];
  const REPO = "https://github.com/auraofintelligence/world-travel-patterns";
  const KIND_LABEL = {
    country: "Country", territory: "Territory", associated: "Associated state", jurisdiction: "Separately travelled jurisdiction",
    state: "State", district: "Council or ward", electorate: "Electorate", region: "Region", island: "Island",
    "island-group": "Island group", nation: "Nation", zone: "Permit zone", city: "City", site: "Site",
  };
  const SOURCE_KIND = {
    council: "Council", ward: "Ward or division", "unincorporated-area": "Unincorporated area", "special-local-body": "Special local body",
    "federal-division": "Federal division", "state-district": "State electoral district", "state-region": "State electoral region",
    "senate-area": "Senate area", "statewide-upper-house": "Statewide upper house",
  };
  const kindOf = (p) => SOURCE_KIND[p.sk] || KIND_LABEL[p.kind] || p.kind;
  const TAG_LABEL = {
    home: "Home", "oceania": "Oceania", "first-nations": "First Nations",
    aura: "Aura", music: "Music", books: "Books", founder: "Founder",
  };
  const LAYERS = [
    ["permission", "Permission", ["entry", "activities", "health-entry", "zone-requirements"]],
    ["law", "Local law", ["local-law"]],
    ["culture", "Culture and protocol", ["culture-and-protocol", "culture-cycles"]],
    ["relationships", "Affection and relationships", ["affection-and-relationships"]],
    ["cycles", "The year here", ["seasons-and-flow", "year-ahead"]],
    ["practical", "Practical", ["consular", "money-and-cost"]],
    ["purpose", "Works and purpose", ["works-and-purpose"]],
  ];
  const AREA_LABEL = { "in-public": "In public", "in-private": "In private", "marriage-and-partnership": "Marriage and partnership", changing: "Changing" };
  const REASON_LABEL = {
    "never-checked": "never checked", imported: "carried from the earlier atlas", "over-budget": "past its recheck age",
    watch: "rule change watched", "source-dead": "source page gone", "source-changed": "source page changed",
  };

  const esc = (v) => String(v ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  const longMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  const fmt = (iso) => {
    if (!iso) return "";
    const [y, m, d] = iso.slice(0, 10).split("-").map(Number);
    return d ? `${d} ${months[m - 1]} ${y}` : `${longMonths[m - 1]} ${y}`;
  };
  const today = () => {
    const b = new Date(Date.now() + 10 * 3600 * 1000);
    return b.toISOString().slice(0, 10);
  };
  const days = (a, b) => Math.round((Date.parse(b) - Date.parse(a)) / 86400000);
  const num = (n) => Number(n || 0).toLocaleString("en-AU");
  const vetPath = (id) => `data/vetting/${id.replace(/\//g, "__")}.json`;

  async function json(path, fallback) {
    try {
      const r = await fetch(path, { cache: "no-cache" });
      if (!r.ok) return fallback;
      return await r.json();
    } catch {
      return fallback;
    }
  }
  async function jsonl(path) {
    try {
      const r = await fetch(path, { cache: "no-cache" });
      if (!r.ok) return [];
      return (await r.text()).split("\n").filter(Boolean).map((l) => JSON.parse(l));
    } catch {
      return [];
    }
  }

  const levelClass = (level) => {
    const l = (level || "").toLowerCase();
    if (l.startsWith("do not")) return "lvl-do-not-travel";
    if (l.startsWith("reconsider")) return "lvl-reconsider";
    if (l.includes("high degree")) return "lvl-high-caution";
    if (l.includes("normal")) return "lvl-normal";
    return "lvl-none";
  };

  /* Shell */
  function shell(page) {
    const nav = document.createElement("nav");
    nav.className = "nav";
    nav.setAttribute("aria-label", "Site");
    nav.innerHTML = `<a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true"></span>World Travel Patterns</a>
      <div class="nav-links">${PAGES.slice(1).filter(([, , key]) => !["queue", "site-map"].includes(key)).map(([href, label, key]) =>
        `<a href="${href}"${key === page || (page === "place" && key === "places") ? ' aria-current="page"' : ""}>${label}</a>`).join("")}</div>`;
    document.body.prepend(nav);
    const footer = document.createElement("footer");
    footer.innerHTML = `<div class="section"><span>🤝🔷 A Luke × Claude build · Strange But True Public Source Licence</span>
      <span>A planning aid, not legal advice. A level marked "not yet checked" has unknown rules, not no rules.</span>
      <span><a href="site-map.html">Site map</a> · <a href="how.html">How it works</a> · <a href="queue.html">Queue</a> · <a href="${REPO}">Source on GitHub</a></span></div>`;
    document.body.append(footer);
  }

  function hero(credits, key, { kicker, title, lede, actions = "", extra = "", photo = undefined, caption = "" }) {
    const c = photo === undefined ? credits[key] || {} : photo || {};
    const src = c.src || (c.file ? `site/heroes/${c.file}` : "");
    const by = c.artist ? `Photo: ${esc(c.artist)}, <a href="${esc(c.licence_url || c.source)}">${esc(c.licence)}</a>, via <a href="${esc(c.source)}">Wikimedia Commons</a>` : "";
    const shape = !src ? " no-photo" : c.shape === "banner" ? " banner" : "";
    return `<header class="hero${shape}">
      ${src ? `<img class="hero-img" src="${esc(src)}" alt="${esc(c.alt)}" style="object-position:${esc(c.position || "50% 50%")}">` : ""}
      <div class="hero-inner">
        ${kicker ? `<div class="kicker">${kicker}</div>` : ""}
        <h1>${title}</h1>
        ${lede ? `<p class="lede">${lede}</p>` : ""}
        ${actions ? `<div class="actions">${actions}</div>` : ""}
        ${extra}
      </div>
      ${by ? `<p class="credit">${esc(c.alt)}.${caption ? ` ${caption}` : ""} ${by}</p>` : caption ? `<p class="credit">${caption}</p>` : ""}
    </header>`;
  }

  function freshBar(fresh, due, total) {
    const f = total ? (fresh / total) * 100 : 0;
    const d = total ? (due / total) * 100 : 0;
    return `<div class="fresh-bar" role="img" aria-label="${fresh} current, ${due} due, ${total - fresh - due} not yet checked"><i class="f" style="width:${f}%"></i><i class="d" style="width:${d}%"></i></div>`;
  }

  function placeCard(p) {
    const due = Object.keys(p.due || {}).length;
    const fresh = p.fresh || 0;
    const records = p.records || 0;
    const total = p.applicable || 0;
    const tags = (p.tags || []).map((t) => `<span class="chip gold">${esc(TAG_LABEL[t] || t)}</span>`).join("");
    return `<a class="card" href="place.html?id=${encodeURIComponent(p.id)}">
      <h3>${esc(p.name)}</h3>
      <div class="meta">${esc(kindOf(p))}${p.children ? ` · ${num(p.children)} inside` : ""}</div>
      <div class="chips" style="margin-top:10px">${p.zone ? '<span class="chip coral">Permit zone scan</span>' : ""}${tags}</div>
      <div class="mini-bar" aria-hidden="true"><i style="width:${total ? (fresh / total) * 100 : 0}%;background:var(--fresh)"></i><i style="width:${total ? ((records - fresh) / total) * 100 : 0}%;background:var(--due)"></i></div>
      <div class="meta" style="margin-top:6px">${total ? `${records} of ${total} patterns on record${due ? `, ${due} due` : ""}` : "Inherits from the levels above"}</div>
    </a>`;
  }

  /* Pages */
  const render = {};

  const norm = (s) => String(s || "").normalize("NFKD").replace(/[̀-ͯ]/g, "").toLowerCase();
  const findPlaces = (index, term) => {
    const t = norm(term.trim());
    if (!t) return [];
    return index.places.filter((p) => norm(p.name).includes(t) || (p.aliases || []).some((a) => norm(a).includes(t)))
      .sort((a, b) => (norm(b.name).startsWith(t) - norm(a.name).startsWith(t)) || (a.id.includes("/") - b.id.includes("/")) || a.name.localeCompare(b.name));
  };
  const placeLine = (index, p) => {
    const parent = p.id.includes("/") ? index.byId[p.id.split("/")[0]] : null;
    return `<a href="place.html?id=${encodeURIComponent(p.id)}"><b>${esc(p.name)}</b><span>${esc(kindOf(p))}${parent ? `, ${esc(parent.name)}` : ""}</span></a>`;
  };
  const LOOKUP = [
    ["Getting in", "Visa or visa-free stay, health entry rules, and what each kind of trip needs: holiday, meetings, speaking, teaching, filming, research or volunteering."],
    ["Local law", "Rules a visitor can break without knowing: drugs and medicines, alcohol, dress, photography, wildlife, driving and money limits, at every level from country to council."],
    ["Culture and protocol", "Each place's own published guidance and names, sacred or restricted places, and who to ask where nothing is published."],
    ["Affection and relationships", "Affection in public, couples in private, how marriages and partnerships are recognised, and what's changing, for every couple, marked as law or custom."],
    ["Permit zones", "Land council permits, community consent, visitor caps, guides, fees and seasonal closures inside a place, with lead times."],
    ["The year here", "Wet and dry seasons, cyclone and storm months, busy and quiet months, festivals, fasting months and public holidays."],
    ["Help and money", "The nearest Australian embassy or consulate, the place's own offices in Australia, currency and cash limits."],
  ];
  const PICKS = ["nz", "fj", "vu", "ws", "to", "id", "jp", "th", "sg", "us", "gb", "fr", "au/minjerribah"];

  render.home = async (ctx) => {
    const { index, credits } = ctx;
    const [adv, changes] = await Promise.all([
      json("data/advisories.json", { destinations: {} }), index.has_change_log ? jsonl("data/logs/advisory-changes.jsonl") : [],
    ]);
    setTimeout(() => wireHomeSearch(index), 0);
    const levels = {};
    Object.values(adv.destinations).forEach((d) => { const l = d.level || "No level"; levels[l] = (levels[l] || 0) + 1; });
    const picks = PICKS.map((id) => index.byId[id]).filter(Boolean);
    return hero(credits, "home", {
      title: "Where are you going?",
      lede: "Entry rules, local law, culture, the seasons and festivals, and who to call: for every place an Australian passport holder might visit.",
      extra: `<div class="home-search"><input class="search" id="hq" type="search" autocomplete="off" placeholder="A country, island, city or region: Fiji, Rapa Nui, Bali…" aria-label="Search places" aria-controls="hres"><div class="home-results" id="hres" role="listbox"></div></div>`,
    }) + `<main>
      <section class="section"><h2>What each place page tells you</h2>
        <div class="grid wide">${LOOKUP.map(([t, d]) => `<div class="card"><h3>${t}</h3><p class="meta">${d}</p></div>`).join("")}</div>
        <p class="note" style="margin-top:22px">Rules stack: a visitor on Minjerribah is bound by Australian, Queensland and Redland City law together, and the place page shows each level. A level marked "not yet checked" has unknown rules, not no rules.</p></section>
      <section class="section tight"><h2>Start with</h2><div class="grid">${picks.map((p) => `<a class="card" href="place.html?id=${encodeURIComponent(p.id)}"><h3>${esc(p.name)}</h3><div class="meta">${esc(kindOf(p))}${p.id.includes("/") ? `, ${esc(index.byId[p.id.split("/")[0]]?.name || "")}` : p.region ? `, ${esc(p.region)}` : ""}</div></a>`).join("")}</div>
        <p style="margin-top:16px"><a class="btn ghost" href="places.html">Every place, by region</a></p></section>
      <section class="section band"><div class="two">
        <div><h2>Travel advice today</h2><p class="meta">Smartraveller's advice levels, checked daily${adv.checked_on ? `, last on ${fmt(adv.checked_on)}` : ""}.</p>
          ${Object.entries(levels).sort((a, b) => b[1] - a[1]).map(([l, n]) => `<p><span class="adv ${levelClass(l)}">${esc(l)}</span> ${num(n)} destination${n === 1 ? "" : "s"}</p>`).join("")}
          <p><a href="advisories.html">Every destination's level</a></p></div>
        <div><h2>Recent changes</h2>
          ${changes.slice(-6).reverse().map((c) => `<p><span class="adv ${levelClass(c.to)}">${esc(c.destination)}</span> ${esc(c.from)} → ${esc(c.to)} <span class="meta">(${fmt(c.date)})</span></p>`).join("") || `<p class="empty">No level changes since tracking began${adv.checked_on ? ` on ${fmt(adv.checked_on)}` : ""}.</p>`}
        </div></div></section>
    </main>`;
  };

  function wireHomeSearch(index) {
    const q = document.getElementById("hq");
    const box = document.getElementById("hres");
    if (!q) return;
    const draw = () => {
      const hits = findPlaces(index, q.value).slice(0, 8);
      box.innerHTML = hits.map((p) => placeLine(index, p)).join("") + (q.value.trim() ? `<a class="all" href="places.html?q=${encodeURIComponent(q.value.trim())}">${hits.length ? "All matches" : "No match yet: search every place"}</a>` : "");
      box.classList.toggle("open", !!q.value.trim());
    };
    q.addEventListener("input", draw);
    q.addEventListener("keydown", (e) => {
      if (e.key !== "Enter") return;
      const first = box.querySelector("a");
      if (first) location.href = first.href;
    });
  }

  function eventCard(index) {
    return (e) => {
      const d = e.closes || e.starts || "";
      const [y, m, dd] = d.split("-");
      const place = e.place && index.byId[e.place];
      const link = place ? `<a href="place.html?id=${encodeURIComponent(place.id)}">${esc(place.name)}</a>` : e.bloc ? "European Union" : "Online or global";
      return `<div class="card event" style="margin-bottom:12px">
        <div class="date-block ${e.kind === "door" ? "door" : ""}"><span>${e.kind === "door" ? "Closes" : "From"}</span><b>${dd ? Number(dd) : "·"}</b><span>${m ? months[Number(m) - 1] : ""} ${y || ""}</span></div>
        <div><h3 style="font-size:1.08rem;margin-bottom:6px">${e.source_url ? `<a href="${esc(e.source_url)}" rel="noopener">${esc(e.title)}</a>` : esc(e.title)}</h3>
          <div class="chips">${e.kind === "door" ? '<span class="chip gold">Open door</span>' : '<span class="chip sky">Event</span>'}<span class="chip">${link}</span></div>
          <p class="meta" style="margin:8px 0 0">${esc(e.when_text || "")}${e.where ? ` · ${esc(e.where)}` : ""}</p></div></div>`;
    };
  }

  render.places = async (ctx) => {
    const { index, credits } = ctx;
    setTimeout(() => wirePlaces(index), 0);
    return hero(credits, "places", {
      kicker: `${num(index.counts.places)} places`,
      title: "Islands within islands",
      lede: "Every country and territory, and beneath them the states, councils, islands, nations and permit zones that each carry their own rules.",
    }) + `<main><section class="section">
      <div class="toolbar"><input class="search" id="q" type="search" placeholder="Search any place: Rapa Nui, Redland City, Bougainville…" aria-label="Search places">
      </div>
      <div class="toolbar" id="filters">
        ${[["spine", "Countries and territories"], ["oceania", "Oceania"], ["native", "First Nations"], ["home", "Home"], ["zones", "Permit zones"], ["records", "Has records"], ["all", "Everything"]]
          .map(([k, l], i) => `<button class="filter" data-f="${k}" aria-pressed="${i === 0}">${l}</button>`).join("")}
      </div>
      <p class="meta" id="count"></p>
      <div id="results"></div>
    </section></main>`;
  };

  function wirePlaces(index) {
    const q = document.getElementById("q");
    const results = document.getElementById("results");
    const count = document.getElementById("count");
    let filter = "spine";
    const tests = {
      spine: (p) => !p.id.includes("/"),
      oceania: (p) => (p.tags || []).includes("oceania"),
      native: (p) => (p.tags || []).includes("first-nations"),
      home: (p) => (p.tags || []).includes("home"),
      zones: (p) => p.zone,
      records: (p) => p.records > 0,
      all: () => true,
    };
    q.value = new URLSearchParams(location.search).get("q") || "";
    function draw() {
      const term = norm(q.value.trim());
      let list = index.places.filter((p) => !p.overlay || term);
      list = term ? list.filter((p) => norm(p.name).includes(term) || (p.aliases || []).some((a) => norm(a).includes(term))) : list.filter(tests[filter]);
      list.sort((a, b) => (a.id.includes("/") - b.id.includes("/")) || a.name.localeCompare(b.name));
      const grouped = !term && filter === "spine";
      const shown = grouped ? list : list.slice(0, 240);
      count.textContent = `${num(list.length)} places${list.length > shown.length ? `, showing the first ${shown.length}: search to narrow` : ""}`;
      if (grouped) {
        const groups = {};
        shown.forEach((p) => { (groups[p.region || ((p.tags || []).includes("oceania") ? "Pacific" : "More places")] ||= []).push(p); });
        const order = ["Pacific", "Asia", "Middle East", "Africa", "Europe", "Americas", "More places"];
        results.innerHTML = order.filter((g) => groups[g]).map((g) => `<h2 class="month-head">${g} <span class="meta">${groups[g].length}</span></h2><div class="grid">${groups[g].map(placeCard).join("")}</div>`).join("");
      } else {
        results.innerHTML = `<div class="grid">${shown.map(placeCard).join("")}</div>`;
      }
    }
    document.getElementById("filters").addEventListener("click", (e) => {
      const b = e.target.closest("button");
      if (!b) return;
      filter = b.dataset.f;
      document.querySelectorAll("#filters button").forEach((x) => x.setAttribute("aria-pressed", x === b));
      q.value = "";
      draw();
    });
    q.addEventListener("input", draw);
    draw();
  }

  render.place = async (ctx) => {
    const { index, credits } = ctx;
    const id = new URLSearchParams(location.search).get("id") || "au/minjerribah";
    const place = index.byId[id];
    if (!place) return hero(credits, "place", { title: "Place not found", lede: `No place has the id “${esc(id)}”. <a href="places.html" style="color:#fff">Search the places</a>.` });
    document.title = `${place.name} · World Travel Patterns`;
    const chain = [];
    for (let p = place; p; p = p.parent && index.byId[p.parent]) chain.push(p);
    const children = index.places.filter((p) => p.parent === id);
    const descendants = [];
    const stack = [...children];
    while (stack.length) { const c = stack.pop(); descendants.push(c); stack.push(...index.places.filter((p) => p.parent === c.id)); }
    const ids = [...new Set([...chain, ...descendants.filter((d) => d.zone)].map((p) => p.id))];
    const vets = Object.fromEntries(await Promise.all(ids.map(async (pid) => [pid, index.byId[pid].vetted ? (await json(vetPath(pid), { patterns: {} })).patterns : {}])));
    const [adv, feed, watch, photoFile, inAus, lawRepos] = await Promise.all([
      json("data/advisories.json", { destinations: {} }), json("data/feeds/gajra-ahead.json", { events: [] }), json("data/watch.json", { items: [] }),
      json("site/data/place-photos.json", { photos: {} }), json("data/missions/in-australia.json", { places: {} }), json("data/law-repositories.json", { places: {} }),
    ]);
    // A photo OF this place, or of somewhere inside it (labelled), or none. Never a stand-in from elsewhere.
    let photo = photoFile.photos[id] || null;
    let caption = "";
    if (!photo) {
      const inside = descendants.filter((d) => photoFile.photos[d.id]).sort((a, b) => (b.tags || []).length - (a.tags || []).length)[0];
      if (inside) {
        photo = photoFile.photos[inside.id];
        caption = `A photo from <a href="place.html?id=${encodeURIComponent(inside.id)}">${esc(inside.name)}</a>, inside ${esc(place.name)}.`;
      } else {
        caption = `No photograph of ${esc(place.name)} has been chosen yet.`;
      }
    }
    const spine = chain[chain.length - 1];
    const offices = inAus.places[spine.id] || [];
    // Where each level's law is officially published, from the place up to the country, plus shared repositories (EU, PacLII).
    const lawLevels = [...chain].reverse().map((p) => [p, lawRepos.places[p.id] || []]).filter(([, l]) => l.length);
    (lawRepos.groups || []).forEach((g) => { if (g.members.includes(spine.id)) lawLevels.push([{ name: g.name }, g.repositories]); });
    const advice = spine.smartraveller && adv.destinations[spine.smartraveller];
    const patterns = Object.fromEntries(index.patterns.map((p) => [p.id, p]));
    const applies = (pat, p) => pat.applies_to.includes(p.kind) && !(pat.only_tagged && !(p.tags || []).length) && !(pat.skip_home && p.id === "au");
    const now = today();

    function resolve(pid, pat) {
      const ch = [];
      for (let p = index.byId[pid]; p; p = p.parent && index.byId[p.parent]) ch.push(p);
      if (pat.inherit === "none") return [[ch[0], vets[pid]?.[pat.id]]];
      if (pat.inherit === "nearest") {
        const hit = ch.find((p) => vets[p.id]?.[pat.id]);
        if (hit) return [[hit, vets[hit.id][pat.id]]];
        const gap = ch.find((p) => applies(pat, p));
        return gap ? [[gap, null]] : [];
      }
      return ch.slice().reverse().filter((p) => applies(pat, p)).map((p) => [p, vets[p.id]?.[pat.id]]);
    }
    let gaps = 0;
    function levelRow(p, rec, pat) {
      if (!rec) { gaps++; return `<li style="--c:var(--never)"><span class="lvl">${esc(p.name)}</span><span class="gap">not yet checked</span></li>`; }
      const due = index.byId[p.id]?.due?.[pat.id];
      const age = rec.checked ? days(rec.checked, now) : null;
      const colour = due ? "var(--due)" : "var(--fresh)";
      const text = rec.summary || rec.status;
      let body = `<li style="--c:${colour}"><span class="lvl">${esc(p.name)}</span><span class="chip ${due ? "gold" : "teal"}">${esc(rec.status)}</span>
        <span class="meta"> checked ${fmt(rec.checked)}${age !== null ? ` (${age} days ago)` : ""}${due ? ` · ${esc(REASON_LABEL[due] || due)}` : ""}</span>`;
      if (pat.id === "activities") {
        const acts = rec.activities || {};
        body += `<div class="acts">${pat.activities.map((a) => {
          const x = acts[a];
          if (!x) { gaps++; return `<div class="act"><b>${esc(a.replace(/-/g, " "))}</b><span class="gap">not yet checked</span></div>`; }
          return `<div class="act ${esc(x.status)}" title="${esc(x.detail || "")}"><b>${esc(a.replace(/-/g, " "))}</b>${esc(x.status)} · ${esc(x.route || "")}</div>`;
        }).join("")}</div>`;
      } else if (text && text !== rec.status) {
        body += `<div class="detail">${esc(text)}</div>`;
      }
      (rec.laws || []).forEach((l) => { body += `<div class="detail"><b>${esc(l.topic)}:</b> ${esc(l.rule)}</div>`; });
      (rec.items || []).forEach((it) => { body += `<div class="detail"><b>${esc(AREA_LABEL[it.area] || it.area)}</b> <span class="chip">${esc(it.kind)}</span> ${esc(it.text)}</div>`; });
      (rec.layers || []).forEach((l) => { body += `<div class="detail"><b>${esc(l.type)}:</b> ${esc(l.process)} (${esc(l.authority)})${l.lead_time_days ? `, lead time ${l.lead_time_days} days` : ""}</div>`; });
      if (rec.pre_arrival) body += `<div class="detail"><b>Before arrival:</b> ${esc(rec.pre_arrival)}</div>`;
      [["max_stay", "Stay"], ["passport_validity", "Passport"], ["other", "Also"], ["mission", "Office"], ["notes", "Note"], ["currency", "Currency"],
       ["cash_card_notes", "Cash and cards"], ["own_names", "Own names"], ["sacred_or_restricted_places", "Sacred and restricted places"],
       ["dress_and_conduct", "Dress and conduct"], ["cultural_authority", "Who to ask"], ["required", "Required"], ["conditional", "Depends on route"], ["note", "Note"]]
        .forEach(([k, label]) => { if (rec[k] && (!Array.isArray(rec[k]) || rec[k].length)) body += `<div class="detail"><b>${label}:</b> ${esc(Array.isArray(rec[k]) ? rec[k].join("; ") : rec[k])}</div>`; });
      [["closures", "Closures"], ["moving_calendars", "Moving calendars"], ["festivals", "Festivals"], ["public_holidays", "Public holidays"]]
        .forEach(([k, label]) => { const v = rec[k]; if (v && (!Array.isArray(v) || v.length)) body += `<div class="detail"><b>${label}:</b> ${esc(Array.isArray(v) ? v.map((x) => (typeof x === "string" ? x : x.what)).join("; ") : v)}</div>`; });
      if (rec.months?.length) {
        const M = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
        body += `<div class="months">${rec.months.map((m) => `<div class="mo${m.hazard ? " hz" : ""}" title="${esc([m.season, m.hazard && "Hazard: " + m.hazard, m.visitor_flow && "Visitors: " + m.visitor_flow].filter(Boolean).join(". "))}">
          <b>${M[m.month - 1]}</b><span>${esc((m.season || "").split(" (")[0])}</span>${m.hazard ? `<i>${esc(m.hazard.split(" (")[0])}</i>` : ""}${m.visitor_flow ? `<em>${esc((m.visitor_flow.match(/^[\d,]+/) || [m.visitor_flow.split(" ").slice(0, 3).join(" ")])[0])}${/^[\d,]+ (air )?visitors/.test(m.visitor_flow) ? " visitors" : ""}</em>` : ""}</div>`).join("")}</div>`;
      }
      (rec.events || []).forEach((e) => { body += `<div class="detail"><b>${esc(e.date)}${e.end ? " to " + esc(e.end) : ""}:</b> ${esc(e.what)}</div>`; });
      if (rec.sources?.length) body += `<div class="detail meta">Sources: ${rec.sources.slice(0, 4).map((s) => `<a href="${esc(s.url)}" rel="noopener">${esc(s.authority || s.title || "source")}</a>`).join(" · ")}${rec.sources.length > 4 ? ` and ${rec.sources.length - 4} more` : ""}</div>`;
      return body + "</li>";
    }
    function patternCard(pat) {
      const rows = pat.id === "zone-requirements"
        ? [...new Map([id, ...descendants.filter((d) => d.zone).map((d) => d.id)].flatMap((z) => resolve(z, pat)).map(([p, r]) => [p.id, [p, r]])).values()]
        : resolve(id, pat);
      if (!rows.length) return "";
      return `<div class="card pattern-card"><h3>${esc(pat.name)} <span class="chip">${pat.inherit === "stack" ? "stacks across levels" : pat.inherit === "nearest" ? "nearest level" : "this place only"}</span></h3>
        <p class="q">${esc(pat.question)}</p><ul class="levels">${rows.map(([p, r]) => levelRow(p, r, pat)).join("")}</ul></div>`;
    }
    const sections = LAYERS.map(([key, label, ids]) => {
      const cards = ids.map((pid) => patterns[pid]).filter(Boolean).map(patternCard).join("");
      return cards ? `<div class="layer-group"><h2>${label}</h2><span class="rule"></span></div>${cards}` : "";
    }).join("");

    const chainIds = new Set([...chain, ...descendants].map((p) => p.id));
    const events = feed.events.filter((e) => (chainIds.has(e.place) || (e.members || []).includes(spine.id)) && (e.closes || e.ends || e.starts || "") >= now);
    const watched = watch.items.filter((w) => w.status !== "resolved" && (w.places.includes(id) || w.places.includes(spine.id)));
    const byKind = {};
    children.forEach((c) => (byKind[kindOf(c)] ||= []).push(c));

    const strata = `<div class="strata">${chain.map((p) => `<a class="stratum ${p.id === id ? "here" : ""}" href="place.html?id=${encodeURIComponent(p.id)}"><small>${esc(kindOf(p))}</small>${esc(p.name)}</a>`).join("")}</div>`;
    const links = [
      advice ? `<a class="btn ghost" href="${esc(advice.url)}" rel="noopener">Smartraveller advice</a>` : "",
    ].join("");
    const html = hero(credits, "place", {
      kicker: esc(chain.slice().reverse().map((p) => p.name).join(" › ")),
      title: esc(place.name),
      lede: advice ? `<span class="adv ${levelClass(advice.level)}">${esc(advice.level)}</span> <span style="opacity:.8">· Australian Government advice for ${esc(spine.name)}, fetched ${fmt(adv.checked_on)}</span>`
        : (place.aliases || []).length ? `Also known as ${esc(place.aliases.join(", "))}.` : "",
      actions: links,
      extra: strata,
      photo,
      caption,
    });
    const body = `<main>
      <section class="section tight"><div class="stats">
        <div class="stat"><b>${chain.length}</b><span>levels whose rules apply here</span></div>
        <div class="stat"><b>${place.records || 0}<span style="font-size:.5em;color:var(--muted)"> / ${place.applicable || 0}</span></b><span>patterns on record at this level</span></div>
        <div class="stat"><b id="gapcount">·</b><span>gaps to check before relying on this page</span></div>
        <div class="stat"><b>${num(descendants.length)}</b><span>places inside it</span></div>
      </div>
      ${watched.map((w) => `<p class="note" style="margin-top:18px"><b>Rule change watched:</b> ${esc(w.what)} Status: ${esc(w.status)}. Effective: ${w.effective ? fmt(w.effective) : "not settled"}. ${esc(w.next)}</p>`).join("")}
      </section>
      <section class="section tight">${sections}</section>
      ${events.length ? `<section class="section tight"><div class="layer-group"><h2>Upcoming here</h2><span class="rule"></span></div>
        <p class="meta">Dated leads from the feeds. An event is not a permission: taking part still runs through entry, activities and zone checks.</p>${events.map(eventCard(index)).join("")}</section>` : ""}
      ${!lawLevels.length && (lawRepos.no_online_source || {})[spine.id] ? `<section class="section tight"><div class="layer-group"><h2>Where the law is published</h2><span class="rule"></span></div>
        <p class="meta">${esc(lawRepos.no_online_source[spine.id])} Not knowing a law is no defence.</p></section>` : ""}
      ${lawLevels.length ? `<section class="section tight"><div class="layer-group"><h2>Where the law is published</h2><span class="rule"></span></div>
        <p class="meta">The official places to read the laws that apply here. Not knowing a law is no defence.</p>
        <div class="grid">${lawLevels.map(([p, list]) => `<div class="card"><h3>${esc(p.name)}</h3>${list.map((r) => `<p><a href="${esc(r.url)}" rel="noopener">${esc(r.name)}</a><br><span class="meta">${esc(r.publisher)}${r.check && r.check !== "loaded" ? ` · ${esc(r.check)}` : ""}</span></p>`).join("")}</div>`).join("")}</div></section>` : ""}
      ${offices.length ? `<section class="section tight"><div class="layer-group"><h2>${esc(spine.name)}'s offices in Australia</h2><span class="rule"></span></div>
        <p class="meta">Where to apply for a visa or ask for a rule in writing before you go. From the DFAT Protocol directory, read ${fmt(inAus.checked)}. Honorary consuls offer limited services.</p>
        <div class="grid">${offices.map((o) => `<div class="card"><h3>${esc(o.name)}</h3><p class="meta">${esc(o.type)}${o.honorary ? " · honorary" : ""}${o.city ? ` · ${esc(o.city)}${o.state ? ` ${esc(o.state)}` : ""}` : ""}</p>
          ${o.notice ? `<p><span class="chip gold">${esc(o.notice)}</span></p>` : ""}<p>${o.website ? `<a href="${esc(o.website)}">Website</a> · ` : ""}<a href="${esc(o.source)}">DFAT listing</a></p></div>`).join("")}</div></section>` : ""}
      ${children.length ? `<section class="section tight"><div class="layer-group"><h2>Inside ${esc(place.name)}</h2><span class="rule"></span></div>
        ${Object.entries(byKind).map(([k, list]) => `<h3 class="month-head">${esc(k)} <span class="meta">${list.length}</span></h3><div class="grid">${list.sort((a, b) => a.name.localeCompare(b.name)).slice(0, 120).map(placeCard).join("")}</div>${list.length > 120 ? `<p class="meta">${list.length - 120} more: use <a href="places.html">search</a>.</p>` : ""}`).join("")}</section>` : ""}
      <section class="section tight"><div class="card"><h3>A dated brief for a trip</h3>
        <p>Trip dates never go on this site. To get a brief with latest safe start dates for permits, run this on your own machine:</p>
        <pre>python scripts/brief.py ${esc(id)} --start 2027-03-01 --end 2027-04-15 --activities tourism,filming</pre></div></section>
    </main>`;
    setTimeout(() => { const g = document.getElementById("gapcount"); if (g) g.textContent = num(gaps); }, 0);
    return html + body;
  };

  render.patterns = async ({ index, credits }) => {
    const colour = { permission: "var(--sky)", safety: "var(--coral)", law: "var(--gold)", culture: "var(--violet)", relationships: "var(--coral)", cycles: "var(--leaf)", logistics: "var(--teal)", purpose: "var(--gold)" };
    return hero(credits, "patterns", {
      kicker: `${index.patterns.length} patterns`,
      title: "One question, asked the same way everywhere",
      lede: "Each pattern is a single file. Add one and every place it applies to shows it as not yet checked, and the routines start vetting it.",
    }) + `<main><section class="section"><div class="grid wide">${index.patterns.map((p) => {
      const c = p.coverage;
      const pct = c && c.active_places ? Math.round((c.with_record / c.active_places) * 100) : null;
      return `<div class="card" style="border-top:4px solid ${colour[p.layer] || "var(--line)"}">
        <h3>${esc(p.name)}</h3><p class="q" style="color:var(--ink-2)">${esc(p.question)}</p>
        <div class="chips"><span class="chip">${esc(p.method)}</span><span class="chip">${p.inherit === "stack" ? "stacks across levels" : p.inherit === "nearest" ? "nearest level" : "this place only"}</span><span class="chip">recheck within ${p.baseline_days} day${p.baseline_days === 1 ? "" : "s"}</span></div>
        ${c ? `<div class="mini-bar"><i style="width:${(c.fresh / Math.max(c.active_places, 1)) * 100}%;background:var(--fresh)"></i><i style="width:${((c.with_record - c.fresh) / Math.max(c.active_places, 1)) * 100}%;background:var(--due)"></i></div>
          <p class="meta" style="margin-top:6px">${c.with_record} of ${c.active_places} active places on record (${pct}%)</p>` : `<p class="meta" style="margin-top:12px">Machine pattern: refreshed automatically for every destination.</p>`}
        ${(p.activities || p.topics || p.requirement_types) ? `<details><summary class="meta">${(p.activities || p.topics || p.requirement_types).length} ${p.activities ? "activities" : p.topics ? "law topics" : "requirement types"}</summary><div class="chips" style="margin-top:8px">${(p.activities || p.topics || p.requirement_types).map((a) => `<span class="chip">${esc(a.replace(/-/g, " "))}</span>`).join("")}</div></details>` : ""}
        <details><summary class="meta">Rules</summary><ul>${p.rules.map((r) => `<li>${esc(r)}</li>`).join("")}</ul></details>
      </div>`;
    }).join("")}</div></section></main>`;
  };

  render.upcoming = async ({ index, credits }) => {
    const feed = await json("data/feeds/gajra-ahead.json", { events: [] });
    const now = today();
    const live = feed.events.filter((e) => (e.closes || e.ends || e.starts || "") >= now);
    setTimeout(() => wireUpcoming(index, live), 0);
    const doors = live.filter((e) => e.kind === "door").length;
    return hero(credits, "upcoming", {
      kicker: "From GAJRA Earth Ahead",
      title: "Open doors ahead",
      lede: `${live.length} upcoming AI governance events and open doors, ${doors} of them consultations, hearings or calls where anyone can put something in writing. Each is mapped to its place.`,
      actions: `<a class="btn ghost" href="https://auraofintelligence.github.io/gajra-earth-claude-build/ahead.html">See the Ahead page</a>`,
    }) + `<main><section class="section">
      <div class="months" id="months"></div>
      <div class="toolbar" id="ufilters">${[["all", "Everything"], ["door", "Open doors"], ["event", "Events"]].map(([k, l], i) => `<button class="filter" data-k="${k}" aria-pressed="${i === 0}">${l}</button>`).join("")}
        <select class="filter" id="ucountry" aria-label="Country"><option value="">All places</option></select></div>
      <div id="elist"></div>
      <p class="note" style="margin-top:28px">These are leads, not permissions. Attending, speaking or filming still runs through the entry, activities and permit zone checks for that place. The Ahead routine owns this content, including its exclusion of military and defence events.</p>
    </section></main>`;
  };

  function wireUpcoming(index, live) {
    let kind = "all";
    const sel = document.getElementById("ucountry");
    const spineOf = (e) => (e.place ? e.place.split("/")[0] : e.bloc || "online");
    const label = (k) => index.byId[k]?.name || (k === "eu" ? "European Union" : "Online or global");
    [...new Set(live.map(spineOf))].sort((a, b) => label(a).localeCompare(label(b))).forEach((k) => sel.insertAdjacentHTML("beforeend", `<option value="${esc(k)}">${esc(label(k))}</option>`));
    function draw() {
      const list = live.filter((e) => (kind === "all" || e.kind === kind) && (!sel.value || spineOf(e) === sel.value))
        .sort((a, b) => (a.closes || a.starts).localeCompare(b.closes || b.starts));
      const groups = {};
      list.forEach((e) => { (groups[(e.closes || e.starts).slice(0, 7)] ||= []).push(e); });
      document.getElementById("months").innerHTML = Object.entries(groups).map(([m, l]) => `<a class="month-pill" href="#m-${m}"><b>${l.length}</b><small>${fmt(m)}</small></a>`).join("");
      document.getElementById("elist").innerHTML = Object.entries(groups).map(([m, l]) => `<h2 class="month-head" id="m-${m}">${fmt(m)}</h2>${l.map(eventCard(index)).join("")}`).join("") || '<p class="empty">Nothing matches.</p>';
    }
    document.getElementById("ufilters").addEventListener("click", (e) => {
      const b = e.target.closest("button");
      if (!b) return;
      kind = b.dataset.k;
      document.querySelectorAll("#ufilters button").forEach((x) => x.setAttribute("aria-pressed", x === b));
      draw();
    });
    sel.addEventListener("change", draw);
    draw();
  }

  render.advisories = async ({ index, credits }) => {
    const [adv, changes] = await Promise.all([json("data/advisories.json", { destinations: {} }), index.has_change_log ? jsonl("data/logs/advisory-changes.jsonl") : []]);
    const list = Object.entries(adv.destinations);
    const bySlug = Object.fromEntries(index.places.filter((p) => p.smartraveller).map((p) => [p.smartraveller, p]));
    const levels = [["Exercise normal safety precautions", "lvl-normal"], ["Exercise a high degree of caution", "lvl-high-caution"], ["Reconsider your need to travel", "lvl-reconsider"], ["Do not travel", "lvl-do-not-travel"]];
    const regions = {};
    list.forEach(([k, d]) => (regions[d.region || "Other"] ||= []).push([k, d]));
    return hero(credits, "advisories", {
      kicker: `Fetched ${fmt(adv.checked_on)}`,
      title: "The light on the headland",
      lede: `Australian Government advice for ${list.length} destinations, refreshed every morning from Smartraveller. Advice is information for the traveller, never an automatic exclusion.`,
      actions: `<a class="btn ghost" href="https://www.smartraveller.gov.au/">Smartraveller</a>`,
    }) + `<main><section class="section">
      <div class="level-tiles">${levels.map(([l, c]) => `<div class="level-tile ${c}"><b>${list.filter(([, d]) => d.level === l).length}</b>${l}</div>`).join("")}</div>
      <p class="meta" style="margin-top:12px">Overall levels only. Many destinations carry higher levels in some regions: the Smartraveller page for each shows them.</p>
      <h2 style="margin-top:40px">Changes</h2>
      ${changes.length ? `<div class="table-wrap"><table><thead><tr><th>Date</th><th>Destination</th><th>From</th><th>To</th></tr></thead><tbody>${changes.slice().reverse().map((c) => `<tr><td>${fmt(c.date)}</td><td><a href="${esc(c.url)}">${esc(adv.destinations[c.destination]?.title || c.destination)}</a></td><td>${esc(c.from)}</td><td><span class="adv ${levelClass(c.to)}">${esc(c.to)}</span></td></tr>`).join("")}</tbody></table></div>`
        : `<p class="empty">No level changes recorded yet. Tracking began on ${fmt(adv.checked_on)}; the daily Action logs every change from here.</p>`}
      ${Object.entries(regions).sort().map(([r, items]) => `<h2 class="month-head">${esc(r)}</h2><div class="table-wrap"><table><tbody>${items.sort((a, b) => a[1].title.localeCompare(b[1].title)).map(([k, d]) => {
        const p = bySlug[k];
        return `<tr><td>${p ? `<a href="place.html?id=${encodeURIComponent(p.id)}">${esc(d.title)}</a>` : esc(d.title)}</td><td><span class="adv ${levelClass(d.level)}">${esc(d.level)}</span></td><td class="meta">updated ${fmt(d.published_change)}</td><td><a href="${esc(d.url)}">advice</a></td></tr>`;
      }).join("")}</tbody></table></div>`).join("")}
    </section></main>`;
  };

  render.queue = async ({ index, credits }) => {
    const [watch, sources] = await Promise.all([json("data/watch.json", { items: [] }), json("data/source-status.json", { sources: {} })]);
    const s = index.queue_summary;
    const dead = Object.entries(sources.sources).filter(([, v]) => v.dead_since);
    return hero(credits, "queue", {
      kicker: `Queue built ${fmt(s.generated_on)}`,
      title: "Every place, in its turn",
      lede: `${num(s.place_passes)} places and ${num(s.pattern_items)} pattern checks waiting. Dead sources and watched rule changes go first, then home and tagged places, then the rest.`,
    }) + `<main><section class="section">
      <div class="stats">${Object.entries(s.by_reason || {}).sort((a, b) => b[1] - a[1]).map(([r, n]) => `<div class="stat"><b>${num(n)}</b><span>${esc(REASON_LABEL[r] || r)}</span></div>`).join("")}</div>
      <h2 style="margin-top:40px">Next in line</h2><p class="meta">The weekly routine takes seven place passes at a time, in this order.</p>
      <div class="grid">${index.next.map((n) => placeCard(index.byId[n.place])).join("")}</div>
      <div class="two" style="margin-top:44px">
        <div><h2>Rule changes watched</h2>${watch.items.map((w) => `<div class="card" style="margin-bottom:12px"><h3>${esc(w.what)}</h3>
          <div class="chips"><span class="chip gold">${esc(w.status)}</span><span class="chip">effective ${w.effective ? fmt(w.effective) : "not settled"}</span><span class="chip">checked ${fmt(w.checked)}</span></div>
          <p class="meta" style="margin-top:8px">${esc(w.next)}</p></div>`).join("")}</div>
        <div><h2>Sources gone missing</h2><p class="meta">From the weekly source watch, checked ${fmt(sources.checked_on)}.</p>${dead.map(([u, v]) => `<p><a href="${esc(u)}" rel="noopener">${esc(u.replace(/^https?:\/\//, "").slice(0, 70))}</a><br><span class="meta">cited by ${esc(v.used_by.join(", "))}</span></p>`).join("") || '<p class="empty">None.</p>'}
          <h2 style="margin-top:30px">Run notes</h2>${index.runs.length ? index.runs.map((r) => `<p><a href="docs/runs/${esc(r)}">${esc(r.replace(".md", ""))}</a></p>`).join("") : '<p class="empty">No routine has run yet. Each run leaves a dated note here.</p>'}</div>
      </div>
    </section></main>`;
  };

  render.how = async ({ index, credits }) => hero(credits, "how", {
    kicker: "Machine checks, routines and the trip watch",
    title: "Three streams, one river",
    lede: "GitHub Actions do the mechanical checks for every place alike. Claude routines vet places from official sources. The trip watch tightens everything as a journey nears.",
  }) + `<main>
    <section class="section"><div class="grid wide">
      <div class="card" style="border-top:4px solid var(--gold)"><h3>Machine checks</h3><p>GitHub Actions, the same for every place, so the public history never shows where a trip is heading.</p>
        <ul><li>Daily, 06:00: Smartraveller advice levels</li><li>Daily, 08:45: GAJRA Earth Ahead events and open doors</li><li>Monday: every cited source page, still there and unchanged?</li><li>Monthly: public holidays for this year and next</li></ul></div>
      <div class="card" style="border-top:4px solid var(--teal)"><h3>Claude routines</h3><p>Vetting from primary sources, in queue order, with a dated run note each time.</p>
        <ul><li>Weekly: the next seven places, every pattern due</li><li>Monthly: seasons, festivals and moving calendars, protocols and dated events for 25 places</li></ul></div>
      <div class="card" style="border-top:4px solid var(--coral)"><h3>Trip watch</h3><p>Runs daily on the home computer and exits in seconds when no trip is near. Trip dates stay private.</p>
        <ul><li>Approach: from 90 days out, or earlier for long permit lead times</li><li>Countdown: 30 days, imminent: 7 days, then daily while there</li><li>Debrief: what the brief got right and missed</li></ul></div>
    </div></section>
    <section class="section band"><div class="section-head"><div><h2>Laws stack. Seasons don't.</h2><p>Each pattern says how it reaches down the tree.</p></div></div>
      <div class="grid wide">
        <div class="card"><h3>Stack</h3><p>Every level at once, country down to the place. A visitor on Minjerribah is bound by Australian, Queensland and Redland City law together.</p><div class="chips"><span class="chip">local law</span><span class="chip">culture and protocol</span><span class="chip">culture cycles</span><span class="chip">permit zones</span></div></div>
        <div class="card"><h3>Nearest</h3><p>The place's own record, else the closest level above that has one. Entry rules are set nationally, so an island uses its country's.</p><div class="chips"><span class="chip">entry</span><span class="chip">activities</span><span class="chip">health</span><span class="chip">seasons</span><span class="chip">consular</span><span class="chip">money</span></div></div>
        <div class="card"><h3>This place only</h3><p>Dated events and works belong to one place and aren't inherited.</p><div class="chips"><span class="chip">year ahead</span><span class="chip">works and purpose</span></div></div>
      </div>
      <p class="note" style="margin-top:22px">Unvetted is not permitted. A level marked "not yet checked" has unknown rules, not no rules.</p></section>
    <section class="section"><div class="two">
      <div><h2>Culture, on its own terms</h2><p>In the GAJRA Earth spirit: connective, not assimilative. Each place's own published guidance and its own names come first. Where nothing is published, the record says to ask locally, and who to ask. No outsider verdicts and no ranking of cultures.</p></div>
      <div><h2>Special permit zones</h2><p>The zone scan walks up to the country and down into any flagged zone inside a place: land council permits, community consent, filming permits, visitor caps, guides, fees and seasonal closures. Each permit's lead time counts back from the travel date to give a latest safe start.</p></div>
    </div></section>
    <section class="section band"><h2>Growing it</h2><div class="grid wide">
      <div class="card"><h3>Add a place</h3><p>One entry in <code>data/places/&lt;country&gt;/extra.json</code> with its parent, kind and reason. Tag it and it joins the queue.</p></div>
      <div class="card"><h3>Add a pattern</h3><p>One file in <code>patterns/</code>. Every place it applies to shows it as not yet checked.</p></div>
      <div class="card"><h3>Add a feed</h3><p>A script that writes the shared event shape to <code>data/feeds/</code>. Briefs and the trip watch pick it up.</p></div>
    </div><p style="margin-top:22px"><a href="${REPO}">Source, data and routines on GitHub</a></p></section>
    <section class="section"><h2>Data, for people and agents</h2><div class="table-wrap"><table><tbody>
      ${[["patterns/", "The fourteen pattern files"], ["data/places/", "The place tree: spine plus one folder per country"], ["data/vetting/", "One record file per vetted place"], ["data/advisories.json", "Smartraveller levels, daily"], ["data/feeds/gajra-ahead.json", "GAJRA Earth Ahead events, daily"], ["data/calendar/", "Public holidays, monthly"], ["data/source-status.json", "Source watch, weekly"], ["queue/due.json", "The public queue"], ["CLAUDE.md", "Working rules for every agent and routine"]]
        .map(([p, d]) => `<tr><td><a href="${REPO}/tree/main/${p}"><code>${p}</code></a></td><td>${d}</td></tr>`).join("")}</tbody></table></div></section>
  </main>`;

  render["site-map"] = async ({ index, credits }) => {
    const [related, placePhotos] = await Promise.all([json("site/data/related.json", { groups: [] }), json("site/data/place-photos.json", { photos: {} })]);
    const groups = {};
    index.places.filter((p) => !p.id.includes("/")).forEach((p) => { (groups[p.region || ((p.tags || []).includes("oceania") ? "Pacific" : "More places")] ||= []).push(p); });
    const order = ["Pacific", "Asia", "Middle East", "Africa", "Europe", "Americas", "More places"];
    const pages = [
      ["Find a place", [["places.html", "Places", "Search and browse every place, from countries to islands, councils and permit zones."], ["place.html?id=au/minjerribah", "A place page", "Every level's rules for one place, stacked. Example: Minjerribah."]]],
      ["Before you go", [["advisories.html", "Advisories", "Today's Smartraveller advice levels and every change since tracking began."], ["upcoming.html", "Upcoming", "Dated events and open calls from GAJRA Earth Ahead, by month and place."]]],
      ["About this site", [["patterns.html", "Patterns", "The fourteen questions every place is checked against."], ["how.html", "How it works", "The checks, how rules reach down from country to council, culture and permit zones."], ["queue.html", "Queue", "What gets checked next."]]],
    ];
    return hero(credits, "site-map", {
      title: "Site map",
      lede: "Every page, and every country and territory by region.",
    }) + `<main>
      <section class="section"><div class="grid wide">${pages.map(([g, list]) => `<div><h2>${g}</h2>${list.map(([h, t, d]) => `<p><a href="${h}"><b>${t}</b></a><br><span class="meta">${d}</span></p>`).join("")}</div>`).join("")}</div></section>
      <section class="section band"><h2>Countries and territories</h2>
        ${order.filter((g) => groups[g]).map((g) => `<h3 class="month-head">${g} <span class="meta">${groups[g].length}</span></h3><p class="az">${groups[g].sort((a, b) => a.name.localeCompare(b.name)).map((p) => `<a href="place.html?id=${encodeURIComponent(p.id)}">${esc(p.name)}</a>`).join("")}</p>`).join("")}</section>
      <section class="section tight">
        <details><summary><b>Related projects</b></summary>${related.groups.map((g) => `<h3 style="margin-top:18px">${esc(g.name)}</h3>${g.repos.map((r) => `<p><a href="${esc(r.site)}">${esc(r.title)}</a> <span class="meta">${esc(r.about)}</span></p>`).join("")}`).join("")}</details>
        <details style="margin-top:14px"><summary><b>Photo credits</b></summary><div class="table-wrap" style="margin-top:12px"><table><thead><tr><th>Page</th><th>Photograph</th><th>By</th><th>Licence</th></tr></thead><tbody>
        ${Object.values(credits).map((c) => `<tr><td>${esc(c.page)}</td><td><a href="${esc(c.source)}">${esc(c.alt)}</a></td><td>${esc(c.artist)}</td><td>${c.licence_url ? `<a href="${esc(c.licence_url)}">${esc(c.licence)}</a>` : esc(c.licence)}</td></tr>`).join("")}
        ${Object.entries(placePhotos.photos).sort((a, b) => (index.byId[a[0]]?.name || a[0]).localeCompare(index.byId[b[0]]?.name || b[0])).map(([pid, p]) => `<tr><td><a href="place.html?id=${encodeURIComponent(pid)}">${esc(index.byId[pid]?.name || pid)}</a></td><td><a href="${esc(p.source)}">${esc(p.title)}</a></td><td>${esc(p.artist)}</td><td>${esc(p.licence)}</td></tr>`).join("")}</tbody></table></div></details>
      </section>
    </main>`;
  };

  async function main() {
    const page = document.body.dataset.page;
    shell(page);
    if (page === "place") {
      const link = document.createElement("link");
      link.rel = "canonical";
      link.href = `https://auraofintelligence.github.io/world-travel-patterns/place.html?id=${encodeURIComponent(new URLSearchParams(location.search).get("id") || "")}`;
      document.head.append(link);
    }
    const app = document.getElementById("app");
    const [index, creditFile] = await Promise.all([json("site/data/index.json", null), json("site/heroes/credits.json", { images: [] })]);
    if (!index) { app.innerHTML = '<section class="section"><h1>Data not built</h1><p>Run <code>python scripts/build_site.py</code>, then serve the repo folder over HTTP.</p></section>'; return; }
    const ORDER = ["advisory", "entry", "activities", "zone-requirements", "health-entry", "local-law", "culture-and-protocol", "affection-and-relationships", "culture-cycles", "seasons-and-flow", "year-ahead", "consular", "money-and-cost", "works-and-purpose"];
    index.patterns.sort((a, b) => (ORDER.indexOf(a.id) + 1 || 99) - (ORDER.indexOf(b.id) + 1 || 99));
    index.byId = Object.fromEntries(index.places.map((p) => [p.id, p]));
    const credits = Object.fromEntries(creditFile.images.map((c) => [c.page, c]));
    app.innerHTML = await render[page]({ index, credits });
  }
  main();
})();
