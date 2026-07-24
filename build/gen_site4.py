import os, json, html as html_lib

ROOT = "/home/claude/authentic-art-and-gallery"
INSTAGRAM_URL = "https://www.instagram.com/authenticartandgallery/"
INSTAGRAM_HANDLE = "@authenticartandgallery"
EMAIL = "authenticartandgallry@gmail.com"   # exactly as given on the real price list
PHONE = "+255 756 414 824"
WEBSITE = "www.authenticartandgallery.com"
ADDRESS_NOTE_KEY = "footer_address"

# ======================================================================
# TRANSLATION DICTIONARY — single source of truth for both the initial
# HTML render (Python) and the client-side language switch (JS).
# ======================================================================
TR = {}
def add(key, en, sw):
    TR[key] = {"en": en, "sw": sw}

def esc(s):
    return html_lib.escape(s, quote=False)

def t(key):
    """Render a data-i18n span using the English default (client JS swaps at runtime)."""
    return f'<span data-i18n="{key}">{esc(TR[key]["en"])}</span>'

def tph(key):
    """Return an attribute fragment for a translatable placeholder."""
    return f'data-i18n-ph="{key}" placeholder="{esc(TR[key]["en"])}"'

# --- nav ---
add("nav_services", "Services", "Huduma")
add("nav_portfolio", "Portfolio", "Kazi Zetu")
add("nav_shop", "Shop", "Duka")
add("nav_about", "About", "Kuhusu Sisi")
add("nav_history", "History", "Historia")

# --- shared buttons / labels ---
add("btn_get_quote", "Get a Quote", "Pata Bei")
add("btn_view_service_details", "View Service Details", "Angalia Maelezo ya Huduma")
add("btn_view_service", "View Service", "Angalia Huduma")
add("btn_signup", "Signup", "Jisajili")
add("btn_see_all_services", "See All Services", "Ona Huduma Zote")
add("btn_request_quote", "Request a Quote", "Omba Bei")
add("btn_shop_prints", "Shop Prints", "Nunua Michoro")
add("newsletter_email_ph", "Your email...", "Barua pepe yako...")

add("label_starting_at", "Starting At:", "Kuanzia:")
add("label_best_for", "Best For:", "Bora Kwa:")
add("label_products", "Products:", "Bidhaa:")
add("label_pricing", "Pricing:", "Bei:")
add("label_includes", "Includes:", "Inajumuisha:")
add("label_on_request", "On Request", "Kwa Ombi")

# --- footer ---
add("footer_heading", "Get updates from Authentic Art & Gallery", "Pata Taarifa kutoka Authentic Art & Gallery")
add("footer_sub", "New drops, print specials, and behind-the-scenes from the studio — straight to your inbox.",
    "Bidhaa mpya, ofa za uchapishaji, na habari za ndani ya studio — moja kwa moja kwenye barua pepe yako.")
add("footer_services_line",
    "Screen Printing · Apparel · Packaging · Signage · Tire Covers · Promo Items · Print · Design · Web & Software · Original Art",
    "Uchapishaji wa Skrini · Mavazi · Ufungashaji · Alama za Matangazo · Vifuniko vya Matairi · Bidhaa za Matangazo · Uchapishaji · Ubunifu · Tovuti na Programu · Sanaa Asili")
add("footer_address", "Arusha, Tanzania", "Arusha, Tanzania")
add("footer_credits", "Site Credits", "Sifa za Tovuti")

# --- home ---
add("home_ghost_word", "Print.", "Chapa.")
add("home_ghost_line1", "One Studio, Every", "Studio Moja, Huduma")
add("home_ghost_line2", "Surface", "Zote")
add("home_quote_role", "Screen Printing Experts & Founders", "Wataalamu wa Uchapishaji wa Skrini na Waanzilishi")
add("home_pill_tag", "Most Requested", "Inayohitajika Zaidi")
add("home_featured_eyebrow", "Featured Services", "Huduma Maalum")
add("home_featured_heading", "Three ways we bring ideas to life.", "Njia Tatu Tunazotimiza Mawazo Yako.")

# --- services page ---
add("services_h1a", "Printing Experts.", "Wataalamu wa Uchapishaji.")
add("services_h1b", "Service by Service.", "Huduma kwa Huduma.")
add("services_script_tag", "Built to Order", "Kutengenezwa kwa Agizo")
add("services_desc",
    "From a single custom t-shirt to a fleet's worth of branded wheel covers, from packaging to full brand identities, websites, and software. If it can carry your brand, we can print it, design it, or build it.",
    "Kuanzia fulana moja maalum hadi vifuniko vya matairi vya gari zima, kutoka ufungashaji hadi chapa kamili za biashara, tovuti, na programu. Ikiwa kinaweza kubeba chapa yako, tunaweza kukichapisha, kukibuni, au kukijenga.")
add("stat_country", "Tanzania", "Tanzania")
add("stat_beyond", "+ Beyond", "+ Zaidi")
add("stat_built_to_order", "Built to Order", "Kutengenezwa kwa Agizo")
add("stat_authentic", "Every Print is Authentic", "Kila Chapa ni Halisi")
add("services_testi_heading", "Clients Behind the Orders", "Wateja Nyuma ya Maagizo")
add("services_testi_sub", "Every service has its own regulars. Here's what a few of them have to say.",
    "Kila huduma ina wateja wake wa kudumu. Haya ndiyo baadhi wanayosema.")

# --- testimonials (default, used on home) ---
add("testi_heading_default", "What Clients Say", "Wateja Wanasemaje")
add("testi_sub_default", "Real feedback from the businesses and collectors we print, design, and build for.",
    "Maoni halisi kutoka kwa biashara na wakusanyaji tunaowachapishia, kuwabunia, na kuwajengea.")

# --- portfolio ---
add("portfolio_h1", "Portfolio", "Kazi Zetu")
add("portfolio_sub", "A running log of what's left the studio recently — from single t-shirts to full fleets, brand identities, and websites.",
    "Orodha ya kazi zilizotoka studio hivi karibuni — kuanzia fulana moja hadi magari yote ya kampuni, chapa za biashara, na tovuti.")
add("portfolio_eyebrow", "Recent Work", "Kazi za Hivi Karibuni")
add("portfolio_heading", "Every project, in order.", "Kila Mradi, kwa Mpangilio.")
add("label_client", "Client", "Mteja")
add("label_service", "Service", "Huduma")

# --- shop ---
add("shop_eyebrow", "Gallery & Prints", "Sanaa na Michoro")
add("shop_h1", "Art worth printing.", "Sanaa Inayostahili Kuchapishwa.")
add("shop_sub", "Original pieces and studio-quality prints, sold straight from the gallery that also runs our print floor — so every canvas ships with the same care as a client order.",
    "Kazi asili na michoro bora ya studio, zinazouzwa moja kwa moja kutoka kwenye sanaa inayoendesha pia sehemu yetu ya uchapishaji — hivyo kila turubai hutumwa kwa uangalifu ule ule kama agizo la mteja.")
add("shop_popular_categories", "Popular Categories", "Aina Maarufu")
add("shop_gear_quote",
    "May every piece we print or paint carry the same authenticity — whether it's on a t-shirt, a wall, or a screen.",
    "Kila kazi tunayoichapisha au kuipaka rangi na ibebe uhalisia ule ule — iwe kwenye fulana, ukuta, au skrini.")
add("shop_badge_bestseller", "Bestseller", "Inayouzwa Zaidi")

# --- about ---
add("about_mission",
    "Every print tells a story. We started as a screen printing shop and grew into a studio that prints apparel, packaging, signage, and tire covers, designs brands and builds websites and software, and sells the original art that inspires all of it. So, what will it carry today — 'just a print' or something Authentic?",
    "Kila chapa ina hadithi yake. Tulianza kama duka la uchapishaji wa skrini na kukua kuwa studio inayochapisha mavazi, ufungashaji, alama za matangazo, na vifuniko vya matairi, kubuni chapa za biashara na kujenga tovuti na programu, na kuuza sanaa asili inayochochea haya yote. Kwa hiyo, leo itabeba nini — 'chapa tu' au kitu Halisi (Authentic)?")
add("about_cta_line", "Have a project in mind?", "Una mradi akilini?")
add("about_eyebrow", "What We Stand For", "Tunachosimamia")
add("about_heading", "Authentic, on every surface.", "Halisi, kwenye kila uso.")
add("value1_title", "Quality craftsmanship", "Ustadi wa Hali ya Juu")
add("value1_desc", "From ink density on a t-shirt to code quality on a website — we hold every medium to the same standard.",
    "Kuanzia unene wa wino kwenye fulana hadi ubora wa msimbo kwenye tovuti — tunashikilia kila njia kwa kiwango kile kile.")
add("value2_title", "Built to order", "Kutengenezwa kwa Agizo")
add("value2_desc", "One tee or a thousand, one banner or a full brand identity — every order gets the same attention to detail.",
    "Fulana moja au elfu, bango moja au chapa kamili ya biashara — kila agizo hupata umakini ule ule.")
add("value3_title", "Authentic, always", "Halisi, Daima")
add("value3_desc", "We print what you actually asked for, design what you actually need, and sell art we'd hang ourselves.",
    "Tunachapisha kile ulichoomba, tunabuni kile unachohitaji, na tunauza sanaa ambayo sisi wenyewe tungependa kuining'iniza.")

# --- history ---
add("history_eyebrow", "Our Story", "Hadithi Yetu")
add("history_h1", "From one table to a full studio.", "Kutoka Meza Moja hadi Studio Kamili.")
add("history_sub",
    "What started as a single screen printing table in Arusha is now a studio that prints, designs, builds, and sells — still run on the same idea: every piece we make should be authentic.",
    "Kilichoanza kama meza moja ya uchapishaji wa skrini jijini Arusha sasa ni studio inayochapisha, kubuni, kujenga, na kuuza — bado ikiendeshwa kwa wazo lile lile: kila kazi tunayoifanya lazima iwe halisi.")
add("history_milestone_tag", "Milestone", "Hatua Muhimu")
add("stat_founded", "Founded", "Ilianzishwa")
add("stat_service_lines", "Service Lines", "Aina za Huduma")
add("stat_clients_served", "Clients Served", "Wateja Waliohudumiwa")
add("stat_standard", "Standard for Everything", "Kiwango kwa Kila Kitu")

# --- service detail pages ---
add("svc_about_heading", "About this service", "Kuhusu Huduma Hii")
add("svc_lead2",
    "Every order starts with a quick consult — send us your artwork, quantities, and deadline, and we'll confirm pricing and turnaround before anything goes to print or into production.",
    "Kila agizo huanza na mazungumzo mafupi — tutumie kazi yako ya sanaa, idadi, na tarehe ya mwisho, nasi tutathibitisha bei na muda kabla ya kuanza uchapishaji au uzalishaji.")
add("svc_pricing_heading", "Pricing", "Bei")
add("th_product", "Product", "Bidhaa")
add("th_size", "Size", "Ukubwa")
add("th_qty", "Qty", "Idadi")
add("th_price", "Price", "Bei")
add("price_note_prefix", "Note:", "Kumbuka:")
add("svc_what_we_offer", "What we offer", "Tunachotoa")
add("svc_contact_line1", "Prefer to talk it through? Call or WhatsApp", "Unapendelea kuzungumza? Piga simu au WhatsApp")
add("svc_contact_line2", "or email", "au barua pepe")
add("svc_or_call", "or call/WhatsApp", "au piga simu/WhatsApp")
add("svc_more_services_eyebrow", "More Services", "Huduma Nyingine")
add("svc_more_services_heading", "Explore what else we do.", "Angalia Tunachofanya Kingine.")
add("info_label_service", "Service", "Huduma")
add("info_label_offerings", "Offerings", "Huduma Ndogo")
add("info_label_options", "Options", "Chaguo")
add("info_val_products", "Products", "Bidhaa")

# ======================================================================
# SERVICE / PRICE-LIST DATA — sourced directly from the 2026 price list
# (bilingual: name/best_for/desc/note in en + sw)
# ======================================================================
SERVICES = [
    dict(slug="screen-printing",
         name_en="Screen Printing & Apparel", name_sw="Uchapishaji wa Skrini na Mavazi",
         hero="images/services/screen-printing-hero.jpg",
         best_for_en="Branded workwear & uniforms", best_for_sw="Mavazi ya kazi na sare",
         desc_en="Our original craft. Screen printing and embroidery-ready apparel for teams, staff uniforms, and giveaways — round-collar tees, polos, safari shirts, and caps, printed with your logo or design.",
         desc_sw="Ustadi wetu wa asili. Uchapishaji wa skrini na mavazi tayari kwa emroidare kwa timu, sare za wafanyakazi, na zawadi za matukio — fulana za kola duara, poloshati, safari shirt, na kofia, zilizochapishwa kwa nembo au muundo wako.",
         note_en="Price changes according to quality of the material used.",
         note_sw="Bei hubadilika kulingana na ubora wa kitambaa kinachotumika.",
         table=[
             ("T-Shirt (Round Collar)", "All Sizes", "1pc", "12,000/-"),
             ("Collar T-Shirt (Polo)", "All Sizes", "1pc", "15,000/-"),
             ("Safari Shirt", "All Sizes", "1pc", "35,000/-"),
             ("Cap", "One Size", "1pc", "10,000/-"),
         ]),
    dict(slug="packaging-bags",
         name_en="Packaging & Branded Bags", name_sw="Ufungashaji na Mifuko ya Chapa",
         hero="images/services/packaging-hero.jpg",
         best_for_en="Retail packaging & takeaway", best_for_sw="Ufungashaji wa rejareja na vyakula vya kuchukua",
         desc_en="Branded lunchboxes, pizza boxes, handle bags, paper bags, and die-cut packaging — printed to your dieline so your product feels considered from the moment it's picked up.",
         desc_sw="Masanduku ya chakula, masanduku ya pizza, mifuko yenye mpini, mifuko ya karatasi, na ufungashaji uliokatwa kwa muundo maalum — tunachapisha kulingana na muundo wako ili bidhaa yako ionekane ya thamani tangu inapochukuliwa.",
         note_en="Price changes according to number of colours your artwork has.",
         note_sw="Bei hubadilika kulingana na idadi ya rangi zilizopo kwenye muundo wako.",
         table=[
             ("Lunchbox", "8 inch", "100pc", "100,000/-"),
             ("Lunchbox", "10 inch", "100pc", "120,000/-"),
             ("Pizza Box", "8 inch", "100pc", "105,000/-"),
             ("Pizza Box", "10 inch", "100pc", "120,000/-"),
             ("Pizza Box", "11 inch", "100pc", "130,000/-"),
             ("Pizza Box", "12 inch", "100pc", "140,000/-"),
             ("Pizza Box", "13 inch", "100pc", "150,000/-"),
             ("Handle Bag (Spiral Hand)", "X-Small", "100pc", "90,000/-"),
             ("Handle Bag (Spiral Hand)", "Small", "100pc", "100,000/-"),
             ("Handle Bag (Spiral Hand)", "Medium", "100pc", "110,000/-"),
             ("Handle Bag (Spiral Hand)", "Large", "100pc", "120,000/-"),
             ("Handle Bag (Spiral Hand)", "X-Large", "100pc", "150,000/-"),
             ("Handle Bag (Spiral Hand)", "2XL", "100pc", "190,000/-"),
             ("Paper Bag", "1kg", "500pc", "40,000/-"),
             ("Paper Bag", "2kg", "500pc", "50,000/-"),
             ("D-Cut Package", "A2", "100pc", "70,000/-"),
             ("D-Cut Package", "A3", "100pc", "60,000/-"),
             ("D-Cut Package", "A4", "100pc", "50,000/-"),
             ("D-Cut Package", "A5", "100pc", "40,000/-"),
             ("D-Cut Package", "A6", "100pc", "30,000/-"),
             ("Loop Handle Bag", "A2", "100pc", "85,000/-"),
             ("Loop Handle Bag", "A3", "100pc", "65,000/-"),
             ("Loop Handle Bag", "A4", "100pc", "55,000/-"),
         ]),
    dict(slug="signage-banners",
         name_en="Signage & Banners", name_sw="Alama za Matangazo na Mabango",
         hero="images/services/tents-banners-hero.jpg",
         best_for_en="Events, storefronts & displays", best_for_sw="Matukio, maduka na maonyesho",
         desc_en="Large-format banners, stickers, and canvas prints for storefronts, events, and displays — black or light banner stock, normal or one-way-vision stickers, and gallery-ready canvas.",
         desc_sw="Mabango makubwa, stika, na michoro ya turubai kwa ajili ya maduka, matukio, na maonyesho — mabango meusi au meupe, stika za kawaida au za kuonekana upande mmoja, na turubai tayari kwa banda la sanaa.",
         note_en="Price changes according to number of quantity acquired.",
         note_sw="Bei hubadilika kulingana na idadi ya vipande vinavyoagizwa.",
         table=[
             ("Black Banner", "1m²", "1pc", "25,000/-"),
             ("Light Banner", "1m²", "1pc", "35,000/-"),
             ("Normal Sticker", "1m²", "1pc", "25,000/-"),
             ("Transparent Sticker", "1m²", "1pc", "35,000/-"),
             ("One-Way Vision Sticker", "1m²", "1pc", "40,000/-"),
             ("Canvas Print", "1m²", "1pc", "50,000/-"),
             ("Canvas with Wooden Frame", "1m²", "1pc", "65,000/-"),
         ]),
    dict(slug="tire-covers",
         name_en="Wheel & Tire Covers", name_sw="Vifuniko vya Matairi",
         hero="images/services/wheel-covers-hero.jpg",
         best_for_en="Fleet & personal vehicles", best_for_sw="Magari ya kampuni na binafsi",
         desc_en="Custom-printed spare wheel covers for personal vehicles, fleets, and dealerships — banner-grade or canvas material, built to handle sun and rain without peeling.",
         desc_sw="Vifuniko vya tairi la akiba vilivyochapishwa maalum kwa magari binafsi, makampuni ya usafirishaji, na wauzaji — nyenzo za bango au turubai, zilizotengenezwa kustahimili jua na mvua bila kumenyuka.",
         note_en="Price changes according to number of quantity acquired.",
         note_sw="Bei hubadilika kulingana na idadi ya vipande vinavyoagizwa.",
         table=[
             ("Banner Tire Cover", "0.81m²", "1pc", "35,000/-"),
             ("Canvas Tire Cover", "0.81m²", "1pc", "75,000/-"),
         ]),
    dict(slug="promo-items",
         name_en="Promotional Items", name_sw="Bidhaa za Matangazo",
         hero="images/products/product-mug.jpg",
         best_for_en="Corporate gifts & giveaways", best_for_sw="Zawadi za kikazi na matukio",
         desc_en="Mugs and drinkware branded with your logo or artwork — including colour-change 'magic' mugs — plus aluminium water bottles for events, gifts, and giveaways.",
         desc_sw="Vikombe na vyombo vya kunywea vilivyochapishwa nembo au muundo wako — ikiwa ni pamoja na vikombe vinavyobadilika rangi — pamoja na chupa za maji za alumini kwa ajili ya matukio, zawadi, na matangazo.",
         note_en="Price changes according to quality of the material used.",
         note_sw="Bei hubadilika kulingana na ubora wa nyenzo inayotumika.",
         table=[
             ("Normal Mug", "All", "1pc", "15,000/-"),
             ("Magic Mug (Colour-Change)", "All", "1pc", "20,000/-"),
             ("Aluminium Water Bottle", "750ml", "1pc", "25,000/-"),
         ]),
    dict(slug="print-stationery",
         name_en="Print & Stationery", name_sw="Uchapishaji wa Karatasi na Vifaa vya Ofisi",
         hero="images/services/t-shirt-printing-hero.jpg",
         best_for_en="Business cards, flyers & brochures", best_for_sw="Kadi za biashara, vipeperushi na vijitabu",
         desc_en="Business cards, flyers, brochures, and product labels — everything a growing business needs on paper, printed to international card sizes and standard flyer/brochure formats.",
         desc_sw="Kadi za biashara, vipeperushi, vijitabu, na lebo za bidhaa — kila kitu ambacho biashara inayokua inahitaji kwenye karatasi, kilichochapishwa kwa vipimo vya kimataifa vya kadi na muundo wa kawaida wa vipeperushi/vijitabu.",
         note_en="Price changes according to quality and size of the product label.",
         note_sw="Bei hubadilika kulingana na ubora na ukubwa wa lebo ya bidhaa.",
         table=[
             ("Business Cards", "International Size", "100pc", "40,000/-"),
             ("Flyers", "A6", "100pc", "25,000/-"),
             ("Flyers", "A5", "100pc", "50,000/-"),
             ("Flyers", "A4", "100pc", "100,000/-"),
             ("Brochure", "A4", "100pc", "150,000/-"),
             ("Brochure", "A3", "100pc", "250,000/-"),
             ("Product Label", "Custom Size", "Custom Qty", "Quote on request"),
         ]),
    dict(slug="design-services", quote_only=True,
         name_en="Design Services", name_sw="Huduma za Ubunifu",
         hero="images/services/web-software-hero.jpg",
         best_for_en="Brands starting from scratch", best_for_sw="Chapa zinazoanza upya",
         desc_en="Beyond printing — a design studio that builds the brand behind the print. Whether you need a first logo or a full identity system, our design team works with you from concept to final files.",
         desc_sw="Zaidi ya uchapishaji — studio ya ubunifu inayojenga chapa nyuma ya uchapishaji. Iwe unahitaji nembo ya kwanza au mfumo kamili wa chapa, timu yetu ya ubunifu inafanya kazi nawe kutoka wazo hadi faili za mwisho.",
         note_en="Prices are available upon request and are determined according to the complexity, dimensions, materials, and specifications of each project.",
         note_sw="Bei hutolewa kwa ombi na huamuliwa kulingana na uzito, vipimo, nyenzo, na maelezo ya kila mradi.",
         items_en=["Logo Design", "Brand Identity System", "Brand Strategy Basics", "Social Media Branding", "Packaging Design"],
         items_sw=["Ubunifu wa Nembo", "Mfumo wa Utambulisho wa Chapa", "Msingi wa Mkakati wa Chapa", "Uundaji wa Chapa kwenye Mitandao ya Kijamii", "Ubunifu wa Ufungashaji"]),
    dict(slug="web-software", quote_only=True,
         name_en="Website & Software Development", name_sw="Tovuti na Uundaji wa Programu",
         hero="images/services/web-software-hero.jpg",
         best_for_en="Businesses going digital", best_for_sw="Biashara zinazoingia mtandaoni",
         desc_en="Beyond ink and fabric — we design and build websites, business tools, and custom software for clients who want their digital presence to match the quality of their print materials.",
         desc_sw="Zaidi ya wino na kitambaa — tunabuni na kujenga tovuti, zana za biashara, na programu maalum kwa wateja wanaotaka uwepo wao wa kidijitali ulingane na ubora wa vifaa vyao vya uchapishaji.",
         note_en="Every project is quoted individually based on scope, features, platform, and timeline.",
         note_sw="Kila mradi hutolewa bei kivyake kulingana na wigo, vipengele, jukwaa, na muda.",
         items_en=["Business Websites", "Web Applications", "Custom Business Software", "E-commerce & Booking Systems", "Ongoing Support & Maintenance"],
         items_sw=["Tovuti za Biashara", "Programu za Wavuti", "Programu Maalum za Biashara", "Mifumo ya Biashara Mtandaoni na Uhifadhi", "Msaada Endelevu na Matengenezo"]),
]

for s in SERVICES:
    add(f"svc-{s['slug']}-name", s["name_en"], s["name_sw"])
    add(f"svc-{s['slug']}-bestfor", s["best_for_en"], s["best_for_sw"])
    add(f"svc-{s['slug']}-desc", s["desc_en"], s["desc_sw"])
    add(f"svc-{s['slug']}-note", s["note_en"], s["note_sw"])
    add(f"svc-{s['slug']}-testi-h", f"Clients Who've Used {s['name_en']}", f"Wateja Waliotumia {s['name_sw']}")
    add(f"svc-{s['slug']}-testi-s", f"A few words from people we've done {s['name_en'].lower()} work for.",
        f"Maneno machache kutoka kwa watu tuliowafanyia kazi ya {s['name_sw']}.")
    if s.get("quote_only"):
        for idx, (ien, isw) in enumerate(zip(s["items_en"], s["items_sw"])):
            add(f"svc-{s['slug']}-item-{idx}", ien, isw)

TESTIMONIALS = [
    dict(img="images/testimonials/testimonial-1.jpg", name="Grace M.", role_en="Retail Boutique Owner", role_sw="Mmiliki wa Duka la Rejareja",
         quote_en="Ordered 300 branded handle bags and they matched our logo colours exactly. Fast, clean, no back-and-forth.",
         quote_sw="Niliagiza mifuko 300 yenye chapa na ilifanana kabisa na rangi za nembo yetu. Haraka, safi, bila mrudirudio."),
    dict(img="images/testimonials/testimonial-2.jpg", name="Kelvin O.", role_en="Events Company", role_sw="Kampuni ya Matukio",
         quote_en="Their banners and signage have covered three of our expos now. Colours still look sharp after a full rainy season.",
         quote_sw="Mabango na alama zao zimetumika kwenye maonyesho matatu yetu sasa. Rangi bado zinaonekana wazi hata baada ya msimu mzima wa mvua."),
    dict(img="images/testimonials/testimonial-3.jpg", name="Fatuma R.", role_en="Small Business Owner", role_sw="Mmiliki wa Biashara Ndogo",
         quote_en="I only needed 12 t-shirts for a team retreat and they still gave it the same attention as a bulk order.",
         quote_sw="Nilihitaji fulana 12 tu kwa mkutano wa timu na bado walinipa umakini ule ule kama agizo kubwa."),
    dict(img="images/testimonials/testimonial-4.jpg", name="James P.", role_en="Fleet Manager", role_sw="Msimamizi wa Magari",
         quote_en="Custom wheel covers for our whole delivery fleet — durable, consistent, and delivered ahead of schedule.",
         quote_sw="Vifuniko maalum vya matairi kwa magari yetu yote ya usafirishaji — vya kudumu, sawia, na vilivyowasilishwa kabla ya muda."),
    dict(img="images/testimonials/testimonial-5.jpg", name="Neema T.", role_en="Art Collector", role_sw="Mkusanyaji wa Sanaa",
         quote_en="Bought a canvas print with the wooden frame option straight from their gallery page. Beautifully finished.",
         quote_sw="Nilinunua mchoro wa turubai wenye fremu ya mbao moja kwa moja kwenye ukurasa wao wa sanaa. Umekamilika kwa uzuri."),
    dict(img="images/testimonials/testimonial-6.jpg", name="Brian K.", role_en="Startup Founder", role_sw="Mwanzilishi wa Kampuni Mpya",
         quote_en="They built our brand identity and website after printing our launch merch. Having one team handle both was genuinely easier.",
         quote_sw="Walijenga utambulisho wa chapa yetu na tovuti baada ya kuchapisha bidhaa za uzinduzi wetu. Kuwa na timu moja ikishughulikia yote mawili kulikuwa rahisi zaidi."),
]
for i, tm in enumerate(TESTIMONIALS):
    add(f"testi-{i}-role", tm["role_en"], tm["role_sw"])
    add(f"testi-{i}-quote", tm["quote_en"], tm["quote_sw"])

TIMELINE = [
    ("2019", "A single screen printing table", "Meza Moja ya Uchapishaji wa Skrini",
     "Authentic Art & Gallery starts as one screen printing table in Arusha, taking on small t-shirt orders for local teams and events.",
     "Authentic Art & Gallery inaanza kama meza moja ya uchapishaji wa skrini jijini Arusha, ikichukua maagizo madogo ya fulana kwa timu na matukio ya karibu.", False),
    ("2020", "Apparel & caps scale up", "Mavazi na Kofia Zinaongezeka",
     "Demand for custom t-shirts, polos, safari shirts, and caps grows fast enough to justify a dedicated apparel printing line.",
     "Mahitaji ya fulana maalum, poloshati, safari shirt, na kofia yanaongezeka kwa kasi ya kutosha kuhalalisha mstari maalum wa uchapishaji wa mavazi.", True),
    ("2021", "Packaging & signage added", "Ufungashaji na Alama za Matangazo Zaongezwa",
     "Clients start asking for more than apparel — branded packaging, bags, banners, and stickers are added as full-time service lines.",
     "Wateja wanaanza kuomba zaidi ya mavazi — ufungashaji wenye chapa, mifuko, mabango, na stika zinaongezwa kama huduma za kudumu.", True),
    ("2022", "Tire covers & promo items", "Vifuniko vya Matairi na Bidhaa za Matangazo",
     "The studio adds custom wheel and tire covers, plus mugs and drinkware, becoming a one-stop shop for branded merchandise.",
     "Studio inaongeza vifuniko maalum vya matairi, pamoja na vikombe na vyombo vya kunywea, na kuwa duka la pamoja kwa bidhaa za chapa.", False),
    ("2024", "Design & software services launch", "Huduma za Ubunifu na Programu Zazinduliwa",
     "A small internal tool for managing print orders turns into a full design and software development arm — logos, brand identities, and websites built in-house.",
     "Chombo kidogo cha ndani cha kusimamia maagizo ya uchapishaji kinageuka kuwa tawi kamili la ubunifu na uundaji wa programu — nembo, utambulisho wa chapa, na tovuti zinajengwa ndani ya kampuni.", True),
    ("2025", "The gallery opens", "Banda la Sanaa Lafunguliwa",
     "Authentic Art & Gallery opens its art sales arm — original paintings and canvas prints, sold with the same craftsmanship as every printed order.",
     "Authentic Art & Gallery inafungua tawi lake la mauzo ya sanaa — michoro asili na turubai, zinazouzwa kwa ustadi ule ule kama kila agizo la uchapishaji.", True),
]
for i, (year, ten, tsw, den, dsw, milestone) in enumerate(TIMELINE):
    add(f"tl-{i}-title", ten, tsw)
    add(f"tl-{i}-desc", den, dsw)

PROJECTS = [
    dict(title="Retail Launch Tees", client="Fatuma Boutique", date="July 2026", service_slug="screen-printing", qty="120 pcs"),
    dict(title="Fleet Wheel Branding", client="Kelvin Logistics", date="June 2026", service_slug="tire-covers", qty="34 vehicles"),
    dict(title="Expo Banner Set", client="Neema Events Co.", date="May 2026", service_slug="signage-banners", qty="6 banners"),
    dict(title="Takeaway Box Redesign", client="Brian's Kitchen", date="April 2026", service_slug="packaging-bags", qty="2,000 units"),
    dict(title="Corporate Gift Mugs", client="Grace Studio", date="March 2026", service_slug="promo-items", qty="300 pcs"),
    dict(title="Brand Identity & Logo", client="James Fleet Rentals", date="Feb 2026", service_slug="design-services", qty="1 brand system"),
]

SVC_BY_SLUG = {s["slug"]: s for s in SERVICES}

def price_min(table):
    vals = []
    for row in table:
        p = row[3].replace("/-", "").replace(",", "").strip()
        if p.isdigit():
            vals.append(int(p))
    return min(vals) if vals else None

def logo_svg():
    return ('<svg viewBox="0 0 40 40" fill="none">'
            '<path d="M20 4 L36 34 H4 Z" fill="currentColor"/>'
            '<path d="M20 19 L27.5 34 H12.5 Z" fill="var(--bg)"/>'
            '</svg>')

def brand_lockup():
    return ('<span class="brand-lockup">'
            '<span class="brand-word">authent<span class="dot-i">i</span>c</span>'
            '<span class="brand-sub">art &amp; gallery</span>'
            '</span>')

def switches():
    return f"""<div class="switches">
      <div class="lang-switch">
        <button class="lang-btn active" data-lang="en">EN</button>
        <button class="lang-btn" data-lang="sw">SW</button>
      </div>
      <div class="theme-switch">
        <button class="theme-btn active" data-theme="dark">Dark</button>
        <button class="theme-btn" data-theme="light">Light</button>
      </div>
    </div>"""

def nav(prefix="", active=""):
    def a(href, key, navkey):
        cls = ' class="active"' if navkey == active else ""
        return f'<a href="{prefix}{href}"{cls}>{t(key)}</a>'
    return f"""<header class="nav" id="nav">
  <a class="brand" href="{prefix}index.html">
    {logo_svg()}
    {brand_lockup()}
  </a>
  <nav class="nav-links">
    {a('services.html','nav_services','services')}
    {a('portfolio.html','nav_portfolio','portfolio')}
    {a('shop.html','nav_shop','shop')}
    {a('about.html','nav_about','about')}
    {a('history.html','nav_history','history')}
  </nav>
  {switches()}
  <div class="nav-social">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg>
    <a href="{INSTAGRAM_URL}" target="_blank" rel="noopener"><span class="ig-text">{INSTAGRAM_HANDLE}</span></a>
  </div>
  <button class="nav-burger" id="burgerBtn" aria-label="Open menu"><span></span></button>
</header>

<div class="mobile-drawer" id="mobileDrawer">
  <div class="close-row"><button id="closeDrawer">&times;</button></div>
  <nav>
    {a('services.html','nav_services','')}
    {a('portfolio.html','nav_portfolio','')}
    {a('shop.html','nav_shop','')}
    {a('about.html','nav_about','')}
    {a('history.html','nav_history','')}
  </nav>
  {switches()}
</div>
"""

def footer(prefix=""):
    return f"""<footer>
  <div class="wrap">
    <div class="footer-top reveal">
      <div>
        <h4>{t('footer_heading')}</h4>
        <p>{t('footer_sub')}</p>
      </div>
      <p>{t('footer_services_line')}</p>
      <form class="signup-row" onsubmit="return handleSignup(event)">
        <input type="email" {tph('newsletter_email_ph')} required>
        <button type="submit">{t('btn_signup')}</button>
      </form>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026, Authentic Art &amp; Gallery</span>
      <div class="footer-links">
        <a href="{INSTAGRAM_URL}" target="_blank" rel="noopener">Instagram</a>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="tel:{PHONE.replace(' ', '')}">{PHONE}</a>
        <span>{t('footer_address')}</span>
      </div>
      <span>{t('footer_credits')}</span>
    </div>
  </div>
</footer>
"""

def testimonials_section(prefix="", heading_key="testi_heading_default", sub_key="testi_sub_default"):
    cards = ""
    for i, tm in enumerate(TESTIMONIALS):
        cards += f"""      <div class="testi-card">
        <div class="testi-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="testi-quote">{t(f'testi-{i}-quote')}</p>
        <div class="testi-person">
          <img src="{prefix}{tm['img']}" alt="{tm['name']}">
          <div class="who"><b>{tm['name']}</b><span>{t(f'testi-{i}-role')}</span></div>
        </div>
      </div>
"""
    return f"""<section class="testimonials">
  <div class="wrap">
    <div class="testi-head reveal">
      <h2>{t(heading_key)}</h2>
      <p>{t(sub_key)}</p>
    </div>
    <div class="testi-grid reveal-stagger">
{cards}    </div>
  </div>
</section>
"""

def head(title, desc, css_list, prefix=""):
    links = "\n".join([f'<link rel="stylesheet" href="{prefix}css/{c}">' for c in css_list])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{links}
<script>try{{if(localStorage.getItem('aag-theme')==='light'){{document.documentElement.classList.add('light-mode');}}}}catch(e){{}}</script>
</head>
<body>
"""

def scripts(prefix=""):
    return (f'<script src="{prefix}js/i18n-data.js"></script>\n'
            f'<script src="{prefix}js/main.js"></script>\n'
            f'<script src="{prefix}js/i18n.js"></script>\n'
            '</body>\n</html>\n')

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", full)

# ======================================================================
# INDEX (home)
# ======================================================================
featured = [SVC_BY_SLUG["screen-printing"], SVC_BY_SLUG["packaging-bags"], SVC_BY_SLUG["design-services"]]
teaser_cards = ""
for s in featured:
    price_tag_html = t('label_on_request') if s.get("quote_only") else f"{price_min(s['table']):,}/-"
    teaser_cards += f"""      <a class="teaser-card" href="services/{s['slug']}.html">
        <img class="bg-photo bg-cover" src="{s['hero']}" alt="{s['name_en']}">
        <div class="content">
          <div class="tag">{price_tag_html}</div>
          <h3>{t(f"svc-{s['slug']}-name")}</h3>
          <span class="arrow-link">{t('btn_view_service_details')} <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
        </div>
      </a>
"""

index_html = head("Authentic Art &amp; Gallery — Screen Printing, Apparel, Packaging &amp; More",
                   "Authentic Art and Gallery — screen printing experts. T-shirts, packaging, signage, tire covers, print, design, websites, software, and original art.",
                   ["base.css", "home.css", "testimonials.css"]) + nav(active="home") + f"""
<section class="hero">
  <img class="bg-photo bg-cover" src="images/hero-bg.jpg" alt="">
  <div class="hero-ghost-word">{t('home_ghost_word')}</div>
  <div class="wrap hero-main">
    <h1 class="hero-title reveal">Authentic <span class="script">Art</span></h1>
    <div class="hero-cta-row reveal">
      <a class="btn accent-btn" href="services.html">{t('btn_get_quote')}</a>
    </div>
  </div>
  <div class="wrap hero-strip reveal">
    <div><div class="label-sm">{t('footer_heading')}</div></div>
    <p>{t('footer_sub')}</p>
    <form class="signup-row" onsubmit="return handleSignup(event)">
      <input type="email" {tph('newsletter_email_ph')} required>
      <button type="submit">{t('btn_signup')}</button>
    </form>
  </div>
</section>

<section class="runband">
  <img class="bg-photo bg-cover" src="images/mission-bg.jpg" alt="">
  <div class="wrap runband-inner">
    <div class="stack reveal">
      <p class="ghost">{t('home_ghost_line1')}</p>
      <p class="ghost">{t('home_ghost_line2')}</p>
      <h2 class="solid">Authentic Art <span class="script">&amp; Gallery</span></h2>
    </div>
    <div class="quote-sig reveal">
      <span class="mark">Authentic Art</span>
      <span class="who"><b>The Studio Team</b>{t('home_quote_role')}</span>
    </div>
  </div>
  <div class="next-run-pill reveal">
    <div><div class="tag">{t('home_pill_tag')}</div><div class="date">{t("svc-screen-printing-name")}</div></div>
    <a class="btn small" href="services/screen-printing.html">{t('btn_get_quote')}</a>
  </div>
</section>

<section class="uniting" id="services">
  <div class="wrap">
    <div class="eyebrow reveal">{t('home_featured_eyebrow')}</div>
    <h2 class="reveal" style="font-family:var(--f-display);font-weight:700;font-size:clamp(2.2rem,5vw,3.6rem);letter-spacing:-0.03em;">{t('home_featured_heading')}</h2>
    <div class="teaser-grid reveal-stagger">
{teaser_cards}    </div>
    <div class="teaser-cta-row reveal">
      <a class="btn ghost-btn" href="services.html">{t('btn_see_all_services')}</a>
    </div>
  </div>
</section>

{testimonials_section()}
{footer()}
""" + scripts()
write("index.html", index_html)

# ======================================================================
# SERVICES (full grid — all 8 categories)
# ======================================================================
service_cards = ""
for s in SERVICES:
    if s.get("quote_only"):
        tag_label, tag_value = t('label_pricing'), t('label_on_request')
        meta_b_k, meta_b_v = t('label_includes'), f"{len(s['items_en'])}"
    else:
        tag_label, tag_value = t('label_starting_at'), f"{price_min(s['table']):,}/-"
        meta_b_k, meta_b_v = t('label_products'), f"{len(s['table'])}"
    service_cards += f"""      <div class="city-card">
        <img class="bg-photo bg-cover" src="{s['hero']}" alt="{s['name_en']}">
        <svg class="route-svg" viewBox="0 0 300 300"><path d="M40,110 L90,70 L150,90 L210,60 L260,100 L230,150 L150,140 L90,160 Z"/></svg>
        <div class="tag">{tag_label}</div>
        <div class="date">{tag_value}</div>
        <h3>{t(f"svc-{s['slug']}-name")}</h3>
        <div class="join">{t('btn_get_quote')}</div>
        <div class="city-meta">
          <div><div class="k">{t('label_best_for')}</div><div class="v">{t(f"svc-{s['slug']}-bestfor")}</div></div>
          <div><div class="k">{meta_b_k}</div><div class="v">{meta_b_v}</div></div>
        </div>
        <a class="details-btn" href="services/{s['slug']}.html">{t('btn_view_service_details')}</a>
        <div class="brandmark">Authentic <span class="script">Art</span></div>
      </div>
"""

services_html = head("Services &amp; Pricing — Authentic Art &amp; Gallery",
                      "Screen printing, apparel, packaging, signage, tire covers, promotional items, print, design, and website & software development — every service, with real pricing.",
                      ["base.css", "services.css", "testimonials.css"]) + nav(active="services") + f"""
<section class="runs-hero">
  <div class="wrap">
    <div class="uniting">
      <div class="stack reveal">
        <h2 class="solid">{t('services_h1a')}</h2>
        <p class="ghost" style="margin-top:2px;">{t('services_h1b')}</p>
      </div>
      <div class="uniting-you script reveal">{t('services_script_tag')}</div>
      <p class="desc reveal">{t('services_desc')}</p>
      <div class="stat-bar reveal">
        <div class="item"><span class="dot-grid"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span>{t('stat_country')}</div>
        <div class="line-mid"></div>
        <div class="item">{t('stat_beyond')}</div>
        <div class="line-mid"></div>
        <div class="item">{t('stat_built_to_order')}</div>
        <div class="line-mid"></div>
        <div class="item">{t('stat_authentic')}</div>
      </div>
      <div class="cities-grid reveal-stagger">
{service_cards}      </div>
    </div>
  </div>
</section>

{testimonials_section(heading_key="services_testi_heading", sub_key="services_testi_sub")}
{footer()}
""" + scripts()
write("services.html", services_html)

# ======================================================================
# PORTFOLIO (recent projects marquee + full list)
# ======================================================================
port_items = ""
for p in PROJECTS:
    port_items += f"""      <div class="cal-item">
        <div class="city-row"><h4>{p['title']}</h4><span class="d">{p['date']}</span></div>
        <div class="meta-row">
          <div><div class="k">{t('label_client')}</div><div class="v">{p['client']}</div></div>
          <div><div class="k">{t('label_service')}</div><div class="v">{t(f"svc-{p['service_slug']}-name")}</div></div>
        </div>
        <a class="view" href="services/{p['service_slug']}.html">{t('btn_view_service')}</a>
      </div>
"""
port_marquee = port_items + port_items

schedule_rows = ""
for p in PROJECTS:
    schedule_rows += f"""    <div class="schedule-row">
      <div class="sr-date">{p['date']}</div>
      <div class="sr-city">{p['title']}</div>
      <div class="sr-addr">{p['client']} &middot; {p['qty']}</div>
      <div class="sr-dist">{t(f"svc-{p['service_slug']}-name")}</div>
      <a class="btn small sr-btn" href="services/{p['service_slug']}.html">{t('btn_view_service')}</a>
    </div>
"""

portfolio_html = head("Portfolio — Authentic Art &amp; Gallery",
                       "Recent print, packaging, signage, tire cover, design, and software projects from Authentic Art &amp; Gallery.",
                       ["base.css", "portfolio.css"]) + nav(active="portfolio") + f"""
<section class="calendar-hero">
  <img class="bg-photo bg-cover" src="images/portfolio-bg.jpg" alt="">
  <div class="wrap">
    <h1 class="reveal">{t('portfolio_h1')}</h1>
    <p class="reveal">{t('portfolio_sub')}</p>
  </div>
  <div class="marquee-track">
    <div class="marquee-inner">
{port_marquee}    </div>
  </div>
</section>

<section class="schedule">
  <div class="wrap">
    <div class="eyebrow reveal">{t('portfolio_eyebrow')}</div>
    <h2 class="reveal" style="font-family:var(--f-display);font-weight:700;font-size:clamp(2rem,4.5vw,3.2rem);letter-spacing:-0.03em;">{t('portfolio_heading')}</h2>
    <div class="schedule-list reveal-stagger">
{schedule_rows}    </div>
  </div>
</section>

{footer()}
""" + scripts()
write("portfolio.html", portfolio_html)

# ======================================================================
# SHOP (art gallery + merch — real prices from the price list)
# ======================================================================
shop_html = head("Shop — Authentic Art &amp; Gallery",
                  "Original art, canvas prints, and studio merch from Authentic Art &amp; Gallery.",
                  ["base.css", "shop.css"]) + nav(active="shop") + f"""
<section class="shop-hero">
  <div class="wrap">
    <div class="eyebrow reveal">{t('shop_eyebrow')}</div>
    <h1 class="reveal">{t('shop_h1')}</h1>
    <p class="reveal">{t('shop_sub')}</p>
  </div>
</section>

<section style="padding-top:0;">
  <div class="wrap">
    <div class="shop-feature reveal">
      <div class="card feat-product">
        <div class="name">Canvas Print (1m&sup2;)</div>
        <div class="price">TZS 50,000</div>
        <div class="stage">
          <img src="images/products/product-canvas.jpg" alt="Canvas Print">
          <span class="badge">{t('shop_badge_bestseller')}</span>
        </div>
      </div>
      <div class="cat-card">
        <img src="images/products/product-category.jpg" alt="Gallery prints category">
        <div class="content">
          <div class="eyebrow-sm">{t('shop_popular_categories')}</div>
          <h3>Gallery Prints</h3>
          <a class="btn" href="#products">{t('btn_shop_prints')}</a>
        </div>
        <div class="cat-nav">
          <button aria-label="prev">&larr;</button>
          <button aria-label="next">&rarr;</button>
        </div>
      </div>
    </div>

    <div class="products-row reveal-stagger" id="products">
      <div class="product-card">
        <div class="name">Canvas with Wooden Frame (1m&sup2;)</div>
        <div class="price">TZS 65,000</div>
        <div class="stage"><img src="images/products/product-print.jpg" alt="Canvas with Wooden Frame"></div>
      </div>
      <div class="product-card">
        <div class="name">Custom T-Shirt</div>
        <div class="price">TZS 12,000</div>
        <div class="stage"><img src="images/products/product-tshirt.jpg" alt="Custom T-Shirt"></div>
      </div>
      <div class="product-card">
        <div class="name">Branded Mug</div>
        <div class="price">TZS 15,000</div>
        <div class="stage"><img src="images/products/product-mug.jpg" alt="Branded Mug"></div>
      </div>
      <div class="product-card">
        <div class="name">Magic Mug (Colour-Change)</div>
        <div class="price">TZS 20,000</div>
        <div class="stage"><img src="images/products/product-tote.jpg" alt="Magic Mug"></div>
      </div>
    </div>
  </div>
</section>

<section class="gear-quote">
  <div class="wrap">
    <div class="gear-photos reveal">
      <img src="images/gear-1.jpg" alt="Ink and squeegee detail">
      <img src="images/gear-2.jpg" alt="Framed canvas print">
    </div>
    <p class="q reveal">{t('shop_gear_quote')}</p>
    <div class="gear-sig reveal">
      <span class="script">Authentic Art</span>
      <span class="tag">&amp; Gallery</span>
    </div>
  </div>
</section>

{footer()}
""" + scripts()
write("shop.html", shop_html)

# ======================================================================
# ABOUT
# ======================================================================
about_html = head("About — Authentic Art &amp; Gallery",
                   "Every print tells a story — the mission behind Authentic Art &amp; Gallery.",
                   ["base.css", "about.css"]) + nav(active="about") + f"""
<section class="about-hero">
  <div class="wrap about-grid">
    <div class="label-col reveal">{t('about_eyebrow')}</div>
    <div class="statement reveal">{t('about_mission')}</div>
  </div>
  <div class="wrap">
    <div class="about-photos reveal">
      <div class="photo-block a"><img src="images/mission-1.jpg" alt="Screen printing in progress"></div>
      <div class="photo-block b">
        <img src="images/mission-2.jpg" alt="Finished apparel rack">
        <div class="find-run-cta">
          <span>{t('about_cta_line')}</span>
          <a class="btn small" href="services.html">{t('btn_get_quote')}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="eyebrow reveal">{t('about_eyebrow')}</div>
    <h2 class="reveal" style="font-family:var(--f-display);font-weight:700;font-size:clamp(2.2rem,5vw,3.6rem);letter-spacing:-0.03em;">{t('about_heading')}</h2>
    <div class="values-grid reveal-stagger">
      <div class="value-card">
        <div class="num">01</div>
        <h3>{t('value1_title')}</h3>
        <p>{t('value1_desc')}</p>
      </div>
      <div class="value-card">
        <div class="num">02</div>
        <h3>{t('value2_title')}</h3>
        <p>{t('value2_desc')}</p>
      </div>
      <div class="value-card">
        <div class="num">03</div>
        <h3>{t('value3_title')}</h3>
        <p>{t('value3_desc')}</p>
      </div>
    </div>
  </div>
</section>

{footer()}
""" + scripts()
write("about.html", about_html)

# ======================================================================
# HISTORY
# ======================================================================
tl_html = ""
for i, (year, ten, tsw, den, dsw, milestone) in enumerate(TIMELINE):
    cls = " is-milestone" if milestone else ""
    tag = f'<span class="tl-tag">{t("history_milestone_tag")}</span>' if milestone else ""
    tl_html += f"""    <div class="tl-item{cls}">
      <div class="tl-year">{year}<span class="tl-dot"></span></div>
      <div class="tl-content">
        <h3>{t(f'tl-{i}-title')}</h3>
        <p>{t(f'tl-{i}-desc')}</p>
        {tag}
      </div>
    </div>
"""

history_html = head("History — Authentic Art &amp; Gallery",
                     "From one screen printing table to a full print, design, software, and gallery studio — the Authentic Art &amp; Gallery story.",
                     ["base.css", "history.css"]) + nav(active="history") + f"""
<section class="history-hero">
  <img class="bg-photo bg-cover" src="images/history-bg.jpg" alt="">
  <div class="wrap">
    <div class="eyebrow reveal">{t('history_eyebrow')}</div>
    <h1 class="reveal">{t('history_h1')}</h1>
    <p class="reveal">{t('history_sub')}</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="timeline reveal-stagger">
{tl_html}    </div>

    <div class="history-stats reveal-stagger">
      <div class="hstat"><div class="n">2019</div><div class="l">{t('stat_founded')}</div></div>
      <div class="hstat"><div class="n">8</div><div class="l">{t('stat_service_lines')}</div></div>
      <div class="hstat"><div class="n">500+</div><div class="l">{t('stat_clients_served')}</div></div>
      <div class="hstat"><div class="n">1</div><div class="l">{t('stat_standard')}</div></div>
    </div>
  </div>
</section>

{footer()}
""" + scripts()
write("history.html", history_html)

# ======================================================================
# SERVICE DETAIL PAGES
# ======================================================================
for s in SERVICES:
    others = [x for x in SERVICES if x["slug"] != s["slug"]][:4]
    other_html = ""
    for o in others:
        other_tag = t('label_on_request') if o.get("quote_only") else f"{price_min(o['table']):,}/-"
        other_html += f"""      <div class="oc">
        <div class="d">{other_tag}</div>
        <h4>{t(f"svc-{o['slug']}-name")}</h4>
        <a href="{o['slug']}.html">{t('btn_view_service_details')} &rarr;</a>
      </div>
"""

    if s.get("quote_only"):
        items_html = "\n".join([f'        <li>{t(f"svc-{s["slug"]}-item-{idx}")}</li>' for idx in range(len(s['items_en']))])
        pricing_block = f"""      <h2 style="margin-top:44px;">{t('svc_what_we_offer')}</h2>
      <ul class="quote-list">
{items_html}
      </ul>
      <div class="quote-banner">
        <p>{t(f"svc-{s['slug']}-note")}</p>
        <a class="btn accent-btn" href="mailto:{EMAIL}?subject=Quote request: {s['name_en']}">{t('btn_request_quote')}</a>
      </div>
      <p class="contact-line">{t('svc_contact_line1')} <a href="tel:{PHONE.replace(' ', '')}">{PHONE}</a> {t('svc_contact_line2')} <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
"""
        sidebar_rows = f"""      <div class="info-row"><span class="k">{t('info_label_service')}</span><span class="v">{t(f"svc-{s['slug']}-name")}</span></div>
      <div class="info-row"><span class="k">{t('label_pricing')}</span><span class="v">{t('label_on_request')}</span></div>
      <div class="info-row"><span class="k">{t('label_best_for')}</span><span class="v">{t(f"svc-{s['slug']}-bestfor")}</span></div>
      <div class="info-row"><span class="k">{t('info_label_offerings')}</span><span class="v">{len(s['items_en'])}</span></div>
"""
    else:
        rows_html = "\n".join([
            f'          <tr><td class="pt-product">{p}</td><td>{sz}</td><td>{qty}</td><td>{price}</td></tr>'
            for (p, sz, qty, price) in s['table']
        ])
        pricing_block = f"""      <h2 style="margin-top:44px;">{t('svc_pricing_heading')}</h2>
      <div class="price-table-wrap">
        <table class="price-table">
          <thead><tr><th>{t('th_product')}</th><th>{t('th_size')}</th><th>{t('th_qty')}</th><th>{t('th_price')}</th></tr></thead>
          <tbody>
{rows_html}
          </tbody>
        </table>
        <p class="price-note">{t('price_note_prefix')} {t(f"svc-{s['slug']}-note")}</p>
      </div>
"""
        sidebar_rows = f"""      <div class="info-row"><span class="k">{t('info_label_service')}</span><span class="v">{t(f"svc-{s['slug']}-name")}</span></div>
      <div class="info-row"><span class="k">{t('label_starting_at')}</span><span class="v">{price_min(s['table']):,}/-</span></div>
      <div class="info-row"><span class="k">{t('label_best_for')}</span><span class="v">{t(f"svc-{s['slug']}-bestfor")}</span></div>
      <div class="info-row"><span class="k">{t('info_label_options')}</span><span class="v">{len(s['table'])} {t('info_val_products')}</span></div>
"""

    detail = head(f"{s['name_en']} — Authentic Art &amp; Gallery",
                   f"{s['name_en']} — {s['best_for_en']}. See pricing and details.",
                   ["base.css", "service-detail.css"], prefix="../") + nav(prefix="../", active="services") + f"""
<section class="run-hero">
  <img class="bg-photo bg-cover" src="../{s['hero']}" alt="{s['name_en']}">
  <div class="wrap">
    <div class="breadcrumb reveal"><a href="../services.html">{t('nav_services')}</a> &rsaquo; <span>{t(f"svc-{s['slug']}-name")}</span></div>
    <h1 class="reveal">{t(f"svc-{s['slug']}-name")}</h1>
    <div class="badges reveal">
      <div class="run-badge"><span class="k">{t('label_best_for')}</span> {t(f"svc-{s['slug']}-bestfor")}</div>
      <div class="run-badge"><span class="k">{t('label_pricing')}</span> {t('label_on_request') if s.get('quote_only') else f"{price_min(s['table']):,}/-"}</div>
    </div>
  </div>
</section>

<section>
  <div class="wrap run-body">
    <div class="reveal">
      <h2>{t('svc_about_heading')}</h2>
      <p class="lead">{t(f"svc-{s['slug']}-desc")}</p>
      <p class="lead">{t('svc_lead2')}</p>

{pricing_block}
    </div>

    <div class="info-card reveal">
{sidebar_rows}      <a class="btn accent-btn" href="mailto:{EMAIL}?subject=Quote request: {s['name_en']}">{t('btn_get_quote')}</a>
      <p class="contact-line" style="text-align:center;margin-top:14px;">{t('svc_or_call')} <a href="tel:{PHONE.replace(' ', '')}">{PHONE}</a></p>
    </div>
  </div>
</section>

<section class="other-runs">
  <div class="wrap">
    <div class="eyebrow reveal">{t('svc_more_services_eyebrow')}</div>
    <h2 class="reveal" style="font-family:var(--f-display);font-weight:700;font-size:clamp(1.8rem,4vw,2.6rem);letter-spacing:-0.03em;">{t('svc_more_services_heading')}</h2>
    <div class="row reveal-stagger">
{other_html}    </div>
  </div>
</section>

""" + testimonials_section(prefix="../", heading_key=f"svc-{s['slug']}-testi-h", sub_key=f"svc-{s['slug']}-testi-s") + footer(prefix="../") + scripts(prefix="../")
    write(f"services/{s['slug']}.html", detail)

# ======================================================================
# Write the shared translation data file consumed by js/i18n.js
# ======================================================================
i18n_js = "// Auto-generated from build/gen_site4.py — single source of truth for EN/SW strings.\nconst I18N = " + json.dumps(TR, ensure_ascii=False, indent=2) + ";\n"
write("js/i18n-data.js", i18n_js)

print("ALL PAGES WRITTEN")
