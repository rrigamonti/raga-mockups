import json, os

with open('../scraping/round6_clean.json') as f:
    leads = json.load(f)
with open('../scraping/round6_slugs.json') as f:
    slugs = json.load(f)
with open('../scraping/round5_logos.json') as f:
    logos_data = json.load(f)  # reuse logo scraping logic

with open('template.html', 'r') as f:
    template = f.read()

# Category to shared image mapping
cat_images = {
    "Restaurant": ("images/shared/bar-restaurant.png", "images/shared/bistro.png"),
    "Hotel": ("images/shared/hotel.png", "images/shared/bistro.png"),
    "Pub": ("images/shared/pub.png", "images/shared/bar-restaurant.png"),
    "Cafe": ("images/shared/bistro.png", "images/shared/farm-shop.png"),
    "Hair Salon": ("images/shared/salon.png", "images/shared/beauty.png"),
    "Beauty Salon": ("images/shared/beauty.png", "images/shared/salon.png"),
    "Other": ("images/shared/bar-restaurant.png", "images/shared/bistro.png"),
}

# Category to color scheme
cat_colors = {
    "Restaurant": ("#3b4f3a", "#242f24", "#d4a84b", "#faf8f5", "#f2efe9", "#242f24", "#5e6e5d", "#5a7358"),
    "Hotel": ("#3a2a4a", "#2a1a3a", "#c9a84c", "#faf8fb", "#f0edf2", "#2a1a2a", "#6a5a6a", "#5a4a6a"),
    "Pub": ("#2c3e50", "#1a2530", "#e67e22", "#f9f9f9", "#f0f0f0", "#1a1a1a", "#5a5a5a", "#3d5a78"),
    "Cafe": ("#6b4226", "#4a2a18", "#d4a84b", "#faf8f5", "#f2efe9", "#2a1a0a", "#6e5a4a", "#8a6a48"),
    "Hair Salon": ("#8b5e83", "#5a3d55", "#d4a0c0", "#faf7f9", "#f2eef0", "#2a1a25", "#6e5a68", "#a07898"),
    "Beauty Salon": ("#9c6b8e", "#6a4a60", "#d4a0c0", "#fdf8f9", "#f5eef0", "#2a1a20", "#6a5a60", "#b888a8"),
    "Other": ("#2c3e50", "#1a2530", "#e67e22", "#f9f9f9", "#f0f0f0", "#1a1a1a", "#5a5a5a", "#3d5a78"),
}

# Category-specific hooks for emails
cat_hooks = {
    "Restaurant": "a modern, mobile-friendly site with online booking and your menu front and centre could turn those searches into actual reservations",
    "Hotel": "a sleek, modern site with direct booking, room galleries and guest reviews front and centre could help you capture more direct reservations",
    "Pub": "a modern, mobile-friendly site with your events calendar, menu and online booking could turn more Google searches into actual footfall",
    "Cafe": "a fresh, modern site with your menu, opening hours and online ordering front and centre could turn more passing searches into loyal regulars",
    "Hair Salon": "a sleek, modern site with online booking, a style gallery and pricing front and centre could turn more Google searches into booked appointments",
    "Beauty Salon": "a polished, modern site with online booking, your treatment menu and client reviews front and centre could turn more searches into booked appointments",
    "Other": "a modern, professional website could help you reach more customers searching online in your area",
}

# Category-specific nav items and features
cat_nav = {
    "Restaurant": ("Home|Menu|About|Gallery|Book", "Book a Table"),
    "Hotel": ("Home|Rooms|Restaurant|Events|Book", "Book Now"),
    "Pub": ("Home|Menu|Drinks|Events|Book", "Book a Table"),
    "Cafe": ("Home|Menu|About|Gallery|Contact", "Visit Us"),
    "Hair Salon": ("Home|Services|Gallery|About|Book", "Book Now"),
    "Beauty Salon": ("Home|Treatments|About|Gallery|Book", "Book Now"),
    "Other": ("Home|About|Events|Gallery|Contact", "Get in Touch"),
}

count = 0
for lead in leads:
    name = lead['name']
    slug = slugs[name]
    cat = lead.get('category', 'Restaurant')
    town = lead.get('town', '')

    colors = cat_colors.get(cat, cat_colors['Restaurant'])
    primary, primary_dark, accent, bg, bg_alt, text, text_light, hero_end = colors
    hero_img, card_img = cat_images.get(cat, cat_images['Restaurant'])
    nav_items_str, cta = cat_nav.get(cat, cat_nav['Restaurant'])
    nav_items = nav_items_str.split('|')

    nav_html = ''.join([f'<li><a href="#">{item}</a></li>' for item in nav_items])

    # Build name for logo (split for styling)
    name_parts = name.split(' ', 1)
    if len(name_parts) > 1:
        logo_text = f'{name_parts[0]} <span>{name_parts[1]}</span>'
    else:
        logo_text = f'<span>{name}</span>'

    body = f"""
<nav><div class="inner">
  <div class="logo serif">{logo_text}</div>
  <ul>{nav_html}</ul>
  <a href="#" class="cta-btn">{cta}</a>
</div></nav>

<section class="hero" style="background: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.65)), url('{hero_img}') center/cover no-repeat;">
  <div class="hero-content">
    <div class="hero-badge">{town}</div>
    <h1 class="serif">Welcome to <em>{name}</em></h1>
    <p>Discover what makes {name} special. Quality, passion and a warm welcome in the heart of {town}.</p>
    <div class="hero-buttons">
      <a href="#" class="btn-primary">{cta} &#8594;</a>
      <a href="#" class="btn-secondary">Learn More</a>
    </div>
  </div>
</section>

<div class="features-strip"><div class="inner">
  <div class="feature-item"><div class="icon">&#11088;</div><h4>Top Rated</h4><p>Excellent reviews</p></div>
  <div class="feature-item"><div class="icon">&#128205;</div><h4>{town}</h4><p>Easy to find</p></div>
  <div class="feature-item"><div class="icon">&#128151;</div><h4>Trusted</h4><p>Local favourite</p></div>
  <div class="feature-item"><div class="icon">&#128197;</div><h4>Book Online</h4><p>Quick and easy</p></div>
</div></div>

<section class="about-section">
  <div class="section-inner about-grid">
    <div class="about-image" style="background: url('{card_img}') center/cover no-repeat; color: transparent;">.</div>
    <div class="about-text">
      <h2 class="serif">About {name}</h2>
      <p>{name} has been proudly serving {town} and the surrounding area. We are passionate about what we do and it shows in everything from our service to our attention to detail.</p>
      <p>Whether you are a regular or visiting for the first time, you will always receive a warm welcome.</p>
      <div class="highlight">
        <div><div class="number">5.0</div><div class="label">Star Rating</div></div>
        <div><div class="number">100+</div><div class="label">Reviews</div></div>
        <div><div class="number">7</div><div class="label">Days a Week</div></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">What We Offer</div>
      <h2 class="serif">Our Services</h2>
      <p>Quality and care in everything we do</p>
    </div>
    <div class="cards-grid">
      <div class="card"><div class="card-img" style="background: url('{hero_img}') center/cover no-repeat; color: transparent;">.</div><div class="card-body"><h3>Our Speciality</h3><p>What we are known for - quality, consistency and a personal touch.</p></div></div>
      <div class="card"><div class="card-img" style="background: url('{card_img}') center/cover no-repeat; color: transparent;">.</div><div class="card-body"><h3>The Experience</h3><p>From the moment you arrive to the moment you leave, we make it special.</p></div></div>
      <div class="card"><div class="card-img" style="background: url('{hero_img}') center/cover no-repeat; color: transparent;">.</div><div class="card-body"><h3>Book With Us</h3><p>Easy online booking available. Reserve your spot today.</p></div></div>
    </div>
  </div>
</section>

<section class="testimonials">
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">Reviews</div>
      <h2 class="serif">What People Are Saying</h2>
    </div>
    <div class="testimonial-grid">
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Absolutely fantastic. One of the best in {town}. Highly recommend."</p><div class="author">Google Review</div></div>
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Brilliant service, wonderful atmosphere. Will definitely be back."</p><div class="author">Google Review</div></div>
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"A real gem. The quality is outstanding and the team are so welcoming."</p><div class="author">Google Review</div></div>
    </div>
  </div>
</section>

<section class="cta-banner">
  <h2 class="serif">Ready to visit?</h2>
  <p>Book online or get in touch with {name} today.</p>
  <a href="#" class="btn-primary">{cta} &#8594;</a>
</section>

<footer><div class="inner">
  <div><div class="brand serif">{name}</div><p>{town}, Scotland.</p></div>
  <div><h4>Quick Links</h4><a href="#">Home</a><br><a href="#">About</a><br><a href="#">Contact</a></div>
  <div><h4>Book</h4><a href="#">Book Online</a><br><a href="#">Gift Vouchers</a></div>
  <div><h4>Contact</h4><p>{town}</p><p>{lead['email']}</p></div>
</div><div class="bottom">Design concept by RAGA Marketing &mdash; ragamarketing.com</div></footer>"""

    html = template.replace("{{PRIMARY_COLOR}}", primary)
    html = html.replace("{{PRIMARY_DARK}}", primary_dark)
    html = html.replace("{{ACCENT_COLOR}}", accent)
    html = html.replace("{{BG_COLOR}}", bg)
    html = html.replace("{{BG_ALT}}", bg_alt)
    html = html.replace("{{TEXT_COLOR}}", text)
    html = html.replace("{{TEXT_LIGHT}}", text_light)
    html = html.replace("{{HERO_GRADIENT_END}}", hero_end)
    html = html.replace("{{BUSINESS_NAME}}", name)
    html = html.replace("{{TAGLINE}}", town)
    html = html.replace("{{BODY_CONTENT}}", body)

    filename = f'{slug}.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    count += 1

print(f"Generated {count} mockups")
