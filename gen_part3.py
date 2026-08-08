#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
from build import assemble
from gen_part2 import head, SEAL_DIVIDER

# ------------------------------------------------------------- INSIGHTS ----
ARTICLES = [
    ("Property Law", "Understanding Your Rights in a Property Dispute",
     "A plain-language overview of the steps involved when a property matter moves toward litigation."),
    ("Corporate Law", "Key Considerations Before Signing a Commercial Contract",
     "What to review, question, and document before entering a binding commercial agreement."),
    ("Client Guidance", "What to Expect From a Legal Consultation",
     "How to prepare, what to bring, and how confidentiality applies from your very first meeting."),
    ("Family Law", "Navigating a Matrimonial Dispute: First Steps",
     "An introduction to the process, timelines, and considerations involved in matrimonial matters."),
    ("Employment Law", "Employee Rights During Workplace Disputes",
     "A general overview of protections available to employees facing a workplace grievance."),
    ("Dispute Resolution", "Arbitration vs. Litigation: Choosing a Path",
     "A comparison of arbitration and traditional litigation to help you understand your options."),
]

cards = ""
for tag, title, desc in ARTICLES:
    cards += '''        <article class="card--practice card--article">
          <span class="tag">''' + tag + '''</span>
          <h3>''' + title + '''</h3>
          <p>''' + desc + '''</p>
          <span class="meta">Sample article &mdash; replace with firm content</span>
        </article>
'''

insights_main = '''
  <div class="page-header">
    <div class="container">
      <p class="eyebrow">Insights &amp; Publications</p>
      <h1>Legal Education &amp; Perspective</h1>
      <p>Educational articles written to help clients understand their rights and the legal process &mdash; not to promote outcomes or advertise services.</p>
    </div>
  </div>

  <section class="section">
    <div class="container">
      <div class="grid grid-3">
''' + cards + '''      </div>
    </div>
  </section>

''' + SEAL_DIVIDER + '''
  <section class="section section--alt">
    <div class="container">
      <div class="text-center max-w-content mx-auto mb-6">
        <p class="eyebrow" style="justify-content:center;">Publications</p>
        <h2>Papers &amp; Publications</h2>
      </div>
      <div class="grid grid-2" style="max-width:800px; margin:0 auto;">
        <div class="card--practice">
          <h3>[Publication Title]</h3>
          <p>[Journal / Publication Name], [Year]. Add a brief description once the entry is confirmed.</p>
        </div>
        <div class="card--practice">
          <h3>[Publication Title]</h3>
          <p>[Journal / Publication Name], [Year]. Add a brief description once the entry is confirmed.</p>
        </div>
      </div>
      <p class="text-center mt-4" style="color:var(--color-text-faint); font-size:0.9rem;">Publications will be listed here as they become available.</p>
    </div>
  </section>
'''

with open('insights.html', 'w') as f:
    f.write(assemble(
        "insights.html",
        head("Insights &amp; Publications | Kesari Law Firm",
             "Educational legal articles and publications from Kesari Law Firm, written to help clients understand their rights and the legal process.",
             "insights.html"),
        insights_main
    ))
print("insights.html written")

# -------------------------------------------------------------- CONTACT ----
ICON_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.4"/></svg>'
ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 3h3l2 5-2.5 1.5a11 11 0 0 0 5 5L15 12l5 2v3a2 2 0 0 1-2 2A16 16 0 0 1 4 5a2 2 0 0 1 2-2z"/></svg>'
ICON_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>'
ICON_CLOCK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg>'
ICON_MAP_LG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.4"/></svg>'

contact_main = '''
  <div class="page-header">
    <div class="container">
      <p class="eyebrow">Contact</p>
      <h1>Request a Consultation</h1>
      <p>Reach out to discuss your matter directly with our team. Every conversation is treated with discretion.</p>
    </div>
  </div>

  <section class="section">
    <div class="container">
      <div class="grid grid-2" style="gap: var(--sp-8); align-items:flex-start;">

        <div>
          <h2 class="mb-4">Office &amp; Contact Details</h2>

          <div class="info-row">
            <span class="icon-badge">''' + ICON_PIN + '''</span>
            <div>
              <h4>Office Address</h4>
              <p>[Office Address Line 1]<br>[Area], [City] &ndash; [PIN Code]<br>[State], India</p>
            </div>
          </div>
          <div class="info-row">
            <span class="icon-badge">''' + ICON_PHONE + '''</span>
            <div>
              <h4>Phone</h4>
              <p><a class="link" href="tel:+91XXXXXXXXXX">+91 XXXXX XXXXX</a></p>
            </div>
          </div>
          <div class="info-row">
            <span class="icon-badge">''' + ICON_MAIL + '''</span>
            <div>
              <h4>Email</h4>
              <p><a class="link" href="mailto:contact@kesarilawfirm.com">contact@kesarilawfirm.com</a></p>
            </div>
          </div>
          <div class="info-row">
            <span class="icon-badge">''' + ICON_CLOCK + '''</span>
            <div>
              <h4>Office Hours</h4>
              <p>Monday &ndash; Friday: 10:00 AM &ndash; 6:00 PM<br>Saturday: 10:00 AM &ndash; 2:00 PM<br>Sunday: Closed</p>
            </div>
          </div>

          <div class="map-placeholder mt-4">
            ''' + ICON_MAP_LG + '''
            <span><strong>Map placeholder.</strong> Replace the embed in this section with a Google Maps iframe once the office address is confirmed.</span>
          </div>
          <!--
            To embed Google Maps once the address is confirmed, replace the
            .map-placeholder div above with, e.g.:
            <iframe class="map-embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
              src="https://www.google.com/maps?q=YOUR+FULL+OFFICE+ADDRESS&output=embed"></iframe>
          -->
        </div>

        <div>
          <h2 class="mb-4">Consultation Request Form</h2>
          <div class="form-disclaimer">
            Submitting this form does not create an advocate-client relationship, and information shared here is not privileged until formal engagement. Please avoid sharing confidential case details through this form &mdash; our team will advise on secure next steps after your initial message.
          </div>
          <form id="consultation-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
            <div class="form-grid">
              <div class="form-group">
                <label for="fname">Full Name <span class="req">*</span></label>
                <input type="text" id="fname" name="name" required>
              </div>
              <div class="form-group">
                <label for="fphone">Phone <span class="req">*</span></label>
                <input type="tel" id="fphone" name="phone" required>
              </div>
              <div class="form-group form-group--full">
                <label for="femail">Email <span class="req">*</span></label>
                <input type="email" id="femail" name="email" required>
              </div>
              <div class="form-group form-group--full">
                <label for="farea">Practice Area</label>
                <select id="farea" name="practice_area">
                  <option value="">Select an area (optional)</option>
                  <option>Civil Litigation</option>
                  <option>Corporate &amp; Commercial Law</option>
                  <option>Family &amp; Matrimonial Matters</option>
                  <option>Real Estate &amp; Property Law</option>
                  <option>Criminal Defence</option>
                  <option>Arbitration &amp; Dispute Resolution</option>
                  <option>Intellectual Property Rights</option>
                  <option>Labour &amp; Employment Law</option>
                  <option>Other / Not Sure</option>
                </select>
              </div>
              <div class="form-group form-group--full">
                <label for="fmsg">Brief Description <span class="req">*</span></label>
                <textarea id="fmsg" name="message" required placeholder="Please share a general outline of your matter. Avoid including sensitive case details at this stage."></textarea>
              </div>
            </div>
            <p class="form-note mb-4">Fields marked <span class="req">*</span> are required.</p>
            <button type="submit" class="btn btn--primary">Request Consultation</button>
          </form>
        </div>

      </div>
    </div>
  </section>
'''

with open('contact.html', 'w') as f:
    f.write(assemble(
        "contact.html",
        head("Contact &amp; Consultation | Kesari Law Firm",
             "Get in touch with Kesari Law Firm to request a confidential legal consultation. Find our office address, phone, email, and office hours.",
             "contact.html"),
        contact_main
    ))
print("contact.html written")
