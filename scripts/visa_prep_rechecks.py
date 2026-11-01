"""Hand-verified visa-preparation rechecks. Every fact here was read on CHECKED at the cited official page."""
CHECKED = "2026-11-01"
SR = {
    "ae": "https://www.smartraveller.gov.au/destinations/middle-east/united-arab-emirates",
    "ar": "https://www.smartraveller.gov.au/destinations/americas/argentina",
    "at": "https://www.smartraveller.gov.au/destinations/europe/austria",
    "be": "https://www.smartraveller.gov.au/destinations/europe/belgium",
    "br": "https://www.smartraveller.gov.au/destinations/americas/brazil",
    "ca": "https://www.smartraveller.gov.au/destinations/americas/canada",
    "ch": "https://www.smartraveller.gov.au/destinations/europe/switzerland",
    "cn": "https://www.smartraveller.gov.au/destinations/asia/china",
    "de": "https://www.smartraveller.gov.au/destinations/europe/germany",
    "es": "https://www.smartraveller.gov.au/destinations/europe/spain",
    "fr": "https://www.smartraveller.gov.au/destinations/europe/france",
    "gb": "https://www.smartraveller.gov.au/destinations/europe/united-kingdom",
    "gr": "https://www.smartraveller.gov.au/destinations/europe/greece",
    "id": "https://www.smartraveller.gov.au/destinations/asia/indonesia",
    "ie": "https://www.smartraveller.gov.au/destinations/europe/ireland",
    "in": "https://www.smartraveller.gov.au/destinations/asia/india",
    "it": "https://www.smartraveller.gov.au/destinations/europe/italy",
    "jp": "https://www.smartraveller.gov.au/destinations/asia/japan",
    "ke": "https://www.smartraveller.gov.au/destinations/africa/kenya",
    "kr": "https://www.smartraveller.gov.au/destinations/asia/south-korea-republic-korea",
    "mx": "https://www.smartraveller.gov.au/destinations/americas/mexico",
    "my": "https://www.smartraveller.gov.au/destinations/asia/malaysia",
    "nl": "https://www.smartraveller.gov.au/destinations/europe/netherlands",
    "nz": "https://www.smartraveller.gov.au/destinations/pacific/new-zealand",
    "ph": "https://www.smartraveller.gov.au/destinations/asia/philippines",
    "pt": "https://www.smartraveller.gov.au/destinations/europe/portugal",
    "pw": "https://www.smartraveller.gov.au/destinations/pacific/palau",
    "qa": "https://www.smartraveller.gov.au/destinations/middle-east/qatar",
    "sa": "https://www.smartraveller.gov.au/destinations/middle-east/saudi-arabia",
    "sg": "https://www.smartraveller.gov.au/destinations/asia/singapore",
    "th": "https://www.smartraveller.gov.au/destinations/asia/thailand",
    "tr": "https://www.smartraveller.gov.au/destinations/europe/turkiye",
    "us": "https://www.smartraveller.gov.au/destinations/americas/united-states-america",
    "uy": "https://www.smartraveller.gov.au/destinations/americas/uruguay",
    "vn": "https://www.smartraveller.gov.au/destinations/asia/vietnam",
    "za": "https://www.smartraveller.gov.au/destinations/africa/south-africa",
}
PASSPORT_6M = "Passport valid for at least 6 months on arrival"
RECHECKS = {
    "th": {
        "fastest_entry": "Visa exemption of up to 30 days for tourism or short-term travel (the 60-day exemption was replaced from 15 September 2026). Visa-free entries may be limited to 2 a calendar year without a justifiable reason.",
        "before_departure": "Thailand Digital Arrival Card (TDAC), free, within 3 days before arrival, on the Immigration Bureau site or the THIM app.",
        "steps": ["Confirm the purpose is tourism or short-term travel; business, work or speaking need the matching visa through the official Thai E-Visa site.",
                  {"step": "Submit the free TDAC within 3 days before arrival (beware fake sites charging a fee).", "url": "https://tdac.immigration.go.th/"},
                  "Carry proof of accommodation, enough funds and an onward or return ticket.",
                  "Get an entry stamp from an immigration officer; never from visa shops or agents."],
        "documents": ["Passport valid for more than 6 months", "TDAC confirmation", "Accommodation proof", "Proof of funds", "Onward or return ticket"],
        "fees": [{"item": "visa exemption (30 days)", "amount": 0, "currency": "THB", "url": "https://www.smartraveller.gov.au/destinations/asia/thailand"},
                 {"item": "TDAC", "amount": 0, "currency": "THB", "url": "https://tdac.immigration.go.th/"}],
        "sources": [{"title": "Thailand Digital Arrival Card", "authority": "Immigration Bureau, Royal Thai Police", "url": "https://tdac.immigration.go.th/", "supports": "official TDAC portal"}],
    },
    "gb": {
        "fastest_entry": "Electronic Travel Authorisation (ETA) for tourism, visiting or transit stays of up to 6 months; enforced from 25 February 2026.",
        "before_departure": "Apply for the ETA on GOV.UK or the UK ETA app; decisions usually within a day, up to 3 working days. Wait for the approval email before travelling.",
        "useful_stay": "Up to 6 months a visit; the ETA lasts 2 years or until the passport expires, multiple journeys.",
        "steps": [{"step": "Apply for the ETA (passport, email, card or Apple/Google Pay, face photo).", "url": "https://www.gov.uk/eta/apply"},
                  "Wait for the email with the 16-digit ETA reference before travelling.",
                  "Paid or unpaid work, volunteering or marrying need a visa arranged before travel.",
                  "Dual Australian-British or Australian-Irish citizens can't get an ETA: travel on the British or Irish passport or a certificate of entitlement."],
        "documents": ["Passport used for the ETA application", "ETA approval email (reference number)"],
        "fees": [{"item": "ETA", "amount": 20, "currency": "GBP", "url": "https://www.gov.uk/eta/apply"}],
        "sources": [{"title": "Apply for an ETA", "authority": "UK Visas and Immigration, GOV.UK", "url": "https://www.gov.uk/eta/apply", "supports": "£20 fee, decision times, validity, what you need"}],
    },
    "us": {
        "fastest_entry": "ESTA under the Visa Waiver Program for tourism or business visits of under 90 days; otherwise a visa before travel.",
        "before_departure": "Apply for ESTA on the official CBP site or app; a decision can take up to 72 hours.",
        "useful_stay": "Under 90 days a visit; ESTA usually valid 2 years or until the passport expires.",
        "steps": ["Check the passport is an e-Passport (with chip).",
                  {"step": "Complete the ESTA application and pay the fee.", "url": "https://www.usa.gov/visa-waiver-esta"},
                  "Keep the ESTA application number to check status (up to 72 hours).",
                  "No paid or unpaid work under the VWP; other purposes need a visa from a US embassy or consulate."],
        "documents": ["Australian e-Passport", "ESTA approval"],
        "fees": [{"item": "ESTA (approved)", "amount": 40.27, "currency": "USD", "url": "https://www.usa.gov/visa-waiver-esta"}],
        "sources": [{"title": "Visa Waiver Program and ESTA application", "authority": "USAGov, US Government", "url": "https://www.usa.gov/visa-waiver-esta", "supports": "steps and the US$40.27 total cost"},
                    {"title": "ESTA", "authority": "US Embassy in Singapore", "url": "https://sg.usembassy.gov/esta/", "supports": "US$40.27 from 1 January 2026; US$10.27 if denied"}],
        "note": "The official ESTA site (esta.cbp.dhs.gov) was reported by a search index to show US$40.62; USAGov and the US Embassy say US$40.27. Recheck the live ESTA payment page.",
    },
    "ca": {
        "fastest_entry": "Electronic travel authorisation (eTA) before flying to Canada; not needed arriving by car, bus, train or boat.",
        "before_departure": "Apply for the eTA through Immigration, Refugees and Citizenship Canada only.",
        "steps": ["Apply for the eTA online with passport, email and a card.",
                  "Most decisions arrive within minutes; some are asked for documents within 72 hours.",
                  "A criminal record, including drink-driving, can make you inadmissible: check with the Government of Canada.",
                  "Children travelling without both parents should carry a consent letter."],
        "documents": ["Passport", "eTA approval", "Consent letter for children travelling without both parents"],
        "fees": [{"item": "eTA", "amount": 7, "currency": "CAD", "url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-227/section-294.1.html"}],
        "sources": [{"title": "Immigration and Refugee Protection Regulations, s. 294.1", "authority": "Government of Canada, Justice Laws", "url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-227/section-294.1.html", "supports": "$7 eTA fee"}],
    },
    "in": {
        "fastest_entry": "e-Visa (tourism, business or medical) before arrival; no visa on arrival.",
        "before_departure": "Apply only on Indian Visa Online and check the arrival port recognises the e-Visa.",
        "steps": [{"step": "Apply for the e-Visa on Indian Visa Online (beware of fake sites).", "url": "https://indianvisaonline.gov.in/evisa/"},
                  "Arrive only at an entry point that recognises the e-Visa; otherwise entry is refused.",
                  "Other visa types go through the Indian High Commission in Australia.",
                  "If a visa expires or you overstay, speak to the FRRO before trying to leave."],
        "documents": ["Passport", "e-Visa approval (print it)"],
        "fees": [{"item": "e-Tourist visa, 30 days, arriving July to March", "amount": 25, "currency": "USD", "url": "https://indianvisaonline.gov.in/evisa/images/Etourist%5Ffee%5Ffinal.pdf"},
                 {"item": "e-Tourist visa, 30 days, arriving April to June", "amount": 10, "currency": "USD", "url": "https://indianvisaonline.gov.in/evisa/images/Etourist%5Ffee%5Ffinal.pdf"},
                 {"item": "e-Tourist visa, 1 year", "amount": 40, "currency": "USD", "url": "https://indianvisaonline.gov.in/evisa/images/Etourist%5Ffee%5Ffinal.pdf"},
                 {"item": "e-Tourist visa, 5 years", "amount": 200, "currency": "USD", "url": "https://indianvisaonline.gov.in/evisa/images/Etourist%5Ffee%5Ffinal.pdf"}],
        "sources": [{"title": "Country/Territory wise e-Tourist visa fee", "authority": "Government of India, Indian Visa Online", "url": "https://indianvisaonline.gov.in/evisa/images/Etourist%5Ffee%5Ffinal.pdf", "supports": "Australia row of the fee table"}],
        "note": "Business and medical e-Visa fees weren't reread.",
    },
    "vn": {
        "fastest_entry": "eVisa for tourism or business, up to 90 days, single or multiple entry; no visa on arrival for Australians.",
        "before_departure": "Apply on the official Vietnam eVisa portal; details must match the passport exactly. Print the approval.",
        "steps": [{"step": "Apply online on the National Portal on Immigration and pay the fee; processing takes about 3 working days.", "url": "https://evisa.immigration.gov.vn/en_US/web/guest/khai-thi-thuc-dien-tu/cap-thi-thuc-dien-tu"},
                  "Check every detail against the passport biodata page, on lodging and again on approval.",
                  "Print the approval; some travellers had trouble showing eVisas at check-in.",
                  "Check the exit date stamped on arrival before leaving border control."],
        "documents": ["Passport", "Printed eVisa approval"],
        "fees": [{"item": "eVisa, single entry", "amount": 25, "currency": "USD", "url": "https://evisa.immigration.gov.vn/en_US/web/guest/khai-thi-thuc-dien-tu/cap-thi-thuc-dien-tu"},
                 {"item": "eVisa, multiple entry", "amount": 50, "currency": "USD", "url": "https://evisa.immigration.gov.vn/en_US/web/guest/khai-thi-thuc-dien-tu/cap-thi-thuc-dien-tu"}],
        "sources": [{"title": "Foreigner apply for e-visa", "authority": "Vietnam Immigration Department, National Portal on Immigration", "url": "https://evisa.immigration.gov.vn/en_US/web/guest/khai-thi-thuc-dien-tu/cap-thi-thuc-dien-tu", "supports": "steps, 3 working days, US$25/US$50"}],
    },
    "ke": {
        "fastest_entry": "Electronic Travel Authorisation (ETA), applied for and paid online before departure.",
        "before_departure": "Apply on the official ETA Kenya site (normally up to 72 hours). The portal now also requires Kenya's inbound travel health insurance.",
        "steps": [{"step": "Apply for the standard ETA on etakenya.go.ke.", "url": "https://etakenya.go.ke/eligibility"},
                  {"step": "Buy the Kenyan inbound travel health insurance in the ETA process (required from 5 October 2026 under Gazette Notice 11492); foreign policies aren't accepted in its place.", "url": "https://insurance.ecitizen.go.ke/dashboard/travel"},
                  "Carry a yellow fever certificate if arriving from a yellow fever country.",
                  "Still hold comprehensive travel insurance; the Kenyan policy has limits."],
        "documents": ["Passport", "ETA approval", "Kenyan inbound travel health insurance policy", "Yellow fever certificate if arriving from a risk country"],
        "fees": [{"item": "standard ETA (single entry)", "amount": 30, "currency": "USD", "url": "https://etakenya.go.ke/eligibility"},
                 {"item": "inbound travel health insurance (up to 3 months)", "amount": 44, "currency": "USD", "url": "https://insurance.ecitizen.go.ke/dashboard/travel"}],
        "sources": [{"title": "ETA eligibility and fees", "authority": "Government of Kenya, ETA Kenya", "url": "https://etakenya.go.ke/eligibility", "supports": "US$30 standard ETA"},
                    {"title": "Inbound travel health insurance", "authority": "Government of Kenya, eCitizen", "url": "https://insurance.ecitizen.go.ke/dashboard/travel", "supports": "required from 5 October 2026; premium up to US$44"}],
        "note": "A trade report says a Kenyan court suspended the insurance mandate in late August 2026 while the portal still enforces it; payment-gateway fees may add a few dollars. Recheck before travel.",
    },
    "br": {
        "fastest_entry": "e-Visa (VIVIS) for tourism, business, transit, sport or artistic activities, stays up to 90 days; no visa at the border.",
        "before_departure": "Apply online only through the VFS Global portal before buying tickets; there's no expedited option.",
        "useful_stay": "Up to 90 days; e-Visa valid up to 5 years, multiple entries.",
        "steps": [{"step": "Apply for the e-Visa at brazil.vfsevisa.com and pay inside the platform.", "url": "https://www.gov.br/mre/pt-br/consulado-miami/information-about-visas-in-english/electronic-visitor-visa-e-visa"},
                  "Wait for the e-Visa by email; arriving without one means return on the next flight.",
                  "Get entry and exit stamps, especially at land borders.",
                  "You may need a yellow fever vaccination certificate."],
        "documents": ["Passport with 2 free visa pages, valid to the end of the trip", "Passport-style photo (2 x 2 inches, white background)", "e-Visa approval", "Yellow fever certificate if required"],
        "fees": [{"item": "e-Visa (consular US$80.00 + platform US$0.90)", "amount": 80.90, "currency": "USD", "url": "https://www.gov.br/mre/pt-br/consulado-miami/information-about-visas-in-english/electronic-visitor-visa-e-visa"}],
        "sources": [{"title": "Electronic Visitor Visa (e-Visa): US, Canadian and Australian citizens", "authority": "Consulate-General of Brazil in Miami, Ministry of Foreign Affairs", "url": "https://www.gov.br/mre/pt-br/consulado-miami/information-about-visas-in-english/electronic-visitor-visa-e-visa", "supports": "requirements and US$80.90 fee"}],
        "note": "The Brazilian Embassy in Canberra's e-Visa page (gov.br/mre/.../embaixada-camberra/.../e-visa) returned 404 on 2026-11-01.",
    },
    "id": {
        "fastest_entry": "e-Visa on Arrival (e-VOA) online at least 48 hours ahead, or a Visa on Arrival at listed ports, for tourism, government duties or business meetings.",
        "before_departure": "Submit the All Indonesia arrival card, then apply for the e-VOA. Bali visitors also pay the tourist levy.",
        "steps": [{"step": "Submit the arrival card on All Indonesia.", "url": "https://allindonesia.imigrasi.go.id/"},
                  {"step": "Apply for the e-VOA at least 48 hours before travel (or get a VOA on arrival at listed ports).", "url": "https://evisa.imigrasi.go.id/"},
                  "For Bali, pay the IDR 150,000 tourist levy online or at the airport or seaport counters.",
                  "You can't transit without an e-VOA or VOA."],
        "documents": ["Passport", "All Indonesia arrival card", "e-VOA or VOA", "Bali levy receipt if visiting Bali"],
        "fees": [{"item": "e-VOA or VOA (e-VOA adds a small processing fee)", "amount": 500000, "currency": "IDR", "url": "https://www.smartraveller.gov.au/destinations/asia/indonesia"},
                 {"item": "Bali tourist levy", "amount": 150000, "currency": "IDR", "url": "https://www.smartraveller.gov.au/destinations/asia/indonesia"}],
        "sources": [{"title": "Indonesia e-Visa", "authority": "Directorate General of Immigration, Indonesia", "url": "https://evisa.imigrasi.go.id/", "supports": "official e-VOA portal"},
                    {"title": "All Indonesia", "authority": "Directorate General of Immigration, Indonesia", "url": "https://allindonesia.imigrasi.go.id/", "supports": "official arrival card portal"}],
    },
    "sg": {
        "fastest_entry": "No visa for tourism, business meetings or conferences up to 90 days in most circumstances.",
        "before_departure": "Singapore Arrival Card (SGAC), free, within 3 days before arrival on the official ICA site.",
        "steps": [{"step": "Submit the free SGAC within 3 days before arrival (avoid scam sites asking for payment).", "url": "https://www.ica.gov.sg/enter-transit-depart/entering-singapore/sg-arrival-card"},
                  "Carry proof of funds, a confirmed onward or return ticket and a visa for the next destination if needed.",
                  "Work or study needs a pass through the Ministry of Manpower or ICA."],
        "documents": [PASSPORT_6M, "SGAC", "Proof of funds", "Onward or return ticket", "Yellow fever certificate if required"],
        "fees": [{"item": "visa-free entry", "amount": 0, "currency": "SGD", "url": "https://www.smartraveller.gov.au/destinations/asia/singapore"},
                 {"item": "SGAC", "amount": 0, "currency": "SGD", "url": "https://www.ica.gov.sg/enter-transit-depart/entering-singapore/sg-arrival-card"}],
        "sources": [{"title": "SG Arrival Card", "authority": "Immigration and Checkpoints Authority, Singapore", "url": "https://www.ica.gov.sg/enter-transit-depart/entering-singapore/sg-arrival-card", "supports": "official SGAC portal"}],
    },
}


def free(pid, item, currency):
    return {"item": item, "amount": 0, "currency": currency, "url": SR[pid]}


RECHECKS.update({
    "jp": {
        "fastest_entry": "Visa exemption for tourism, business trips, conferences or visiting friends and family, under 90 days.",
        "before_departure": "Optional pre-registration for immigration and customs on Visit Japan Web.",
        "steps": [{"step": "Pre-register immigration and customs details on Visit Japan Web (optional, faster).", "url": "https://www.vjw.digital.go.jp/"},
                  "Expect photographs and fingerprints on arrival (under-16s exempt).",
                  "Status can't be changed inside Japan: work, study or spouse visas need departure and re-entry with that visa.",
                  "Transiting between two airports means entering Japan, so entry rules apply."],
        "documents": ["Passport", "Visit Japan Web QR codes (optional)"],
        "fees": [free("jp", "visa exemption", "JPY")],
        "sources": [{"title": "Visit Japan Web", "authority": "Digital Agency, Government of Japan", "url": "https://www.vjw.digital.go.jp/", "supports": "official pre-registration portal"}],
    },
    "kr": {
        "fastest_entry": "Visa-free tourist stays up to 90 days; Australians are exempt from K-ETA until 31 December 2026.",
        "before_departure": "Optional e-Arrival card online (paper still available).",
        "steps": ["Check whether the K-ETA exemption has been extended past 31 December 2026 before booking 2027 travel.",
                  {"step": "Submit the e-Arrival card online before arrival (optional).", "url": "https://www.e-arrivalcard.go.kr/"},
                  "Other purposes need a visa from a South Korean embassy or consulate."],
        "documents": ["Passport", "e-Arrival card (optional)"],
        "fees": [free("kr", "visa-free entry, K-ETA exempt to 31 December 2026", "KRW")],
        "sources": [{"title": "e-Arrival card", "authority": "Korea Immigration Service, Ministry of Justice", "url": "https://www.e-arrivalcard.go.kr/", "supports": "official e-Arrival portal"}],
        "note": "K-ETA exemption ends 31 December 2026 unless extended; recheck in December.",
    },
    "nz": {
        "fastest_entry": "Australian citizens need no visa or NZeTA, unless they have a criminal record or have been deported from any country.",
        "before_departure": "New Zealand Traveller Declaration (NZTD), free, online or in the app, before passport control.",
        "steps": [{"step": "Complete the free NZTD before arrival.", "url": "https://www.travellerdeclaration.govt.nz/"},
                  "With a conviction or past deportation, contact a New Zealand Visa Application Centre well before travel."],
        "documents": ["Passport", "NZTD"],
        "fees": [free("nz", "entry for Australian citizens", "NZD"), {"item": "NZTD", "amount": 0, "currency": "NZD", "url": "https://www.travellerdeclaration.govt.nz/"}],
        "sources": [{"title": "New Zealand Traveller Declaration", "authority": "New Zealand Government", "url": "https://www.travellerdeclaration.govt.nz/", "supports": "official NZTD portal"}],
    },
    "ph": {
        "fastest_entry": "Visa-free for 30 days or less.",
        "before_departure": "Register on eTravel and complete the electronic health declaration to get a QR code for arrival and departure.",
        "steps": [{"step": "Register on eTravel and get the QR code.", "url": "https://etravel.gov.ph/"},
                  "Carry an onward or return ticket for no later than 30 days after arrival.",
                  "To stay longer, extend through the Bureau of Immigration (fees apply)."],
        "documents": [PASSPORT_6M, "eTravel QR code", "Onward or return ticket within 30 days"],
        "fees": [free("ph", "visa-free entry (30 days)", "PHP")],
        "sources": [{"title": "eTravel", "authority": "Government of the Philippines", "url": "https://etravel.gov.ph/", "supports": "official eTravel portal"}],
    },
    "cn": {
        "fastest_entry": "Visa waiver for ordinary Australian passports, up to 30 days for business, tourism, visiting family and friends or transit, until 31 December 2026.",
        "steps": ["Confirm the purpose fits the waiver (business, tourism, family visits, transit) and the stay is 30 days or less.",
                  "Anything else needs a full visa from the Chinese embassy before travel.",
                  "Expect fingerprints on arrival (ages 14 to 70). Entry can be refused at the border."],
        "documents": ["Ordinary Australian passport"],
        "fees": [free("cn", "visa waiver (30 days)", "CNY")],
        "note": "The waiver runs until 31 December 2026; recheck in December for an extension.",
    },
    "ie": {
        "fastest_entry": "No visa before travel; permission to stay up to 90 days is given on arrival by the immigration officer.",
        "steps": ["Be ready to show accommodation bookings, return flights and contacts in Ireland.",
                  "Work needs an employment permit (EPOS); study or longer stays need a visa before leaving Australia.",
                  "Ireland isn't in Schengen; check UK rules if travelling via the UK."],
        "documents": ["Passport with at least one blank page", "Accommodation bookings", "Return flight"],
        "fees": [free("ie", "visa-free entry", "EUR")],
        "sources": [{"title": "Entry for non-EU, non-EEA, non-Swiss and non-UK nationals", "authority": "Immigration Service Delivery, Department of Justice, Ireland", "url": "https://www.irishimmigration.ie/at-the-border/entry-for-non-eu-non-eea-non-swiss-and-non-uk-nationals/", "supports": "what to show at the border"}],
    },
    "ar": {
        "fastest_entry": "Tourists can stay up to 90 days without a visa.",
        "steps": ["Carry evidence of departure within 90 days (return or onward ticket).",
                  "Officials may ask for proof of accommodation and enough money or a credit card.",
                  "Other purposes or non-ordinary passports need a visa before travel; none on arrival."],
        "documents": ["Passport", "Return or onward ticket", "Accommodation proof", "Proof of funds"],
        "fees": [free("ar", "visa-free entry (tourism)", "ARS")],
    },
    "uy": {
        "fastest_entry": "Tourists can enter without a visa for up to 90 days.",
        "steps": ["Confirm details with the Uruguayan embassy for other purposes.", "Minors travelling alone or with one parent may need a letter of consent (Permiso de Menor)."],
        "documents": ["Passport"],
        "fees": [free("uy", "visa-free entry (tourism)", "UYU")],
    },
    "tr": {
        "fastest_entry": "No visa for tourism, business or transit up to 90 days in any 180 days (ordinary passports).",
        "steps": ["Other purposes need a visa from a Turkish embassy or consulate before arrival.",
                  "Longer stays need a Turkish residence permit.",
                  "Arriving by sea, get entry and exit stamps."],
        "documents": ["Ordinary passport"],
        "fees": [free("tr", "visa-free entry (90 in 180 days)", "TRY")],
    },
    "za": {
        "fastest_entry": "No visa for tourism up to 90 days. Leaving and re-entering doesn't reset the 90 days.",
        "before_departure": "Online traveller declaration within 24 hours before the last leg into South Africa (and before leaving).",
        "steps": ["Submit the online traveller declaration within 24 hours of the last leg into South Africa.",
                  "Carry a yellow fever certificate if arriving from a yellow fever country.",
                  "Other purposes need a visa through the Department of Home Affairs."],
        "documents": ["Passport (provisional travel documents not accepted)", "Traveller declaration", "Yellow fever certificate if required"],
        "fees": [free("za", "visa-free entry (tourism)", "ZAR")],
    },
})


def schengen(pid, name, extra_step=None, extra_source=None):
    steps = [f"{name} is in the Schengen area: short stays of 90 days or less can be visa-free in some cases; other purposes or longer stays need a visa before travel.",
             "At the first Schengen border, give fingerprints and a photo for the Entry/Exit System (EES). It's free; nothing is needed before arrival, and sites charging for it are fraudulent.",
             "Carry your passport when crossing borders, including inside Schengen (temporary internal checks are in place in places)."]
    if extra_step:
        steps.append(extra_step)
    spec = {"fastest_entry": f"Visa-free short stays (90 days or less) as part of the Schengen area, in some cases.",
            "before_departure": "Nothing to lodge before travel today: EES registration happens at the border. ETIAS hadn't started on 2026-11-01.",
            "steps": steps, "documents": ["Passport"], "fees": [free(pid, "visa-free short stay; EES registration", "EUR" if pid != "ch" else "CHF")]}
    if extra_source:
        spec["sources"] = [extra_source]
    return spec


RECHECKS.update({
    "at": schengen("at", "Austria", "An Austrian-Australian bilateral agreement on visa-free short stays exists; check its terms with the Austrian Embassy Canberra before relying on it."),
    "be": schengen("be", "Belgium", "Adults travelling with children may need proof of relationship (birth certificate or court order)."),
    "ch": schengen("ch", "Switzerland"),
    "de": schengen("de", "Germany", "A German-Australian visa exemption agreement exists; check its terms with the German Embassy Canberra. Non-travelling parents can sign a consent form for children."),
    "es": schengen("es", "Spain", "Get a legible entry stamp at the first Schengen entry; airlines may check you haven't overstayed 90 days."),
    "fr": schengen("fr", "France", "Visas must be applied for in Australia; status can't be changed once in France. France Diplomacy has an online visa tool."),
    "gr": schengen("gr", "Greece", "Get an entry stamp at the first Schengen entry."),
    "it": schengen("it", "Italy", "If you can't leave before the visa-free limit, contact the local questura; report wrong EES records at the next external border."),
    "nl": schengen("nl", "the Netherlands", "Check visa needs on NetherlandsWorldwide; temporary checks run at the Belgian and German land borders."),
    "pt": schengen("pt", "Portugal", "Get a clear entry stamp; AIMA residence and long-stay visa processing has long delays."),
    "ae": {"flag": True, "note": "Not verified 2026-11-01: Smartraveller confirms a tourist visa on arrival, but the length of stay (30 vs 90 days) and any fee need an official UAE source (ICP or GDRFA pages blocked fetches from here)."},
    "qa": {"flag": True, "note": "Not verified 2026-11-01: Smartraveller confirms visa on arrival and accommodation proof, but the stay length and fee weren't found on an official Qatari page (gov.qa timed out)."},
    "sa": {"flag": True, "note": "Not verified 2026-11-01: Smartraveller confirms a 1-year multiple-entry tourist e-visa (stays up to 90 days) from visa.visitsaudi.com; the fee (reported as SAR 395 with insurance by non-official sites) wasn't readable on the official portal."},
    "pw": {"flag": True, "note": "Not verified 2026-11-01: Smartraveller confirms a 30-day visitor visa on arrival and a free online Palau Entry Form within 72 hours; the Palau entry portal didn't load and any arrival fee wasn't confirmed."},
    "my": {"flag": True, "note": "Partly verified 2026-11-01: Smartraveller confirms a 90-day tourism entry in most cases and the MDAC within 3 days before arrival (imigresen-online.imi.gov.my); whether any fee applies wasn't stated, so left flagged."},
    "mx": {"flag": True, "note": "Partly verified 2026-11-01: Smartraveller confirms tourism entry without a visa (e-gates up to 180 days with a chipped passport) and the online FMM with QR code; the FMM cost wasn't stated on an official page read, so left flagged."},
})

SR.update({
    "af": "https://www.smartraveller.gov.au/destinations/asia/afghanistan",
    "al": "https://www.smartraveller.gov.au/destinations/europe/albania",
    "am": "https://www.smartraveller.gov.au/destinations/europe/armenia",
    "ao": "https://www.smartraveller.gov.au/destinations/africa/angola",
    "az": "https://www.smartraveller.gov.au/destinations/europe/azerbaijan",
    "ba": "https://www.smartraveller.gov.au/destinations/europe/bosnia-and-herzegovina",
    "bd": "https://www.smartraveller.gov.au/destinations/asia/bangladesh",
    "bf": "https://www.smartraveller.gov.au/destinations/africa/burkina-faso",
    "bg": "https://www.smartraveller.gov.au/destinations/europe/bulgaria",
    "bh": "https://www.smartraveller.gov.au/destinations/middle-east/bahrain",
    "bi": "https://www.smartraveller.gov.au/destinations/africa/burundi",
    "bj": "https://www.smartraveller.gov.au/destinations/africa/benin",
    "bn": "https://www.smartraveller.gov.au/destinations/asia/brunei-darussalam",
    "bo": "https://www.smartraveller.gov.au/destinations/americas/bolivia",
    "bs": "https://www.smartraveller.gov.au/destinations/americas/bahamas",
    "bt": "https://www.smartraveller.gov.au/destinations/asia/bhutan",
    "bw": "https://www.smartraveller.gov.au/destinations/africa/botswana",
    "by": "https://www.smartraveller.gov.au/destinations/europe/belarus",
    "bz": "https://www.smartraveller.gov.au/destinations/americas/belize",
    "cd": "https://www.smartraveller.gov.au/destinations/africa/democratic-republic-congo",
    "cf": "https://www.smartraveller.gov.au/destinations/africa/central-african-republic",
    "ci": "https://www.smartraveller.gov.au/destinations/africa/cote-divoire-ivory-coast",
    "ck": "https://www.smartraveller.gov.au/destinations/pacific/cook-islands",
    "cl": "https://www.smartraveller.gov.au/destinations/americas/chile",
    "cm": "https://www.smartraveller.gov.au/destinations/africa/cameroon",
    "co": "https://www.smartraveller.gov.au/destinations/americas/colombia",
    "cr": "https://www.smartraveller.gov.au/destinations/americas/costa-rica",
    "cu": "https://www.smartraveller.gov.au/destinations/americas/cuba",
    "cy": "https://www.smartraveller.gov.au/destinations/europe/cyprus",
    "cz": "https://www.smartraveller.gov.au/destinations/europe/czech-republic",
    "dj": "https://www.smartraveller.gov.au/destinations/africa/djibouti",
    "dk": "https://www.smartraveller.gov.au/destinations/europe/denmark",
    "do": "https://www.smartraveller.gov.au/destinations/americas/dominican-republic",
    "dz": "https://www.smartraveller.gov.au/destinations/africa/algeria",
    "ec": "https://www.smartraveller.gov.au/destinations/americas/ecuador",
    "ee": "https://www.smartraveller.gov.au/destinations/europe/estonia",
    "eg": "https://www.smartraveller.gov.au/destinations/africa/egypt",
    "eh": "https://www.smartraveller.gov.au/destinations/africa/morocco",
    "er": "https://www.smartraveller.gov.au/destinations/africa/eritrea",
    "et": "https://www.smartraveller.gov.au/destinations/africa/ethiopia",
    "fi": "https://www.smartraveller.gov.au/destinations/europe/finland",
    "fj": "https://www.smartraveller.gov.au/destinations/pacific/fiji",
    "fm": "https://www.smartraveller.gov.au/destinations/pacific/federated-states-micronesia",
    "ga": "https://www.smartraveller.gov.au/destinations/africa/gabon",
    "ge": "https://www.smartraveller.gov.au/destinations/europe/georgia",
    "gh": "https://www.smartraveller.gov.au/destinations/africa/ghana",
    "gm": "https://www.smartraveller.gov.au/destinations/africa/gambia",
    "gn": "https://www.smartraveller.gov.au/destinations/africa/guinea",
    "gt": "https://www.smartraveller.gov.au/destinations/americas/guatemala",
    "gy": "https://www.smartraveller.gov.au/destinations/americas/guyana",
    "hk": "https://www.smartraveller.gov.au/destinations/asia/hong-kong",
    "hn": "https://www.smartraveller.gov.au/destinations/americas/honduras",
    "hr": "https://www.smartraveller.gov.au/destinations/europe/croatia",
    "ht": "https://www.smartraveller.gov.au/destinations/americas/haiti",
    "hu": "https://www.smartraveller.gov.au/destinations/europe/hungary",
    "il": "https://www.smartraveller.gov.au/destinations/middle-east/israel",
    "iq": "https://www.smartraveller.gov.au/destinations/middle-east/iraq",
    "ir": "https://www.smartraveller.gov.au/destinations/middle-east/iran",
    "is": "https://www.smartraveller.gov.au/destinations/europe/iceland",
    "jm": "https://www.smartraveller.gov.au/destinations/americas/jamaica",
    "jo": "https://www.smartraveller.gov.au/destinations/middle-east/jordan",
    "kg": "https://www.smartraveller.gov.au/destinations/asia/kyrgyz-republic",
    "kh": "https://www.smartraveller.gov.au/destinations/asia/cambodia",
    "kp": "https://www.smartraveller.gov.au/destinations/asia/north-korea-democratic-peoples-republic-korea",
    "kw": "https://www.smartraveller.gov.au/destinations/middle-east/kuwait",
    "kz": "https://www.smartraveller.gov.au/destinations/asia/kazakhstan",
    "la": "https://www.smartraveller.gov.au/destinations/asia/laos",
    "lb": "https://www.smartraveller.gov.au/destinations/middle-east/lebanon",
    "lk": "https://www.smartraveller.gov.au/destinations/asia/sri-lanka",
    "lr": "https://www.smartraveller.gov.au/destinations/africa/liberia",
    "ls": "https://www.smartraveller.gov.au/destinations/africa/lesotho",
    "lt": "https://www.smartraveller.gov.au/destinations/europe/lithuania",
    "lv": "https://www.smartraveller.gov.au/destinations/europe/latvia",
    "ly": "https://www.smartraveller.gov.au/destinations/africa/libya",
    "ma": "https://www.smartraveller.gov.au/destinations/africa/morocco",
    "md": "https://www.smartraveller.gov.au/destinations/europe/moldova",
    "me": "https://www.smartraveller.gov.au/destinations/europe/montenegro",
    "mg": "https://www.smartraveller.gov.au/destinations/africa/madagascar",
    "mh": "https://www.smartraveller.gov.au/destinations/pacific/marshall-islands",
    "mk": "https://www.smartraveller.gov.au/destinations/europe/north-macedonia",
    "ml": "https://www.smartraveller.gov.au/destinations/africa/mali",
    "mm": "https://www.smartraveller.gov.au/destinations/asia/myanmar",
    "mn": "https://www.smartraveller.gov.au/destinations/asia/mongolia",
    "mo": "https://www.smartraveller.gov.au/destinations/asia/macau",
    "mr": "https://www.smartraveller.gov.au/destinations/africa/mauritania",
    "mt": "https://www.smartraveller.gov.au/destinations/europe/malta",
    "mu": "https://www.smartraveller.gov.au/destinations/africa/mauritius",
    "mv": "https://www.smartraveller.gov.au/destinations/asia/maldives",
    "mw": "https://www.smartraveller.gov.au/destinations/africa/malawi",
    "mz": "https://www.smartraveller.gov.au/destinations/africa/mozambique",
    "na": "https://www.smartraveller.gov.au/destinations/africa/namibia",
    "ne": "https://www.smartraveller.gov.au/destinations/africa/niger",
    "ng": "https://www.smartraveller.gov.au/destinations/africa/nigeria",
    "ni": "https://www.smartraveller.gov.au/destinations/americas/nicaragua",
    "no": "https://www.smartraveller.gov.au/destinations/europe/norway",
    "np": "https://www.smartraveller.gov.au/destinations/asia/nepal",
    "nu": "https://www.smartraveller.gov.au/destinations/pacific/niue",
    "om": "https://www.smartraveller.gov.au/destinations/middle-east/oman",
    "pa": "https://www.smartraveller.gov.au/destinations/americas/panama",
    "pe": "https://www.smartraveller.gov.au/destinations/americas/peru",
    "pg": "https://www.smartraveller.gov.au/destinations/pacific/papua-new-guinea",
    "pk": "https://www.smartraveller.gov.au/destinations/asia/pakistan",
    "pl": "https://www.smartraveller.gov.au/destinations/europe/poland",
    "ps": "https://www.smartraveller.gov.au/destinations/middle-east/palestine",
    "py": "https://www.smartraveller.gov.au/destinations/americas/paraguay",
    "ro": "https://www.smartraveller.gov.au/destinations/europe/romania",
    "rs": "https://www.smartraveller.gov.au/destinations/europe/serbia",
    "ru": "https://www.smartraveller.gov.au/destinations/europe/russia",
    "rw": "https://www.smartraveller.gov.au/destinations/africa/rwanda",
    "sb": "https://www.smartraveller.gov.au/destinations/pacific/solomon-islands",
    "sc": "https://www.smartraveller.gov.au/destinations/africa/seychelles",
    "sd": "https://www.smartraveller.gov.au/destinations/africa/sudan",
    "se": "https://www.smartraveller.gov.au/destinations/europe/sweden",
    "si": "https://www.smartraveller.gov.au/destinations/europe/slovenia",
    "sk": "https://www.smartraveller.gov.au/destinations/europe/slovakia",
    "sl": "https://www.smartraveller.gov.au/destinations/africa/sierra-leone",
    "sn": "https://www.smartraveller.gov.au/destinations/africa/senegal",
    "so": "https://www.smartraveller.gov.au/destinations/africa/somalia",
    "ss": "https://www.smartraveller.gov.au/destinations/africa/south-sudan",
    "sv": "https://www.smartraveller.gov.au/destinations/americas/el-salvador",
    "sy": "https://www.smartraveller.gov.au/destinations/middle-east/syria",
    "sz": "https://www.smartraveller.gov.au/destinations/africa/eswatini",
    "td": "https://www.smartraveller.gov.au/destinations/africa/chad",
    "tj": "https://www.smartraveller.gov.au/destinations/asia/tajikistan",
    "tl": "https://www.smartraveller.gov.au/destinations/asia/timor-leste",
    "tm": "https://www.smartraveller.gov.au/destinations/asia/turkmenistan",
    "tn": "https://www.smartraveller.gov.au/destinations/africa/tunisia",
    "to": "https://www.smartraveller.gov.au/destinations/pacific/tonga",
    "tt": "https://www.smartraveller.gov.au/destinations/americas/trinidad-and-tobago",
    "tw": "https://www.smartraveller.gov.au/destinations/asia/taiwan",
    "tz": "https://www.smartraveller.gov.au/destinations/africa/tanzania",
    "ua": "https://www.smartraveller.gov.au/destinations/europe/ukraine",
    "ug": "https://www.smartraveller.gov.au/destinations/africa/uganda",
    "uz": "https://www.smartraveller.gov.au/destinations/asia/uzbekistan",
    "ve": "https://www.smartraveller.gov.au/destinations/americas/venezuela",
    "vu": "https://www.smartraveller.gov.au/destinations/pacific/vanuatu",
    "ws": "https://www.smartraveller.gov.au/destinations/pacific/samoa",
    "xk": "https://www.smartraveller.gov.au/destinations/europe/kosovo",
    "ye": "https://www.smartraveller.gov.au/destinations/middle-east/yemen",
    "zm": "https://www.smartraveller.gov.au/destinations/africa/zambia",
    "zw": "https://www.smartraveller.gov.au/destinations/africa/zimbabwe",
})


def visa(pid, fastest, steps, documents, fees, sources=(), before=None, note=None, stay=None):
    out = {"fastest_entry": fastest, "steps": steps, "documents": documents, "fees": fees, "sources": list(sources)}
    if before:
        out["before_departure"] = before
    if stay:
        out["useful_stay"] = stay
    if note:
        out["note"] = note
    return out


def fee(item, amount, currency, url):
    return {"item": item, "amount": amount, "currency": currency, "url": url}


def src(title, authority, url, supports):
    return {"title": title, "authority": authority, "url": url, "supports": supports}


def flag(note):
    return {"flag": True, "note": "Not verified 2026-11-01: " + note}


SNAP = " (read via a search-index snapshot; the page blocked direct fetches from the checking network)"
RECHECKS.update({
    "fj": visa("fj", "No tourist visa needed; a visa on arrival for stays under 4 months.",
               ["Carry proof of booked accommodation and a return ticket for the visa on arrival.", "Other purposes need a visa through the Fiji High Commission.", "A criminal record can lead to refused entry."],
               ["Passport", "Accommodation booking", "Return ticket"], [free("fj", "visitor entry (tourism)", "FJD")]),
    "ws": visa("ws", "90-day Visitor Permit on arrival for tourism, applied for on the passenger arrival card.",
               ["Hold a confirmed return or onward ticket and enough funds.", "Business visits need a Business Visitor Permit (Samoa Immigration)."],
               ["Passport valid at least 6 months beyond the stay", "Return or onward ticket", "Proof of funds", "Passenger arrival card"], [free("ws", "visitor permit on arrival", "WST")],
               note="Smartraveller doesn't state a fee for the visitor permit; recorded as free because none is listed. Confirm with Samoa Immigration."),
    "nu": visa("nu", "No visa for tourist visits up to 30 days. Flights only via New Zealand, so NZ entry rules also apply.",
               ["Pre-book accommodation for the whole stay.", "Carry an onward or return ticket and enough money."],
               ["Passport", "Accommodation booking", "Onward or return ticket", "Proof of funds"], [free("nu", "visa-free entry (30 days)", "NZD")]),
    "hk": visa("hk", "Generally no visa for visitors staying less than 90 days.",
               ["Hong Kong has separate immigration rules from mainland China; check a Chinese visa allows re-entry to the mainland if needed.", "If the Chinese visa is in an old passport, carry both."],
               ["Passport"], [free("hk", "visa-free visit (under 90 days)", "HKD")],
               [src("Visit visa and entry permit requirements", "Immigration Department, Hong Kong SAR", "https://www.immd.gov.hk/eng/services/visas/visit-transit/visit-visa-entry-permit.html", "official requirements page")]),
    "mo": visa("mo", "Generally no visa for visits under 30 days.",
               ["Keep the paper entry slip (entry and latest departure dates); hotels and police ask for it.", "Visas, if needed, come through a PRC embassy or consulate."],
               ["Passport", "Entry slip"], [free("mo", "visa-free visit (under 30 days)", "MOP")]),
    "tw": visa("tw", "Visa-exempt entry up to 90 days for tourism or business, with a confirmed onward ticket; not available with a criminal record.",
               [{"step": "Submit the free Taiwan Arrival Card (TWAC) within 3 days before arrival (beware imitation sites).", "url": "https://twac.immigration.gov.tw/"},
                "Check the visa-exempt conditions on the Bureau of Consular Affairs site."],
               ["Passport", "TWAC", "Confirmed onward or return ticket"], [free("tw", "visa-exempt entry (90 days)", "TWD"), fee("TWAC", 0, "TWD", "https://twac.immigration.gov.tw/")],
               [src("Taiwan Arrival Card", "National Immigration Agency, Ministry of the Interior", "https://twac.immigration.gov.tw/", "official TWAC portal")],
               before="Free TWAC within 3 days before arrival."),
    "mn": visa("mn", "Tourists can stay up to 30 days without a visa.",
               ["Business or longer stays need a visa (up to 90 days) and health entry conditions.", "Register with the Mongolian immigration authority if required (see Smartraveller).", "Border areas need local permission."],
               ["Passport"], [free("mn", "visa-free entry (30 days)", "MNT")], note="Smartraveller flags a fuel shortage disrupting flights and roads."),
    "mv": visa("mv", "Free tourist visa on arrival, if all entry requirements are met.",
               ["Submit the Traveller Declaration within 96 hours before arrival.", "Hold a confirmed booking at a registered hotel, resort or tourist facility.", "Carry a yellow fever certificate if arriving from a risk country."],
               ["Passport", "Traveller Declaration", "Confirmed registered accommodation booking"], [free("mv", "tourist visa on arrival", "MVR")],
               before="Traveller Declaration within 96 hours before arrival; beware fake sites charging for the visa."),
    "lk": visa("lk", "Electronic Travel Authorisation (ETA) before travel, free for Australian tourists, up to 30 days; no ETA on arrival at Colombo.",
               [{"step": "Get the ETA online before travel.", "url": "https://www.eta.gov.lk/"}, "Stays over 30 days need a paid extension.", "Carry yellow fever or cholera vaccination proof if arriving from an affected country."],
               ["Passport", "ETA approval"], [free("lk", "tourist ETA (30 days)", "LKR")],
               [src("Sri Lanka ETA", "Department of Immigration and Emigration, Sri Lanka", "https://www.eta.gov.lk/", "official ETA portal")]),
    "sb": visa("sb", "Tourist Visa applied for before travel, valid up to 90 days (a temporary grace period may still allow visas on arrival).",
               [{"step": "Apply for the Tourist Visa with passport copy, itinerary, hotel booking and proof of funds.", "url": "https://immigration.gov.sb/visas/"},
                "Carry proof of measles vaccination (recommended).", "Extensions cost extra."],
               ["Passport copy", "Travel itinerary", "Hotel booking", "Proof of funds", "Measles vaccination proof (recommended)"],
               [fee("Tourist Visa", 100, "USD", SR["sb"])], [src("Visas", "Solomon Islands Immigration Division", "https://immigration.gov.sb/visas/", "official visa page")]),
    "kh": visa("kh", "e-Visa online or a tourist visa on arrival, valid 30 days.",
               [{"step": "Apply for the Visa T e-Visa (about 3 business days) and bring the certificate.", "url": "https://www.evisa.gov.kh/information/visa_type/4"},
                "Submit the Cambodia e-Arrival, recommended within 7 days before arrival.", "Don't overstay: fines, detention and bans apply."],
               ["Passport valid more than 6 months", "Digital passport photo", "e-Visa certificate", "e-Arrival"],
               [fee("e-Visa T (tourist, 1 month)", 30, "USD", "https://www.evisa.gov.kh/information/visa_type/4"), fee("e-Visa E (ordinary/business, 1 month)", 35, "USD", "https://www.evisa.gov.kh/information/visa_type/4")],
               [src("Visa type information", "eVisa Kingdom of Cambodia, Ministry of Foreign Affairs", "https://www.evisa.gov.kh/information/visa_type/4", "fees, validity, requirements" + SNAP)]),
    "np": visa("np", "Tourist visa on arrival (multiple entry); visit an embassy for other categories.",
               [{"step": "Fill in the online Tourist Visa form before arrival (receipt valid 15 days) or at an airport kiosk.", "url": "https://immigration.gov.np/en/page/tourist-visa"},
                "Pay at the bank counter for 15, 30 or 90 days; carry some cash.", "Keep a valid visa to leave; extend at the Department of Immigration if needed."],
               ["Passport valid at least 6 months", "Tourist visa form receipt", "Arrival card", "Payment receipt"],
               [fee("tourist visa, 15 days", 30, "USD", "https://immigration.gov.np/en/page/tourist-visa"), fee("tourist visa, 30 days", 50, "USD", "https://immigration.gov.np/en/page/tourist-visa"), fee("tourist visa, 90 days", 125, "USD", "https://immigration.gov.np/en/page/tourist-visa")],
               [src("Tourist Visa", "Department of Immigration, Nepal", "https://immigration.gov.np/en/page/tourist-visa", "steps and fees" + SNAP)]),
    "bt": visa("bt", "Visa needed, approved in advance (through a Bhutanese tour operator, hotel or the Department of Immigration) and issued on arrival.",
               [{"step": "Apply online and pay the visa fee and Sustainable Development Fee (SDF) during the application.", "url": "https://visit.doi.gov.bt/help/faq"},
                "Some areas need permits; a guide can arrange them.", "Get the visa stamped on arrival."],
               ["Passport valid at least 6 months", "Visa clearance letter"],
               [fee("visa", 40, "USD", "https://visit.doi.gov.bt/help/faq"), fee("Sustainable Development Fee, per adult per night (discount to 31 August 2027)", 100, "USD", "https://visit.doi.gov.bt/help/faq")],
               [src("Visit Bhutan FAQ", "Department of Immigration, Bhutan", "https://visit.doi.gov.bt/help/faq", "visa fee and SDF" + SNAP)]),
    "ck": flag("Smartraveller confirms a 31-day visitor visa on arrival (up to 8 months on application) with onward ticket, funds and accommodation, but refers fees to the Cook Islands Ministry of Foreign Affairs and Immigration."),
    "vu": flag("Smartraveller confirms a single-entry tourist visa on arrival up to 120 days (accredited booking or support letter, return ticket, 6 months passport); no fee stated."),
    "fm": flag("Smartraveller confirms a 30-day visitor visa on arrival with an onward ticket; no fee stated."),
    "mh": flag("Smartraveller confirms a 30-day visitor visa on arrival with an outbound ticket; no fee stated."),
    "tl": flag("Smartraveller confirms a 30-day visa on arrival at Dili airport or seaport, paid in US dollar cash; the amount isn't stated."),
    "to": flag("Smartraveller gives no visa details for Tonga (contact the High Commission); airlines require a return or onward ticket."),
    "pg": flag("Smartraveller confirms a visa is needed before travel (PNG eVisa portal; no visa on arrival) and a Digital Arrival Card; eVisa fee not confirmed."),
    "la": flag("Smartraveller confirms paid visas on arrival and e-visas plus the optional Lao Digital Immigration Form; the Australian fee wasn't on an official page read (eVisa fee calculator needs interaction)."),
    "mm": flag("Smartraveller advises against travel and confirms a visa is needed (Ministry of Immigration and Population e-Visa); fee not confirmed."),
    "bd": flag("Smartraveller confirms a visa before travel (online form) and arrival/departure cards; fee not confirmed."),
    "bn": flag("Smartraveller says a visa is needed to travel to Brunei, plus e-Arrival card, BruHealth declaration and BND 10,000 medical insurance for tourists; fee and exemptions not confirmed."),
    "pk": flag("Smartraveller confirms a visa in advance through the Pakistan Online Visa System; fee not confirmed."),
})
RECHECKS["ws"] = flag("Smartraveller confirms a 90-day Visitor Permit on arrival via the arrival card (return ticket, funds, passport valid 6 months beyond the stay); no fee stated.")


def vf(pid, fastest, steps, cur, documents=("Passport",), note=None):
    return visa(pid, fastest, steps, list(documents), [free(pid, "visa-free entry", cur)], note=note)


RECHECKS.update({
    "cy": vf("cy", "No tourist visa for stays up to 90 days in 6 months (Cyprus isn't in Schengen).", ["Longer stays need a visa (applications can be made in-country).", "Overstaying can mean a stop-list entry and up to 5 years' refusal."], "EUR"),
    "al": vf("al", "Visit for up to 90 days without a visa.", ["Longer stays need a visa."], "ALL"),
    "ba": vf("ba", "No visa for stays up to 90 days in 6 months.", ["Make sure the passport is stamped on entry.", "Register your address if staying 3 days or more (see Smartraveller).", "Longer stays need a temporary residence permit."], "BAM"),
    "me": vf("me", "Up to 90 days in 6 months without a tourist visa.", ["Register your address with police or a tourist organisation within 24 hours (hotels usually do it)."], "EUR"),
    "mk": vf("mk", "Up to 90 days in a 6-month period without a visa.", ["Children not travelling with both parents need written consent."], "MKD"),
    "rs": vf("rs", "No visa for tourist visits up to 90 days in 6 months from first entry.", ["Don't enter Serbia from Kosovo unless you first went to Kosovo from Serbia; you need a recent Serbian entry stamp."], "RSD"),
    "xk": vf("xk", "No visa for tourist stays under 90 days in any 180 days; a 90-day stamp is given on arrival.", ["Be ready to show documents on the reason for the visit.", "Serbia doesn't recognise Kosovo border crossings: plan routes accordingly."], "EUR"),
    "md": vf("md", "No visa for visits up to 90 days in 6 months.", ["Entry is registered at the border; record the entry date and avoid overstaying."], "MDL"),
    "am": vf("am", "No visa for stays up to 180 days a year.", ["Longer stays need a resident card (up to 30 days to process)."], "AMD"),
    "ge": vf("ge", "Visit for up to 12 months without a visa on an Australian passport.", ["Don't enter or exit via the land borders with Russia.", "Dual nationals: get advice from a Georgian embassy first."], "GEL"),
    "ua": vf("ua", "Visa-free visits up to 90 days in 180 days. Smartraveller advises do not travel.", ["Hold valid health insurance to enter.", "Check the Visit Ukraine site before travel."], "UAH", ("Passport", "Health insurance")),
    "by": vf("by", "30-day visa-free entry until 31 December 2026 (90 days a calendar year), only through Minsk National Airport and Brest, Vitebsk, Gomel and Mogilev airports. Smartraveller advises do not travel.", ["Not available when coming from or going to Russia.", "Compulsory medical insurance applies."], "BYN", ("Passport", "Medical insurance"), note="Visa-free scheme ends 31 December 2026 unless extended."),
    "ru": flag("Smartraveller confirms a visa is needed before travel (no visa on arrival; biometrics may be required) and advises do not travel; fee not confirmed."),
    "az": flag("Smartraveller confirms an e-visa from the Official Electronic Visa Portal (valid 90 days, stays up to 30 days); fee not confirmed on the portal."),
    "lv": schengen("lv", "Latvia", "Hold a valid health insurance policy covering health-related expenses (required to enter)."),
    "ro": schengen("ro", "Romania", "Get an entry stamp at the first Schengen entry."),
    "bg": schengen("bg", "Bulgaria", "Security incidents have occurred in the Black Sea off the coast; monitor local advice."),
    "hr": schengen("hr", "Croatia", "Get a clear entry stamp at the first Schengen entry."),
    "is": schengen("is", "Iceland"),
    "no": schengen("no", "Norway", "Svalbard isn't in Schengen; Schengen rules apply again on return to the mainland."),
    "dk": schengen("dk", "Denmark", "Greenland and the Faroe Islands aren't in Schengen or the EU."),
    "se": schengen("se", "Sweden"),
    "fi": schengen("fi", "Finland"),
    "ee": schengen("ee", "Estonia", "Russian border crossings can close at short notice."),
    "lt": schengen("lt", "Lithuania", "Temporary checks at the border with Poland."),
    "pl": schengen("pl", "Poland", "Officials may ask for an onward ticket; land borders from Belarus and Russia are closed to entry."),
    "cz": schengen("cz", "Czechia"),
    "sk": schengen("sk", "Slovakia"),
    "hu": schengen("hu", "Hungary"),
    "si": schengen("si", "Slovenia"),
    "mt": schengen("mt", "Malta", "Visa-free stays cover up to 90 days in any 180 for tourism, family visits, business meetings, events and short study."),
})
for _p in ("ro", "bg", "hr", "is", "no", "dk", "se", "fi", "ee", "lv", "lt", "pl", "cz", "sk", "hu", "si", "mt"):
    RECHECKS[_p]["fees"] = [free(_p, "visa-free short stay; EES registration", {"ro": "RON", "bg": "EUR", "is": "ISK", "no": "NOK", "dk": "DKK", "se": "SEK", "pl": "PLN", "cz": "CZK", "hu": "HUF"}.get(_p, "EUR"))]


RECHECKS.update({
    "ao": vf("ao", "No visa for tourism: 30 days an entry, up to 90 days a year.", ["Other travel needs a visa applied for online with the Serviço de Migração."], "AOA"),
    "bo": vf("bo", "No visa for tourism; 30 days on entry, extendable to 90 days a calendar year at an immigration office.", ["Get entry and exit stamps (especially at land borders) or pay a fine on leaving."], "BOB"),
    "bs": vf("bs", "No visa for visits of 90 days or less with a return or onward ticket.", ["Recent presence in Ebola-affected countries can mean screening and quarantine."], "BSD", ("Passport", "Return or onward ticket")),
    "bw": vf("bw", "No visa for tourists up to 90 days.", ["Children may need extra documents.", "Entering on an emergency passport needs a visa in advance."], "BWP"),
    "cl": vf("cl", "No visa for stays up to 90 days (Chile announced this for Australians on 17 September 2026).", ["Rapa Nui (Easter Island) stays are capped at 30 consecutive days."], "CLP"),
    "co": vf("co", "Generally no visa for tourism up to 90 days.", ["Be ready to show an onward or return ticket or proof of funds."], "COP", ("Passport", "Onward or return ticket", "Proof of funds")),
    "cr": vf("cr", "No visa for tourist visits under 90 days.", ["Show you'll return home or travel on, or you may be refused entry.", "A departure tax applies (may be in the airfare)."], "CRC", ("Passport", "Onward or return ticket")),
    "ec": vf("ec", "Up to 90 days without a visa; one paid extension of up to 90 more days.", ["Request any extension before the first 90 days end."], "USD"),
    "gy": vf("gy", "No visa; generally 30 days on arrival, extensions from the Ministry of Foreign Affairs.", ["Complete the online Immigration and Customs form within 48 hours before travel."], "GYD"),
    "hn": vf("hn", "No visa with a passport valid more than 6 months; CA-4 area (with El Salvador, Guatemala, Nicaragua) allows 90 days across members.", ["Your CA-4 period starts at the first entry into any member country."], "HNL", ("Passport valid more than 6 months",)),
    "jm": vf("jm", "No visa for tourism under 6 months or business under 30 days.", ["Complete the Immigration/Customs C5 form online before travel."], "JMD"),
    "kg": vf("kg", "No tourist visa for up to 30 days in each 60-day period; e-visa (Sapar) for up to 90 days.", ["Use the official e-visa site for longer stays."], "KGS"),
    "kz": vf("kz", "Visa-free up to 30 days an entry, 90 days in 180; no work.", ["Your host or accommodation provider registers you (see Smartraveller for the deadline)."], "KZT"),
    "ls": vf("ls", "Up to 30 days without a visa; extensions within the first 14 days.", ["Other purposes need a visa in advance."], "LSL"),
    "ma": vf("ma", "Generally no visa for visits under 90 days.", ["Don't overstay; you may not be able to leave until it's resolved."], "MAD"),
    "eh": vf("eh", "Smartraveller covers Western Sahara under its Morocco advice: generally no visa for visits under 90 days.", ["Entry is through Moroccan border control."], "MAD", note="Smartraveller's Western Sahara link resolves to the Morocco page; confirm local conditions."),
    "mu": vf("mu", "Free visa on arrival for stays under 60 days.", ["Other visits need a visa before travel; extensions through the Passport and Immigration Office."], "MUR"),
    "om": visa("om", "Free entry visa up to 14 days for tourism (may not be extendable).", ["Carry a confirmed accommodation booking, health insurance and a return ticket.", "Leave before day 14 to avoid penalties."],
               ["Passport valid more than 6 months", "Accommodation booking", "Health insurance", "Return ticket"], [free("om", "14-day tourist entry visa", "OMR")]),
    "pe": vf("pe", "No visa; a permit for up to 90 days on arrival, maximum 183 days a year.", ["Overstays mean a fine before leaving."], "PEN"),
    "py": vf("py", "No visitor visa for tourism up to 90 days on a regular passport.", ["Make sure the passport is stamped, signed and dated on entry."], "PYG"),
    "rw": vf("rw", "Free 30-day tourist visa on arrival for Commonwealth citizens.", ["Travel to or through the DRC in the last 30 days means refused entry."], "RWF"),
    "sz": vf("sz", "Up to 30 days without a visa.", ["Passport must be valid 6 months after departure with two blank pages."], "SZL", ("Passport valid 6 months after departure, 2 blank pages",)),
    "tj": vf("tj", "Visa-free stays up to 30 days.", ["Longer stays need a visa; check its dates when issued."], "TJS"),
    "tn": vf("tn", "No visa for visits of 90 days or less.", ["Other travel needs a visa before arrival."], "TND"),
    "uz": vf("uz", "No visa for stays up to 30 days.", ["Longer stays need a visa before arrival."], "UZS"),
    "zm": vf("zm", "No visa: tourists 90 days in any 12 months, business visitors 30 days.", ["Arriving by air, carry a return ticket; by land or water, enough funds.", "Business visitors may need an invitation letter."], "ZMW", ("Passport", "Return ticket or proof of funds")),
    "tt": visa("tt", "e-Visa needed before travel (multiple entry).", ["Apply on the official E-Visa Online Portal.", "Complete the digital Immigration and Customs form within 72 hours before travel."],
               ["Passport", "e-Visa", "Immigration and Customs form"], [fee("multiple-entry e-Visa", 800, "TTD", SR["tt"])]),
    "mg": visa("mg", "Tourist visa on arrival up to 60 days, single entry.", ["Show onward or return travel.", "Under 15 days there's no visa fee but a EUR 10 border administration fee; 30 and 60-day visas cost more (not stated)."],
               ["Passport", "Onward or return ticket"], [fee("visa under 15 days", 0, "EUR", SR["mg"]), fee("border administration fee", 10, "EUR", SR["mg"])], note="30 and 60-day visa fees not stated by Smartraveller."),
})
for _p, _why in {
    "bh": "visa on arrival resumed and eVisa available; fee not stated", "bi": "visa needed (nearest embassy Tokyo) and online registration; fee not stated",
    "bj": "e-visa for a fee plus yellow fever certificate; amount not stated", "bz": "Smartraveller's entry text covers health screening and an online form; visa status not clear in the section read",
    "ci": "no visa details in the section read", "cm": "e-visa before travel, no visa on arrival; fee not stated", "cu": "tourist card needed plus an online declaration; fee not stated",
    "dj": "visa needed via the e-visa portal; fee not stated", "do": "tourist card bought on arrival (30 days) and electronic entry/exit form; amount not stated",
    "dz": "visa in advance; fee not stated", "eg": "eVisa or visa on entry paid in USD or card; amount not stated", "er": "visa and exit permit needed; fee not stated",
    "et": "online visa needed; fee not stated", "ga": "visa advised plus a French invitation letter; fee not stated", "gh": "visa needed and yellow fever certificate; fee not stated",
    "gm": "visa may be needed and an airport security fee applies; amounts not stated", "gn": "no visa details in the section read", "gt": "CA-4 tourist card bought at the airport (90 days); amount not stated",
    "ni": "CA-4 tourist card bought at the airport (90 days); amount not stated", "sv": "CA-4 tourist card bought at the airport (90 days); amount not stated",
    "il": "ETA-IL needed for stays under 90 days (valid 2 years); fee not stated", "jo": "visa needed (90-day single entry on arrival or e-services); fee not stated",
    "kw": "visa on arrival or e-visa with fee; amount not stated", "lr": "visa needed and yellow fever certificate; fee not stated", "mr": "e-visa before travel, no visa on arrival; fee not stated",
    "mw": "visa needed, fees apply (eVisa); amount not stated", "mz": "tourist visa or eVisa depending on stay length; fee not stated", "na": "visa on arrival or online before travel, fees apply; amount not stated",
    "ng": "visa online through Nigeria Immigration Service, passport may need mailing; fee not stated", "sc": "no visa but a paid Digital Travel Authorisation (up to 30 days ahead); amount not stated",
    "sl": "visa needed plus airport security fee; amounts not stated", "sn": "visa details referred to the embassy; onward ticket and accommodation proof needed",
    "tz": "eVisa (some visas on arrival) plus mandatory NIC or ZIC inbound insurance; fees not stated", "ug": "visa or EAC Tourist Visa online; fees not stated",
    "zw": "30-day tourist visa on arrival or e-visa, fee in USD; amount not stated", "pa": "entry section didn't extract from Smartraveller", "tm": "entry section didn't extract from Smartraveller",
}.items():
    RECHECKS[_p] = flag("Smartraveller read: " + _why + ".")


# Batch D (2026-11-01): the 24 countries with no Smartraveller advice page. Smartraveller only has
# stub pages for these, so the primary source is the destination government's own page (or the
# Smartraveller Schengen page for Schengen members). ofc() sets SR[pid] to that URL so free() cites it.
SR_SCHENGEN = "https://www.smartraveller.gov.au/travel-essentials/getting-foreign-visa/travelling-europe-and-schengen-area"
EC_SCHENGEN = src("Schengen area", "European Commission, Migration and Home Affairs", "https://home-affairs.ec.europa.eu/policies/schengen/schengen-area_en", "Schengen membership and 90/180 rule")


def ofc(pid, primary, spec):
    SR[pid] = primary["url"]
    spec["primary"] = primary
    for f in spec["fees"]:
        f["url"] = f["url"] or primary["url"]
    return spec


def micro(pid, name, via, step):
    prim = src("Travelling to Europe and the Schengen Area", "Smartraveller, Australian Government", SR_SCHENGEN,
               "Australians visa-free in Schengen up to 90 days in 180; Smartraveller gives no separate advice for " + name)
    return ofc(pid, prim, visa(pid, f"No visa: {name} is reached through {via}, so the Schengen 90 days in 180 rule applies in practice.",
               [step, "At the first Schengen border, give fingerprints and a photo for the Entry/Exit System (EES); it's free.",
                "Stays over 90 days need a national visa or a bilateral waiver arranged before travel."],
               ["Passport"], [fee("visa-free entry", 0, "EUR", None)], [EC_SCHENGEN]))


AG = src("Countries exempt from visa", "Immigration Department, Antigua and Barbuda", "https://immigration.gov.ag/visa-services/countries-exempt-from-visa/", "Australia listed as visa-exempt")
BB = src("Visitors to Barbados", "Barbados Immigration Department", "https://immigration.gov.bb/pages/visitor.aspx", "visitor documents and the online Immigration and Customs form")
DM = src("Do I need a visa to enter into Dominica?", "Government of Dominica", "https://www.dominica.gov.dm/services/passports-and-travel-documents-non-nationals/do-i-need-a-visa-to-enter-into-dominica", "Commonwealth citizens visa-free up to 6 months")
GD = src("Visa requirements for travelling to Grenada", "Embassy of Grenada (Ministry of Foreign Affairs)", "https://gndembassyprc.mofa.gov.gd/wp-content/uploads/2023/08/Visa-Requirements-for-Grenada-final-UPDATED-February-2021-Approved1.pdf", "Australia: no visa required")
KN = src("Visa-required countries for entry", "Ministry of Foreign Affairs, Saint Kitts and Nevis", "https://www.mofa.gov.kn/visa-required-countries-for-entry-2/", "Australia not on the 67-country visa-required list")
LC = src("Immigration Act, Schedule 1 (Revised Laws of Saint Lucia 2023)", "Attorney General's Chambers, Saint Lucia", "http://attorneygeneralchambers.com/laws-of-saint-lucia/immigration-act/schedule-1-01", "Australia listed among countries whose citizens need a visa")
LCF = "https://www.govt.lc/services/apply-for-saint-lucia-non-immigrant-visa"
VC = src("Entry requirements", "Tourism Authority, Saint Vincent and the Grenadines", "https://tourism.gov.vc/tourism/index.php/svg-facts/459-entry-requirements", "visa-required nationalities list (Australia not on it)" + SNAP)
AD = src("Travel to Andorra", "Govern d'Andorra, Ministry of Foreign Affairs", "https://www.govern.ad/en/ministries-and-secretaries-of-state/ministry-of-foreign-affairs/travel-to-andorra", "no visa for tourists; entry is through France or Spain" + SNAP)

RECHECKS.update({
    "lu": micro("lu", "Luxembourg", "Schengen (it's a member)", "Luxembourg has a bilateral visa waiver with Australia usable after the Schengen 90 days; tell the first border guard if you plan to use it."),
    "li": micro("li", "Liechtenstein", "Switzerland or Austria (it's a Schengen member)", "There's no airport; arrive through Zurich or another Schengen airport."),
    "mc": micro("mc", "Monaco", "France (no border controls)", "Monaco isn't a Schengen member but has an open border with France; time there counts in practice."),
    "sm": micro("sm", "San Marino", "Italy (open border)", "San Marino isn't a Schengen member but is only reached through Italy."),
    "va": micro("va", "Vatican City", "Rome, Italy", "Areas beyond St Peter's and the Museums need permission."),
    "ad": ofc("ad", AD, visa("ad", "No visa for tourists; Andorra is outside Schengen but only reached through France or Spain.",
               ["Meet Schengen entry rules for France or Spain on the way in.", "Leaving Andorra means re-entering Schengen; carry your passport."],
               ["Passport"], [fee("visa-free entry", 0, "EUR", None)], [EC_SCHENGEN])),
    "ag": ofc("ag", AG, visa("ag", "No visa; stays up to 6 months on holiday or business.",
               ["Carry proof you can support yourself, an accommodation confirmation and an onward or return ticket."],
               ["Passport", "Accommodation confirmation", "Onward or return ticket", "Proof of funds"], [fee("visa-free entry", 0, "XCD", None)],
               [src("General visa information", "Immigration Department, Antigua and Barbuda", "https://immigration.gov.ag/visa-services/general-visa-information/", "stay up to 6 months and conditions")])),
    "bb": ofc("bb", BB, visa("bb", "No visa; Australians can stay up to 6 months.",
               ["Complete the online Immigration and Customs form (opens 72 hours before arrival) and keep the receipt.", "Carry a return ticket, intended address and evidence of support."],
               ["Passport valid for the trip", "Immigration and Customs form receipt", "Return ticket", "Address in Barbados", "Proof of funds"],
               [fee("visa-free entry", 0, "BBD", "https://www.foreign.gov.bb/wp-content/uploads/2025/11/Updated-visa-list-May-09-2025-002.pdf")],
               [src("Visa requirements list (revised 9 May 2025)", "Ministry of Foreign Affairs and Foreign Trade, Barbados", "https://www.foreign.gov.bb/wp-content/uploads/2025/11/Updated-visa-list-May-09-2025-002.pdf", "Australians: no visa, maximum 6 months")])),
    "dm": ofc("dm", DM, visa("dm", "No visa for Commonwealth citizens (including Australians) for up to 6 months.",
               ["Submit the online ED card (immigration and customs) before arrival.", "Carry a return ticket, enough funds and a local address."],
               ["Passport", "ED card", "Return ticket"], [fee("visa-free entry", 0, "XCD", None)],
               [src("Online immigration and customs form", "Government of Dominica", "https://edcard.dominica.gov.dm/", "official ED card portal")])),
    "gd": ofc("gd", GD, visa("gd", "No visa required for Australians.",
               ["Complete the online Immigration and Customs form (opens 72 hours before arrival).", "Staying beyond the permitted visitor period, or work or study, needs a visa."],
               ["Passport valid 6 months from arrival", "Return or onward ticket", "Immigration and Customs form"], [fee("visa-free entry", 0, "XCD", None)],
               [src("Online Immigration and Customs portal", "Government of Grenada", "https://edcard.gov.gd/", "official arrival form")],
               note="Stay length for Australians isn't given on the official list (visitor periods range from 14 days to 6 months).")),
    "kn": ofc("kn", KN, visa("kn", "No visa: Australia isn't on the visa-required list.",
               ["Complete the Saint Kitts and Nevis online immigration form before arrival (linked from the Ministry's Travel menu)."],
               ["Passport", "Online immigration form"], [fee("visa-free entry", 0, "XCD", None)],
               note="Permitted stay isn't stated on the Ministry page; set at the border.")),
    "lc": ofc("lc", LC, visa("lc", "Visa needed: Australia is on Saint Lucia's visa-required list. Apply through the Royal Saint Lucia Police Force visa office (about 5 working days).",
               ["Apply at least 2 weeks before travel (visaoffice@police.govt.lc); an airport application is sometimes possible but can be refused.",
                "Include 2 certified photos, return ticket, itinerary and accommodation proof."],
               ["Passport valid 6 months", "2 certified passport photos", "Return ticket", "Itinerary", "Accommodation proof", "Invitation letter if staying with someone"],
               [fee("single-entry visa (3 months)", 125, "XCD", LCF), fee("multiple-entry visa (1 year)", 190, "XCD", LCF)],
               [src("Apply for Saint Lucia non-immigrant visa", "Government of Saint Lucia", LCF, "fees, documents and processing time")])),
    "vc": ofc("vc", VC, visa("vc", "No visa before travel; the visa-required list doesn't include Australia. Immigration sets the stay on arrival.",
               ["Carry a return or onward ticket, enough funds and accommodation details."],
               ["Passport valid 6 months beyond entry", "Return or onward ticket", "Proof of funds", "Accommodation details"], [fee("visa-free entry", 0, "XCD", None)])),
})


NR = src("Immigration Division: visas and visa fees", "Department of Justice and Border Control, Nauru", "https://justice.gov.nr/immigration-division/", "visitor visa classes and fees under the Immigration Act 2014")
KI = src("Visa Exemption Order 2023", "Ministry of Foreign Affairs and Immigration, Kiribati", "https://www.mfa.gov.ki/wp-content/uploads/2023/09/VISA-EXEMPTION-ORDER-2023-1.pdf", "Australian citizens exempt; up to 90 days in 12 months; passport valid 6 months after departure" + SNAP)
TG = src("A propos du e-Visa", "Voyage Togo, Government of Togo", "https://voyage.gouv.tg/about", "tourist e-visa durations, prices and documents")
RECHECKS.update({
    "nr": ofc("nr", NR, visa("nr", "Visitor visa needed before travel; applicants from Australia need a sponsorship letter from a Nauruan citizen living in Nauru.",
               ["Download the visitor visa application form from the Immigration Division and lodge it with the fee.", "Get the sponsorship letter first; overstaying costs $50 a day."],
               ["Passport", "Visitor visa application form", "Sponsorship letter from a Nauruan citizen in Nauru"],
               [fee("visitor visa, up to 1 month", 50, "AUD", None), fee("visitor visa, up to 2 months", 150, "AUD", None), fee("visitor visa, up to 3 months", 250, "AUD", None)],
               [src("Immigration Regulations 2014", "Republic of Nauru (PacLII)", "https://pacliirms.austlii.edu.au/nr/legis/sub_leg/ia2014ir2014385", "sponsorship requirement")])),
    "ki": ofc("ki", KI, visa("ki", "No visa: Australian citizens are exempt for up to 90 days in any 12 months; entry permission is still granted on arrival.",
               ["Apply for entry permission on arrival (separate from the visa exemption).", "Passport must be valid 6 months after you leave Kiribati."],
               ["Passport valid 6 months after departure", "Onward or return ticket"], [fee("visa exemption", 0, "AUD", None)],
               [src("Visa", "Ministry of Foreign Affairs and Immigration, Kiribati", "https://www.mfa.gov.ki/visa/", "visa rules under the Immigration Act 2019 and Procedures 2020")])),
    "tg": ofc("tg", TG, visa("tg", "e-Visa needed, applied for online at least 5 days before arrival (visas on arrival suspended).",
               ["Fill in the immigration form on voyage.gouv.tg; it routes you to the e-visa and online payment (card or mobile money).",
                "Apply at least 5 to 6 days ahead; processing takes up to 5 working days.", "Carry a yellow fever vaccination card."],
               ["Passport valid 3 months beyond the visa", "Recent photo", "Accommodation booking", "Yellow fever certificate"],
               [fee("tourist e-visa 1 to 15 days, single entry", 25000, "XOF", None), fee("tourist e-visa 1 to 15 days, multiple entry", 35000, "XOF", None),
                fee("tourist e-visa 16 to 30 days, multiple entry", 45000, "XOF", None), fee("tourist e-visa 31 to 90 days, multiple entry", 65000, "XOF", None)])),
    "cv": flag("no Smartraveller advice. The Cabo Verde government (gov.cv) visa-exempt list doesn't include Australia, so a visa is needed; EASE pre-registration and the Airport Security Fee (CVE 3,400, gov.cv/pedir-tsa) apply. The tourist visa fee wasn't found on gov.cv."),
    "st": flag("no Smartraveller advice. Search snapshots of the national law (smf.st) and the tourism office say a 15-day exemption covers listed nationalities and holders of a Schengen or US visa; Australia's place on the list and the e-visa fee weren't confirmed on an official page."),
    "gw": flag("no Smartraveller advice. Only a pre-enrolment e-visa site (rgb-visa.com, government status unclear) and foreign-ministry reports (visa on arrival about EUR 80) were found."),
    "km": flag("no Smartraveller advice. Visa on arrival (reported EUR 30 for 45 days) only in foreign government advice; no Comoros government page found."),
    "cg": flag("no Smartraveller advice and no Republic of the Congo government visa page found."),
    "gq": flag("no Smartraveller advice and no Equatorial Guinea government visa page found."),
    "tv": flag("no Smartraveller advice. Search snapshots of Tuvalu's Immigration Regulations 2014 say a visitor permit up to 30 days is issued on arrival for AUD 100 unless the nationality is on a fee-exemption list; the PDF wouldn't load to check whether Australia is exempt."),
    "sr": flag("no Smartraveller advice. Suriname's e-visa/entry-fee portal (suriname.vfsevisa.com, run by VFS for the government) blocked fetches; snapshots show a US$50 single-entry entry fee plus US$8 service fee. Needs a direct government read."),
})


# Batch F1 (2026-11-01): official fee pages found for previously flagged records.
def pv(pid, fastest, steps, documents, fees, portal, note=None, before=None):
    return visa(pid, fastest, steps, documents, fees, [portal], before=before, note=note)


EGP = "https://visa2egypt.gov.eg/eVisa/FAQ?VISTK"
ILP = "https://israel-entry.piba.gov.il/learn-about/"
TZP = "https://www.immigration.go.tz/websiteportal/uploads/information_links/info_link_20260910_084204_a50ed70947.pdf"
UGP = "https://immigration.go.ug/services/tourist-visa"
SCP = "https://seychelles.govtas.com/en/FAQ/dc3d5be6-d29e-4881-84f8-ad93a2759682"
ETP = "https://www.evisa.gov.et/information/tourist"
JOP = "https://www.mota.gov.jo/En/Pages/Visa_information"
ZWP = "https://www.zimembassyberlin.gov.zw/?page_id=791"
MWP = "https://www.immigration.gov.mw/visa/visa-fees/"
NAP = "https://eservices.mhaiss.gov.na/holidayvisa-services"
KWP = "https://kuwaitvisa.moi.gov.kw/tourist-visa-instructions"
BHP = "https://www.bahrain.bh/wps/portal/en/BNP/ServicesCatalogue/GSX-UI-PServiceDetails?psID=1871"
RECHECKS.update({
    "eg": pv("eg", "Single-entry tourist visa: e-Visa before travel or visa on arrival (paid in USD or by card).",
             ["Apply on the official e-Visa portal (visa2egypt.gov.eg) or buy on arrival at the airport.", "Avoid look-alike sites charging extra."],
             ["Passport valid 6 months", "e-Visa approval or cash/card for the arrival visa"], [fee("single-entry tourist visa (from 1 March 2026)", 30, "USD", EGP)],
             src("Egypt e-Visa portal FAQ", "Government of Egypt", EGP, "single-entry fee USD 30" + SNAP)),
    "il": pv("il", "ETA-IL needed before travel for stays under 90 days; valid up to 2 years or until the passport expires.",
             ["Apply on the official PIBA site only (israel-entry.piba.gov.il).", "Check Smartraveller's current advice level for Israel before booking."],
             ["Passport", "ETA-IL approval"], [fee("ETA-IL (non-refundable)", 25, "ILS", ILP)],
             src("ETA-IL", "Population and Immigration Authority, Israel", ILP, "NIS 25 fee, 2-year validity, 90-day visits" + SNAP)),
    "tz": pv("tz", "Ordinary (single-entry) visa, online or on arrival (Australia is on the on-arrival list); valid up to 90 days.",
             ["Apply on the official eVisa portal (visa.immigration.go.tz) or get it on arrival.", "Buy the mandatory inbound travel insurance (NIC for the mainland, ZIC for Zanzibar) per Smartraveller."],
             ["Passport", "Return ticket", "Inbound insurance certificate", "Yellow fever certificate if arriving from a risk country"],
             [fee("Ordinary visa (single entry, up to 90 days)", 50, "USD", TZP)],
             src("Tanzania Visa Guidelines (September 2026)", "Immigration Services Department, Tanzania", TZP, "Australia on the visa-on-arrival list; Ordinary visa USD 50"),
             note="Mandatory NIC/ZIC insurance cost not confirmed on an official page."),
    "ug": pv("ug", "Tourist visa (single entry) applied for online before travel.",
             ["Apply only on visas.immigration.go.ug; the immigration service warns about fake portals.", "Carry a yellow fever certificate."],
             ["Passport", "Recent photo", "Hotel booking or host address", "Yellow fever certificate"], [fee("tourist visa, single entry", 50, "USD", UGP)],
             src("Uganda tourist visa, single entry", "National Citizenship and Immigration Control, Uganda", UGP, "documents and USD 50 fee")),
    "sc": pv("sc", "No visa; a paid Travel Authorisation is needed, applied for up to 30 days before travel.",
             ["Apply only on seychelles.govtas.com (third-party sites charge more).", "Carry return ticket, accommodation proof and enough funds."],
             ["Passport", "Travel Authorisation", "Return ticket", "Accommodation booking"],
             [fee("Travel Authorisation (enrolment EUR 10 plus charges)", 12.06, "EUR", SCP)],
             src("Price of the Travel Authorisation", "Seychelles Electronic Border System (Government of Seychelles)", SCP, "EUR 12.06 total" + SNAP)),
    "et": pv("et", "e-Visa needed before travel (tourist, single entry, 30 days).",
             ["Apply on evisa.gov.et; processing is about 3 days."], ["Passport", "e-Visa", "Yellow fever certificate if required"],
             [fee("tourist e-visa, 30 days", 62, "USD", ETP)],
             src("Tourist visa", "Ethiopian Immigration and Citizenship Service e-Visa", ETP, "USD 62 for 30 days" + SNAP)),
    "jo": pv("jo", "Single-entry visa (valid 3 months) on arrival at airports and most crossings, or paid in advance online.",
             ["Pay online through the Ministry of Interior e-services (eservices.moi.gov.jo/MOI_EVISA) or on arrival.", "The Jordan Pass (tourism ministry) can cover the fee if you stay 3 nights or more."],
             ["Passport valid 6 months"], [fee("single-entry visa", 40, "JOD", JOP)],
             src("Visa information", "Ministry of Tourism and Antiquities, Jordan", JOP, "JOD 40 single-entry visa" + SNAP)),
    "zw": pv("zw", "Tourist visa on arrival or e-visa before travel, paid in USD.",
             ["Apply on evisa.gov.zw or pay on arrival.", "KAZA UNIVISA covers Zimbabwe and Zambia at some crossings."], ["Passport", "Return ticket"],
             [fee("single-entry visa", 30, "USD", ZWP)],
             src("Visas", "Embassy of the Republic of Zimbabwe, Berlin", ZWP, "single entry USD 30" + SNAP)),
    "mw": pv("mw", "Visa needed; apply on the official e-Visa portal (about 3 working days).",
             ["Apply on evisa.gov.mw and pay online by card; fees are non-refundable."], ["Passport", "e-Visa approval"],
             [fee("single-entry visa", 50, "USD", MWP)],
             src("Visa fees", "Department of Immigration and Citizenship Services, Malawi", MWP, "single entry USD 50" + SNAP)),
    "na": pv("na", "Visa needed: apply online before travel (visa on arrival issued at the port of entry).",
             ["Apply on the Ministry's e-services portal before arriving.", "Manual applications at the border were announced at a higher fee (N$2,000)."],
             ["Passport", "e-visa approval", "Return ticket"], [fee("visa on arrival / e-visa (non-African nationals)", 1600, "NAD", NAP)],
             src("Holiday visa services", "Ministry of Home Affairs, Immigration, Safety and Security, Namibia", NAP, "N$1,600 fee" + SNAP)),
    "kw": pv("kw", "Tourist e-Visa before travel (single entry, valid 30 days from issue, stay up to 90 days), or visa on arrival.",
             ["Apply on kuwaitvisa.moi.gov.kw; the portal shows the fee for your nationality at payment."], ["Passport valid 6 months from entry"],
             [fee("tourist e-Visa", 3, "KWD", KWP)],
             src("Tourist visa instructions", "Ministry of Interior, Kuwait", KWP, "KWD 3 standard fee" + SNAP),
             note="Fee can vary by nationality; confirm at payment."),
    "bh": pv("bh", "Tourist eVisa before travel (or visa on arrival, per Smartraveller).",
             ["Apply only on evisa.gov.bh."], ["Passport", "eVisa"],
             [fee("14-day single-entry eVisa (BD 9 plus BD 4 application)", 13, "BHD", BHP), fee("3-month multiple-entry eVisa", 29, "BHD", BHP)],
             src("eVisa service", "Government of Bahrain portal", BHP, "eVisa fees" + SNAP)),
})


# Batch F2 (2026-11-01)
QAP = "https://portal.moi.gov.qa/wps/wcm/connect/wcmlib-internet-en/sa-departmentcommittee/generaladministrationofnationalitybordersandexpatriateaffairs/visas/sad"
CMP = "https://www.diplocam.cm/e-visa/"
BJP = "https://catis.xroad.bj/publicservices/PS00005/eServiceSection"
DJP = "https://www.evisa.gouv.dj/"
PGP = "https://ica.gov.pg/visa-information/migration-service-fees"
LAP = "https://laoevisa.gov.la/fee-calculator"
BDP = "https://voa.specialbranch.gov.bd/public/voa-instructions.html"
TLP = "https://migracao.gov.tl/wp/tourist-visa/"
AZP = "https://evisa.gov.az/en/information"
RECHECKS.update({
    "qa": pv("qa", "Free multiple-entry tourist visa on arrival for 30 days, extendable once for 30 more.",
             ["Carry proof of accommodation (Smartraveller) and a return or onward ticket.", "Check the Ministry of Interior's health-insurance requirement before travel."],
             [PASSPORT_6M, "Return or onward ticket", "Accommodation proof"], [fee("tourist visa on arrival (30 days)", 0, "QAR", QAP)],
             src("Free tourist visas with multiple entries (30 days)", "Ministry of Interior, Qatar", QAP, "free, 30 days, extendable 30; Australia's listing read via snapshot" + SNAP)),
    "cm": pv("cm", "e-Visa before travel (no visa on arrival): pre-enrol online, then the visa is issued at entry.",
             ["Pre-enrol and pay on the official e-visa platform linked from MINREX.", "Carry a yellow fever certificate."],
             ["Passport", "e-Visa pre-enrolment receipt", "Yellow fever certificate"],
             [fee("short-stay visa, ordinary (6 months)", 100000, "XAF", CMP), fee("short-stay visa, express", 150000, "XAF", CMP)],
             src("e-Visa", "Ministry of External Relations (MINREX), Cameroon", CMP, "harmonised e-visa fees")),
    "bj": pv("bj", "e-Visa before travel on the official platform.",
             ["Apply on evisa.bj (government e-service).", "Carry a yellow fever certificate."], ["Passport", "e-Visa", "Yellow fever certificate"],
             [fee("tourist e-visa, 30 days single entry", 32798, "XOF", BJP), fee("tourist e-visa, 30 days multiple entry", 49197, "XOF", BJP)],
             src("Délivrance de visa électronique", "Government of Benin e-services (CatIS)", BJP, "30-day e-visa prices" + SNAP)),
    "dj": pv("dj", "e-Visa needed before travel.", ["Apply on evisa.gouv.dj; the charge is shown at payment."], ["Passport", "e-Visa"],
             [fee("short-stay e-visa (15 to 90 days)", 23, "USD", DJP)], src("Djibouti electronic visa platform", "Government of Djibouti", DJP, "e-visa fees" + SNAP)),
    "pg": pv("pg", "Tourist eVisa before travel: the visa itself is free, but online lodgement costs US$50 (charged in AUD).",
             ["Apply on evisa.ica.gov.pg; the AUD amount is shown before payment."], ["Passport", "eVisa"],
             [fee("tourist visa", 0, "PGK", PGP), fee("online lodgement service fee", 50, "USD", PGP)],
             src("Migration service fees", "Immigration and Citizenship Authority, PNG", PGP, "tourist visa nil, US$50 online lodgement" + SNAP)),
    "la": pv("la", "Tourist eVisa (single entry, 30 days, valid 60 days after approval) or visa on arrival at main checkpoints.",
             ["Use the fee calculator on laoevisa.gov.la (fees vary by nationality)."], ["Passport", "eVisa approval"],
             [fee("tourist eVisa (excluding bank charges)", 50, "USD", LAP)], src("Lao eVisa fee calculator", "Government of Lao PDR", LAP, "USD 50 tourist eVisa" + SNAP),
             note="Fee varies by nationality; confirm the Australian figure in the calculator."),
    "bd": pv("bd", "Visa on arrival (single entry, up to 30 days), or a visa from a Bangladesh mission before travel.",
             ["Fill in the VOA form on voa.specialbranch.gov.bd before arrival.", "Pay in cash (USD, EUR or GBP) at entry."], ["Passport", "Return ticket", "Hotel booking"],
             [fee("visa on arrival (excluding processing fee)", 50, "USD", BDP)],
             src("Visa-on-arrival instructions", "Special Branch, Bangladesh Police", BDP, "USD 50 VOA" + SNAP)),
    "tl": pv("tl", "Tourist visa on arrival at Dili airport or seaport, 30 days, US$30 cash. Land arrivals need prior authorisation.",
             ["Fill in the arrival declaration.", "Carry proof of funds, accommodation and onward travel if asked."],
             [PASSPORT_6M, "Arrival declaration", "US$30 cash"], [fee("tourist visa on arrival (30 days)", 30, "USD", TLP)],
             src("Tourist visa", "Migration Service of Timor-Leste", TLP, "US$30, 30 days, conditions" + SNAP)),
    "az": pv("az", "ASAN e-Visa before travel: single entry, valid 90 days, stay up to 30 days.",
             ["Apply on evisa.gov.az (standard 3 working days; urgent 3 hours costs more)."], ["Passport", "e-Visa"],
             [fee("standard e-Visa (USD 20 state fee + USD 9 service)", 29, "USD", AZP)],
             src("About e-Visa", "ASAN Visa, Republic of Azerbaijan", AZP, "USD 29 total" + SNAP)),
})
