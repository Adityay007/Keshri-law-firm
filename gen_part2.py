#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
from build import assemble
from gen_part1 import head, LEGAL_SERVICE_JSONLD, ICON_ARROW

SEAL_DIVIDER = '''  <div class="seal-divider"><span class="line"></span>
    <svg class="mark" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <circle cx="50" cy="50" r="46" stroke-width="1.25"/><circle cx="50" cy="50" r="40" stroke-width="1"/>
      <g stroke-width="1.25"><line x1="90" y1="50" x2="94" y2="50"/><line x1="78.28" y1="78.28" x2="81.11" y2="81.11"/><line x1="50" y1="90" x2="50" y2="94"/><line x1="21.72" y1="78.28" x2="18.89" y2="81.11"/><line x1="10" y1="50" x2="6" y2="50"/><line x1="21.72" y1="21.72" x2="18.89" y2="18.89"/><line x1="50" y1="10" x2="50" y2="6"/><line x1="78.28" y1="21.72" x2="81.11" y2="18.89"/></g>
      <g stroke-width="1.75"><line x1="50" y1="32" x2="50" y2="62"/><circle cx="50" cy="32" r="2.3" fill="currentColor" stroke="none"/><line x1="34" y1="32" x2="66" y2="32"/><line x1="34" y1="32" x2="34" y2="42"/><path d="M27 42 Q34 50 41 42"/><line x1="66" y1="32" x2="66" y2="42"/><path d="M59 42 Q66 50 73 42"/><line x1="42" y1="64" x2="58" y2="64"/><path d="M50 62 L42 64 M50 62 L58 64"/></g>
    </svg>
  <span class="line"></span></div>
'''

PRACTICE_AREAS = [
    ("Civil Litigation",
     '<rect x="13.5" y="2.5" width="4" height="9" rx="0.5" transform="rotate(45 15.5 7)"/><line x1="11" y1="9.5" x2="6" y2="14.5"/><line x1="9" y1="7.5" x2="4" y2="12.5"/><line x1="3" y1="20" x2="13" y2="20"/>',
     "Representation in civil disputes before trial and appellate courts, including contractual, property, and recovery matters. We focus on clear case strategy and realistic guidance at every stage of the proceeding."),
    ("Corporate &amp; Commercial Law",
     '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4"/><path d="M9.5 12h5M9.5 15.5h5"/>',
     "Advisory and documentation support for businesses, including incorporation guidance, commercial contracts, compliance matters, and general corporate advisory for growing enterprises."),
    ("Family &amp; Matrimonial Matters",
     '<circle cx="9" cy="7" r="3"/><circle cx="17" cy="9" r="2.2"/><path d="M4 20c0-3.3 2.2-5.5 5-5.5s5 2.2 5 5.5M14.5 20c0-2.3 1.3-4 3.5-4.3"/>',
     "Considered, sensitive guidance in matrimonial disputes, divorce proceedings, custody matters, and family settlements &mdash; handled with the discretion these matters require."),
    ("Real Estate &amp; Property Law",
     '<path d="M4 11l8-7 8 7"/><path d="M6 10v10h12V10"/>',
     "Title due diligence, sale and lease documentation, and dispute resolution in property matters, for individual buyers, sellers, and developers alike."),
    ("Criminal Defence",
     '<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3z"/>',
     "Diligent representation in criminal proceedings at every stage, from initial advisory through trial, with careful attention to procedural safeguards."),
    ("Arbitration &amp; Dispute Resolution",
     '<line x1="12" y1="5" x2="12" y2="19"/><circle cx="12" cy="5" r="1.4" fill="currentColor" stroke="none"/><line x1="5" y1="5" x2="19" y2="5"/><line x1="5" y1="5" x2="5" y2="10"/><path d="M2 10 Q5 15 8 10"/><line x1="19" y1="5" x2="19" y2="10"/><path d="M16 10 Q19 15 22 10"/>',
     "Representation in arbitration and alternative dispute resolution proceedings, offering clients a considered, often less adversarial path to resolution."),
    ("Intellectual Property Rights",
     '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.4 1 1.1 1 1.9V17h5v-1.2c0-.8.4-1.5 1-1.9A6 6 0 0 0 12 3z"/>',
     "Guidance on the protection and enforcement of trademarks, copyrights, and related intellectual property rights for individuals and businesses."),
    ("Labour &amp; Employment Law",
     '<rect x="3" y="8" width="18" height="12" rx="1.5"/><path d="M8 8V6a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/>',
     "Advisory and representation in workplace and employment disputes, covering both employer compliance matters and individual employee representation."),
]

cards_html = ""
for i, (name, icon_path, desc) in enumerate(PRACTICE_AREAS):
    cards_html += '''        <div class="card--practice" id="area-''' + str(i+1) + '''">
          <span class="icon-badge"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">''' + icon_path + '''</svg></span>
          <h3>''' + name + '''</h3>
          <p>''' + desc + '''</p>
        </div>
'''

practice_main = '''
  <div class="page-header">
    <div class="container">
      <p class="eyebrow">Practice Areas</p>
      <h1>Areas of Practice</h1>
      <p>Considered representation across the matters that affect individuals, families, and businesses most.</p>
    </div>
  </div>

  <section class="section">
    <div class="container">
      <div class="grid grid-3">
''' + cards_html + '''      </div>
    </div>
  </section>

''' + SEAL_DIVIDER + '''
  <section class="section section--alt">
    <div class="container text-center max-w-content mx-auto">
      <h2>Not sure which area applies to your matter?</h2>
      <p class="mt-2">Many matters span more than one practice area. Share a brief description of your situation and we will advise on the right path forward.</p>
      <div class="btn-row" style="justify-content:center;"><a href="contact.html" class="btn btn--primary mt-4">Request a Consultation</a></div>
    </div>
  </section>
'''

with open('practice-areas.html', 'w') as f:
    f.write(assemble(
        "practice-areas.html",
        head("Areas of Practice | Kesari Law Firm",
             "Kesari Law Firm provides representation across civil litigation, corporate law, family law, real estate, criminal defence, arbitration, IP, and employment law.",
             "practice-areas.html"),
        practice_main
    ))
print("practice-areas.html written")

# ---------------------------------------------------------------- TEAM ----
ICON_MEDAL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4L2 9l10 5 10-5-10-5z"/><path d="M6 11.5V17c0 1.5 2.7 3 6 3s6-1.5 6-3v-5.5"/></svg>'

team_main = '''
  <div class="page-header">
    <div class="container">
      <p class="eyebrow">Our Team</p>
      <h1>Meet the Team</h1>
      <p>Kesari Law Firm is guided by considered, principled advocacy at every level of the practice.</p>
    </div>
  </div>

  <section class="section">
    <div class="container">
      <div class="grid grid-3">
        <div class="team-card">
          <div class="portrait-frame">
            <span class="monogram">KM</span>
            <span class="caption">Professional portrait to be added</span>
          </div>
          <span class="role">Founder &amp; Managing Partner</span>
          <h3>Adv. Kalinga Mohapatra</h3>
          <p>LL.B., [University Name] &middot; Enrolled Advocate, Bar Council of [State] &middot; English, Hindi</p>
          <a href="about.html" class="link mt-2" style="display:inline-flex;">Full Profile
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h16M13 5l7 7-7 7"/></svg>
          </a>
        </div>
        <div class="team-card team-card--placeholder">
          Additional team member profile &mdash; add associate advocates, of counsel, or support staff as the firm grows.
        </div>
        <div class="team-card team-card--placeholder">
          Additional team member profile &mdash; add associate advocates, of counsel, or support staff as the firm grows.
        </div>
      </div>
    </div>
  </section>

''' + SEAL_DIVIDER + '''
  <section class="section section--alt">
    <div class="container">
      <div class="text-center max-w-content mx-auto mb-6">
        <p class="eyebrow" style="justify-content:center;">Professional Standing</p>
        <h2>Memberships &amp; Standing</h2>
      </div>
      <div class="grid grid-3">
        <div class="pillar">
          <span class="icon-badge">''' + ICON_MEDAL + '''</span>
          <h3 class="mt-2">Bar Council Enrolment</h3>
          <p>Enrolled Advocate, Bar Council of [State].</p>
        </div>
        <div class="pillar">
          <span class="icon-badge">''' + ICON_MEDAL + '''</span>
          <h3 class="mt-2">Bar Association Membership</h3>
          <p>Member, [State] Bar Association.</p>
        </div>
        <div class="pillar">
          <span class="icon-badge">''' + ICON_MEDAL + '''</span>
          <h3 class="mt-2">Court Practice</h3>
          <p>Practising before the High Court of [State] and District Courts of [State].</p>
        </div>
      </div>
    </div>
  </section>
'''

with open('team.html', 'w') as f:
    f.write(assemble(
        "team.html",
        head("Our Team | Kesari Law Firm",
             "Meet the team at Kesari Law Firm, led by Adv. Kalinga Mohapatra, Founder &amp; Managing Partner.",
             "team.html"),
        team_main
    ))
print("team.html written")
