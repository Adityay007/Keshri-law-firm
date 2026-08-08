#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
from build import assemble
from gen_part2 import head

def policy_page(eyebrow, title, intro, body_html):
    return '''
  <div class="page-header">
    <div class="container">
      <p class="eyebrow">''' + eyebrow + '''</p>
      <h1>''' + title + '''</h1>
      <p>''' + intro + '''</p>
    </div>
  </div>
  <section class="section">
    <div class="container">
      <div class="policy-content">
        <p class="updated">Last updated: August 2026</p>
''' + body_html + '''
      </div>
    </div>
  </section>
'''

# ----------------------------------------------------------- DISCLAIMER ----
disclaimer_body = '''
        <div class="callout">
          <p>This website has been developed solely for informational purposes in accordance with the applicable rules of the Bar Council of India. It is not intended to advertise or solicit work in any manner whatsoever. By accessing this website, you acknowledge that you are seeking information about Kesari Law Firm on your own accord.</p>
        </div>

        <h2>1. No Advertisement or Solicitation</h2>
        <p>The Bar Council of India does not permit advocates or law firms to advertise or solicit work in any form. This website is not an advertisement and is not intended to solicit clients or to induce any person to engage the services of Kesari Law Firm. Any information obtained or downloaded from this website is entirely at the user&rsquo;s own volition, and any transmission, receipt, or use of this website does not constitute solicitation of any kind.</p>

        <h2>2. Voluntary and Informed Access</h2>
        <p>The user wishes to gain more information about Kesari Law Firm for their own information and use, and takes full responsibility for their decision to access this website. The information provided on this website is not intended to be a substitute for legal advice and should not be relied upon as such.</p>

        <h2>3. No Attorney-Client Relationship</h2>
        <p>No attorney-client relationship is created between Kesari Law Firm and the user of this website merely by browsing this website or by transmitting information through the Consultation Request Form. Such a relationship is established only upon the firm&rsquo;s express written confirmation of engagement, following a conflict check and mutually agreed terms.</p>

        <h2>4. Accuracy of Information</h2>
        <p>While we endeavour to keep the information on this website accurate and up to date, Kesari Law Firm makes no warranty, express or implied, regarding the completeness, accuracy, reliability, or suitability of the content for any particular purpose. Laws and regulations referenced on this website may change, and readers should not act, or refrain from acting, on the basis of any content on this website without first seeking appropriate professional advice specific to their circumstances.</p>

        <h2>5. Third-Party Links</h2>
        <p>This website may contain links to third-party websites for the user&rsquo;s convenience. Kesari Law Firm does not endorse and is not responsible for the content, accuracy, or practices of any linked third-party website.</p>

        <h2>6. Compliance with Bar Council of India Rules</h2>
        <p>This website and its content have been designed with the intent of complying with Rule 36 of the Bar Council of India Rules and related professional conduct rules governing advocates in India. Should any content on this website be found inconsistent with these rules, Kesari Law Firm will take prompt steps to correct it.</p>

        <h2>7. Contact</h2>
        <p>For any questions regarding this Disclaimer, please contact us at <a class="link" href="mailto:contact@kesarilawfirm.com">contact@kesarilawfirm.com</a>.</p>
'''

with open('disclaimer.html', 'w') as f:
    f.write(assemble(
        "disclaimer.html",
        head("Disclaimer | Kesari Law Firm",
             "This website has been developed solely for informational purposes in accordance with the Bar Council of India Rules. Read the full disclaimer.",
             "disclaimer.html"),
        policy_page("Legal", "Disclaimer",
                    "Please read this Disclaimer carefully before using this website.",
                    disclaimer_body)
    ))
print("disclaimer.html written")

# ------------------------------------------------------- PRIVACY POLICY ----
privacy_body = '''
        <h2>1. Introduction</h2>
        <p>Kesari Law Firm (&ldquo;we&rdquo;, &ldquo;us&rdquo;, or &ldquo;the firm&rdquo;) respects the privacy of visitors to this website. This Privacy Policy explains what information we collect, how we use it, and the choices available to you.</p>

        <h2>2. Information We Collect</h2>
        <ul>
          <li><strong>Information you provide:</strong> name, phone number, email address, and any details you choose to share through our Consultation Request Form.</li>
          <li><strong>Automatically collected information:</strong> standard technical data such as browser type, device type, and pages visited, typically gathered through cookies (see our <a class="link" href="cookie-policy.html">Cookie Policy</a>).</li>
        </ul>

        <h2>3. How We Use Your Information</h2>
        <ul>
          <li>To respond to consultation requests and general enquiries.</li>
          <li>To maintain internal records consistent with our professional obligations.</li>
          <li>To improve the content and usability of this website.</li>
        </ul>
        <p>We do not sell, rent, or trade personal information to third parties for marketing purposes.</p>

        <h2>4. Confidentiality of Consultation Requests</h2>
        <div class="callout">
          <p>Please note that information submitted through the Consultation Request Form before a formal engagement is confirmed is not protected by attorney-client privilege. Avoid including sensitive or confidential case details in your initial message; our team will advise on secure next steps once contact is established.</p>
        </div>

        <h2>5. Cookies</h2>
        <p>This website may use essential and, where applicable, analytics cookies to understand site usage. You can control cookie preferences through your browser settings. See our <a class="link" href="cookie-policy.html">Cookie Policy</a> for details.</p>

        <h2>6. Data Security</h2>
        <p>We take reasonable technical and organisational measures to protect the personal information we hold from unauthorised access, alteration, or disclosure. However, no method of transmission over the internet is entirely secure, and we cannot guarantee absolute security.</p>

        <h2>7. Data Retention</h2>
        <p>We retain personal information only for as long as necessary to fulfil the purposes described in this policy, or as required by applicable law and professional record-keeping obligations.</p>

        <h2>8. Third-Party Links</h2>
        <p>This website may link to third-party websites. We are not responsible for the privacy practices or content of those websites and encourage you to review their respective privacy policies.</p>

        <h2>9. Your Rights</h2>
        <p>You may request access to, correction of, or deletion of personal information we hold about you, subject to our professional record-keeping obligations, by contacting us using the details below.</p>

        <h2>10. Changes to This Policy</h2>
        <p>We may update this Privacy Policy from time to time. Any changes will be posted on this page with a revised &ldquo;last updated&rdquo; date.</p>

        <h2>11. Contact / Grievance Officer</h2>
        <p>For privacy-related questions or concerns, please contact:<br>
        [Grievance Officer Name]<br>
        Kesari Law Firm<br>
        <a class="link" href="mailto:contact@kesarilawfirm.com">contact@kesarilawfirm.com</a> &middot; <a class="link" href="tel:+91XXXXXXXXXX">+91 XXXXX XXXXX</a></p>
'''

with open('privacy-policy.html', 'w') as f:
    f.write(assemble(
        "privacy-policy.html",
        head("Privacy Policy | Kesari Law Firm",
             "Read the Kesari Law Firm Privacy Policy to understand what information we collect through this website, how it is used, and your rights.",
             "privacy-policy.html"),
        policy_page("Legal", "Privacy Policy",
                    "How Kesari Law Firm collects, uses, and protects information gathered through this website.",
                    privacy_body)
    ))
print("privacy-policy.html written")
