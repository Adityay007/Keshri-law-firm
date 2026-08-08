# Kesari Law Firm — Website

A premium, BCI Rule 36–compliant informational website. Static HTML/CSS/JS,
no build step, no framework — deploys directly to GitHub Pages or any static
host.

## File Structure

```
kesari-law-firm/
├── index.html                    Home
├── about.html                    Firm philosophy + Advocate profile
├── practice-areas.html           8 practice areas
├── team.html                     Team profiles + memberships
├── insights.html                 Articles + Publications
├── contact.html                  Office info + Consultation form
├── disclaimer.html
├── privacy-policy.html
├── terms-conditions.html
├── cookie-policy.html
├── accessibility-statement.html
├── sitemap.xml
├── robots.txt
├── favicon.svg
├── css/styles.css                Single shared stylesheet (design system)
├── js/main.js                    Progressive-enhancement only, no critical
│                                  functionality depends on it
└── build.py, gen_part1–5.py,     Optional: regenerates the HTML from these
    regenerate_all.py             scripts. Safe to delete before deploying —
                                   they are not referenced by the live site.
```

## Before Going Live — Replace These Placeholders

Search each file for square brackets and the following, and replace sitewide:

| Placeholder | Found in |
|---|---|
| `[Office Address]`, `[City]`, `[State]`, `[PIN Code]` | footer (all pages), contact.html, JSON-LD in every `<head>` |
| `+91 XXXXX XXXXX` / `+91-XXXXXXXXXX` | footer, contact.html, JSON-LD |
| `contact@kesarilawfirm.com` | placeholder derived from firm name — confirm the real inbox |
| `www.kesarilawfirm.com` | **Confirm domain spelling.** Used throughout as the canonical domain — verify against the registered domain before launch (I have `kesharilawfirm.com`, with an "h", on file from an earlier compliance audit — please confirm which is correct) |
| `https://formspree.io/f/YOUR_FORM_ID` | `contact.html` — the consultation form won't submit anywhere until this is replaced with a real endpoint |
| `[University Name]`, Bar Council enrolment details, Bar Association names | about.html, team.html, JSON-LD Person block |
| Google Maps embed | `contact.html` has a placeholder box with the ready-to-use iframe snippet in an HTML comment right above it |
| `assets/og-image.jpg` | referenced in every page's Open Graph/Twitter tags but not generated — add a real 1200×630 share image (happy to design one if useful) |
| Sample articles (insights.html) and publication entries | clearly labelled as samples — swap for real content |
| Team placeholder cards (team.html) | intentionally left as editable placeholders rather than invented names — add real associates if applicable |

## Editing Content

**Small text edits:** edit the HTML files directly — they're plain, readable
markup.

**Sitewide changes** (e.g. phone number, footer links, nav structure): edit
the shared blocks in `build.py`, then run:

```bash
python3 regenerate_all.py
```

This rewrites every generated page from the `gen_part*.py` scripts so the
header, footer, and disclaimer stay byte-identical across all 11 pages.
`index.html` is hand-authored and isn't touched by this script.

## Deployment (GitHub Pages)

1. Delete the `build.py` / `gen_part*.py` / `regenerate_all.py` files if you
   don't want the build tooling in the public repo (optional — they aren't
   linked from anywhere and are harmless either way).
2. Push the contents of this folder to the repo root (`index.html` must sit
   at the repository root for GitHub Pages to serve it correctly).
3. Point the custom domain at GitHub Pages via Namecheap DNS, same pattern
   as the LegalScale site.
4. Once live, submit `sitemap.xml` in Google Search Console.

## Design System

- **Palette:** Off-White `#F8F9FA` background · Forest Green `#1B4332`
  primary · Champagne Gold `#D4AF37` accent (used only for dividers, icons,
  borders, and button fills — never for body text, to preserve contrast) ·
  Onyx `#353535` text.
- **Type:** Cormorant Garamond (headings) + Inter (body), loaded via Google
  Fonts with system-font fallbacks if the connection is slow or blocked.
- **Signature motif:** a custom line-art scales-of-justice mark, used as the
  favicon, the header/footer brand mark, and — set inside a ringed seal — as
  the section-divider and hero watermark. It's the one recurring visual idea
  that ties every page together, standing in for the "official seal" register
  of trust and authority the brief asked for.
- **Interaction:** the entry disclaimer and the mobile nav are both pure
  CSS (checkbox pattern, no JavaScript), so they work even if scripts are
  blocked. There's deliberately **no** load-in or scroll-reveal animation —
  early QA found that both JS-triggered and animation-based reveal effects
  can leave content stuck at `opacity:0` if the trigger never fires (a real
  risk for search crawlers and slow connections), so motion is limited to
  hover and toggle states, which only ever start from a visible default.

## BCI Rule 36 Compliance Notes

- No testimonials, ratings, superlatives ("best", "top", "no. 1"), success-
  rate claims, or unverified awards anywhere in the copy.
- No comparative claims against other advocates or firms.
- Entry disclaimer (CSS-driven, no localStorage) plus a full `/disclaimer.html`.
- Advocate name is present sitewide; the Bar Council enrolment number is
  placeholdered and must be added before launch — it's currently the one
  required compliance element that's missing real data.
- Legal/policy pages (Privacy, Terms, Cookies, Accessibility) are drafted as
  solid standard templates but are not a substitute for review by qualified
  counsel before publishing — recommend a final pass given LegalScale's own
  compliance expertise.
