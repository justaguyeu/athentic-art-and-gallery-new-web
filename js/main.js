// ---- Nav scroll state ----
const nav = document.getElementById('nav');
if (nav) {
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 40);
  }, { passive: true });
}

// ---- Mobile drawer ----
const burgerBtn = document.getElementById('burgerBtn');
const drawer = document.getElementById('mobileDrawer');
const closeDrawer = document.getElementById('closeDrawer');
if (burgerBtn && drawer) {
  burgerBtn.addEventListener('click', () => {
    drawer.classList.add('open');
    document.body.classList.add('drawer-open');
  });
  closeDrawer.addEventListener('click', () => {
    drawer.classList.remove('open');
    document.body.classList.remove('drawer-open');
  });
  drawer.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    drawer.classList.remove('open');
    document.body.classList.remove('drawer-open');
  }));
}

// ---- Scroll reveal (including left/right variants) ----
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal, .reveal-stagger, .reveal-left, .reveal-right').forEach(el => io.observe(el));

// ---- Signup handler (demo only — wire up to your backend/ESP) ----
function handleSignup(ev) {
  ev.preventDefault();
  const btn = ev.target.querySelector('button');
  const original = btn.textContent;
  btn.textContent = 'Joined ✓';
  setTimeout(() => btn.textContent = original, 2200);
  return false;
}

// ---- Active nav link highlighting ----
(function highlightActiveNav() {
  const path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a, .mobile-drawer nav a').forEach(a => {
    const href = a.getAttribute('href');
    if (href && href.indexOf(path) !== -1 && path !== '') {
      a.classList.add('active');
    }
  });
})();

// ---- Cursor spotlight glow ----
(function initCursorGlow() {
  // Respect reduced-motion preference
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const glow = document.createElement('div');
  glow.id = 'cursor-glow';
  Object.assign(glow.style, {
    position: 'fixed',
    pointerEvents: 'none',
    zIndex: '9999',
    width: '380px',
    height: '380px',
    borderRadius: '50%',
    background: 'radial-gradient(circle, rgba(232,121,42,.10) 0%, transparent 72%)',
    transform: 'translate(-50%, -50%)',
    transition: 'opacity .4s ease',
    opacity: '0',
    left: '-9999px',
    top: '-9999px',
    mixBlendMode: 'screen'
  });
  document.body.appendChild(glow);

  let raf;
  let tx = 0, ty = 0, cx = 0, cy = 0;

  window.addEventListener('mousemove', (e) => {
    tx = e.clientX; ty = e.clientY;
    glow.style.opacity = '1';
    if (!raf) raf = requestAnimationFrame(animateGlow);
  }, { passive: true });

  window.addEventListener('mouseleave', () => { glow.style.opacity = '0'; });

  function animateGlow() {
    cx += (tx - cx) * 0.1;
    cy += (ty - cy) * 0.1;
    glow.style.left = cx + 'px';
    glow.style.top  = cy + 'px';
    const dist = Math.hypot(tx - cx, ty - cy);
    raf = dist > 0.5 ? requestAnimationFrame(animateGlow) : null;
  }
})();

// ---- 3-D tilt on cards ----
(function initCardTilt() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if ('ontouchstart' in window) return; // skip on touch

  document.querySelectorAll('.teaser-card, .testi-card, .halisi-inner').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const r  = card.getBoundingClientRect();
      const mx = (e.clientX - r.left) / r.width  - 0.5;
      const my = (e.clientY - r.top)  / r.height - 0.5;
      card.style.transform = `perspective(700px) rotateY(${mx * 6}deg) rotateX(${-my * 5}deg) translateZ(4px)`;
      card.style.transition = 'transform 0s';
    });
    card.addEventListener('mouseleave', () => {
      card.style.transition = 'transform .55s cubic-bezier(.16,.84,.28,1)';
      card.style.transform  = 'perspective(700px) rotateY(0) rotateX(0) translateZ(0)';
    });
  });
})();
