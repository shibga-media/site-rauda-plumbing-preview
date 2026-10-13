"""All words and facts for the preview site. Edit here, run build.py. Public repo: no private data."""
import json, os
BUSINESS_NAME = "D&Sons Plumbing"          # PLACEHOLDER - name unconfirmed (see internal checklist)
PHONE = "(615) 000-0000"                   # TODO-CALLRAIL: tracking number bought after agreement is signed
PHONE_TEL = "+16150000000"                 # TODO-CALLRAIL
SITE_URL = "https://shibga-media.github.io/site-rauda-plumbing-preview"   # becomes the real domain later
BASE = "/site-rauda-plumbing-preview"      # "" once a custom domain is attached
SINCE = 2020
COPY = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "copy.json")))

SERVICES = [  # slug, name, short blurb
 ("drain-cleaning", "Drain Cleaning", "Clogged sinks, tubs, showers and slow drains cleared."),
 ("water-heater", "Water Heater Repair & Installation", "Repair or replace a water heater that is failing or leaking."),
 ("leak-repair", "Leak Repair", "Track down and fix dripping pipes and supply line leaks."),
 ("sewer-line", "Sewer Line Service", "Backups, slow main drains, gurgling and sewer odors."),
 ("toilet-faucet-fixtures", "Toilet, Faucet & Fixture Repair", "Running toilets, dripping faucets and worn fixtures."),
 ("repiping", "Repiping", "Replace aging supply piping in your home."),
 ("garbage-disposal", "Garbage Disposal", "Jammed, leaking or humming disposals repaired or replaced."),
 ("emergency-plumbing", "Emergency Plumbing", "Burst pipes, major leaks, overflowing toilets and backups."),
]
AREAS = [  # slug, city
 ("murfreesboro", "Murfreesboro"), ("columbia", "Columbia"), ("smyrna", "Smyrna"), ("mount-juliet", "Mount Juliet"), ("franklin", "Franklin"),
 ("spring-hill", "Spring Hill"), ("brentwood", "Brentwood"), ("nashville", "Nashville"),
]
WHY = [
 ("Plumbing only", "We do one trade. Every call is a plumbing call."),
 ("Owner-operated", "A small local company, not a franchise call center."),
 ("Serving Middle Tennessee since 2020", "Based in Murfreesboro, working across the region."),
 ("Call or text to book", "Reach us by phone or text and book an appointment."),
]
