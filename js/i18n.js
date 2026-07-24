// Requires I18N (from js/i18n-data.js) to be loaded first.
(function () {

  /**
   * Safely set translated text on an element.
   * - If the element has NO child element nodes (it is a pure text leaf),
   *   we simply set textContent — safe and fast.
   * - If the element has child element nodes (e.g. a <span class="script"> inside),
   *   we walk its child nodes and update only Text nodes, preserving element children.
   *   This prevents wiping icons, decorative spans, etc.
   */
  function safeSetText(el, text) {
    var hasElementChild = false;
    el.childNodes.forEach(function(n) { if (n.nodeType === 1) hasElementChild = true; });
    if (!hasElementChild) {
      el.textContent = text;
    } else {
      // Replace the first direct text node only (common pattern: text before/after inline elements)
      var replaced = false;
      el.childNodes.forEach(function(n) {
        if (!replaced && n.nodeType === 3 && n.textContent.trim().length > 0) {
          n.textContent = text + ' ';
          replaced = true;
        }
      });
      if (!replaced) {
        // Fallback: prepend a text node
        el.insertBefore(document.createTextNode(text), el.firstChild);
      }
    }
  }

  function applyLang(lang) {
    var l = (lang === 'sw') ? 'sw' : 'en';
    document.documentElement.setAttribute('lang', l);

    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var key = el.getAttribute('data-i18n');
      var entry = window.I18N && window.I18N[key];
      if (entry) { safeSetText(el, entry[l] || entry.en); }
    });

    document.querySelectorAll('[data-i18n-ph]').forEach(function (el) {
      var key = el.getAttribute('data-i18n-ph');
      var entry = window.I18N && window.I18N[key];
      if (entry) { el.setAttribute('placeholder', entry[l] || entry.en); }
    });

    try { localStorage.setItem('aag-lang', l); } catch (e) {}

    document.querySelectorAll('.lang-btn').forEach(function (b) {
      b.classList.toggle('active', b.getAttribute('data-lang') === l);
    });
  }

  function setTheme(mode) {
    var m = (mode === 'light') ? 'light' : 'dark';
    document.documentElement.classList.toggle('light-mode', m === 'light');
    try { localStorage.setItem('aag-theme', m); } catch (e) {}
    document.querySelectorAll('.theme-btn').forEach(function (b) {
      b.classList.toggle('active', b.getAttribute('data-theme') === m);
    });
  }

  document.querySelectorAll('.lang-btn').forEach(function (b) {
    b.addEventListener('click', function () { applyLang(b.getAttribute('data-lang')); });
  });
  document.querySelectorAll('.theme-btn').forEach(function (b) {
    b.addEventListener('click', function () { setTheme(b.getAttribute('data-theme')); });
  });

  var savedLang = 'en';
  try { savedLang = localStorage.getItem('aag-lang') || 'en'; } catch (e) {}
  applyLang(savedLang);

  var savedTheme = 'light';
  try { savedTheme = localStorage.getItem('aag-theme') || 'light'; } catch (e) {}
  setTheme(savedTheme);
})();
