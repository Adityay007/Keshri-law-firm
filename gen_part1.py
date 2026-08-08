#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
from build import assemble

LEGAL_SERVICE_JSONLD = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "name": "Kesari Law Firm",
  "url": "https://www.kesarilawfirm.com/",
  "image": "https://www.kesarilawfirm.com/assets/og-image.jpg",
  "telephone": "+91-XXXXXXXXXX",
  "email": "contact@kesarilawfirm.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Office Address Line]",
    "addressLocality": "[City]",
    "addressRegion": "[State]",
    "postalCode": "[PIN Code]",
    "addressCountry": "IN"
  },
  "areaServed": "IN",
  "openingHoursSpecification": [
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "10:00", "closes": "18:00" },
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Saturday"], "opens": "10:00", "closes": "14:00" }
  ],
  "founder": { "@type": "Person", "name": "Kalinga Mohapatra", "jobTitle": "Founder & Managing Partner" }
}
</script>'''

PERSON_JSONLD = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Kalinga Mohapatra",
  "honorificPrefix": "Adv.",
  "jobTitle": "Founder & Managing Partner",
  "worksFor": { "@type": "LegalService", "name": "Kesari Law Firm" },
  "knowsLanguage": ["English", "Hindi"],
  "memberOf": { "@type": "Organization", "name": "[State Bar Council / Bar Association]" }
}
</script>'''

def head(title, desc, path):
    return '''<title>''' + title + '''</title>
<meta name="description" content="''' + desc + '''">
<link rel="canonical" href="https://www.kesarilawfirm.com/''' + path + '''">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Kesari Law Firm">
<meta property="og:title" content="''' + title + '''">
<meta property="og:description" content="''' + desc + '''">
<meta property="og:url" content="https://www.kesarilawfirm.com/''' + path + '''">
<meta property="og:image" content="https://www.kesarilawfirm.com/assets/og-image.jpg">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="''' + title + '''">
<meta name="twitter:description" content="''' + desc + '''">
<meta name="twitter:image" content="https://www.kesarilawfirm.com/assets/og-image.jpg">
''' + LEGAL_SERVICE_JSONLD

ICON_GRAD_CAP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4L2 9l10 5 10-5-10-5z"/><path d="M6 11.5V17c0 1.5 2.7 3 6 3s6-1.5 6-3v-5.5"/></svg>'
ICON_GLOBE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.8 5.7 3.8 9s-1.3 6.5-3.8 9c-2.5-2.5-3.8-5.7-3.8-9S9.5 5.5 12 3z"/></svg>'
ICON_BUILDING = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 21h16M5 21V10M9 21V10M15 21V10M19 21V10M3 10l9-6 9 6M4 10h16"/></svg>'
ICON_CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12.5l5 5L20 6"/></svg>'
ICON_ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h16M13 5l7 7-7 7"/></svg>'

SEAL_DIVIDER = '''  <div class="seal-divider"><span class="line"></span>
    <svg class="mark" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <circle cx="50" cy="50" r="46" stroke-width="1.25"/><circle cx="50" cy="50" r="40" stroke-width="1"/>
      <g stroke-width="1.25"><line x1="90" y1="50" x2="94" y2="50"/><line x1="78.28" y1="78.28" x2="81.11" y2="81.11"/><line x1="50" y1="90" x2="50" y2="94"/><line x1="21.72" y1="78.28" x2="18.89" y2="81.11"/><line x1="10" y1="50" x2="6" y2="50"/><line x1="21.72" y1="21.72" x2="18.89" y2="18.89"/><line x1="50" y1="10" x2="50" y2="6"/><line x1="78.28" y1="21.72" x2="81.11" y2="18.89"/></g>
      <g stroke-width="1.75"><line x1="50" y1="32" x2="50" y2="62"/><circle cx="50" cy="32" r="2.3" fill="currentColor" stroke="none"/><line x1="34" y1="32" x2="66" y2="32"/><line x1="34" y1="32" x2="34" y2="42"/><path d="M27 42 Q34 50 41 42"/><line x1="66" y1="32" x2="66" y2="42"/><path d="M59 42 Q66 50 73 42"/><line x1="42" y1="64" x2="58" y2="64"/><path d="M50 62 L42 64 M50 62 L58 64"/></g>
    </svg>
  <span class="line"></span></div>
'''

# ---------------------------------------------------------------- ABOUT ----
about_main = '''
  <div class="page-header">
    <div class="container">
      <p class="eyebrow">About the Firm</p>
      <h1>Counsel Rooted in Integrity</h1>
      <p>Kesari Law Firm was founded on the belief that legal representation should be thorough, ethical, and genuinely responsive to the people it serves.</p>
    </div>
  </div>

  <section class="section">
    <div class="container">
      <div class="grid grid-2" style="align-items:center; gap: var(--sp-7);">
        <div>
          <p class="eyebrow">Our Philosophy</p>
          <h2>Considered advocacy, not volume practice.</h2>
          <p class="mt-4">We take on matters we can give proper attention to, and we handle each one &mdash; regardless of scale &mdash; with the same discretion, diligence, and respect for due process. Our approach favours clear communication over legal jargon, so clients always understand where their matter stands.</p>
          <p>We believe access to sound legal guidance is not a privilege but a foundation of a fair legal system, and we conduct our practice accordingly &mdash; within the bounds of the Bar Council of India&rsquo;s Rules on professional conduct and advertising.</p>
        </div>
        <div class="portrait-frame" aria-hidden="true">
          <span class="monogram">KLF</span>
          <span class="caption">Firm / office photography to be added</span>
        </div>
      </div>
    </div>
  </section>

SEALDIVIDER

  <section class="section section--alt">
    <div class="container">
      <div class="grid grid-2" style="gap: var(--sp-7); align-items:flex-start;">
        <div class="portrait-frame" aria-hidden="true">
          <span class="monogram">KM</span>
          <span class="caption">Professional portrait to be added</span>
        </div>
        <div>
          <p class="eyebrow">Founder &amp; Managing Partner</p>
          <h2>Adv. Kalinga Mohapatra</h2>
          <p class="mt-4">Adv. Kalinga Mohapatra founded Kesari Law Firm with a commitment to ethical, client-centred legal practice. Guided throughout by careful attention to each client&rsquo;s circumstances, the practice is built around principled application of the law rather than promised outcomes.</p>

          <h3 class="mt-6">Qualifications</h3>
          <ul class="policy-content" style="max-width:none;">
            <li>LL.B., [University Name]</li>
            <li>Enrolled Advocate, Bar Council of [State]</li>
          </ul>

          <h3 class="mt-4">Professional Memberships</h3>
          <ul class="policy-content" style="max-width:none;">
            <li>[State] Bar Association</li>
            <li>[Relevant Bar Association / Chamber, if applicable]</li>
          </ul>

          <div class="grid grid-2 mt-6" style="gap: var(--sp-4);">
            <div class="info-row" style="margin-bottom:0;">
              <span class="icon-badge">''' + ICON_GLOBE + '''</span>
              <div><h4>Languages Spoken</h4><p>English, Hindi</p></div>
            </div>
            <div class="info-row" style="margin-bottom:0;">
              <span class="icon-badge">''' + ICON_BUILDING + '''</span>
              <div><h4>Court Practice</h4><p>High Court of [State]; District Courts of [State]</p></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

SEALDIVIDER

  <section class="section cta-band section--primary">
    <div class="container">
      <p class="eyebrow" style="justify-content:center;">Get in Touch</p>
      <h2>Discuss Your Matter With Us</h2>
      <p class="lede" style="margin:0 auto;">Every consultation request is handled with discretion from the very first message.</p>
      <div class="btn-row"><a href="contact.html" class="btn btn--gold">Request a Consultation</a></div>
    </div>
  </section>
'''

about_main = (about_main
    .replace("SEALDIVIDER\n\n  <section class=\"section section--alt\">",
             SEAL_DIVIDER + "\n  <section class=\"section section--alt\">")
    .replace("SEALDIVIDER\n\n  <section class=\"section cta-band section--primary\">",
             SEAL_DIVIDER + "\n  <section class=\"section cta-band section--primary\">")
)

with open('about.html', 'w') as f:
    f.write(assemble(
        "about.html",
        head("About Us | Kesari Law Firm — Advocate Profile &amp; Firm Philosophy",
             "Learn about Kesari Law Firm&#39;s approach to ethical, client-focused legal practice, and the background and qualifications of Adv. Kalinga Mohapatra.",
             "about.html") + "\n" + PERSON_JSONLD,
        about_main
    ))

print("about.html written")
