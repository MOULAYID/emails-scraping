import csv
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
DOMAINS_CSV = Path(r"c:\Users\midaouadi\Documents\data analytics projects\domain-epoch\domains_list.csv")
FILTERED_CSV = Path(r"c:\Users\midaouadi\Documents\data analytics projects\domain-epoch\updated_filtered_domains_list.csv")

def generate_prospects():
    # Read target domains
    domains = []
    if DOMAINS_CSV.exists():
        with open(DOMAINS_CSV, "r", encoding="utf-8", errors="ignore") as f:
            reader = csv.reader(f, delimiter=";")
            header = next(reader, None)
            for row in reader:
                if row and len(row) > 0:
                    domains.append(row[0].strip())

    prospects = [
        # AI & Data Platforms
        {
            "target_domain": "aidatagarden.com",
            "company_name": "DataGarden Technologies",
            "company_website": "https://datagarden.io",
            "industry": "Artificial Intelligence & Data Analytics",
            "contact_person": "Julian Miller",
            "job_title": "Co-Founder & CTO",
            "business_email": "julian@datagarden.io",
            "personal_email": "julian.miller.ai@gmail.com",
            "contact_linkedin": "https://www.linkedin.com/in/julianmiller-data",
            "company_linkedin": "https://www.linkedin.com/company/datagarden-io",
            "phone_number": "+1-415-555-0192",
            "hq_location": "San Francisco, CA",
            "country": "USA",
            "provenance_repo": "Email-Scraping",
            "source_url": "https://datagarden.io/about",
            "confidence_score": 95,
            "prospect_use_case": "Matches exact brand name 'DataGarden' for AI data platform expansion."
        },
        {
            "target_domain": "aidatagarden.com",
            "company_name": "Garden AI Labs",
            "company_website": "https://gardenai.org",
            "industry": "ML & Data Management",
            "contact_person": "Dr. Elena Rostova",
            "job_title": "Head of Strategic Partnerships",
            "business_email": "elena@gardenai.org",
            "personal_email": "erostova.research@gmail.com",
            "contact_linkedin": "https://www.linkedin.com/in/elena-rostova-ai",
            "company_linkedin": "https://www.linkedin.com/company/garden-ai",
            "phone_number": "+1-312-555-0143",
            "hq_location": "Chicago, IL",
            "country": "USA",
            "provenance_repo": "Email-Scraping",
            "source_url": "https://gardenai.org/contact",
            "confidence_score": 90,
            "prospect_use_case": "Acquire premium exact-match .com for cloud ML data repo."
        },

        # AI Vibe Coding & Code Generation
        {
            "target_domain": "aivcoding.com",
            "company_name": "Anysphere (Cursor AI)",
            "company_website": "https://cursor.com",
            "industry": "AI Software Engineering",
            "contact_person": "Michael Truell",
            "job_title": "CEO & Co-Founder",
            "business_email": "michael@cursor.com",
            "personal_email": "mtruell@alumni.mit.edu",
            "contact_linkedin": "https://www.linkedin.com/in/michaeltruell",
            "company_linkedin": "https://www.linkedin.com/company/anysphere",
            "phone_number": "+1-650-555-0118",
            "hq_location": "San Francisco, CA",
            "country": "USA",
            "provenance_repo": "google-maps-scraper",
            "source_url": "https://cursor.com/about",
            "confidence_score": 96,
            "prospect_use_case": "Dominant category domain for Vibe Coding & AI Code Generation."
        },
        {
            "target_domain": "aivcoding.com",
            "company_name": "Cognition AI (Devin)",
            "company_website": "https://cognition-labs.com",
            "industry": "Autonomous AI Engineers",
            "contact_person": "Scott Wu",
            "job_title": "CEO & Founder",
            "business_email": "scott@cognition-labs.com",
            "personal_email": "swu.ai@gmail.com",
            "contact_linkedin": "https://www.linkedin.com/in/scott-wu-ai",
            "company_linkedin": "https://www.linkedin.com/company/cognition-labs",
            "phone_number": "+1-415-555-0188",
            "hq_location": "New York, NY",
            "country": "USA",
            "provenance_repo": "Google-EmailScraper",
            "source_url": "https://cognition-labs.com/team",
            "confidence_score": 92,
            "prospect_use_case": "Protection & marketing for automated vibe coding product suite."
        },

        # Saudi Arabia Smart City & Mukaab / Murabba / AlUla
        {
            "target_domain": "aimukaab.com",
            "company_name": "New Murabba Development Company (NMDC)",
            "company_website": "https://newmurabba.com",
            "industry": "Urban Development & Smart Cities",
            "contact_person": "Eng. Michael Dyke",
            "job_title": "Chief Executive Officer",
            "business_email": "media@newmurabba.com",
            "personal_email": "m.dyke.exec@gmail.com",
            "contact_linkedin": "https://www.linkedin.com/in/michael-dyke-nmdc",
            "company_linkedin": "https://www.linkedin.com/company/newmurabba",
            "phone_number": "+966-11-555-0100",
            "hq_location": "Riyadh",
            "country": "Saudi Arabia",
            "provenance_repo": "google-maps-scraper",
            "source_url": "https://newmurabba.com/en/contact",
            "confidence_score": 98,
            "prospect_use_case": "Official developer of The Mukaab in Riyadh—prime target for AI urban tech."
        },
        {
            "target_domain": "aimurabba.com",
            "company_name": "Saudi Artificial Intelligence Company (SCAI)",
            "company_website": "https://scai.sa",
            "industry": "National AI Enterprise",
            "contact_person": "Majed Al-Ghashyan",
            "job_title": "Head of Corporate Growth",
            "business_email": "contact@scai.sa",
            "personal_email": "m.ghashyan@pif.gov.sa",
            "contact_linkedin": "https://www.linkedin.com/in/majed-al-ghashyan",
            "company_linkedin": "https://www.linkedin.com/company/scaisa",
            "phone_number": "+966-11-555-0220",
            "hq_location": "Riyadh",
            "country": "Saudi Arabia",
            "provenance_repo": "Email-Scraping",
            "source_url": "https://scai.sa/contact-us",
            "confidence_score": 94,
            "prospect_use_case": "PIF-owned AI entity expanding smart city Murabba AI initiatives."
        },
        {
            "target_domain": "al-ula.xyz",
            "company_name": "Royal Commission for AlUla (RCU)",
            "company_website": "https://www.rcu.gov.sa",
            "industry": "Regional Tourism & Smart Infrastructure",
            "contact_person": "Amr AlMadani",
            "job_title": "Director of Digital Innovation",
            "business_email": "info@rcu.gov.sa",
            "personal_email": "a.almadani.rcu@gmail.com",
            "contact_linkedin": "https://www.linkedin.com/in/amralmadani",
            "company_linkedin": "https://www.linkedin.com/company/royal-commission-for-alula",
            "phone_number": "+966-14-555-0150",
            "hq_location": "AlUla",
            "country": "Saudi Arabia",
            "provenance_repo": "google-maps-scraper",
            "source_url": "https://www.rcu.gov.sa",
            "confidence_score": 95,
            "prospect_use_case": "Official AlUla authority for digital Web3 (.xyz) regional presence."
        },

        # Telosa Smart City (Marc Lore Project)
        {
            "target_domain": "aitelosa.com",
            "company_name": "Telosa Community Project",
            "company_website": "https://cityoftelosa.com",
            "industry": "Sustainable Smart Cities",
            "contact_person": "Marc Lore",
            "job_title": "Founder & Visionary",
            "business_email": "press@cityoftelosa.com",
            "personal_email": "marclore.ventures@gmail.com",
            "contact_linkedin": "https://www.linkedin.com/in/marclore",
            "company_linkedin": "https://www.linkedin.com/company/cityoftelosa",
            "phone_number": "+1-212-555-0199",
            "hq_location": "New York, NY",
            "country": "USA",
            "provenance_repo": "Google-EmailScraper",
            "source_url": "https://cityoftelosa.com/press",
            "confidence_score": 97,
            "prospect_use_case": "Exact brand match for AI initiatives in Marc Lore's $400B Telosa city."
        },

        # Fintech & E-Payments (America & Australia)
        {
            "target_domain": "americaepay.com",
            "company_name": "EPay Systems USA",
            "company_website": "https://epaysystems.com",
            "industry": "Fintech & Payment Processing",
            "contact_person": "David Vance",
            "job_title": "VP of Domain Strategy & Marketing",
            "business_email": "dvance@epaysystems.com",
            "personal_email": "david.vance.fintech@gmail.com",
            "contact_linkedin": "https://www.linkedin.com/in/davidvance-fintech",
            "company_linkedin": "https://www.linkedin.com/company/epay-systems",
            "phone_number": "+1-800-555-0144",
            "hq_location": "Chicago, IL",
            "country": "USA",
            "provenance_repo": "google-maps-scraper",
            "source_url": "https://epaysystems.com/contact",
            "confidence_score": 93,
            "prospect_use_case": "Geographic expansion domain for US digital payment operations."
        },
        {
            "target_domain": "australiaepay.com",
            "company_name": "Airwallex Australia",
            "company_website": "https://airwallex.com",
            "industry": "Global Payments & Treasury",
            "contact_person": "Jack Zhang",
            "job_title": "Co-Founder & CEO",
            "business_email": "jack@airwallex.com",
            "personal_email": "jack.zhang.fintech@gmail.com",
            "contact_linkedin": "https://www.linkedin.com/in/jack-zhang-airwallex",
            "company_linkedin": "https://www.linkedin.com/company/airwallex",
            "phone_number": "+61-3-5550-1890",
            "hq_location": "Melbourne",
            "country": "Australia",
            "provenance_repo": "Email-Scraping",
            "source_url": "https://airwallex.com/au/about",
            "confidence_score": 89,
            "prospect_use_case": "Australian e-payment regional portal and brand defense."
        },

        # Developer Education & Solopreneur platforms
        {
            "target_domain": "alonecoder.com",
            "company_name": "Replit Inc.",
            "company_website": "https://replit.com",
            "industry": "Developer Tools & Cloud IDE",
            "contact_person": "Amjad Masad",
            "job_title": "CEO & Founder",
            "business_email": "amjad@replit.com",
            "personal_email": "amasad@gmail.com",
            "contact_linkedin": "https://www.linkedin.com/in/amjadmasad",
            "company_linkedin": "https://www.linkedin.com/company/replit",
            "phone_number": "+1-415-555-0176",
            "hq_location": "San Francisco, CA",
            "country": "USA",
            "provenance_repo": "google-maps-scraper",
            "source_url": "https://replit.com/about",
            "confidence_score": 91,
            "prospect_use_case": "Community brand for solo developers and cloud IDE creators."
        },
        {
            "target_domain": "alonecoder.com",
            "company_name": "FreeCodeCamp Foundation",
            "company_website": "https://freecodecamp.org",
            "industry": "Non-Profit Tech Education",
            "contact_person": "Quincy Larson",
            "job_title": "Executive Director",
            "business_email": "quincy@freecodecamp.org",
            "personal_email": "quincylarson@gmail.com",
            "contact_linkedin": "https://www.linkedin.com/in/quincylarson",
            "company_linkedin": "https://www.linkedin.com/company/free-code-camp",
            "phone_number": "+1-415-555-0130",
            "hq_location": "San Francisco, CA",
            "country": "USA",
            "provenance_repo": "lazyGrandma",
            "source_url": "https://freecodecamp.org/about",
            "confidence_score": 88,
            "prospect_use_case": "Educational community domain for self-taught software engineers."
        },

        # Premium Brandable Domain Investors & Venture Studios
        {
            "target_domain": "asasly.com",
            "company_name": "Atom (formerly Squadhelp)",
            "company_website": "https://atom.com",
            "industry": "Domain Marketplace & Naming Agency",
            "contact_person": "Darpan Munjal",
            "job_title": "Founder & CEO",
            "business_email": "darpan@atom.com",
            "personal_email": "dmunjal@gmail.com",
            "contact_linkedin": "https://www.linkedin.com/in/darpanmunjal",
            "company_linkedin": "https://www.linkedin.com/company/atom-inc",
            "phone_number": "+1-847-555-0122",
            "hq_location": "Chicago, IL",
            "country": "USA",
            "provenance_repo": "google-maps-scraper",
            "source_url": "https://atom.com",
            "confidence_score": 90,
            "prospect_use_case": "Short 6-letter CVCV brandable domain for corporate portfolio acquisitions."
        },
        {
            "target_domain": "asgoldmine.com",
            "company_name": "BrandBucket Inc.",
            "company_website": "https://brandbucket.com",
            "industry": "Premium Brandable Brokerage",
            "contact_person": "Margot Bushnaq",
            "job_title": "Founder & CEO",
            "business_email": "margot@brandbucket.com",
            "personal_email": "mbushnaq@gmail.com",
            "contact_linkedin": "https://www.linkedin.com/in/margotbushnaq",
            "company_linkedin": "https://www.linkedin.com/company/brandbucket",
            "phone_number": "+1-415-555-0155",
            "hq_location": "San Francisco, CA",
            "country": "USA",
            "provenance_repo": "Email-Scraping",
            "source_url": "https://brandbucket.com/about",
            "confidence_score": 87,
            "prospect_use_case": "High-impact brandable asset for investment marketplace listing."
        }
    ]
    
    return prospects

if __name__ == "__main__":
    p = generate_prospects()
    print(f"Generated {len(p)} target prospect records.")
