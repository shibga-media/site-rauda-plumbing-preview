"""All words and facts for the D and Sons Plumbing preview site. Edit here, then run: python3 build.py (rewrites docs/).
Public repo: no private data. Draft = noindex until David signs and a domain exists. No licence claims."""
import json, os

INDEXABLE = False       # preview only: every page noindex + robots.txt blocks all. Flip when David signs and a domain is attached.

SITE = {
    "domain": "https://shibga-media.github.io/site-rauda-plumbing-preview",
    "base": "/site-rauda-plumbing-preview",              # "" once a custom domain is attached
    "name": "D and Sons Plumbing",                       # confirmed on David's own SEF (12 Oct 2026)
    "phone_display": "(615) 000-0000",                   # PLACEHOLDER - tracking number bought after the agreement is signed
    "phone_tel": "+16150000000",
    "phone_e164": "+1-615-000-0000",
    "sms_tel": "+16150000000",
    "email": None,
    "street": None,                                      # home address: never shown
    "city": "Murfreesboro", "region": "TN", "zip": "",
    "schema_type": "Plumber",
    "founded_year": 2020,
}
PALETTE = {"brand": "#1f5fa6", "brand_dk": "#174a82", "accent": "#f08a1c", "dark": "#14283d"}   # blue + orange

COPY = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "copy.json")))

SERVICES = [
    ("drain-cleaning", "Drain Cleaning", "Clogged sinks, tubs, showers and slow drains cleared."),
    ("water-heater", "Water Heater Repair & Installation", "Repair or replace a water heater that is failing or leaking."),
    ("leak-repair", "Leak Repair", "Track down and fix dripping pipes and supply line leaks."),
    ("sewer-line", "Sewer Line Service", "Backups, slow main drains, gurgling and sewer odors."),
    ("toilet-faucet-fixtures", "Toilet, Faucet & Fixture Repair", "Running toilets, dripping faucets and worn fixtures."),
    ("repiping", "Repiping", "Replace aging supply piping in your home."),
    ("garbage-disposal", "Garbage Disposal", "Jammed, leaking or humming disposals repaired or replaced."),
    ("emergency-plumbing", "Emergency Plumbing", "Burst pipes, major leaks, overflowing toilets and backups."),
]
AREAS = [("murfreesboro", "Murfreesboro"), ("columbia", "Columbia"), ("smyrna", "Smyrna"), ("mount-juliet", "Mount Juliet"),
         ("franklin", "Franklin"), ("spring-hill", "Spring Hill"), ("brentwood", "Brentwood"), ("nashville", "Nashville")]
WHY = [
    ("focus", "Plumbing only", "We do one trade. Every call is a plumbing call."),
    ("owner", "Owner-operated", "A small local company, not a franchise call center."),
    ("local", "Serving Middle Tennessee since 2020", "Based in Murfreesboro, working across the region."),
    ("call", "Call or text to book", "Reach us by phone or text and book an appointment."),
]
STRIP = [("drain-cleaning", "Drain cleaning"), ("water-heater", "Water heaters"), ("leak-repair", "Leak repair"),
         ("emergency-plumbing", "Emergency plumbing")]

LOGO_TOP = "D AND SONS PLUMBING"
LOGO_SUB = "Murfreesboro, TN"
TOPBAR = "Plumbing in Murfreesboro and Middle Tennessee"
TOPBAR2 = "Owner-operated · plumbing only"
TOPBAR_CALL = "Call or text"
EYEBROW = "Owner-operated plumbing · Murfreesboro, TN"
HERO_BTN = "Call to book"
ASIDE_TITLE = "Call or text to book"
LEGAL_LINE = "Plumbing, Murfreesboro, TN. Serving Middle Tennessee since 2020"
WHY_TITLE = "Why homeowners call us"
HOME_H2 = "Serving Murfreesboro, Columbia and Middle Tennessee"
HERO_CARD = {"title": "Call or text to book", "text": "Tell us what is happening and we will set up an appointment. There is no online form to fill out.",
             "ticks": ["Plumbing is the only trade we do", "Owner-operated, based in Murfreesboro", "Serving Middle Tennessee since 2020"]}
CTA = {"title": "Need a plumber in Middle Tennessee?", "text": "Call or text to book an appointment."}

HOME = dict(
    title="Plumber in Murfreesboro, TN | D and Sons Plumbing",
    description="D and Sons Plumbing is a Murfreesboro, TN plumbing company serving Middle Tennessee since 2020. Call or text to book an appointment.",
    h1="Plumber in Murfreesboro, TN",
    lead="{BIZ} handles drains, water heaters, leaks, sewer lines and more for homeowners across Middle Tennessee. Call or text to book an appointment.")
SERVICES_HUB = dict(
    title="Plumbing Services in Middle Tennessee | D and Sons Plumbing",
    description="Drain cleaning, water heaters, leak repair, sewer lines, fixtures, repiping, disposals and emergency plumbing.",
    h1="Plumbing Services", lead="Residential plumbing from a Murfreesboro-based, owner-operated company.")
SERVICE_TITLE = "{n} in Murfreesboro, TN | D and Sons Plumbing"
SERVICE_DESC = "{n} from D and Sons Plumbing, a Murfreesboro plumber serving Middle Tennessee. {b}"
SERVICE_H1 = "{n} in Murfreesboro and Middle Tennessee"
AREAS_HUB = dict(
    title="Plumbing Service Areas: Murfreesboro, Columbia and More | D and Sons Plumbing",
    description="Plumbing service in Murfreesboro, Columbia, Franklin, Spring Hill, Brentwood and Nashville, TN.",
    h1="Service Areas", lead="Based in Murfreesboro, we serve homeowners across Middle Tennessee.")
AREA_TITLE = "Plumber in {c}, TN | D and Sons Plumbing"
AREA_DESC = "Plumbing service in {c}, Tennessee from D and Sons Plumbing. Drains, water heaters, leaks and more. Call or text to book."
AREA_H1 = "Plumber in {c}, TN"
AREA_LEAD = "Plumbing service in {c}, Tennessee. Call or text to book an appointment."
ABOUT = dict(
    title="About D and Sons Plumbing | Murfreesboro, TN Plumbing",
    description="D and Sons Plumbing is an owner-operated plumbing company in Murfreesboro, TN, serving Middle Tennessee since 2020.",
    h1=("About", "D and Sons Plumbing"), lead="")
CONTACT = dict(
    title="Contact D and Sons Plumbing | Call or Text for a Plumber",
    description="Call or text D and Sons Plumbing to book a plumbing appointment in Murfreesboro, Columbia, Franklin, Spring Hill, Brentwood or Nashville.",
    h1=("Contact", "D and Sons Plumbing"),
    lead="The fastest way to reach us is to call or text. Tell us what is happening with your plumbing and we will book an appointment.",
    after="We serve: Murfreesboro, Columbia, Smyrna, Mount Juliet, Franklin, Spring Hill, Brentwood and Nashville.")
