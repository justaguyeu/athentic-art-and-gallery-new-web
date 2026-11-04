"""Generate labelled placeholder images for every image slot on the site.

Each placeholder shows its file name, exact pixel size, aspect ratio, where it
is used and what the real photo should show. Export your real image at the same
size, save it over the placeholder with the same name, and the site picks it up.

Real photos already in place are listed in KEEP and never overwritten.

Run:  python build/gen_images.py
"""
from PIL import Image, ImageDraw, ImageFont
from math import gcd
import os

OUT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "images"))

# Already real photos - never overwrite these.
KEEP = {"hero-bg.jpg", "mission-bg.jpg"}

DARK = (10, 10, 11)
ACCENT = (232, 121, 42)
INK = (245, 244, 242)
DIM = (141, 141, 146)

FONT_BOLD = ["C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/arialbd.ttf",
             "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/Library/Fonts/Arial Bold.ttf"]
FONT_REG = ["C:/Windows/Fonts/segoeui.ttf", "C:/Windows/Fonts/arial.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/Library/Fonts/Arial.ttf"]


def font(paths, size):
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default(size=size)


def ratio(w, h):
    g = gcd(w, h)
    return f"{w // g}:{h // g}"


def grad(w, h, c1, c2):
    img = Image.new("RGB", (w, h), c1)
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t = y / h
        draw.line([(0, y), (w, y)], fill=tuple(int(a + (b - a) * t) for a, b in zip(c1, c2)))
    return img


def guides(draw, w, h):
    # faint grid + corner-to-corner cross so crop/focal area is easy to judge
    step = max(40, min(w, h) // 10)
    for x in range(0, w, step):
        draw.line([(x, 0), (x, h)], fill=(255, 255, 255, 10))
    for y in range(0, h, step):
        draw.line([(0, y), (w, y)], fill=(255, 255, 255, 10))
    draw.line([(0, 0), (w, h)], fill=(255, 255, 255, 18), width=2)
    draw.line([(w, 0), (0, h)], fill=(255, 255, 255, 18), width=2)


def centered(draw, w, y, text, f, fill):
    bw = draw.textbbox((0, 0), text, font=f)[2]
    draw.text(((w - bw) / 2, y), text, font=f, fill=fill)
    b = draw.textbbox((0, 0), text, font=f)
    return b[3] - b[1]


def make(name, w, h, tint, usage, subject):
    if os.path.basename(name) in KEEP:
        print("keep   ", name)
        return
    img = grad(w, h, tint, DARK).convert("RGBA")
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    guides(draw, w, h)

    s = min(w, h)
    f_name = font(FONT_BOLD, max(18, s // 16))
    f_dim = font(FONT_BOLD, max(16, s // 11))
    f_sm = font(FONT_REG, max(12, s // 34))

    # panel behind the text
    pw, ph = int(w * 0.84), int(s * 0.52)
    px, py = (w - pw) // 2, (h - ph) // 2
    draw.rectangle([px, py, px + pw, py + ph], fill=(10, 10, 11, 190), outline=(*ACCENT, 160), width=2)

    y = py + ph * 0.17
    y += centered(draw, w, y, f"{w} \u00d7 {h}", f_dim, ACCENT) + s * 0.04
    y += centered(draw, w, y, os.path.basename(name), f_name, INK) + s * 0.05
    y += centered(draw, w, y, f"{ratio(w, h)}  \u00b7  {usage}", f_sm, DIM) + s * 0.025
    centered(draw, w, y, subject, f_sm, DIM)

    draw.rectangle([0, 0, w - 1, h - 1], outline=ACCENT, width=4)
    out = Image.alpha_composite(img, layer).convert("RGB")
    path = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    out.save(path, quality=88)
    print("saved  ", name, f"{w}x{h}")


# (file, width, height, tint, where it's used, what the real photo should show)
IMAGES = [
    # Full-bleed page backgrounds - 16:9
    ("hero-bg.jpg", 1920, 1080, (30, 16, 14), "Home hero background", "Print shop / screen printing action shot"),
    ("mission-bg.jpg", 1920, 1080, (34, 20, 16), "Home mission background", "Printed banner / work on location"),
    ("history-bg.jpg", 1920, 1080, (16, 16, 20), "History page hero", "Founders / original shop photo"),
    ("portfolio-bg.jpg", 1920, 1080, (26, 20, 14), "Portfolio page hero", "Finished print products flat-lay"),

    # About page photo blocks - 4:5 portrait
    ("about-studio-1.jpg", 1000, 1250, (40, 40, 44), "About page photo block A", "Screen printing in progress"),
    ("about-studio-2.jpg", 1000, 1250, (28, 28, 32), "About page photo block B", "Finished apparel rack"),

    # Shop page gear strip - 3:2
    ("shop-gear-1.jpg", 1200, 800, (34, 34, 36), "Shop gear strip (left)", "Ink & squeegee close-up"),
    ("shop-gear-2.jpg", 1200, 800, (22, 26, 42), "Shop gear strip (right)", "Framed canvas print"),

    # Shop featured blocks
    ("products/product-canvas.jpg", 1000, 1000, (26, 38, 58), "Shop featured product", "Canvas print (1m\u00b2), bestseller"),
    ("products/product-category.jpg", 1600, 1000, (30, 30, 32), "Shop 'Gallery Prints' category card", "Wall of gallery prints"),

    # Shop product cards - 3:4 portrait
    ("products/product-canvas-framed.jpg", 900, 1200, (22, 30, 48), "Shop product card", "Canvas with wooden frame"),
    ("products/product-tshirt.jpg", 900, 1200, (34, 34, 34), "Shop product card", "Custom printed T-shirt"),
    ("products/product-mug.jpg", 900, 1200, (22, 26, 42), "Shop product card", "Branded mug"),
    ("products/product-magic-mug.jpg", 900, 1200, (40, 26, 40), "Shop product card", "Magic (colour-change) mug"),

    # Service heroes - 16:9, used on services.html, home cards and each service page
    ("services/screen-printing-hero.jpg", 1920, 1080, (30, 18, 16), "Screen Printing & Apparel", "Screen printing press / printed apparel"),
    ("services/packaging-bags-hero.jpg", 1920, 1080, (28, 22, 14), "Packaging & Branded Bags", "Branded bags & boxes"),
    ("services/signage-banners-hero.jpg", 1920, 1080, (30, 16, 16), "Signage & Banners", "Banners, tents, roll-ups at an event"),
    ("services/tire-covers-hero.jpg", 1920, 1080, (20, 20, 24), "Wheel & Tire Covers", "Branded spare-wheel cover on a vehicle"),
    ("services/promo-items-hero.jpg", 1920, 1080, (22, 26, 42), "Promotional Items", "Mugs, pens, caps, keyrings with logos"),
    ("services/print-stationery-hero.jpg", 1920, 1080, (18, 24, 30), "Print & Stationery", "Business cards, letterheads, flyers"),
    ("services/design-services-hero.jpg", 1920, 1080, (32, 20, 30), "Design Services", "Designer at work / logo sketches"),
    ("services/web-software-hero.jpg", 1920, 1080, (16, 20, 32), "Website & Software Development", "Laptop with website / code"),
]

# Testimonial avatars - square, shown small and round
TESTIMONIALS = [
    ("Grace M.", (60, 40, 40)), ("Kelvin O.", (40, 50, 60)), ("Fatuma R.", (55, 45, 30)),
    ("James P.", (35, 45, 35)), ("Neema T.", (50, 35, 50)), ("Brian K.", (45, 45, 55)),
]


def make_avatar(i, person, tint, size=400):
    img = grad(size, size, tint, DARK)
    draw = ImageDraw.Draw(img)
    initials = "".join(p[0] for p in person.split()[:2])
    centered(draw, size, size * 0.24, initials, font(FONT_BOLD, size // 4), INK)
    centered(draw, size, size * 0.58, f"{size} \u00d7 {size}", font(FONT_BOLD, size // 14), ACCENT)
    centered(draw, size, size * 0.70, f"testimonial-{i}.jpg", font(FONT_REG, size // 18), DIM)
    draw.rectangle([0, 0, size - 1, size - 1], outline=ACCENT, width=4)
    name = f"testimonials/testimonial-{i}.jpg"
    os.makedirs(os.path.join(OUT, "testimonials"), exist_ok=True)
    img.save(os.path.join(OUT, name), quality=88)
    print("saved  ", name, f"{size}x{size}  ({person})")


if __name__ == "__main__":
    for args in IMAGES:
        make(*args)
    for i, (person, tint) in enumerate(TESTIMONIALS, start=1):
        make_avatar(i, person, tint)
    print("DONE")
