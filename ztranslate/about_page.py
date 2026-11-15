"""About page in the zapps.ltd look: one HTML page, built each time it is
opened so the developers team is listed in a random order, and shown in
the default browser. Nothing on the page loads from the internet; its
links open only when they are clicked."""

import html
import os
import random

SUPPORT_EMAIL = "support@zapps.ltd"
HOME_PAGE = "https://zapps.ltd"
TEAM = ("Harith", "Mesar")

CSS = """
:root { color-scheme: light dark; --bg: #f4f6fb; --card: #ffffff;
  --text: #1a1e29; --muted: #4b5366; --accent: #1d5bbf; --on-accent: #ffffff;
  --border: #d8dce6; --focus: #ffb000; }
@media (prefers-color-scheme: dark) { :root { --bg: #11141b; --card: #1a1f2c;
  --text: #eef1f7; --muted: #bcc3d2; --accent: #8ab4ff; --on-accent: #0b1220;
  --border: #2c3346; } }
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--text);
  font: 17px/1.6 "Segoe UI", system-ui, -apple-system, Roboto, sans-serif; }
main { max-width: 46rem; margin: 0 auto; padding: 1.5rem 1.1rem 2.5rem; }
.hero { background: linear-gradient(135deg, #1d5bbf, #6a3fc2); color: #ffffff;
  border-radius: 18px; padding: 1.6rem 1.5rem; margin-bottom: 1.25rem; }
.hero h1 { margin: 0 0 .35rem; font-size: 1.9rem; line-height: 1.25; }
.hero p { margin: .15rem 0; }
.hero .by { font-size: 1.15rem; font-weight: 600; }
section { background: var(--card); border: 1px solid var(--border);
  border-radius: 14px; padding: 1.1rem 1.4rem; margin: 0 0 1rem; }
h2 { margin: 0 0 .6rem; font-size: 1.3rem; color: var(--accent); }
ul { margin: .3rem 0; padding-inline-start: 1.3rem; }
li { margin-bottom: .4rem; }
a { color: var(--accent); }
.buttons { display: flex; flex-wrap: wrap; gap: .6rem; margin: .4rem 0 0; }
a.button { display: inline-block; background: var(--accent); color: var(--on-accent);
  padding: .65rem 1.15rem; border-radius: 10px; text-decoration: none; font-weight: 600; }
a.button.secondary { background: transparent; color: var(--accent);
  border: 2px solid var(--accent); }
a:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
footer { color: var(--muted); text-align: center; font-size: .95rem; margin-top: 1.4rem; }
@media (forced-colors: active) { .hero { background: Canvas; color: CanvasText;
  border: 1px solid CanvasText; } a.button { border: 2px solid LinkText; } }
"""


def _plain(key, default, **values):
    return default.format(**values) if values else default


def _block(item):
    if isinstance(item, (list, tuple)):
        return "<ul>%s</ul>" % "".join(
            "<li>%s</li>" % html.escape(str(x)) for x in item)
    return "<p>%s</p>" % html.escape(str(item))


def build_html(app, version, sections, credits, license_line="", t=_plain,
               rtl=False, lang_code="en", static_team=False):
    """sections: [(heading, [paragraph or [items]])]; credits: [str]."""
    e = html.escape
    first, second = random.sample(TEAM, 2)
    title = t("title", "About {app}", app=app)
    out = ['<!DOCTYPE html>',
           '<html lang="%s" dir="%s">' % (e(lang_code), "rtl" if rtl else "ltr"),
           '<head>', '<meta charset="utf-8">',
           '<meta name="viewport" content="width=device-width, initial-scale=1">',
           '<title>%s</title>' % e(title), '<style>%s</style>' % CSS, '</head>',
           '<body>', '<main>', '<header class="hero">',
           '<h1>%s</h1>' % e(title),
           '<p class="by">%s</p>' % e(t("by", "By zapps-ltd"))]
    if version:
        out.append('<p>%s</p>' % e(t("version", "Version {version}", version=version)))
    out.append('</header>')
    for heading, blocks in sections:
        out.append('<section>')
        out.append('<h2>%s</h2>' % e(heading))
        out.extend(_block(b) for b in blocks)
        out.append('</section>')
    team = t("team", "zapps.ltd developers: {first} and {second}",
             first="\x00a", second="\x00b")
    team = e(team)
    if static_team:
        team = team.replace("\x00a", '<span id="team-first">%s</span>' % TEAM[0])
        team = team.replace("\x00b", '<span id="team-second">%s</span>' % TEAM[1])
    else:
        team = team.replace("\x00a", e(first)).replace("\x00b", e(second))
    out += ['<section>', '<h2>%s</h2>' % e(t("team_heading", "Developers team")),
            '<p>%s</p>' % team, '</section>',
            '<section>', '<h2>%s</h2>' % e(t("contact_heading", "Contact")),
            '<p class="buttons"><a class="button" href="mailto:%s">%s</a>'
            ' <a class="button secondary" href="%s">%s</a></p>' % (
                SUPPORT_EMAIL, e(t("email", "Email {email}", email=SUPPORT_EMAIL)),
                HOME_PAGE, e(t("home", "Visit zapps.ltd"))),
            '</section>']
    if credits or license_line:
        out += ['<section>', '<h2>%s</h2>' % e(t("credits_heading", "Credits and licenses"))]
        if credits:
            out.append(_block(list(credits)))
        if license_line:
            out.append(_block(license_line))
        out.append('</section>')
    out += ['<footer><p>%s</p></footer>' % e(t(
        "copyright", "Copyright © 2026 ZAPPS SOFTWARE LTD.")), '</main>']
    if static_team:
        out.append('<script>(function () { if (Math.random() < 0.5) {'
                   ' var a = document.getElementById("team-first"),'
                   ' b = document.getElementById("team-second");'
                   ' if (a && b) { var x = a.textContent; a.textContent = b.textContent;'
                   ' b.textContent = x; } } })();</script>')
    out += ['</body>', '</html>', '']
    return "\n".join(out)


def open_page(folder, page):
    """Write the page into folder (inside the app's own data) and open it
    in the default browser."""
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "about.html")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(page)
    os.startfile(path)
    return path


def show_about():
    """The About page for ZTranslate, written into its settings folder."""
    from . import __version__, config
    sections = [("What it does", [
        "ZTranslate translates the text you select or focus, with global "
        "hotkeys, speaks the translation and can copy it to the clipboard."])]
    credits = [
        "wxPython - wxWindows Library Licence",
        "pywin32 - Python Software Foundation License",
        "comtypes - MIT License",
        "Python - Python Software Foundation License",
        "PyInstaller (bootloader, in the built program) - GNU General Public License version 2 or later with the bootloader exception",
    ]
    license_line = ("ZTranslate is free software under the GNU Affero General Public License, version 3 or later. This applies to the code of ZTranslate only: every component listed above keeps its own license, and the full list is in THIRD_PARTY_NOTICES.md at github.com/zapps-ltd/ZTranslate. The translation services you choose "
                    "(LibreTranslate, Google Translate, DeepL and others) have "
                    "their own terms.")
    return open_page(config.APPDATA_DIR, build_html(
        "ZTranslate", __version__, sections, credits, license_line))
