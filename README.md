# Authentic Art &amp; Gallery — Website

A multi-page static site (plain HTML/CSS/JS, no build step required). Open `index.html` in a browser, or upload the whole folder to any static host (Netlify, Render, GitHub Pages, etc.).

## Language switch (EN / SW) and Dark / Light mode

Every page has two controls in the top-right of the nav (and in the mobile menu):

- **EN / SW** — switches the entire site between English and Swahili. Nav, buttons, headings, paragraphs, footer, testimonials, service descriptions, pricing table headers, and the full history timeline are all translated. The choice is remembered (via `localStorage`) so it stays consistent as visitors move between pages.
- **Dark / Light** — switches the whole site between the default dark theme and a full light theme (not just a grayscale filter): background, card surfaces, borders, and text all swap to a warm off-white/cream palette with dark text, while the brand orange accent stays consistent in both. Also remembered across pages.

### How it works

- `js/i18n-data.js` — auto-generated from `build/gen_site4.py`; a single JSON object (`I18N`) with every translatable string in both languages, keyed by name (e.g. `nav_services`, `svc-screen-printing-desc`).
- `js/i18n.js` — small runtime script: reads `I18N`, swaps `textContent` on every element tagged `data-i18n="key"` (and `placeholder` on `data-i18n-ph`), and toggles a `light-mode` class on `<html>` for the theme switch. Both preferences persist in `localStorage` (`aag-lang`, `aag-theme`) and are re-applied instantly on every page load (a tiny inline script in `<head>` applies the `light-mode` class before first paint to avoid a flash of the wrong theme).
- `css/base.css` — every color in the site (backgrounds, text, borders, overlay gradients on hero/photo sections, table hover states) is driven by CSS custom properties (`--bg`, `--ink`, `--line`, `--bg-rgb`, `--ink-rgb`, etc.). `html.light-mode` simply overrides those tokens, and every component — nav, cards, footer, pricing tables, hero overlays — cascades correctly because nothing else hardcodes a color.

### What's translated vs. left as-is

Translated: navigation, buttons, headings, section intros, footer, testimonials, all 8 service names/descriptions/"best for" notes, Design Services & Website/Software offering lists, the full History timeline, and the About mission statement.

Left in English in both languages (matches your original PDF, which is itself in English): individual pricing-table rows — product names, sizes, quantities, and prices (e.g. "Lunchbox", "8 inch", "100pc", "100,000/-"). Only the table **column headers** ("Product/Size/Qty/Price" → "Bidhaa/Ukubwa/Idadi/Bei") are translated. This mirrors how the real price list is written and avoids translating SKU-style catalog terms that read oddly translated.

### Adding or editing translations

Everything routes through one dictionary at the top of `build/gen_site4.py` (the `TR` dict, built via the `add(key, english, swahili)` helper, plus bilingual fields directly on the `SERVICES`, `TESTIMONIALS`, and `TIMELINE` data). Edit the Swahili (or English) text there and rerun:

```
python3 gen_site4.py
```

— this regenerates every HTML page **and** `js/i18n-data.js` together, so they never drift out of sync. If you only need a quick wording tweak, editing `js/i18n-data.js` directly is also fine — it drives the switch on every page without needing to touch the HTML.

## Responsiveness

The site is built mobile-first with fluid type (`clamp()`) throughout, and has been checked across these breakpoints:

- **≤560px** (small phones) — single-column grids, stacked footer, price tables switch to horizontal scroll instead of squeezing columns
- **≤620–780px** (large phones / small tablets) — service/product/testimonial grids collapse to 1–2 columns, schedule rows restack
- **≤820px** (tablets / narrow laptops) — nav collapses into the slide-in mobile drawer (language/theme switches move there too)
- **821–1150px** (small laptops) — nav gaps tighten and the Instagram handle text hides (icon stays) so the language/theme switches don't crowd the nav links
- **≥1150px** (desktop) — full layout

All animations respect `prefers-reduced-motion`, and the mobile drawer, price tables, and sticky sidebar all have explicit fallback layouts rather than just shrinking.

## What's real vs. placeholder

**Real, taken directly from your 2026 price list PDF:**

- All product pricing across every service (screen printing, apparel, packaging, signage, tire covers, promo items, print & stationery)
- The 5 Design Services: Logo Design, Brand Identity System, Brand Strategy Basics, Social Media Branding, Packaging Design
- Contact details: **authenticartandgallry@gmail.com**, **+255 756 414 824**, **www.authenticartandgallery.com**
- Instagram: **https://www.instagram.com/authenticartandgallery/**
- Brand colors: orange `#e8792a` and dark navy `#29343d`, sampled from your logo and price list headers
- A serif logotype ("authentic" in Playfair Display with an orange dot on the "i", small-caps "art & gallery" beneath) approximating your real lockup, plus a simplified triangle/"A" mark inspired by your logo icon

**Still placeholder — replace before launch:**

- All photography in `/images` (see table below)
- The studio address in the footer ("Arusha, Tanzania" — generic, not a real street address)
- The nav/footer logo mark is a simplified SVG approximation of your real logo, not the actual file

## Structure

```
/
├── index.html            Home
├── services.html         Full services grid — all 8 categories with real pricing
├── portfolio.html        Recent work marquee + full project list
├── shop.html              Gallery & merch shop (canvas prints, mugs, tees — real prices)
├── about.html             Mission / values
├── history.html           Company timeline
├── services/
│   ├── screen-printing.html        T-Shirts, Polos, Safari Shirts, Caps
│   ├── packaging-bags.html         Lunchboxes, Pizza Boxes, Handle Bags, Paper Bags, D-Cut, Loop Handle
│   ├── signage-banners.html        Banners, Stickers, Canvas
│   ├── tire-covers.html            Banner & Canvas Tire Covers
│   ├── promo-items.html            Mugs, Magic Mugs, Water Bottles
│   ├── print-stationery.html       Business Cards, Flyers, Brochures, Product Labels
│   ├── design-services.html        Logo, Brand Identity, Brand Strategy, Social Media Branding, Packaging Design (quote-based)
│   └── web-software.html           Website & Software Development (quote-based)
├── css/
│   ├── base.css              Shared tokens, nav, footer, buttons, reveal animation, brand logotype, language/theme switch styles, B&W mode
│   ├── testimonials.css      Shared testimonials component
│   ├── home.css               index.html only
│   ├── services.css           services.html only
│   ├── portfolio.css          portfolio.html only
│   ├── shop.css                shop.html only
│   ├── about.css               about.html only
│   ├── history.css             history.html only
│   └── service-detail.css      services/*.html only — includes the price-table component
├── js/
│   ├── main.js                 Nav scroll state, mobile drawer, scroll-reveal, newsletter demo handler
│   ├── i18n-data.js            Auto-generated EN/SW translation dictionary (see above)
│   └── i18n.js                 Language switch + B&W mode runtime logic
└── images/                     Placeholder photography — replace these, keep the filenames
```

## Pricing pages

Every physical-product service (screen printing, packaging, signage, tire covers, promo items, print & stationery) has a full **Product / Size / Qty / Price** table on its detail page, taken straight from your price list, plus the same "price changes according to..." note that appeared on the original PDF page for that category.

Design Services and Website & Software Development are **quote-only** — their detail pages list what's included and point to a "Request a Quote" button (pre-filled mailto) plus your phone number, matching how your PDF handles them ("Prices available upon request...").

## Using your real logo

Right now the nav/footer mark is an inline SVG approximation (a triangle with a smaller triangle cut out, similar in spirit to your peak/"A" icon). To use your actual logo:

1. Export your real logo as an SVG or PNG (transparent background) and drop it in `/images/logo.svg` (or `.png`).
2. In `css/base.css`, the `.brand svg` rule controls sizing — you can replace the inline `<svg>...</svg>` markup in each page's `<a class="brand">` block with `<img src="images/logo.svg" alt="Authentic Art & Gallery">` instead.
3. If you want to regenerate all pages at once, edit the `logo_svg()` function at the top of `build/gen_site4.py` and rerun `python3 gen_site4.py`.

## Replacing placeholder images

Every image in `/images` is a labeled placeholder generated at the correct aspect ratio for its slot. **Keep the exact filenames** and everything updates automatically:

| File                                    | Used for                         |
| --------------------------------------- | -------------------------------- |
| `images/hero-bg.jpg`                    | Home hero background             |
| `images/mission-bg.jpg`                 | "One Studio, Every Surface" band |
| `images/portfolio-bg.jpg`               | Portfolio page hero              |
| `images/history-bg.jpg`                 | History page hero                |
| `images/mission-1.jpg`, `mission-2.jpg` | About page photos                |
| `images/gear-1.jpg`, `gear-2.jpg`       | Shop craft section               |
| `images/products/*.jpg`                 | Shop product cards               |
| `images/services/*-hero.jpg`            | Each service's detail page hero  |
| `images/testimonials/testimonial-*.jpg` | Testimonial avatars              |

## Editing content

All pricing, service descriptions, design service offerings, contact info, testimonials, and translations are defined once at the top of `build/gen_site4.py`. Edit the data there and rerun:

```
python3 gen_site4.py
```

to regenerate every page (and the translation file) consistently — or edit each HTML file directly if you only need a small tweak.

Newsletter signup currently just shows a "Joined ✓" confirmation client-side (`handleSignup` in `js/main.js`) — wire it up to your actual email provider / backend endpoint.

## Notes

- Fonts: Playfair Display (logotype), Space Grotesk (headings), Manrope (body), Caveat (script accents) — all via Google Fonts CDN.
- All animations respect `prefers-reduced-motion`.
- Fully responsive down to small mobile widths, with a slide-in mobile nav drawer under 820px (language/theme switches move into that drawer on mobile).
#   a t h e n t i c - a r t - a n d - g a l l e r y - n e w - w e b  
 #   a t h e n t i c - a r t - a n d - g a l l e r y - n e w - w e b  
 