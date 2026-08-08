#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
from build import assemble
from gen_part2 import head
from gen_part4 import policy_page

# --------------------------------------------------------- TERMS & COND ----
terms_body = '''
        <h2>1. Acceptance of Terms</h2>
        <p>By accessing and using this website, you agree to be bound by these Terms &amp; Conditions. If you do not agree with any part of these terms, please discontinue use of this website.</p>

        <h2>2. Purpose of This Website</h2>
        <p>This website is intended solely to provide general information about Kesari Law Firm, in accordance with the Bar Council of India Rules. It is not intended as advertising, solicitation, or an invitation to engage the firm. See our full <a class="link" href="disclaimer.html">Disclaimer</a>.</p>

        <h2>3. No Attorney-Client Relationship</h2>
        <p>Use of this website, including submission of the Consultation Request Form, does not create an attorney-client relationship between you and Kesari Law Firm. Such a relationship arises only upon formal written engagement.</p>

        <h2>4. Intellectual Property</h2>
        <p>All content on this website &mdash; including text, graphics, logos, and design elements &mdash; is the property of Kesari Law Firm unless otherwise noted, and is protected by applicable intellectual property laws. You may view and print content for personal, non-commercial reference, but may not reproduce, distribute, or modify it without prior written permission.</p>

        <h2>5. Accuracy of Information; No Warranty</h2>
        <p>Content on this website is provided &ldquo;as is&rdquo; for general informational purposes only, without warranties of any kind, express or implied, regarding its accuracy, completeness, or currency. Legal information can change; always seek independent professional advice for your specific situation.</p>

        <h2>6. Limitation of Liability</h2>
        <p>To the fullest extent permitted by law, Kesari Law Firm shall not be liable for any direct, indirect, incidental, or consequential loss or damage arising from your use of, or reliance on, this website or its content.</p>

        <h2>7. External Links</h2>
        <p>This website may contain links to external websites provided for convenience. We do not control and are not responsible for the content or practices of any linked third-party site.</p>

        <h2>8. Governing Law &amp; Jurisdiction</h2>
        <p>These Terms &amp; Conditions are governed by the laws of India. Any disputes arising out of or in connection with this website shall be subject to the exclusive jurisdiction of the courts at [City], [State].</p>

        <h2>9. Amendments</h2>
        <p>We may revise these Terms &amp; Conditions at any time. Continued use of this website after changes are posted constitutes acceptance of the revised terms.</p>

        <h2>10. Contact</h2>
        <p>For questions about these Terms &amp; Conditions, please contact us at <a class="link" href="mailto:contact@kesarilawfirm.com">contact@kesarilawfirm.com</a>.</p>
'''

with open('terms-conditions.html', 'w') as f:
    f.write(assemble(
        "terms-conditions.html",
        head("Terms &amp; Conditions | Kesari Law Firm",
             "Read the Terms &amp; Conditions governing the use of the Kesari Law Firm website.",
             "terms-conditions.html"),
        policy_page("Legal", "Terms &amp; Conditions",
                    "The terms governing your use of this website.",
                    terms_body)
    ))
print("terms-conditions.html written")

# ------------------------------------------------------------- COOKIES ----
cookie_body = '''
        <h2>1. What Are Cookies</h2>
        <p>Cookies are small text files placed on your device when you visit a website. They help the website function properly and, where used, help us understand how visitors interact with our content.</p>

        <h2>2. How We Use Cookies</h2>
        <p>This website uses cookies to support core functionality and, where enabled, to gather anonymised analytics about site usage so that we can improve the content and experience we provide.</p>

        <h2>3. Types of Cookies We Use</h2>
        <ul>
          <li><strong>Essential cookies:</strong> required for the website to function correctly.</li>
          <li><strong>Analytics cookies:</strong> help us understand how visitors use the site (if and when an analytics tool is enabled on this site, it will be listed here by name).</li>
        </ul>
        <p>This website does not currently use advertising or third-party marketing cookies.</p>

        <h2>4. Managing Cookies</h2>
        <p>Most web browsers allow you to control cookies through their settings, including blocking or deleting them. Please note that disabling essential cookies may affect the functionality of this website.</p>

        <h2>5. Third-Party Cookies</h2>
        <p>Where this website embeds third-party content (such as a Google Maps location), that third party may set its own cookies in accordance with its own policy. We encourage you to review the relevant third party&rsquo;s cookie policy for details.</p>

        <h2>6. Changes to This Policy</h2>
        <p>We may update this Cookie Policy from time to time to reflect changes in the tools this website uses. Any changes will be posted on this page with a revised &ldquo;last updated&rdquo; date.</p>

        <h2>7. Contact</h2>
        <p>Questions about this Cookie Policy can be directed to <a class="link" href="mailto:contact@kesarilawfirm.com">contact@kesarilawfirm.com</a>.</p>
'''

with open('cookie-policy.html', 'w') as f:
    f.write(assemble(
        "cookie-policy.html",
        head("Cookie Policy | Kesari Law Firm",
             "Learn how Kesari Law Firm uses cookies on this website and how you can manage your preferences.",
             "cookie-policy.html"),
        policy_page("Legal", "Cookie Policy",
                    "How this website uses cookies, and how you can manage your preferences.",
                    cookie_body)
    ))
print("cookie-policy.html written")

# ------------------------------------------------------- ACCESSIBILITY ----
access_body = '''
        <h2>1. Our Commitment</h2>
        <p>Kesari Law Firm is committed to ensuring this website is accessible to the widest possible audience, including people with disabilities, in keeping with our broader commitment to access to justice.</p>

        <h2>2. Standards We Aim to Follow</h2>
        <p>We aim for this website to conform to the Web Content Accessibility Guidelines (WCAG) 2.1, Level AA, published by the World Wide Web Consortium (W3C). This is an ongoing effort rather than a one-time achievement.</p>

        <h2>3. Measures We Have Taken</h2>
        <ul>
          <li>Semantic HTML structure to support screen readers and assistive technology.</li>
          <li>A visible &ldquo;skip to main content&rdquo; link for keyboard users.</li>
          <li>Clear focus indicators on all interactive elements.</li>
          <li>Colour combinations chosen with text contrast in mind.</li>
          <li>Descriptive alternative text for meaningful images once photography is added.</li>
          <li>Respect for the &ldquo;prefers-reduced-motion&rdquo; setting for visitors sensitive to animation.</li>
        </ul>

        <h2>4. Known Limitations</h2>
        <p>Despite our efforts, some content may not yet be fully accessible. We are working to address known gaps and welcome feedback that helps us identify further improvements.</p>

        <h2>5. Feedback</h2>
        <p>If you encounter any accessibility barriers while using this website, please let us know so we can address them:<br>
        <a class="link" href="mailto:contact@kesarilawfirm.com">contact@kesarilawfirm.com</a> &middot; <a class="link" href="tel:+91XXXXXXXXXX">+91 XXXXX XXXXX</a></p>

        <h2>6. Date of Last Review</h2>
        <p>This Accessibility Statement was last reviewed in August 2026.</p>
'''

with open('accessibility-statement.html', 'w') as f:
    f.write(assemble(
        "accessibility-statement.html",
        head("Accessibility Statement | Kesari Law Firm",
             "Learn about Kesari Law Firm&#39;s commitment to web accessibility and how to share feedback.",
             "accessibility-statement.html"),
        policy_page("Legal", "Accessibility Statement",
                    "Our commitment to making this website usable for everyone.",
                    access_body)
    ))
print("accessibility-statement.html written")
