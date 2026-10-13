#!/usr/bin/env python3
"""Builds the preview site into docs/ (GitHub Pages serves main:/docs). python3 build.py
Words: content.py + copy.json. Layout follows Shibga's default template (site 1): utility bar, sticky header,
hero with one CTA, service tiles, why-us, areas, CTA band, footer."""
import html, json, os, shutil
import content as C
# THE SWITCH. False = every page noindex,nofollow + robots.txt blocks all. Flip only after Shib approves.
INDEXABLE = False
ROOT = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(ROOT, "docs")
E = html.escape; B = C.BASE; N = C.BUSINESS_NAME
TEL = f"tel:{C.PHONE_TEL}"; SMS = f"sms:{C.PHONE_TEL}"
ICON = {"drain-cleaning":"M12 3v10m0 0-4-4m4 4 4-4M5 21h14M7 17h10","water-heater":"M8 3h8v18H8zM8 8h8M12 12v4","leak-repair":"M12 3c3 4 6 7 6 11a6 6 0 0 1-12 0c0-4 3-7 6-11z","sewer-line":"M3 8h18M3 16h18M7 8v8M17 8v8","toilet-faucet-fixtures":"M5 6h9a4 4 0 0 1 4 4v1M18 11v6M12 11v3M4 14h10","repiping":"M3 7h8v10h10M3 7V4M21 17v3","garbage-disposal":"M5 8h14l-2 12H7zM9 4h6M10 12v4M14 12v4","emergency-plumbing":"M12 3 2 20h20zM12 10v5M12 18v.5"}
def ic(slug, size=40):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="{ICON.get(slug,ICON["leak-repair"])}"/></svg>'

CSS = """:root{--navy:#10324d;--blue:#1d6fa5;--accent:#f08a1c;--bg:#f5f8fb;--ink:#1b2733;--mut:#5b6b7a}
*{box-sizing:border-box}body{margin:0;font:17px/1.65 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:#fff}
a{color:var(--blue)}h1,h2,h3{line-height:1.2;color:var(--navy)}h1{font-size:2.3rem;margin:.2em 0}h2{font-size:1.7rem}
.wrap{max-width:1100px;margin:auto;padding:0 18px}
.ribbon{background:#b3261e;color:#fff;text-align:center;font-weight:700;font-size:.85rem;padding:6px 10px;letter-spacing:.04em}
.util{background:var(--navy);color:#fff;font-size:.9rem;padding:7px 0}.util a{color:#fff;font-weight:700}
.util .wrap{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap}
header.top{position:sticky;top:0;background:#fff;border-bottom:1px solid #dde5ec;z-index:5}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:14px;padding-top:12px;padding-bottom:12px;flex-wrap:wrap}
.brand{font-weight:800;font-size:1.3rem;color:var(--navy);text-decoration:none}nav a{margin-left:16px;text-decoration:none;color:var(--ink);font-weight:600;font-size:.95rem}
.btn{display:inline-block;background:var(--accent);color:#1b1b1b!important;font-weight:800;padding:13px 24px;border-radius:6px;text-decoration:none;margin:4px 8px 4px 0}
.btn.alt{background:#fff;border:2px solid var(--navy);color:var(--navy)!important}
.hero{background:linear-gradient(135deg,var(--navy),var(--blue));color:#fff;padding:64px 0}.hero h1,.hero p{color:#fff}.hero p{max-width:640px;font-size:1.15rem}
.strip{background:var(--bg);padding:42px 0}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:18px}
.card{background:#fff;border:1px solid #dde5ec;border-radius:8px;padding:20px;text-decoration:none;color:var(--ink);display:block}.card svg{color:var(--blue)}.card h3{margin:.4em 0 .2em;font-size:1.1rem}.card p{margin:0;color:var(--mut);font-size:.95rem}
section.s{padding:48px 0}.why{background:var(--bg)}.band{background:var(--navy);color:#fff;text-align:center;padding:48px 0}.band h2{color:#fff}
.pill{display:inline-block;background:#fff;border:1px solid #cdd9e4;border-radius:999px;padding:8px 16px;margin:4px;text-decoration:none;font-weight:600}
.body p{max-width:760px}.body ul{max-width:760px}footer{background:#0b2236;color:#b9c6d2;padding:36px 0;font-size:.92rem}footer a{color:#fff}
.float{position:fixed;bottom:0;left:0;right:0;display:flex;z-index:9}.float a{flex:1;text-align:center;padding:14px;font-weight:800;text-decoration:none;color:#fff;background:var(--blue)}.float a+a{background:var(--accent);color:#1b1b1b}
body{padding-bottom:52px}@media(min-width:760px){.float{display:none}body{padding-bottom:0}}@media(max-width:640px){h1{font-size:1.8rem}nav{display:none}}"""

def layout(path, title, desc, h1, body, schema=True):
    robots = "" if INDEXABLE else '<meta name="robots" content="noindex,nofollow">\n'
    canon = C.SITE_URL + path
    nav = "".join(f'<a href="{B}{u}">{t}</a>' for u,t in [("/services/","Services"),("/service-areas/","Areas"),("/about/","About"),("/contact/","Contact")])
    ld = ""
    if schema:
        d = {"@context":"https://schema.org","@type":"Plumber","name":N,"url":canon.split("/",3)[0]+"//"+canon.split("/")[2]+B+"/",
             "areaServed":[{"@type":"City","name":c+", TN"} for _,c in C.AREAS],"foundingDate":str(C.SINCE)}
        ld = f'<script type="application/ld+json">{json.dumps(d)}</script>'
    return f"""<!doctype html><html lang="en-US"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
{robots}<link rel="canonical" href="{canon}">{ld}<style>{CSS}</style></head><body>
<div class="ribbon">DRAFT PREVIEW - business name unconfirmed - not a live website</div>
<div class="util"><div class="wrap"><span>Plumbing in Murfreesboro and Middle Tennessee</span><a href="{TEL}">Call {C.PHONE}</a></div></div>
<header class="top"><div class="wrap"><a class="brand" href="{B}/">{E(N)}</a><nav>{nav}</nav><a class="btn" href="{TEL}">Call Now</a></div></header>
{body}
<section class="band"><div class="wrap"><h2>Need a plumber in Middle Tennessee?</h2><p>Call or text to book an appointment.</p><a class="btn" href="{TEL}">Call {C.PHONE}</a><a class="btn alt" style="background:#fff" href="{SMS}">Text Us</a></div></section>
<footer><div class="wrap"><strong style="color:#fff">{E(N)}</strong> - plumbing, based in Murfreesboro, TN. Serving Middle Tennessee since {C.SINCE}.<br>
Service areas: {", ".join(c for _,c in C.AREAS)}.<br><a href="{TEL}">{C.PHONE}</a> - <a href="{B}/contact/">Contact</a> - <a href="{B}/service-areas/">Service areas</a><br>&copy; {E(N)}. Draft preview.</div></footer>
<div class="float"><a href="{TEL}">Call</a><a href="{SMS}">Text</a></div></body></html>"""

def write(path, html_):
    p = os.path.join(OUT, path.strip("/"), "index.html") if path != "/" else os.path.join(OUT, "index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "w").write(html_)

def copy_block(key):
    d = C.COPY[key]; f = lambda s: E(s.replace("{BIZ}", N))
    out = "".join(f"<p>{f(p)}</p>" for p in d["paras"])
    if d.get("bullets"): out += "<ul>" + "".join(f"<li>{f(b)}</li>" for b in d["bullets"]) + "</ul>"
    return out

def cta(): return f'<p><a class="btn" href="{TEL}">Call {C.PHONE}</a><a class="btn alt" href="{SMS}">Text Us</a></p>'
def tiles(): return '<div class="grid">' + "".join(f'<a class="card" href="{B}/services/{s}/">{ic(s)}<h3>{E(n)}</h3><p>{E(b)}</p></a>' for s,n,b in C.SERVICES) + "</div>"
def pills(): return "".join(f'<a class="pill" href="{B}/service-areas/{s}/">{c}</a>' for s,c in C.AREAS)

def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT); open(os.path.join(OUT,".nojekyll"),"w").close()
    pages = ["/"]
    # Home
    why = '<div class="grid">' + "".join(f'<div class="card"><h3>{E(t)}</h3><p>{E(d)}</p></div>' for t,d in C.WHY) + "</div>"
    body = f"""<div class="hero"><div class="wrap"><h1>Plumber in Murfreesboro, TN</h1><p>{E(N)} handles drains, water heaters, leaks, sewer lines and more for homeowners across Middle Tennessee. Call or text to book an appointment.</p>{cta()}</div></div>
<div class="strip"><div class="wrap"><h2>Plumbing services</h2>{tiles()}</div></div>
<section class="s why"><div class="wrap"><h2>Why homeowners call us</h2>{why}</div></section>
<section class="s"><div class="wrap body"><h2>Serving Murfreesboro, Columbia and Middle Tennessee</h2>{copy_block("home")}<p>{pills()}</p></div></section>"""
    write("/", layout("/", f"Plumber in Murfreesboro, TN | {N}", f"{N} is a Murfreesboro, TN plumbing company serving Middle Tennessee since {C.SINCE}. Call or text to book an appointment.", "", body))
    # Services hub
    pages.append("/services/")
    write("/services/", layout("/services/", f"Plumbing Services in Middle Tennessee | {N}", "Drain cleaning, water heaters, leak repair, sewer lines, fixtures, repiping, disposals and emergency plumbing.", "", f'<section class="s"><div class="wrap"><h1>Plumbing Services</h1><p>Residential plumbing from a Murfreesboro-based, owner-operated company.</p>{tiles()}{cta()}</div></section>'))
    for s,n,b in C.SERVICES:
        pages.append(f"/services/{s}/")
        body = f'<section class="s"><div class="wrap body"><h1>{E(n)} in Murfreesboro and Middle Tennessee</h1>{copy_block(s)}{cta()}<h2>Other plumbing services</h2>{tiles()}</div></section>'
        write(f"/services/{s}/", layout(f"/services/{s}/", f"{n} in Murfreesboro, TN | {N}", f"{n} from {N}, a Murfreesboro plumber serving Middle Tennessee. {b}", "", body))
    pages.append("/service-areas/")
    write("/service-areas/", layout("/service-areas/", f"Plumbing Service Areas: Murfreesboro, Columbia and More | {N}", "Plumbing service in Murfreesboro, Columbia, Franklin, Spring Hill, Brentwood and Nashville, TN.", "", f'<section class="s"><div class="wrap body"><h1>Service Areas</h1><p>Based in Murfreesboro, we serve homeowners across Middle Tennessee.</p><p>{pills()}</p>{cta()}</div></section>'))
    for s,c in C.AREAS:
        pages.append(f"/service-areas/{s}/")
        body = f'<section class="s"><div class="wrap body"><h1>Plumber in {c}, TN</h1>{copy_block(s)}{cta()}<h2>Plumbing services in {c}</h2>{tiles()}<h2>Other areas we serve</h2><p>{pills()}</p></div></section>'
        write(f"/service-areas/{s}/", layout(f"/service-areas/{s}/", f"Plumber in {c}, TN | {N}", f"Plumbing service in {c}, Tennessee from {N}. Drains, water heaters, leaks and more. Call or text to book.", "", body))
    pages.append("/about/")
    write("/about/", layout("/about/", f"About {N} | Murfreesboro, TN Plumbing", f"{N} is an owner-operated plumbing company in Murfreesboro, TN, serving Middle Tennessee since {C.SINCE}.", "", f'<section class="s"><div class="wrap body"><h1>About {E(N)}</h1>{copy_block("about")}{cta()}<h2>Why homeowners call us</h2>{why}</div></section>'))
    pages.append("/contact/")
    write("/contact/", layout("/contact/", f"Contact {N} | Call or Text for a Plumber", f"Call or text {N} to book a plumbing appointment in Murfreesboro, Columbia, Franklin, Spring Hill, Brentwood or Nashville.", "", f'<section class="s"><div class="wrap body"><h1>Contact {E(N)}</h1><p>The fastest way to reach us is to call or text. Tell us what is happening with your plumbing and we will book an appointment.</p><p style="font-size:1.4rem"><strong>{C.PHONE}</strong></p>{cta()}<p>We serve: {", ".join(c for _,c in C.AREAS)}.</p></div></section>', schema=True))
    write("/404.html".replace("/404.html","/404"), "<!doctype html><meta name=robots content='noindex,nofollow'><title>Not found</title><p>Page not found. <a href='%s/'>Home</a>" % B)
    shutil.move(os.path.join(OUT,"404","index.html"), os.path.join(OUT,"404.html")); os.rmdir(os.path.join(OUT,"404"))
    open(os.path.join(OUT,"robots.txt"),"w").write("User-agent: *\n" + ("Allow: /\n" if INDEXABLE else "Disallow: /\n"))
    print(len(pages), "pages built; INDEXABLE =", INDEXABLE)
if __name__ == "__main__": build()
