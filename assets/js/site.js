// Mobile nav, work filters, scroll reveal.
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.addEventListener('click', function (e) {
      if (e.target.closest('a')) { links.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); }
    });
  }

  var filters = document.querySelectorAll('.filter');
  var cards = document.querySelectorAll('.work .card');
  filters.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var f = btn.getAttribute('data-filter');
      filters.forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
      cards.forEach(function (c) {
        var tags = (c.getAttribute('data-tags') || '').split(' ');
        c.hidden = !(f === 'all' || tags.indexOf(f) !== -1);
      });
    });
  });

  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) { els.forEach(function (el) { el.classList.add('in'); }); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { rootMargin: '0px 0px -8% 0px' });
  els.forEach(function (el) { io.observe(el); });
})();

// Cal.com booking pop-up. The embed script loads on the first click only;
// without JavaScript the button is a normal link to the booking page.
(function () {
  var CAL_LINK = 'abduloare/intro';
  var ready = false;
  function loadCal() {
    (function (C, A, L) { var p = function (a, ar) { a.q.push(ar); }; var d = C.document; C.Cal = C.Cal || function () { var cal = C.Cal; var ar = arguments; if (!cal.loaded) { cal.ns = {}; cal.q = cal.q || []; d.head.appendChild(d.createElement('script')).src = A; cal.loaded = true; } if (ar[0] === L) { var api = function () { p(api, arguments); }; var namespace = ar[1]; api.q = api.q || []; if (typeof namespace === 'string') { cal.ns[namespace] = cal.ns[namespace] || api; p(cal.ns[namespace], ar); p(cal, ['initNamespace', namespace]); } else p(cal, ar); return; } p(cal, ar); }; })(window, 'https://app.cal.com/embed/embed.js', 'init');
    window.Cal('init', 'intro', { origin: 'https://cal.com' });
    window.Cal.ns.intro('ui', { theme: 'dark', hideEventTypeDetails: false, layout: 'month_view', cssVarsPerTheme: { dark: { 'cal-brand': '#08D2DF', 'cal-brand-text': '#001414' } } });
    ready = true;
  }
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('[data-book]');
    if (!btn || e.metaKey || e.ctrlKey || e.shiftKey) return;
    e.preventDefault();
    if (!ready) loadCal();
    window.Cal.ns.intro('modal', { calLink: CAL_LINK, config: { layout: 'month_view', theme: 'dark' } });
  });
})();
