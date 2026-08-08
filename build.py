#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Internal build script — assembles shared chrome (disclaimer, header, footer)
around per-page content so every page is byte-identical in its shared parts.
Not part of the final deliverable; removed after the site is generated.
"""
import os

SCALE_GLYPH = '''<line x1="24" y1="15" x2="24" y2="37"/><circle cx="24" cy="15" r="1.6" fill="currentColor" stroke="none"/>
        <line x1="15" y1="15" x2="33" y2="15"/><line x1="15" y1="15" x2="15" y2="21"/><path d="M10 21 Q15 27 20 21"/>
        <line x1="33" y1="15" x2="33" y2="21"/><path d="M28 21 Q33 27 38 21"/>
        <line x1="18" y1="39" x2="30" y2="39"/><path d="M24 37 L18 39 M24 37 L30 39"/>'''

SEAL_INNER = '''<circle cx="50" cy="50" r="46" stroke-width="1.25"/><circle cx="50" cy="50" r="40" stroke-width="1"/>
      <g stroke-width="1.25"><line x1="90" y1="50" x2="94" y2="50"/><line x1="78.28" y1="78.28" x2="81.11" y2="81.11"/><line x1="50" y1="90" x2="50" y2="94"/><line x1="21.72" y1="78.28" x2="18.89" y2="81.11"/><line x1="10" y1="50" x2="6" y2="50"/><line x1="21.72" y1="21.72" x2="18.89" y2="18.89"/><line x1="50" y1="10" x2="50" y2="6"/><line x1="78.28" y1="21.72" x2="81.11" y2="18.89"/></g>
      <g stroke-width="1.75"><line x1="50" y1="32" x2="50" y2="62"/><circle cx="50" cy="32" r="2.3" fill="currentColor" stroke="none"/><line x1="34" y1="32" x2="66" y2="32"/><line x1="34" y1="32" x2="34" y2="42"/><path d="M27 42 Q34 50 41 42"/><line x1="66" y1="32" x2="66" y2="42"/><path d="M59 42 Q66 50 73 42"/><line x1="42" y1="64" x2="58" y2="64"/><path d="M50 62 L42 64 M50 62 L58 64"/></g>'''

def seal_divider():
    return f'''  <div class="seal-divider"><span class="line"></span>
    <svg class="mark" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      {SEAL_INNER}
    </svg>
  <span class="line"></span></div>
'''

def disclaimer_block():
    return f'''<input type="checkbox" id="disclaimer-toggle" class="disclaimer-toggle">
<div class="disclaimer-overlay" role="dialog" aria-modal="true" aria-labelledby="disclaimer-title">
  <div class="disclaimer-box">
    <svg class="brand__mark" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      {SCALE_GLYPH}
    </svg>
    <h2 id="disclaimer-title">Before You Enter</h2>
    <p>This website has been developed solely for informational purposes in accordance with the applicable rules of the Bar Council of India. It is not intended to advertise or solicit work.</p>
    <p>By accessing this website, you acknowledge that you are seeking information about Kesari Law Firm on your own accord, and that no advocate-client relationship is formed by browsing this site.</p>
    <div class="btn-row">
      <label for="disclaimer-toggle" class="btn btn--gold">I Have Read &amp; Agree — Enter Website</label>
    </div>
    <p class="fine">Read the <a href="disclaimer.html">full Disclaimer</a> for complete terms.</p>
  </div>
</div>
'''

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("practice-areas.html", "Practice Areas"),
    ("team.html", "Team"),
    ("insights.html", "Insights"),
    ("contact.html", "Contact"),
]

def header_block(active):
    links = []
    for href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if href == active else ''
        links.append(f'        <a href="{href}"{cur}>{label}</a>')
    links_html = "\n".join(links)

    mlinks = []
    for href, label in NAV_ITEMS:
        mlinks.append(f'      <a href="{href}">{label}</a>')
    mlinks_html = "\n".join(mlinks)

    return f'''<header class="site-header">
  <input type="checkbox" id="nav-toggle" class="nav-toggle-checkbox">
  <nav class="nav" aria-label="Primary">
    <a href="index.html" class="brand">
      <svg class="brand__mark" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        {SCALE_GLYPH}
      </svg>
      <span>
        <span class="brand__word">Kesari Law Firm</span>
        <span class="brand__tagline">Advocates &amp; Legal Consultants</span>
      </span>
    </a>
    <div class="nav__right">
      <div class="nav__links">
{links_html}
        <a href="contact.html" class="btn btn--outline nav__cta">Request Consultation</a>
      </div>
      <label for="nav-toggle" class="hamburger" aria-label="Toggle menu"><span></span><span></span><span></span></label>
    </div>
  </nav>
  <div class="mobile-nav-panel">
    <div class="mobile-nav-panel__inner">
{mlinks_html}
      <a href="contact.html" class="btn btn--gold">Request Consultation</a>
    </div>
  </div>
</header>
'''

def footer_block():
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer__top">
      <div>
        <div class="footer__brand">
          <svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            {SCALE_GLYPH}
          </svg>
          <span>Kesari Law Firm</span>
        </div>
        <p>Advocates &amp; Legal Consultants providing ethical, client-focused legal guidance.</p>
        <div class="mt-4">
          <div class="footer__contact-item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.4"/></svg>
            <span>[Office Address], [City] – [PIN Code], [State]</span>
          </div>
          <div class="footer__contact-item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 3h3l2 5-2.5 1.5a11 11 0 0 0 5 5L15 12l5 2v3a2 2 0 0 1-2 2A16 16 0 0 1 4 5a2 2 0 0 1 2-2z"/></svg>
            <span><a href="tel:+91XXXXXXXXXX">+91 XXXXX XXXXX</a></span>
          </div>
          <div class="footer__contact-item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>
            <span><a href="mailto:contact@kesarilawfirm.com">contact@kesarilawfirm.com</a></span>
          </div>
        </div>
      </div>
      <div class="footer__col">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="about.html">About the Firm</a></li>
          <li><a href="practice-areas.html">Practice Areas</a></li>
          <li><a href="team.html">Our Team</a></li>
          <li><a href="insights.html">Insights</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4>Legal</h4>
        <ul>
          <li><a href="disclaimer.html">Disclaimer</a></li>
          <li><a href="privacy-policy.html">Privacy Policy</a></li>
          <li><a href="terms-conditions.html">Terms &amp; Conditions</a></li>
          <li><a href="cookie-policy.html">Cookie Policy</a></li>
          <li><a href="accessibility-statement.html">Accessibility Statement</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4>Office Hours</h4>
        <p>Monday – Friday<br>10:00 AM – 6:00 PM</p>
        <p class="mt-2">Saturday<br>10:00 AM – 2:00 PM</p>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> Kesari Law Firm. All rights reserved.</span>
      <span>Advocate enrolled with the Bar Council of [State]</span>
    </div>
    <p class="footer__disclaimer-line">This website is intended solely for informational purposes in accordance with the Bar Council of India Rules and does not constitute advertising, solicitation, or an invitation to engage the firm. See our full <a href="disclaimer.html">Disclaimer</a>.</p>
  </div>
</footer>
'''

def assemble(active, head_extra, main_html, include_disclaimer=True):
    parts = []
    parts.append('<a href="#main" class="skip-link">Skip to main content</a>\n')
    if include_disclaimer:
        parts.append(disclaimer_block())
    parts.append(header_block(active))
    parts.append(f'\n<main id="main">\n{main_html}\n</main>\n')
    parts.append(footer_block())
    parts.append('\n<script src="js/main.js"></script>\n')
    body = "\n".join(parts)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{head_extra}
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
</head>
<body>

{body}
</body>
</html>
'''

if __name__ == "__main__":
    print("Module loaded — see individual page scripts.")
