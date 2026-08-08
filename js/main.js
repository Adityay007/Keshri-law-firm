/* ==========================================================================
   KESARI LAW FIRM — main.js
   Progressive enhancement only. Navigation, the mobile menu, and the entry
   disclaimer all work with CSS alone (checkbox pattern) — nothing here is
   load-bearing. This keeps the site resilient to script blockers, ad
   blockers, or DNS/CDN-level script interference.
   ========================================================================== */

// Flag JS as available so CSS can safely enable the reveal-on-scroll effect.
// (Elements only start hidden once this class exists — see html.js .reveal in styles.css)
document.documentElement.classList.add('js');

document.addEventListener('DOMContentLoaded', function () {

  // Scroll-reveal for elements marked .reveal
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(function (el) { observer.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
  }

  // Auto-update footer copyright year
  var yearEls = document.querySelectorAll('[data-year]');
  yearEls.forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Close the mobile nav panel automatically after a link is tapped
  var navToggle = document.getElementById('nav-toggle');
  var mobileLinks = document.querySelectorAll('.mobile-nav-panel a');
  mobileLinks.forEach(function (link) {
    link.addEventListener('click', function () {
      if (navToggle) { navToggle.checked = false; }
    });
  });

  // Basic client-side confirmation state for the consultation form.
  // Actual submission handling (Formspree endpoint or equivalent) is set
  // via the form's action attribute — see contact.html.
  var consultForm = document.getElementById('consultation-form');
  if (consultForm) {
    consultForm.addEventListener('submit', function () {
      var btn = consultForm.querySelector('button[type="submit"]');
      if (btn) {
        btn.setAttribute('disabled', 'true');
        btn.textContent = 'Sending…';
      }
    });
  }
});
