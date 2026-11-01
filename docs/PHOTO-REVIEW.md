# Place photo review

For Luke. Every place photo is marked `review: pending` until you've looked. Change a decision in `site/heroes/place-photo-choices.json` (`banner`, `main` or `none`, with a reason) or add a chosen photo to `site/heroes/place-photos-curated.json`, then run `python scripts/place_photos.py`.

## The rule

A place page shows a photo of that place, or of somewhere inside it (labelled), or none. Never a stand-in from elsewhere.

## Where it stands (1 November 2026)

- 313 places have a photo. 312 are approved and 1 is pending: **au**, the Uluṟu sunset, which is waiting for your decision.
- **The review:** Grok Bot reviewed all 316 original picks by eye, and checked camera EXIF to enforce the no-drone rule. 280 were confirmed, 36 rejected and 1 left unsure (au). See [PHOTO-REVIEW-RECOMMENDATIONS.md](PHOTO-REVIEW-RECOMMENDATIONS.md).
- **Replacements:** 33 rejected photos were replaced with approved, openly licensed Commons photos, which are in `site/heroes/place-photos-curated.json`.
- **Rejected with no replacement (no photo shown):** gn, io, us/papahanaumokuakea.
- **No photo for other reasons:** au/kakadu, au/nt, au/torres-strait-islands, au/uluru-kata-tjuta, ca/haida-gwaii, de, kp, st, us/navajo-nation, us/new-jersey, us/north-carolina.
- Approvals live in `site/heroes/place-photo-choices.json` (`review: approved` with the file title). If a rebuild picks a different file, it goes back to pending.
- Sub-places without their own photo (councils, wards, electorates) borrow one from a place inside them, labelled, or show none.

## Chosen by hand

- **au/minjerribah**: Main Beach, Minjerribah, seen from Point Lookout (Mooloomba) (S. Newrick, CC BY-SA 4.0). [Source](https://commons.wikimedia.org/wiki/File:View_of_Main_Beach_from_Point_Lookout_(North_Stradbroke_Island).JPG)
- **sa**: Sandstone outcrops near AlUla, Saudi Arabia (Richard Mortel, CC BY 2.0). [Source](https://commons.wikimedia.org/wiki/File:Landscape_at_Shaden_Resort,_al-Ula,_Saudi_Arabia.jpg)
- **ir**: Naqsh-e Jahan Square, Isfahan, seen through the Qeysarieh arch (Amir Pashaei, CC BY-SA 4.0). [Source](https://commons.wikimedia.org/wiki/File:Naqsh-e_Jahan_Square_from_the_gheisariye_Vault.jpg)
- **tz**: An elephant on the floor of Ngorongoro Crater, Tanzania (Zenith4237, CC BY-SA 4.0). [Source](https://commons.wikimedia.org/wiki/File:Nature_of_Ngorongoro_Conservation_Area_(129).jpg)
- **pg**: Rabaul and Simpson Harbour, East New Britain, Papua New Guinea (Stefan Krasowski, CC BY 2.0). [Source](https://commons.wikimedia.org/wiki/File:Rabaul_from_Vulcanology_Observatory.jpg)

## Decisions made over the automatic pick

- **kp** → none: Banner shows soldiers marching at a martyrs' cemetery; peace-first guardrail.
- **mm** → banner: Main image is a close portrait of identifiable monks.
- **ps** → banner: Main image is the separation wall at a checkpoint; a neutral landscape suits a planning page.
- **ro** → banner: Main image is a pile of postage stamps, not the place.
- **sa** → main: Banner is the Kaaba in Mecca, which non-Muslim visitors cannot enter.
- **pg** → main: Banner shows identifiable people in ceremonial dress; avoid costume imagery as a national symbol.
- **st** → main: Banner is a photo of bird eggs.
- **us/north-carolina** → main: Banner is a plate of barbecue.
- **us/new-jersey** → main: Banner is a neon slogan sign.
- **us/minnesota** → banner: Main image is a roadside welcome sign.
- **cn/tibet** → banner: Main image is a space-station view captioned as China, not specifically Tibet.
- **au/nt** → none: Banner shows rock art at Uluru; Anangu ask that sacred sites and rock art not be photographed or used. Main image is a bushfire satellite view.

## Worth your eye first

- **Australia**: the Wikivoyage banner is the Uluṟu sunset from the official viewing area. Widely shared, but you may prefer a photo that isn't of a sacred site.
- **Fiji**: the banner is a resort beach (Shangri-La Fijian Resort).
- **Satellite views** remain where no ground photo or banner exists: New South Wales, South Australia, Texas, New Caledonia, the Tuamotus and a few US states.
- **Cultural rule**: no automatic photo for Kakadu, Uluṟu-Kata Tjuṯa, Aboriginal lands, the Torres Strait Islands, Navajo Nation, Haida Gwaii and Papahānaumokuākea. Choose those with their communities.
