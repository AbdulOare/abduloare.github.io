#!/usr/bin/env python3
"""Generate the portfolio site's HTML from the content below.

Run from the repo root:  python3 _build/build.py
Writes index.html and work/*.html. Jekyll ignores folders that start with "_", so this script is not published.
House rule: no em dashes anywhere in the copy.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
SITE_URL = "https://abduloare.github.io/"
EMAIL = "abdul.oare@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/abduloare"
CLIPPINGS = "https://www.clippings.me/abduloare"
CV = "assets/docs/Abdulkerimu-Oare-CV.pdf"
BOOKING = "https://cal.com/abduloare/intro"
I_CAL = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="2.5" y="3.5" width="11" height="10" rx="2"/><path d="M2.5 7h11M5.5 2v3M10.5 2v3"/></svg>'


def book_btn(text="Book a call", cls="btn-primary"):
    return f'<a class="btn {cls}" href="{BOOKING}" target="_blank" rel="noopener" data-book>{I_CAL} {text}</a>'

# ---------- icons and motif ----------
CHEV = '<svg class="chev" viewBox="0 0 400 400" aria-hidden="true"><g fill="currentColor"><path d="M30 40h92l118 160-118 160H30l118-160z"/><path d="M176 40h92l118 160-118 160h-92l118-160z"/></g></svg>'
I_ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
I_BACK = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M13 8H3M7 4L3 8l4 4"/></svg>'
I_DOWN = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M8 2v9M4 7l4 4 4-4M3 14h10"/></svg>'
I_EXT = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M9 3h4v4M13 3L7 9M12 10v3H3V4h3"/></svg>'
I_PLAY = '<svg viewBox="0 0 12 12" fill="currentColor" aria-hidden="true"><path d="M3 1.5v9l7-4.5z"/></svg>'
I_MENU = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 6h14M3 10h14M3 14h14"/></svg>'
FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%2308D2DF'/%3E%3Ctext x='32' y='42' text-anchor='middle' font-family='Helvetica Neue,Helvetica,Arial' font-weight='700' font-size='28' letter-spacing='-1.5' fill='%23001414'%3EAO%3C/text%3E%3C/svg%3E"


def label(text):
    return f'<div class="label-row"><span class="pill">{text}</span></div>'


def head(title, desc, prefix, path=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="theme-color" content="#001414">
<link rel="canonical" href="{SITE_URL}{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{SITE_URL}{path}">
<meta property="og:image" content="{SITE_URL}assets/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def nav(prefix, current=""):
    home = prefix or "./"
    def item(href, text):
        cur = ' aria-current="page"' if text == current else ""
        return f'<li><a href="{home}{href}"{cur}>{text}</a></li>'
    return f"""<header class="nav">
  <div class="wrap">
    <a class="brand" href="{home}"><span class="mono">AO</span>Abdul Oare</a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false" aria-controls="nav-links">{I_MENU}</button>
    <ul class="nav-links" id="nav-links">
      {item('#work', 'Work')}
      {item('#services', 'Services')}
      {item('#experience', 'Experience')}
      {item('#about', 'About')}
      {item('#contact', 'Contact')}
      <li><a class="btn btn-primary" href="{prefix}{CV}" download>{I_DOWN} Download CV</a></li>
    </ul>
  </div>
</header>
"""


def footer(prefix):
    return f"""<footer class="footer">
  <div class="wrap">
    <span>&copy; 2026 Abdulkerimu Oare &middot; Abuja, Nigeria</span>
    <span><a href="mailto:{EMAIL}">{EMAIL}</a> &middot; <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></span>
  </div>
</footer>
<script src="{prefix}assets/js/site.js"></script>
</body>
</html>
"""


# ---------- content ----------
STATS = [
    ("70<small>+</small>", "integration interfaces documented at Afreximbank"),
    ("35", "training videos produced for one platform, about 53 minutes"),
    ("79", "help centre and knowledge base articles, built from zero for one platform"),
    ("2,000<small>+</small>", "professionals trained in strategic communication"),
    ("96<small>%</small>", "participant satisfaction in strategic communication training"),
    ("98<small>%</small>", "customer satisfaction with the Subkit knowledge base"),
]

CAPS = [
    ("Documentation", "User manuals, product documentation, solution design documents and integration guides, written to enterprise standards and kept current as products ship.",
     ["User manuals", "API and integration docs", "SDDs and BRDs", "Release notes"]),
    ("Knowledge management", "Help centres, knowledge bases and repositories that give people one source of truth, with the structure, style guides and templates to keep them that way.",
     ["Help centres", "Knowledge bases", "SharePoint", "Style guides and SOPs"]),
    ("Technology enablement", "Onboarding that gets people using a new system: product tours, quick guides, email series and walkthroughs aimed at adoption, not just reference.",
     ["Onboarding kits", "Quick guides", "Product tours", "Adoption"]),
    ("Instructional design", "Turning unstructured expertise into sequenced learning, with clear objectives, hands-on exercises and pre-workshop surveys that fit the audience and the time available.",
     ["Curriculum design", "Learning objectives", "Exercises", "Facilitator guides"]),
    ("Training and course development", "Training videos and course materials, from script to finished episode, using an AI-assisted pipeline where I write the scripts and check every claim.",
     ["Video series", "Scripts", "Gemini TTS", "Remotion"]),
    ("Facilitation", "Live workshops on strategic messaging, media literacy and information integrity, for national-level programmes, institutions and young people.",
     ["Workshops", "Strategic communication", "Media literacy", "Information integrity"]),
]

STEPS = [
    ("Learn the system", "I use the product end to end and interview the engineers and subject experts before writing anything, and I log the bugs and UX issues I find on the way."),
    ("Structure it", "I map content to real tasks and audiences: what each person needs to do, in what order, and where they will look for help."),
    ("Build the content", "Guides, manuals and videos, produced with docs as code and AI-assisted tooling, with every claim checked against the source."),
    ("Keep it current", "Style guides, templates, version control and a single source of truth, so the content stays accurate after I hand it over."),
]

TIMELINE = [
    ("Jul 2026 to Oct 2026", "Documentation and Training Lead (contract)", "My Car Importer, remote",
     "Built the customer help centre, a 49-article staff knowledge base, a 35-video training library and the onboarding kit from scratch.", "work/my-car-importer.html"),
    ("Jul 2024 to present", "Documentation Engineer (Middleware)", "Afreximbank, via Revent Technologies",
     "70+ middleware interfaces across Fiorano, Boomi, Kafka and SFTP; solution design documents, BRDs and user manuals, including the 129-page Vendor Management System manual.", "work/afreximbank-vms.html"),
    ("2023 to present", "Leadership Strategy Consultant and Facilitator", "Priori Orators",
     "Strategic communications training for national-level programmes: 2,000+ professionals trained, 96% satisfaction.", "work/stratcomms-training.html"),
    ("2026", "Lead Trainer, Media Literacy Workshops for Young People", "The Naija Collective",
     "Designed and led a filmed three-day programme on digital, media and information literacy.", "work/media-literacy.html"),
    ("Dec 2023 to May 2025", "Team Lead, Technical Writing", "Access Bank Plc",
     "Founded the bank's Technical Writing unit, with its style guide, templates, SOPs and SharePoint knowledge repository.", "work/access-bank-writing-unit.html"),
    ("2019 to 2023", "Lead Consultant and Senior Technical Writer", "Axon Consults",
     "B2B content, user guides and SOPs for IT service clients; lifted email open rates from 8% to over 20%.", None),
    ("2017 to 2023", "Senior Technical Writer (freelance)", "Upwork clients in the US, UK and Europe",
     "Built Subkit's knowledge base in HubSpot (98% customer satisfaction) and wrote Uphance ERP documentation.", None),
    ("2016 to 2018", "Managing Editor", "Obiaks Digital Media",
     "Ran editorial operations and publication standards for a news website and trained its writers.", None),
    ("2010 to 2016", "Earlier career", "London, UK",
     "Business development, technical writing and customer team leadership roles.", None),
]

# Project pages. "samples" entries: kind video | doc | deck | link
PROJECTS = [
    {
        "slug": "my-car-importer",
        "client": "My Car Importer · 2026",
        "title": "A help centre, knowledge base and video library, built from zero in three months",
        "card_title": "Help centre, knowledge base and 35-video training library",
        "summary": "My Car Importer buys cars at US auctions and ships them to Nigeria. Customers, car dealers and staff had no documentation and no training. I built all of it.",
        "card_summary": "Everything customers, dealers and staff need to use a US-to-Nigeria car import platform, from a blank page.",
        "tags": ["kb", "video", "training", "docs"],
        "tag_labels": ["Help centre", "Knowledge base", "Training video", "Onboarding"],
        "image": "assets/img/mci-p5-poster.jpg", "badge": "Video",
        "wide": True,
        "facts": [("Role", "Documentation and Training Lead"), ("Dates", "Jul 2026 to Oct 2026"), ("Engagement", "Remote contract"), ("Tools", "Docs as code, Gemini TTS, Remotion")],
        "kpis": [("30", "help centre guides in 7 collections"), ("49", "staff ERP knowledge base articles"), ("35", "training videos, about 53 minutes"), ("5", "emails in the onboarding series")],
        "sections": [
            ("The brief", ["<p>The platform has two products: a customer portal for bidding, shipping, payments and tracking, and an internal ERP that staff use to run orders, trucking, shipping, containers and finance. Neither had any documentation.</p>"]),
            ("What I did", ["<ul>"
                "<li>Walked through both products end to end before writing, and logged the bugs and UX issues I found for the engineers.</li>"
                "<li>Designed and wrote the customer help centre at <a href=\"https://mycarimporter.com/help\" target=\"_blank\" rel=\"noopener\">mycarimporter.com/help</a>: 30 task-based guides in 7 collections that follow the customer journey from sign-up to bidding, shipping, payments and delivery.</li>"
                "<li>Built a 49-article staff knowledge base for the ERP.</li>"
                "<li>Produced a 35-video training library (about 53 minutes) in three series: How to Become a Car Dealer (9 episodes), Using My Car Importer (11) and Staff Training (15). I adapted about 3 hours of raw staff recordings into structured episodes.</li>"
                "<li>Created the onboarding kit (narrated product tours and a 5-email series for new users) and wrote the system documentation from the codebase.</li>"
                "</ul>"]),
            ("How it was made", ["<p>I ran the documentation the way an engineering team runs code. Every guide is a Markdown file under version control, and scripts publish the help centre, check for broken links and add search metadata, so a guide can be updated the day the product changes. The guides carry 188 screenshots and GIFs.</p>",
                                 "<p>For the videos, AI did the repetitive work and I did the judgement. I wrote the scripts, an AI voice (Gemini text-to-speech) recorded the narration, and the episodes were assembled in code with Remotion, which made a 35-video library possible in three months. Whisper checked the captions, and I checked every fee, rule and figure against official sources before an episode went out.</p>"]),
        ],
        "samples_intro": "Two episodes from the customer-facing series. The staff series is internal and not shown.",
        "samples": [
            {"kind": "video", "src": "assets/video/mci-p5-bid-for-me.mp4", "poster": "assets/img/mci-p5-poster.jpg", "meta": "Using My Car Importer · Episode 5 · 1:08", "title": "Bid For Me", "text": "How customers get a car bought at auction without their own auction account."},
            {"kind": "video", "src": "assets/video/mci-d3-know-your-max-bid.mp4", "poster": "assets/img/mci-d3-poster.jpg", "meta": "How to Become a Car Dealer · Episode 3 · 2:02", "title": "Know your max bid", "text": "Setting a maximum bid that leaves room for the full landed cost of the car."},
            {"kind": "link", "href": "https://mycarimporter.com/help", "meta": "Live site", "title": "My Car Importer Help Centre", "text": "30 task-based guides in 7 collections, live on the product.", "wide": True},
        ],
    },
    {
        "slug": "afreximbank-vms",
        "client": "Afreximbank · 2024 to present",
        "title": "Vendor Management System: a 129-page user manual and quick guides",
        "card_title": "Vendor Management System user manual and quick guides",
        "summary": "Vendors across Africa register, get certified, submit work and get paid through Afreximbank's Vendor Management System. I wrote the documentation that walks them through it.",
        "card_summary": "A 129-page vendor manual, an 11-page Statement of Work quick guide and video walkthroughs for a pan-African bank's vendor portal.",
        "tags": ["docs", "training"],
        "tag_labels": ["User manual", "Quick guide", "Enterprise"],
        "image": "assets/img/vms-manual-cover.jpg", "badge": "PDF",
        "facts": [("Role", "Documentation Engineer"), ("Engagement", "Contract via Revent Technologies"), ("Audience", "External vendors"), ("Formats", "Manual, quick guides, video")],
        "kpis": [("129", "page vendor user manual (v1.2)"), ("11", "page SOW quick guide"), ("7", "steps from setup to Paid in the SOW flow"), ("2", "registration paths: individual and corporate")],
        "sections": [
            ("The brief", ["<p>The VMS covers the full vendor lifecycle: invitation, registration, KYC, re-certification, work requests, and the Statement of Work, timesheet and invoice module. Many vendors have never used the bank's systems before, so the documentation has to do the training.</p>"]),
            ("What I did", ["<ul>"
                "<li>Wrote the Vendor User Manual: 129 pages of step-by-step, screenshot-led tasks, from receiving an invitation to resubmitting KYC data and confirming payment.</li>"
                "<li>Condensed the Statement of Work module into an 11-page quick guide that shows the whole flow, from resource setup to Paid, on one page before going step by step.</li>"
                "<li>Produced video walkthroughs to go with the written guides.</li>"
                "<li>Kept the manual current through product phases (v1.2 adds the Phase 3 update).</li>"
                "</ul>"]),
        ],
        "samples_intro": "All three documents are classified Public.",
        "samples": [
            {"kind": "doc", "href": "assets/docs/afreximbank-vms-vendor-user-manual-sample.pdf", "img": "assets/img/vms-manual-p9.jpg", "meta": "PDF · 129 pages · 4.9 MB", "title": "Vendor User Manual v1.2", "text": "Registration, KYC, access, work requests, SOWs, timesheets and invoices."},
            {"kind": "doc", "href": "assets/docs/afreximbank-vms-sow-quick-guide-sample.pdf", "img": "assets/img/sow-guide-p3.jpg", "meta": "PDF · 11 pages · 0.7 MB", "title": "SOW Quick Guide for Vendors", "text": "The Statement of Work module from setup to Paid, in eleven pages."},
            {"kind": "drive", "href": "https://drive.google.com/file/d/1qo_4gJYCp6IOkuIVQu76yb82v0jZEkei/view?usp=drive_link", "img": "assets/img/vms-manual-old-cover.jpg", "meta": "PDF · 45 pages · Google Drive", "title": "Vendor User Manual, earlier edition", "text": "An earlier edition covering individual and corporate registration, KYC and contract management, with a glossary and FAQ.", "wide": True},
        ],
    },
    {
        "slug": "stratcomms-training",
        "client": "Priori Orators · 2023 to present",
        "title": "Strategic communications training for national-level programmes",
        "card_title": "STRATCOMMS: strategic messaging and information integrity",
        "summary": "I design and deliver strategic communications training for senior communicators, spokespersons and institutional leaders. In 2026 that included sessions for military communications and public relations officers.",
        "card_summary": "Sessions on strategic messaging, AI trends and information integrity for senior communicators. 2,000+ trained, 96% satisfaction.",
        "tags": ["training", "id"],
        "tag_labels": ["Facilitation", "Instructional design", "Strategic communication"],
        "image": "assets/img/stratcomms-messaging-cover.jpg", "badge": "Deck",
        "facts": [("Role", "Leadership Strategy Consultant and Facilitator"), ("Dates", "2023 to present"), ("Audience", "Senior communicators and leaders"), ("Format", "Live workshops, 90-minute sessions")],
        "kpis": [("2,000+", "professionals trained"), ("96%", "satisfaction rate"), ("90", "minute sessions, built to the clock"), ("3", "day programmes")],
        "sections": [
            ("The approach", ["<p>Each session is built around one deliverable participants produce under time pressure, not a lecture. Strategic Messaging ends with every table building and pitching a complete Message House. Social Media Warfare stress-tests those messages against an anonymised Nigerian composite case, in which a false claim outran the official correction.</p>"]),
            ("What I did", ["<ul>"
                "<li>Designed the session objectives, route maps, exercises and simulations, and wrote the facilitator materials.</li>"
                "<li>Built the decks as interactive HTML, with built-in timers for exercises, so they run in any browser without extra software.</li>"
                "<li>Delivered the sessions as part of multi-day programmes alongside other facilitators.</li>"
                "</ul>"]),
        ],
        "samples_intro": "Open the interactive version to see the decks as delivered, timers included, or download the PDF.",
        "samples": [
            {"kind": "deck", "html": "assets/decks/stratcomms-strategic-messaging.html", "pdf": "assets/decks/stratcomms-strategic-messaging.pdf", "img": "assets/img/stratcomms-messaging-cover.jpg", "meta": "Day 1 · 90 minutes · 29 slides", "title": "Strategic Messaging", "text": "Clear, aligned messages fitted to the audience, ending in a timed Message House workshop."},
            {"kind": "deck", "html": "assets/decks/stratcomms-social-media-warfare.html", "pdf": "assets/decks/stratcomms-social-media-warfare.pdf", "img": "assets/img/stratcomms-smw-cover.jpg", "meta": "Day 2 · 90 minutes · 30 slides", "title": "Social Media Warfare", "text": "Influence, information threats and AI: holding the terrain without losing the plot."},
        ],
    },
    {
        "slug": "media-literacy",
        "client": "The Naija Collective · 2026",
        "title": "Media literacy workshops for young people",
        "card_title": "A three-day media literacy programme for young people",
        "summary": "A filmed three-day programme that builds young people's resilience to misleading information, and equips them to pass what they learn on to friends and family.",
        "card_summary": "Three modules on digital literacy, critical reading and verification, with hands-on exercises built for young audiences.",
        "tags": ["training", "id"],
        "tag_labels": ["Course design", "Facilitation", "Media literacy"],
        "image": "assets/img/media-literacy-m1-cover.jpg", "badge": "Deck",
        "facts": [("Role", "Lead Trainer"), ("Year", "2026"), ("Audience", "Young people"), ("Format", "Three-day filmed programme")],
        "kpis": [("3", "days, one module each"), ("5", "post types in the closing exercise"), ("2", "hands-on exercises on Day 2"), ("3", "programme aims")],
        "sections": [
            ("Programme design", ["<p>Three aims hold the programme together: build resilience to misleading information, understand how widely it operates across social, digital and traditional media, and equip participants to share what they learn in their own words.</p>",
                                  "<ul><li><strong>Day 1:</strong> digital, media and information literacy. A working map of the landscape, the vocabulary to describe it, and first habits to use straight away.</li>"
                                  "<li><strong>Day 2:</strong> reading critically and investigative thinking. Persuasion tactics, bias and manipulation patterns, including an exercise where participants write the fake news themselves.</li>"
                                  "<li><strong>Day 3:</strong> fact-checking and verification, ending in a closing exercise on five posts (genuine, distorted, imposter, AI-generated and heuristic) that stays the same for every cohort so results can be compared.</li></ul>"]),
            ("What I did", ["<p>Designed the curriculum, built the module decks and the companion exercise deck, including pre-workshop surveys, timed exercises and take-home checklists, and led the sessions.</p>"]),
        ],
        "samples_intro": "Modules 1 and 2 and the Day 3 closing exercise, as interactive decks and PDFs.",
        "samples": [
            {"kind": "deck", "html": "assets/decks/media-literacy-module-1.html", "pdf": "assets/decks/media-literacy-module-1.pdf", "img": "assets/img/media-literacy-m1-cover.jpg", "meta": "Module 1 · Day 1 · 44 slides", "title": "Digital, Media and Information Literacy", "text": "The landscape, the vocabulary and the first habits."},
            {"kind": "deck", "html": "assets/decks/media-literacy-module-2.html", "pdf": "assets/decks/media-literacy-module-2.pdf", "img": "assets/img/media-literacy-m2-cover.jpg", "meta": "Module 2 · Day 2 · 38 slides", "title": "Reading Critically and Investigative Thinking", "text": "Three habits, six tactics, four ways propaganda scales."},
            {"kind": "deck", "html": "assets/decks/media-literacy-module-3.html", "pdf": "assets/decks/media-literacy-module-3.pdf", "img": "assets/img/media-literacy-m3-cover.jpg", "meta": "Module 3 · Closing exercise · 8 slides", "title": "Five Posts", "text": "The comparable closing exercise: CRAAP, triangulation, heuristics and AI checks.", "wide": True},
        ],
    },
    {
        "slug": "afreximbank-middleware",
        "client": "Afreximbank · 2024 to present",
        "title": "Middleware documentation at enterprise scale",
        "card_title": "Middleware documentation for 70+ integration interfaces",
        "summary": "One reliable reference for how a pan-African bank's systems connect, for the engineers who maintain them and the business teams who depend on them.",
        "card_summary": "Solution designs, requirements documents and interface documentation across Fiorano, Boomi, Kafka and SFTP.",
        "tags": ["docs", "kb"],
        "tag_labels": ["Integration docs", "SDDs and BRDs", "Architecture"],
        "text_media": ("70+", "interfaces documented"),
        "facts": [("Role", "Documentation Engineer (Middleware)"), ("Engagement", "Contract via Revent Technologies"), ("Platforms", "Fiorano, Boomi, Kafka, SFTP"), ("Audience", "Engineers, architects, business owners")],
        "sections": [
            ("What I did", ["<ul>"
                "<li>Own end-to-end documentation for multiple enterprise systems: integration flows, APIs, middleware processes and user guides.</li>"
                "<li>Documented 70+ integration interfaces across Fiorano, Boomi, Kafka, SFTP and event-driven architectures.</li>"
                "<li>Write solution design documents, business requirement documents and user manuals to enterprise governance standards, working daily with developers, architects and business owners.</li>"
                "<li>Document legacy and target-state architectures to support system migrations, so knowledge stays with the bank when people move on.</li>"
                "</ul>"]),
        ],
        "note": "This documentation is internal to the bank, so there are no samples here. I am happy to walk through how it is structured on a call.",
    },
    {
        "slug": "access-bank-writing-unit",
        "client": "Access Bank · 2023 to 2025",
        "title": "Building a technical writing unit from zero",
        "card_title": "Founding a bank's technical writing unit",
        "summary": "Access Bank had no technical writing function. I set one up: the team, the standards, the tools and the first priorities.",
        "card_summary": "Team, style guide, templates, SOPs and a SharePoint knowledge repository for an Africa-wide bank.",
        "tags": ["kb", "docs"],
        "tag_labels": ["Knowledge management", "Style guide", "Team building"],
        "text_media": ("From zero", "to a documentation function"),
        "facts": [("Role", "Team Lead, Technical Writing"), ("Dates", "Dec 2023 to May 2025"), ("Location", "Lagos, Nigeria"), ("Scope", "Group-wide digital products")],
        "sections": [
            ("What I did", ["<ul>"
                "<li>Founded the unit, and recruited, trained and led the writing team.</li>"
                "<li>Audited the bank's application catalogue and built a prioritisation matrix to decide which products to document first, based on user volume and adoption gaps.</li>"
                "<li>Authored the technical style guide, API and code documentation templates, and team SOPs.</li>"
                "<li>Set up a SharePoint knowledge repository as the single source of truth.</li>"
                "<li>Wrote user manuals and onboarding documentation to increase adoption of the bank's digital products across subsidiaries.</li>"
                "<li>Ran documentation gap analyses and introduced a configuration status accounting template for change tracking.</li>"
                "</ul>"]),
        ],
        "samples_intro": "How the unit was set up, in slides.",
        "samples": [
            {"kind": "drive", "href": "https://docs.google.com/presentation/d/1PRnHEDwbXF8xC-5iRKQZRlKDtgwimTmk/edit?usp=drive_link", "meta": "Slides · Google Drive", "title": "Building a Technical Writing Unit from Zero", "text": "The gap analysis, team, repository, style guide, templates and SOPs behind the unit.", "wide": True},
        ],
    },
]

FILTERS = [("all", "All work"), ("docs", "Documentation"), ("kb", "Knowledge bases"), ("video", "Training video"), ("training", "Training"), ("id", "Instructional design")]


# ---------- builders ----------
def card(p, prefix=""):
    tags = " ".join(p["tags"])
    wide = " wide" if p.get("wide") else ""
    if p.get("image"):
        icon = I_PLAY if p.get("badge") == "Video" else ""
        focus = f' style="object-position:{p["focus"]}"' if p.get("focus") else ""
        media = f'<div class="card-media"><img src="{prefix}{p["image"]}" alt="" loading="lazy"{focus}><span class="badge">{icon}{p["badge"]}</span></div>'
    else:
        big, small = p["text_media"]
        media = f'<div class="card-media text">{CHEV}<div><strong>{big}</strong><span>{small}</span></div></div>'
    tag_html = "".join(f'<span class="tag">{t}</span>' for t in p["tag_labels"])
    return f"""<a class="card{wide} reveal" href="{prefix}work/{p['slug']}.html" data-tags="{tags}">
  {media}
  <div class="card-body">
    <span class="client">{p['client']}</span>
    <h3>{p['card_title']}</h3>
    <p>{p['card_summary']}</p>
    <div class="card-tags">{tag_html}</div>
  </div>
</a>"""


def build_index():
    stats = "".join(f'<div class="stat"><b>{n}</b><span>{t}</span></div>' for n, t in STATS)
    caps = "".join(
        f'<article class="cap reveal"><span class="num">0{i}</span><h3>{t}</h3><p>{d}</p><ul>{"".join(f"<li class=tag>{x}</li>" for x in tags)}</ul></article>'
        for i, (t, d, tags) in enumerate(CAPS, 1))
    filters = "".join(f'<button class="filter" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{v}</button>' for k, v in FILTERS)
    cards = "\n".join(card(p) for p in PROJECTS)
    steps = "".join(f'<div class="step reveal"><span class="n">0{i}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(STEPS, 1))
    tl = ""
    for when, role, org, text, link in TIMELINE:
        lk = f'<a class="link" href="{link}">View work &rarr;</a>' if link else "<span></span>"
        tl += f'<li class="reveal"><span class="when">{when}</span><div><h3>{role}</h3><span class="org">{org}</span><p>{text}</p></div>{lk}</li>'

    html = head("Abdul Oare · Documentation, Knowledge and Learning Enablement",
                "Abdulkerimu (Abdul) Oare turns complex systems into knowledge people can use: documentation, knowledge bases, instructional design, training video and facilitation. Abuja, Nigeria, working remotely worldwide.",
                "", "")
    html += nav("", "")
    html += f"""<main id="main">
<section class="hero">
  <div class="wrap">
    {CHEV}
    {label("Documentation, Knowledge &amp; Learning Enablement")}
    <h1>I turn complex systems into <em>knowledge people can use.</em></h1>
    <div class="hero-row">
      <div>
        <p class="lede">When a new system launches, people need more than a login. I write the manuals, build the help centres and design the training that gets them using it, for organisations from Afreximbank and Access Bank to SaaS companies and national training programmes.</p>
        <div class="btn-row">
          {book_btn()}
          <a class="btn btn-ghost" href="#work">See the work {I_ARROW}</a>
        </div>
        <p class="alt-contact">Prefer to write first? <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <aside class="hero-clients" aria-label="Recent work with">
        <span class="k">Recent work with</span>
        <ul><li>Afreximbank</li><li>Access Bank</li><li>My Car Importer</li><li>Priori Orators</li><li>The Naija Collective</li><li>Subkit</li></ul>
      </aside>
    </div>
    <div class="hero-meta">
      <span><i class="dot-live"></i>Available for remote contracts and consultancies</span>
      <span>Abuja, Nigeria (GMT+1)</span>
    </div>
  </div>
</section>

<section class="section light" aria-label="Key numbers" style="padding-top:clamp(56px,7vw,88px);padding-bottom:clamp(56px,7vw,88px)">
  <div class="wrap"><div class="stats">{stats}</div></div>
</section>

<section class="section" id="services">
  <div class="wrap">
    <div class="section-head">
      <div>{label("What I do")}<h2>Six disciplines, one goal: people who can use the system.</h2></div>
      <p class="lede">Most projects need more than one. A new platform needs documentation, a knowledge base, onboarding and training, and the best results come when one person designs them to work together.</p>
    </div>
    <div class="caps">{caps}</div>
  </div>
</section>

<section class="section light" id="work">
  <div class="wrap">
    <div class="section-head">
      <div>{label("Selected work")}<h2>Manuals, help centres, video and workshops.</h2></div>
      <p class="lede">Each project opens with the brief, what I did and, where the client allows, the real documents and videos.</p>
    </div>
    <div class="filters" role="group" aria-label="Filter work">{filters}</div>
    <div class="work">
{cards}
    </div>
    <div class="also">
      <div><h4>Subkit knowledge base</h4><p>Built from scratch in HubSpot for a New York subscription SaaS's v2 launch. Rated 98% in customer satisfaction.</p></div>
      <div><h4>Uphance ERP documentation</h4><p>Knowledge base articles, tutorials and release notes for a cloud ERP for fashion brands; introduced version control.</p></div>
      <div><h4>UN and development consulting</h4><p>Registered UN Global Marketplace (UNGM) vendor, available for UN and development communications and knowledge management work.</p></div>
      <div><h4>Published writing</h4><p>Articles and editorial work, collected in one place. <a href="{CLIPPINGS}" target="_blank" rel="noopener">Read on clippings.me</a></p></div>
    </div>
  </div>
</section>

<section class="section" id="approach">
  <div class="wrap">
    <div class="section-head">
      <div>{label("How I work")}<h2>Understand it first. Then make it easy to learn.</h2></div>
      <p class="lede">The same four steps, whether the output is a manual, a knowledge base or a video series.</p>
    </div>
    <div class="steps">{steps}</div>
  </div>
</section>

<section class="section" id="experience" style="padding-top:0">
  <div class="wrap">
    <div class="section-head">
      <div>{label("Experience")}<h2>More than ten years of making complex things clear.</h2></div>
      <p class="lede">Banking, SaaS, logistics, media and public institutions, in Nigeria, the UK and remotely worldwide.</p>
    </div>
    <ol class="timeline">{tl}</ol>
  </div>
</section>

<section class="section light" id="about">
  <div class="wrap about-grid">
    <div>{label("About")}<h2>Writer, trainer and systems thinker.</h2></div>
    <div class="about-copy">
      <p>I'm Abdulkerimu Oare, Abdul to most people. I've spent more than ten years in writing and documentation, eight of them documenting SaaS and enterprise software, and alongside that I train people in strategic communication.</p>
      <p>I'm often the person who builds the documentation function from scratch: a bank's first technical writing unit, a SaaS product's knowledge base, a car import platform's entire help centre and training library. I work directly with engineers, product managers and support teams, and treat documentation and training as part of the product.</p>
      <p>I'm based in Abuja, Nigeria, after six years working in London, and I work remotely with teams worldwide.</p>
      <div class="creds">
        <div>
          <h4>Education and certification</h4>
          <ul>
            <li>BA (Hons) Business and Management, University of Sunderland, 2013</li>
            <li>Advanced Diploma in Management Practice (Distinction), University of Ulster, 2012</li>
            <li>HubSpot Inbound Certified</li>
            <li>HubSpot Content Marketing Certified</li>
          </ul>
        </div>
        <div>
          <h4>Tools and methods</h4>
          <div class="tools">
            {"".join(f'<span class="tag">{t}</span>' for t in ["Markdown", "Git and GitHub", "HubSpot KB", "Intercom", "SharePoint", "WordPress", "HTML/CSS", "Remotion", "Gemini TTS", "Whisper", "REST APIs", "Boomi", "Fiorano", "Kafka", "SFTP", "SME interviews", "Content audits", "Usability testing", "Agile/SDLC"])}
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section contact" id="contact" style="overflow:hidden">
  <div class="wrap">
    {CHEV}
    {label("Contact")}
    <h2>Have a system people need to learn?</h2>
    <p class="lede">Book a 30-minute call, or email me about the product, the audience and the deadline.</p>
    <div class="btn-row" style="margin-top:32px">
      {book_btn()}
      <a class="btn btn-ghost" href="mailto:{EMAIL}">Email me</a>
      <a class="btn btn-ghost" href="{CV}" download>{I_DOWN} Download CV</a>
    </div>
    <div class="contact-links">
      <a href="mailto:{EMAIL}"><small>Email</small><span>{EMAIL}</span></a>
      <a href="{LINKEDIN}" target="_blank" rel="noopener"><small>LinkedIn</small><span>in/abduloare</span></a>
      <a href="{CLIPPINGS}" target="_blank" rel="noopener"><small>Published writing</small><span>clippings.me/abduloare</span></a>
      <a href="{CV}" download><small>CV</small><span>PDF, 2 pages</span></a>
    </div>
  </div>
</section>
</main>
"""
    html += footer("")
    (ROOT / "index.html").write_text(html, encoding="utf-8")


def sample_html(s, prefix):
    wide = " wide" if s.get("wide") else ""
    if s["kind"] == "video":
        return f"""<article class="sample{wide}">
  <video controls preload="none" playsinline poster="{prefix}{s['poster']}"><source src="{prefix}{s['src']}" type="video/mp4">Your browser cannot play this video. <a href="{prefix}{s['src']}">Download it</a>.</video>
  <div class="sample-body"><small>{s['meta']}</small><h3>{s['title']}</h3><p>{s['text']}</p></div>
</article>"""
    if s["kind"] == "doc":
        return f"""<article class="sample{wide}">
  <a class="thumb" href="{prefix}{s['href']}" target="_blank" rel="noopener"><img src="{prefix}{s['img']}" alt="A page from {escape(s['title'])}" loading="lazy"></a>
  <div class="sample-body"><small>{s['meta']}</small><h3>{s['title']}</h3><p>{s['text']}</p>
    <div class="btn-row"><a class="btn btn-primary" href="{prefix}{s['href']}" target="_blank" rel="noopener">Read online {I_EXT}</a><a class="btn btn-ghost" href="{prefix}{s['href']}" download>{I_DOWN} Download</a></div>
  </div>
</article>"""
    if s["kind"] == "drive":
        thumb = ""
        if s.get("img"):
            thumb = f'<a class="thumb" href="{s["href"]}" target="_blank" rel="noopener"><img src="{prefix}{s["img"]}" alt="Cover of {escape(s["title"])}" loading="lazy"></a>'
        return f"""<article class="sample{wide}">
  {thumb}
  <div class="sample-body"><small>{s['meta']}</small><h3>{s['title']}</h3><p>{s['text']}</p>
    <div class="btn-row"><a class="btn btn-primary" href="{s['href']}" target="_blank" rel="noopener">Open in Google Drive {I_EXT}</a></div>
  </div>
</article>"""
    if s["kind"] == "deck":
        return f"""<article class="sample{wide}">
  <a class="thumb" href="{prefix}{s['html']}" target="_blank" rel="noopener"><img src="{prefix}{s['img']}" alt="Title slide of {escape(s['title'])}" loading="lazy"></a>
  <div class="sample-body"><small>{s['meta']}</small><h3>{s['title']}</h3><p>{s['text']}</p>
    <div class="btn-row"><a class="btn btn-primary" href="{prefix}{s['html']}" target="_blank" rel="noopener">Open interactive deck {I_EXT}</a><a class="btn btn-ghost" href="{prefix}{s['pdf']}" target="_blank" rel="noopener">PDF</a></div>
  </div>
</article>"""
    return f"""<article class="sample{wide}">
  <div class="sample-body"><small>{s['meta']}</small><h3>{s['title']}</h3><p>{s['text']}</p>
    <div class="btn-row"><a class="btn btn-primary" href="{s['href']}" target="_blank" rel="noopener">Visit the help centre {I_EXT}</a></div>
  </div>
</article>"""


def build_project(i, p):
    prefix = "../"
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    facts = "".join(f"<div><small>{k}</small><span>{v}</span></div>" for k, v in p["facts"])
    kpis = ""
    if p.get("kpis"):
        kpis = '<div class="kpis">' + "".join(f"<div><b>{n}</b><span>{t}</span></div>" for n, t in p["kpis"]) + "</div>"
    body = ""
    for j, (h, parts) in enumerate(p["sections"]):
        extra = kpis if j == 0 else ""
        body += f'<div class="p-body reveal"><h2>{h}</h2><div class="copy">{extra}{"".join(parts)}</div></div>'
    if p.get("note"):
        body += f'<div class="p-body reveal"><h2>Samples</h2><div class="copy"><p class="note">{p["note"]}</p></div></div>'

    samples = ""
    if p.get("samples"):
        items = "\n".join(sample_html(s, prefix) for s in p["samples"])
        samples = f"""<section class="section">
  <div class="wrap">
    <div class="section-head"><div>{label("Samples")}<h2>See the work.</h2></div><p class="lede">{p['samples_intro']}</p></div>
    <div class="samples">{items}</div>
  </div>
</section>"""

    next_cls = " light" if p.get("samples") else ""
    html = head(f"{p['card_title']} · Abdul Oare", p["summary"], prefix, f"work/{p['slug']}.html")
    html += nav(prefix)
    html += f"""<main id="main">
<section class="p-hero">
  <div class="wrap">
    {CHEV}
    <a class="crumb" href="../#work">{I_BACK} All work</a>
    {label(p['client'])}
    <h1>{p['title']}</h1>
    <p class="lede">{p['summary']}</p>
    <div class="facts">{facts}</div>
  </div>
</section>
<section class="section light">
  <div class="wrap">{body}</div>
</section>
{samples}
<section class="section{next_cls}" style="padding:clamp(48px,6vw,72px) 0">
  <div class="wrap next">
    <div><span class="muted" style="display:block;margin-bottom:8px;font-size:.9rem">Next project</span><a class="big" href="{nxt['slug']}.html">{nxt['card_title']} &rarr;</a></div>
    <div class="btn-row">{book_btn()}<a class="btn btn-ghost" href="mailto:{EMAIL}">Email me</a></div>
  </div>
</section>
</main>
"""
    html += footer(prefix)
    (ROOT / "work" / f"{p['slug']}.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    (ROOT / "work").mkdir(exist_ok=True)
    build_index()
    for i, p in enumerate(PROJECTS):
        build_project(i, p)
    # guard the house rule
    for f in [ROOT / "index.html", *(ROOT / "work").glob("*.html")]:
        if "\u2014" in f.read_text(encoding="utf-8"):
            raise SystemExit(f"Em dash found in {f}")
    print("Built index.html and", len(PROJECTS), "project pages")
