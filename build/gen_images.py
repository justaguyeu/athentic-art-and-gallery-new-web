from PIL import Image, ImageDraw, ImageFont
import os, random
random.seed(11)

OUT = "/home/claude/authentic-art-and-gallery/images"

def grad(w,h,c1,c2):
    img = Image.new("RGB",(w,h),c1)
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t = y/h
        r = int(c1[0]+(c2[0]-c1[0])*t)
        g = int(c1[1]+(c2[1]-c1[1])*t)
        b = int(c1[2]+(c2[2]-c1[2])*t)
        draw.line([(0,y),(w,y)], fill=(r,g,b))
    return img

def label(img, text, sub=""):
    draw = ImageDraw.Draw(img)
    w,h = img.size
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size=max(16,w//24))
        font_sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size=max(11,w//48))
    except Exception:
        font = ImageFont.load_default(); font_sm = font
    bbox = draw.textbbox((0,0), text, font=font)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    draw.text(((w-tw)/2, (h-th)/2 - 10), text, font=font, fill=(245,244,242))
    if sub:
        bbox2 = draw.textbbox((0,0), sub, font=font_sm)
        sw, sh = bbox2[2]-bbox2[0], bbox2[3]-bbox2[1]
        draw.text(((w-sw)/2, (h-th)/2 + th + 6), sub, font=font_sm, fill=(141,141,146))
    draw.rectangle([0,0,w-1,h-1], outline=(232,121,42), width=3)
    return img

def make(name, w, h, c1, c2, title, sub="Replace with real photo"):
    img = grad(w,h,c1,c2)
    label(img, title, sub)
    path = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, quality=85)
    print("saved", path)

DARK = (10,10,11)

make("hero-bg.jpg", 1600, 900, (30,16,14), DARK, "HERO BG", "Print shop / screen printing action shot")
make("mission-bg.jpg", 1600, 900, (34,20,16), DARK, "MISSION BG", "Close-up of ink press in motion")
make("portfolio-bg.jpg", 1600, 900, (26,20,14), DARK, "PORTFOLIO BG", "Finished print products flat-lay")
make("history-bg.jpg", 1600, 900, (16,16,20), DARK, "HISTORY BG", "Founders / original shop photo")
make("mission-1.jpg", 900, 1125, (40,40,44), DARK, "STUDIO PHOTO 1", "Screen printing in progress")
make("mission-2.jpg", 900, 1125, (28,28,32), DARK, "STUDIO PHOTO 2", "Finished apparel rack")
make("gear-1.jpg", 900, 600, (34,34,36), DARK, "CRAFT PHOTO 1", "Ink & squeegee close-up")
make("gear-2.jpg", 900, 600, (22,26,42), DARK, "CRAFT PHOTO 2", "Framed art / canvas print")

products = [
    ("product-canvas.jpg", 800, 1000, (26,38,58), "CANVAS PRINT"),
    ("product-category.jpg", 1200, 900, (30,30,32), "GALLERY PRINTS"),
    ("product-tote.jpg", 700, 900, (24,24,26), "CUSTOM TOTE BAG"),
    ("product-mug.jpg", 700, 900, (22,26,42), "BRANDED MUG"),
    ("product-print.jpg", 700, 900, (22,30,48), "A3 ART PRINT"),
    ("product-tshirt.jpg", 700, 900, (34,34,34), "CUSTOM TEE"),
]
for fn,w,h,c,title in products:
    make(f"products/{fn}", w, h, c, DARK, title, "Product photo")

services = [
    ("screen-printing-hero.jpg", (30,18,16), "SCREEN PRINTING"),
    ("t-shirt-printing-hero.jpg", (18,24,30), "T-SHIRT PRINTING"),
    ("packaging-hero.jpg", (28,22,14), "PACKAGING"),
    ("wheel-covers-hero.jpg", (20,20,24), "WHEEL COVERS"),
    ("tents-banners-hero.jpg", (30,16,16), "TENTS & BANNERS"),
    ("web-software-hero.jpg", (16,20,32), "WEB & SOFTWARE"),
]
for fn,c,title in services:
    make(f"services/{fn}", 1600, 900, c, DARK, title, "Project / workspace photo")

names = ["Grace M.", "Kelvin O.", "Fatuma R.", "James P.", "Neema T.", "Brian K."]
colors = [(60,40,40),(40,50,60),(55,45,30),(35,45,35),(50,35,50),(45,45,55)]
for i,(n,c) in enumerate(zip(names,colors), start=1):
    img = grad(300,300,c,DARK)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size=64)
    except Exception:
        font = ImageFont.load_default()
    initials = "".join([p[0] for p in n.split()[:2]])
    bbox = draw.textbbox((0,0), initials, font=font)
    tw,th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    draw.text(((300-tw)/2, (300-th)/2-10), initials, font=font, fill=(245,244,242))
    draw.rectangle([0,0,299,299], outline=(232,121,42), width=3)
    img.save(f"{OUT}/testimonials/testimonial-{i}.jpg", quality=85)
    print("saved testimonial", i)

print("DONE")
