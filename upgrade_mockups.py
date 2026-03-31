import json, re, os

# Map each business to its logo URL, mockup slug, and which shared image to use
businesses = [
    {"slug": "st-johns-perth", "logo": "https://stjohnsperth.co.uk/wp-content/uploads/2024/01/Text-Logo.png", "hero_img": "images/shared/bar-restaurant.png", "card_img": "images/shared/bistro.png"},
    {"slug": "taste-perthshire", "logo": "https://www.tasteperthshire.co.uk/images/taste-perthshire-logo.png", "hero_img": "images/shared/farm-shop.png", "card_img": "images/shared/bistro.png"},
    {"slug": "angela-lamont", "logo": "https://angelalamonthairandbeauty.co.uk/wp-content/uploads/2021/03/AL-White-Logo.png", "hero_img": "images/shared/salon.png", "card_img": "images/shared/beauty.png"},
    {"slug": "cutting-room-perth", "logo": "https://thecuttingroomperth.co.uk/wp-content/uploads/2022/04/The-Cutting-Room-Logo.png", "hero_img": "images/shared/salon.png", "card_img": "images/shared/beauty.png"},
    {"slug": "copperfields-perth", "logo": "https://www.copperfieldshairandbeauty.co.uk/img/Untitled-1.png", "hero_img": "images/shared/salon.png", "card_img": "images/shared/beauty.png"},
    {"slug": "rae-peacock", "logo": "https://img1.wsimg.com/isteam/ip/7a8394c6-8104-4a53-bb09-d5e75d73d1a2/favicon/74c8b8e7-3f2a-4a52-b8c6-5eac41c0f2d2.png", "hero_img": "images/shared/salon.png", "card_img": "images/shared/beauty.png"},
    {"slug": "harmony-perth", "logo": "https://www.harmonyhealthandbeauty.co.uk/images/logo.png", "hero_img": "images/shared/beauty.png", "card_img": "images/shared/salon.png"},
    {"slug": "park-bistro", "logo": "https://img1.wsimg.com/isteam/ip/019a9d30-806b-4ab2-8c2d-8d2f3be68221/favicon/63c9ad27-4c32-4e9b-b5c1-9e0afd8b1c2d.png", "hero_img": "images/shared/bistro.png", "card_img": "images/shared/bar-restaurant.png"},
    # champany-inn already done
    {"slug": "nineteen62", "logo": "https://images.squarespace-cdn.com/content/v1/5cdbcdaa2727be3dc98bf7e5/5afc5aff-e2c3-4a8e-b5c0-9f9b7e5e5d5d/1962+logo.png", "hero_img": "images/shared/bar-restaurant.png", "card_img": "images/shared/bistro.png"},
    {"slug": "livingston-inn", "logo": "https://thelivingstoninn.co.uk/wp-content/uploads/2019/08/Livingston-Inn-Logo.jpg", "hero_img": "images/shared/pub.png", "card_img": "images/shared/bistro.png"},
    {"slug": "hopetoun-bistro", "logo": "https://images.squarespace-cdn.com/content/v1/5f899eb5403f48228845e7c3/8dc294a1-c3a4-4e8a-b5c0-9f9b7e5e5d5d/hopetoun-logo.png", "hero_img": "images/shared/bar-restaurant.png", "card_img": "images/shared/bistro.png"},
    {"slug": "hilcroft-hotel", "logo": "https://www.hilcrofthotel.com/assets/images/logos/bw-core-h-small.png", "hero_img": "images/shared/hotel.png", "card_img": "images/shared/bistro.png"},
    {"slug": "emmie-hair", "logo": "https://cdn.prod.website-files.com/63dd402490421884e0b41d72/63dd40249042186e73b41d91_emmie-logo.png", "hero_img": "images/shared/salon.png", "card_img": "images/shared/beauty.png"},
    {"slug": "charlie-taylor", "logo": "https://www.charlie-taylor.co.uk/wp-content/uploads/2020/06/Charlie-Taylor-Logo.png", "hero_img": "images/shared/salon.png", "card_img": "images/shared/beauty.png"},
    {"slug": "mcintyres-perth", "logo": "https://www.mcintyres.co.uk/wp-content/blogs.dir/188/files/2020/10/200x80-McIntyres-Logo.png", "hero_img": "images/shared/salon.png", "card_img": "images/shared/beauty.png"},
    {"slug": "dalziel-park", "logo": "https://dalzielpark.co.uk/wp-content/uploads/2024/12/dalziel-logo.png", "hero_img": "images/shared/hotel.png", "card_img": "images/shared/pub.png"},
]

count = 0
for biz in businesses:
    slug = biz["slug"]
    filepath = f"{slug}.html"

    if not os.path.exists(filepath):
        print(f"SKIP: {filepath} not found")
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    original = html

    # 1. Replace text logo with image logo in nav
    logo_pattern = r'<div class="logo serif">.*?</div>'
    logo_img = f'<img src="{biz["logo"]}" alt="{slug}" style="height: 40px; filter: brightness(0) invert(1);">'
    html = re.sub(logo_pattern, logo_img, html, count=1)

    # 2. Add hero background image
    hero_pattern = r'<section class="hero">'
    hero_img_url = biz["hero_img"]
    hero_replacement = f'<section class="hero" style="background: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.65)), url(\'{hero_img_url}\') center/cover no-repeat;">'
    html = html.replace('<section class="hero">', hero_replacement, 1)

    # Also remove the ::before pattern overlay since we now have a real image
    # The CSS handles the gradient, but we need to override the hero gradient background
    old_hero_bg = re.search(r'\.hero \{[^}]*background: linear-gradient\([^)]+\)[^;]*;', html)

    # 3. Replace about-image placeholder with real image
    about_pattern = r'<div class="about-image">.*?</div>'
    about_replacement = f'<div class="about-image" style="background: url(\'{biz["card_img"]}\') center/cover no-repeat; color: transparent;">.</div>'
    html = re.sub(about_pattern, about_replacement, html, count=1)

    # 4. Replace card-img placeholders with real images
    card_imgs = [biz["hero_img"], biz["card_img"], biz["hero_img"]]
    card_counter = [0]
    def replace_card_img(match):
        img = card_imgs[card_counter[0] % len(card_imgs)]
        card_counter[0] += 1
        return f'<div class="card-img" style="background: url(\'{img}\') center/cover no-repeat; color: transparent;">.</div>'

    html = re.sub(r'<div class="card-img">(.*?)</div>', replace_card_img, html)

    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"UPGRADED: {filepath}")
        count += 1
    else:
        print(f"NO CHANGE: {filepath}")

print(f"\nTotal upgraded: {count}")
