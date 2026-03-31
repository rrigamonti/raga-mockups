import os

template_path = os.path.join(os.path.dirname(__file__), 'template.html')
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

businesses = [
    {
        "slug": "meigan-alessandra",
        "name": "Meigan Alessandra",
        "tagline": "Bridal Hair Scotland",
        "primary": "#3d2c2e",
        "primary_dark": "#1f1517",
        "accent": "#d4a574",
        "bg": "#faf8f6",
        "bg_alt": "#f3ede8",
        "text": "#2c2220",
        "text_light": "#7a6b65",
        "hero_gradient": "#5a3a3e",
        "body": """
<nav><div class="inner">
  <div class="logo serif">Meigan <span>Alessandra</span></div>
  <ul><li><a href="#">Home</a></li><li><a href="#">Services</a></li><li><a href="#">Gallery</a></li><li><a href="#">About</a></li><li><a href="#">Contact</a></li></ul>
  <a href="#" class="cta-btn">Book a Consultation</a>
</div></nav>

<section class="hero">
  <div class="hero-content">
    <div class="hero-badge">Award-Winning Bridal Stylist</div>
    <h1 class="serif">Effortless, <em>romantic</em> bridal hair</h1>
    <p>Creating beautiful, timeless hairstyles for your most special day. Based in Stirling, serving brides across Scotland.</p>
    <div class="hero-buttons">
      <a href="#" class="btn-primary">Book Your Trial &#8594;</a>
      <a href="#" class="btn-secondary">View Portfolio</a>
    </div>
  </div>
</section>

<div class="features-strip"><div class="inner">
  <div class="feature-item"><div class="icon">&#128141;</div><h4>400+ Brides Styled</h4><p>Trusted by hundreds of happy brides</p></div>
  <div class="feature-item"><div class="icon">&#11088;</div><h4>5-Star Reviews</h4><p>Perfect rating across all platforms</p></div>
  <div class="feature-item"><div class="icon">&#128205;</div><h4>Scotland-Wide</h4><p>Travel to any venue across Scotland</p></div>
  <div class="feature-item"><div class="icon">&#128151;</div><h4>Bespoke Styling</h4><p>Every bride gets a unique look</p></div>
</div></div>

<section class="about-section">
  <div class="section-inner about-grid">
    <div class="about-image">"Making brides feel like the most beautiful version of themselves"</div>
    <div class="about-text">
      <h2 class="serif">Your Day, Your Style</h2>
      <p>With over a decade of experience in bridal hair, Meigan creates stunning, personalised hairstyles that last from ceremony to last dance.</p>
      <p>From romantic updos to flowing waves, every style is crafted to complement your dress, venue and personality.</p>
      <div class="highlight">
        <div><div class="number">400+</div><div class="label">Brides Styled</div></div>
        <div><div class="number">10+</div><div class="label">Years Experience</div></div>
        <div><div class="number">5.0</div><div class="label">Star Rating</div></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">Packages</div>
      <h2 class="serif">Find Your Perfect Package</h2>
      <p>Three tiers designed to suit every bride's needs</p>
    </div>
    <div class="cards-grid">
      <div class="card"><div class="card-img">Simply Bridal</div><div class="card-body"><h3>Simply Bridal</h3><p>Perfect for the low-key bride. Includes trial and wedding day styling for the bride.</p><div class="price">From &pound;350</div></div></div>
      <div class="card"><div class="card-img">Signature Bride</div><div class="card-body"><h3>Signature Bride</h3><p>Our most popular package. Trial, wedding day styling for bride plus two bridesmaids.</p><div class="price">From &pound;550</div></div></div>
      <div class="card"><div class="card-img">VIP Bride</div><div class="card-body"><h3>VIP Bride</h3><p>The ultimate experience. Full bridal party styling with luxury extras and priority booking.</p><div class="price">From &pound;850</div></div></div>
    </div>
  </div>
</section>

<section class="testimonials">
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">Love Letters</div>
      <h2 class="serif">What Our Brides Say</h2>
      <p>Real reviews from real brides</p>
    </div>
    <div class="testimonial-grid">
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Meigan made me feel so relaxed and beautiful on my wedding day. My hair lasted all night!"</p><div class="author">Emma, Stirling</div></div>
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Absolutely incredible. She knew exactly what I wanted before I could even explain it."</p><div class="author">Sophie, Edinburgh</div></div>
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"The trial was so thorough, I had zero stress on the day. Worth every penny."</p><div class="author">Laura, Glasgow</div></div>
    </div>
  </div>
</section>

<section class="cta-banner">
  <h2 class="serif">Ready to find your perfect bridal look?</h2>
  <p>Book your free consultation and let's create something beautiful together.</p>
  <a href="#" class="btn-primary">Get in Touch &#8594;</a>
</section>

<footer><div class="inner">
  <div><div class="brand serif">Meigan Alessandra</div><p>Award-winning bridal hair stylist based in Stirling, serving brides across Scotland.</p></div>
  <div><h4>Quick Links</h4><a href="#">Services</a><br><a href="#">Gallery</a><br><a href="#">About</a><br><a href="#">FAQs</a></div>
  <div><h4>Packages</h4><a href="#">Simply Bridal</a><br><a href="#">Signature Bride</a><br><a href="#">VIP Bride</a></div>
  <div><h4>Contact</h4><p>Stirling, Scotland</p><p>hello@meiganalessandra.com</p><p>07714 930555</p></div>
</div><div class="bottom">Design concept by RAGA Marketing &mdash; ragamarketing.com</div></footer>"""
    },
    {
        "slug": "the-woodside",
        "name": "The Woodside",
        "tagline": "Eat &bull; Drink &bull; Stay &mdash; Doune",
        "primary": "#2d4a3e",
        "primary_dark": "#1a2e26",
        "accent": "#c8a96e",
        "bg": "#f9f7f4",
        "bg_alt": "#f0ece6",
        "text": "#1a2e26",
        "text_light": "#5c7a6d",
        "hero_gradient": "#3a5f4f",
        "body": """
<nav><div class="inner">
  <div class="logo serif">The <span>Woodside</span></div>
  <ul><li><a href="#">Home</a></li><li><a href="#">Menu</a></li><li><a href="#">Rooms</a></li><li><a href="#">Events</a></li><li><a href="#">Contact</a></li></ul>
  <a href="#" class="cta-btn">Book a Table</a>
</div></nav>

<section class="hero">
  <div class="hero-content">
    <div class="hero-badge">Doune, Perthshire</div>
    <h1 class="serif">Eat, Drink &amp; <em>Stay</em> in the heart of Doune</h1>
    <p>A warm Scottish welcome with exceptional food, great drinks and comfortable rooms. Just moments from Doune Castle.</p>
    <div class="hero-buttons">
      <a href="#" class="btn-primary">Book a Table &#8594;</a>
      <a href="#" class="btn-secondary">View Rooms</a>
    </div>
  </div>
</section>

<div class="features-strip"><div class="inner">
  <div class="feature-item"><div class="icon">&#127860;</div><h4>Fresh Local Menu</h4><p>Seasonal Scottish produce daily</p></div>
  <div class="feature-item"><div class="icon">&#11088;</div><h4>4.5 Star Rating</h4><p>731 reviews on Google</p></div>
  <div class="feature-item"><div class="icon">&#127968;</div><h4>Boutique Rooms</h4><p>Stylish overnight accommodation</p></div>
  <div class="feature-item"><div class="icon">&#127867;</div><h4>Craft Bar</h4><p>Scottish gins, ales &amp; whisky</p></div>
</div></div>

<section class="about-section">
  <div class="section-inner about-grid">
    <div class="about-image">"Where Scottish hospitality meets modern comfort"</div>
    <div class="about-text">
      <h2 class="serif">A Doune Institution</h2>
      <p>The Woodside has been the heart of Doune's social scene for generations. Whether you're popping in for a pint, settling down for a three-course dinner, or staying the night in one of our stylish rooms, you'll always feel at home.</p>
      <p>Our kitchen champions local Scottish suppliers, bringing the best seasonal produce to your plate.</p>
      <div class="highlight">
        <div><div class="number">731</div><div class="label">Google Reviews</div></div>
        <div><div class="number">4.5</div><div class="label">Star Rating</div></div>
        <div><div class="number">7</div><div class="label">Days a Week</div></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">Eat &amp; Drink</div>
      <h2 class="serif">From Our Kitchen</h2>
      <p>Seasonal Scottish dishes with a modern twist</p>
    </div>
    <div class="cards-grid">
      <div class="card"><div class="card-img">Lunch Menu</div><div class="card-body"><h3>Lunch</h3><p>Light bites, soups and hearty mains. Perfect for a midday stop in Doune. Served 12-3pm daily.</p></div></div>
      <div class="card"><div class="card-img">Dinner Menu</div><div class="card-body"><h3>Dinner</h3><p>Our evening menu showcases the best of Scottish produce. Book ahead for weekends.</p></div></div>
      <div class="card"><div class="card-img">Sunday Roast</div><div class="card-body"><h3>Sunday Roast</h3><p>A Woodside tradition. Slow-roasted meats with all the trimmings. Booking essential.</p></div></div>
    </div>
  </div>
</section>

<section class="testimonials">
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">Our Guests</div>
      <h2 class="serif">What People Are Saying</h2>
    </div>
    <div class="testimonial-grid">
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Best pub food we've had in Scotland. The steak pie was absolutely incredible."</p><div class="author">TripAdvisor Review</div></div>
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Lovely rooms, great breakfast, and the staff couldn't have been more welcoming."</p><div class="author">Google Review</div></div>
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Our go-to spot whenever we visit Doune Castle. Never disappoints."</p><div class="author">Google Review</div></div>
    </div>
  </div>
</section>

<section class="cta-banner">
  <h2 class="serif">Your table is waiting</h2>
  <p>Book online for lunch, dinner, or an overnight stay in Doune.</p>
  <a href="#" class="btn-primary">Reserve Now &#8594;</a>
</section>

<footer><div class="inner">
  <div><div class="brand serif">The Woodside</div><p>Eat, Drink &amp; Stay in the heart of Doune, Perthshire.</p></div>
  <div><h4>Menu</h4><a href="#">Lunch</a><br><a href="#">Dinner</a><br><a href="#">Drinks</a><br><a href="#">Sunday Roast</a></div>
  <div><h4>Stay</h4><a href="#">Rooms</a><br><a href="#">Book Online</a><br><a href="#">Gift Vouchers</a></div>
  <div><h4>Contact</h4><p>Doune, Perthshire</p><p>info@thewoodsidedoune.co.uk</p><p>01786 643399</p></div>
</div><div class="bottom">Design concept by RAGA Marketing &mdash; ragamarketing.com</div></footer>"""
    },
    {
        "slug": "crown-hotel",
        "name": "The Crown Hotel",
        "tagline": "Callander's Historic Hotel &amp; Bar",
        "primary": "#3b2d1f",
        "primary_dark": "#1e1610",
        "accent": "#bf9f3f",
        "bg": "#faf8f5",
        "bg_alt": "#f2ede6",
        "text": "#2a2018",
        "text_light": "#7a6b5a",
        "hero_gradient": "#5a4530",
        "body": """
<nav><div class="inner">
  <div class="logo serif">The <span>Crown</span> Hotel</div>
  <ul><li><a href="#">Home</a></li><li><a href="#">Rooms</a></li><li><a href="#">Dining</a></li><li><a href="#">Bar</a></li><li><a href="#">Explore</a></li></ul>
  <a href="#" class="cta-btn">Check Availability</a>
</div></nav>

<section class="hero">
  <div class="hero-content">
    <div class="hero-badge">Est. Callander, Scotland</div>
    <h1 class="serif">Your gateway to the <em>Trossachs</em></h1>
    <p>A charming historic hotel in the heart of Callander. Comfortable rooms, excellent food and the perfect base for exploring Scotland's first national park.</p>
    <div class="hero-buttons">
      <a href="#" class="btn-primary">Book Your Stay &#8594;</a>
      <a href="#" class="btn-secondary">Explore Dining</a>
    </div>
  </div>
</section>

<div class="features-strip"><div class="inner">
  <div class="feature-item"><div class="icon">&#127968;</div><h4>Historic Rooms</h4><p>Character-filled accommodation</p></div>
  <div class="feature-item"><div class="icon">&#11088;</div><h4>4.4 Stars</h4><p>619 reviews on Google</p></div>
  <div class="feature-item"><div class="icon">&#127966;</div><h4>Trossachs Gateway</h4><p>Steps from walking trails</p></div>
  <div class="feature-item"><div class="icon">&#127863;</div><h4>Award-Winning Bar</h4><p>Scottish whisky &amp; craft ales</p></div>
</div></div>

<section class="about-section">
  <div class="section-inner about-grid">
    <div class="about-image">"The perfect base for your Scottish adventure"</div>
    <div class="about-text">
      <h2 class="serif">History Meets Hospitality</h2>
      <p>Nestled in the heart of Callander, The Crown Hotel has welcomed travellers for generations. Whether you're here for the walking, the whisky or simply the warm Scottish welcome, we'll make sure your stay is one to remember.</p>
      <p>Our restaurant serves locally-sourced Scottish cuisine, and our bar stocks over 100 whiskies from across Scotland.</p>
      <div class="highlight">
        <div><div class="number">619</div><div class="label">Reviews</div></div>
        <div><div class="number">4.4</div><div class="label">Stars</div></div>
        <div><div class="number">100+</div><div class="label">Whiskies</div></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">Accommodation</div>
      <h2 class="serif">Rest &amp; Recharge</h2>
      <p>Comfortable rooms with character in the heart of Callander</p>
    </div>
    <div class="cards-grid">
      <div class="card"><div class="card-img">Classic Double</div><div class="card-body"><h3>Classic Double</h3><p>Cosy room with views over Callander's Main Street. En-suite, TV and tea/coffee facilities.</p><div class="price">From &pound;89/night</div></div></div>
      <div class="card"><div class="card-img">Superior Room</div><div class="card-body"><h3>Superior Room</h3><p>Spacious room with upgraded furnishings and mountain views. Perfect for a longer stay.</p><div class="price">From &pound;119/night</div></div></div>
      <div class="card"><div class="card-img">Family Suite</div><div class="card-body"><h3>Family Suite</h3><p>Generous suite ideal for families exploring the Trossachs. Sleeps up to four.</p><div class="price">From &pound;149/night</div></div></div>
    </div>
  </div>
</section>

<section class="testimonials">
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">Guest Reviews</div>
      <h2 class="serif">What Our Guests Say</h2>
    </div>
    <div class="testimonial-grid">
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Fantastic location, friendly staff, and the food was superb. Will definitely return."</p><div class="author">Google Review</div></div>
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"The whisky selection is incredible. Staff really know their stuff and the bar has great atmosphere."</p><div class="author">Google Review</div></div>
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Perfect base for walking the Trossachs. Room was comfortable and breakfast was excellent."</p><div class="author">TripAdvisor</div></div>
    </div>
  </div>
</section>

<section class="cta-banner">
  <h2 class="serif">Plan Your Callander Escape</h2>
  <p>Book directly for the best rates and a warm Scottish welcome.</p>
  <a href="#" class="btn-primary">Check Availability &#8594;</a>
</section>

<footer><div class="inner">
  <div><div class="brand serif">The Crown Hotel</div><p>Historic hotel &amp; bar in the heart of Callander, gateway to the Trossachs.</p></div>
  <div><h4>Stay</h4><a href="#">Rooms</a><br><a href="#">Book Online</a><br><a href="#">Special Offers</a></div>
  <div><h4>Experience</h4><a href="#">Restaurant</a><br><a href="#">Bar</a><br><a href="#">Local Walks</a></div>
  <div><h4>Contact</h4><p>Main Street, Callander</p><p>bookings@crownhotelcallander.co.uk</p><p>01877 330040</p></div>
</div><div class="bottom">Design concept by RAGA Marketing &mdash; ragamarketing.com</div></footer>"""
    },
    {
        "slug": "crams-bar",
        "name": "Crams Bar",
        "tagline": "Est. 1784 &mdash; Alloa",
        "primary": "#1a1a1a",
        "primary_dark": "#0d0d0d",
        "accent": "#f1c761",
        "bg": "#f8f7f5",
        "bg_alt": "#efede8",
        "text": "#1a1a1a",
        "text_light": "#666666",
        "hero_gradient": "#2a2520",
        "body": """
<nav><div class="inner">
  <div class="logo serif">Crams <span>Bar</span></div>
  <ul><li><a href="#">Home</a></li><li><a href="#">Drinks</a></li><li><a href="#">Events</a></li><li><a href="#">Sport</a></li><li><a href="#">Contact</a></li></ul>
  <a href="#" class="cta-btn">What's On</a>
</div></nav>

<section class="hero">
  <div class="hero-content">
    <div class="hero-badge">Est. 1784 &mdash; Alloa</div>
    <h1 class="serif">Alloa's finest since <em>1784</em></h1>
    <p>Live sport. Live music. Great drinks. The beating heart of Alloa's social scene for over 240 years.</p>
    <div class="hero-buttons">
      <a href="#" class="btn-primary">See What's On &#8594;</a>
      <a href="#" class="btn-secondary">Our Drinks</a>
    </div>
  </div>
</section>

<div class="features-strip"><div class="inner">
  <div class="feature-item"><div class="icon">&#127866;</div><h4>Craft Beer</h4><p>Local brewing &amp; guest ales</p></div>
  <div class="feature-item"><div class="icon">&#9917;</div><h4>Live Sport</h4><p>All the big games, every screen</p></div>
  <div class="feature-item"><div class="icon">&#127928;</div><h4>Live Music</h4><p>Regular gigs &amp; open mic nights</p></div>
  <div class="feature-item"><div class="icon">&#11088;</div><h4>4.6 Stars</h4><p>106 five-star reviews</p></div>
</div></div>

<section class="about-section">
  <div class="section-inner about-grid">
    <div class="about-image">"240 years of great craic and even better drinks"</div>
    <div class="about-text">
      <h2 class="serif">A Bar With History</h2>
      <p>Since 1784, Crams has been the place where Alloa comes together. Whether it's a quiet pint after work, a big match on the screens, or a Friday night with live music, there's always a reason to pull up a stool.</p>
      <p>We pride ourselves on our selection of local craft beers, premium gins and a whisky list that would make your grandad proud.</p>
      <div class="highlight">
        <div><div class="number">240+</div><div class="label">Years</div></div>
        <div><div class="number">4.6</div><div class="label">Stars</div></div>
        <div><div class="number">106</div><div class="label">Reviews</div></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">What's On</div>
      <h2 class="serif">Upcoming Events</h2>
      <p>There's always something happening at Crams</p>
    </div>
    <div class="cards-grid">
      <div class="card"><div class="card-img">Live Music Friday</div><div class="card-body"><h3>Live Music Fridays</h3><p>Local bands and solo artists every Friday night from 9pm. Free entry, great atmosphere.</p></div></div>
      <div class="card"><div class="card-img">Saturday Sport</div><div class="card-body"><h3>Big Match Saturdays</h3><p>Every Premier League and Scottish Prem game shown live on our big screens. Pints from &pound;3.50.</p></div></div>
      <div class="card"><div class="card-img">Sunday Session</div><div class="card-body"><h3>Sunday Sessions</h3><p>Acoustic sets, roast specials and a relaxed vibe to round off the weekend.</p></div></div>
    </div>
  </div>
</section>

<section class="testimonials">
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">Our Regulars</div>
      <h2 class="serif">What People Say</h2>
    </div>
    <div class="testimonial-grid">
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Best bar in Alloa, hands down. Great atmosphere and the staff are always sound."</p><div class="author">Google Review</div></div>
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Love the live music nights. Always a brilliant selection of beers on tap too."</p><div class="author">Google Review</div></div>
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"A proper local pub with character. None of that chain pub nonsense."</p><div class="author">Google Review</div></div>
    </div>
  </div>
</section>

<section class="cta-banner">
  <h2 class="serif">See you at the bar?</h2>
  <p>Follow us on social media for the latest events and drink specials.</p>
  <a href="#" class="btn-primary">Follow Us &#8594;</a>
</section>

<footer><div class="inner">
  <div><div class="brand serif">Crams Bar</div><p>Alloa's favourite local since 1784. Live sport, live music, great drinks.</p></div>
  <div><h4>Quick Links</h4><a href="#">What's On</a><br><a href="#">Drinks Menu</a><br><a href="#">Private Hire</a></div>
  <div><h4>Follow Us</h4><a href="#">Facebook</a><br><a href="#">Instagram</a></div>
  <div><h4>Find Us</h4><p>Alloa, Clackmannanshire</p><p>info@cramsbaralloa.co.uk</p><p>01259 219420</p></div>
</div><div class="bottom">Design concept by RAGA Marketing &mdash; ragamarketing.com</div></footer>"""
    },
    {
        "slug": "campania-pizza",
        "name": "CAMPA-NIA PIZZA",
        "tagline": "Authentic Pizza &mdash; Denny, Scotland",
        "primary": "#8b2500",
        "primary_dark": "#4a1400",
        "accent": "#f0c040",
        "bg": "#faf8f5",
        "bg_alt": "#f5efe8",
        "text": "#2a1a10",
        "text_light": "#7a5a40",
        "hero_gradient": "#a83000",
        "body": """
<nav><div class="inner">
  <div class="logo serif">Campa<span>-nia</span></div>
  <ul><li><a href="#">Home</a></li><li><a href="#">Menu</a></li><li><a href="#">Order Online</a></li><li><a href="#">About</a></li><li><a href="#">Contact</a></li></ul>
  <a href="#" class="cta-btn">Order Now</a>
</div></nav>

<section class="hero">
  <div class="hero-content">
    <div class="hero-badge">Denny, Scotland</div>
    <h1 class="serif">Authentic Italian pizza, <em>made in Scotland</em></h1>
    <p>Hand-stretched dough. San Marzano tomatoes. Fresh mozzarella. Real Italian pizza from the heart of Denny.</p>
    <div class="hero-buttons">
      <a href="#" class="btn-primary">Order Online &#8594;</a>
      <a href="#" class="btn-secondary">View Menu</a>
    </div>
  </div>
</section>

<div class="features-strip"><div class="inner">
  <div class="feature-item"><div class="icon">&#127829;</div><h4>Hand-Stretched</h4><p>Authentic Italian dough, every time</p></div>
  <div class="feature-item"><div class="icon">&#11088;</div><h4>4.8 Stars</h4><p>108 five-star reviews</p></div>
  <div class="feature-item"><div class="icon">&#128666;</div><h4>Fast Delivery</h4><p>Hot to your door in 30 mins</p></div>
  <div class="feature-item"><div class="icon">&#127813;</div><h4>Fresh Ingredients</h4><p>Premium imported toppings</p></div>
</div></div>

<section>
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">Our Pizzas</div>
      <h2 class="serif">Made With Love</h2>
      <p>Classic Italian recipes with premium ingredients</p>
    </div>
    <div class="cards-grid">
      <div class="card"><div class="card-img">Margherita</div><div class="card-body"><h3>Classic Margherita</h3><p>San Marzano tomato sauce, fior di latte mozzarella, fresh basil. Simple perfection.</p><div class="price">From &pound;8.50</div></div></div>
      <div class="card"><div class="card-img">Pepperoni</div><div class="card-body"><h3>Pepperoni Classica</h3><p>Spicy pepperoni, mozzarella, our signature tomato base. The people's favourite.</p><div class="price">From &pound;10.50</div></div></div>
      <div class="card"><div class="card-img">Speciale</div><div class="card-body"><h3>Campania Speciale</h3><p>Our signature creation. Italian sausage, roasted peppers, olives and fresh chilli.</p><div class="price">From &pound;12.00</div></div></div>
    </div>
  </div>
</section>

<section class="testimonials">
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">Reviews</div>
      <h2 class="serif">What Denny Is Saying</h2>
    </div>
    <div class="testimonial-grid">
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Best pizza in the area by a mile. Tastes like proper Italian, not just another takeaway."</p><div class="author">Google Review</div></div>
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Fresh, fast and absolutely delicious. The dough is incredible."</p><div class="author">Google Review</div></div>
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Our Friday night regular now. The kids love it and so do we!"</p><div class="author">Google Review</div></div>
    </div>
  </div>
</section>

<section class="cta-banner">
  <h2 class="serif">Hungry? Let's fix that.</h2>
  <p>Order online for collection or delivery. Fresh from our oven to your door.</p>
  <a href="#" class="btn-primary">Order Now &#8594;</a>
</section>

<footer><div class="inner">
  <div><div class="brand serif">Campania Pizza</div><p>Authentic Italian pizza made fresh in Denny, Scotland.</p></div>
  <div><h4>Menu</h4><a href="#">Pizzas</a><br><a href="#">Sides</a><br><a href="#">Desserts</a><br><a href="#">Drinks</a></div>
  <div><h4>Order</h4><a href="#">Order Online</a><br><a href="#">Collection</a><br><a href="#">Delivery Info</a></div>
  <div><h4>Contact</h4><p>Denny, Stirlingshire</p><p>campaniapizzascotland@gmail.com</p><p>01324 640352</p></div>
</div><div class="bottom">Design concept by RAGA Marketing &mdash; ragamarketing.com</div></footer>"""
    },
    {
        "slug": "callander-meadows",
        "name": "Callander Meadows",
        "tagline": "Restaurant &amp; Rooms &mdash; Callander",
        "primary": "#4a3728",
        "primary_dark": "#2a1f16",
        "accent": "#b99247",
        "bg": "#faf8f5",
        "bg_alt": "#f2ece4",
        "text": "#2a1f16",
        "text_light": "#7a6a58",
        "hero_gradient": "#5c4535",
        "body": """
<nav><div class="inner">
  <div class="logo serif">Callander <span>Meadows</span></div>
  <ul><li><a href="#">Home</a></li><li><a href="#">Menus</a></li><li><a href="#">Rooms</a></li><li><a href="#">About</a></li><li><a href="#">Book</a></li></ul>
  <a href="#" class="cta-btn">Reserve a Table</a>
</div></nav>

<section class="hero">
  <div class="hero-content">
    <div class="hero-badge">Callander, The Trossachs</div>
    <h1 class="serif">Fine dining in the <em>Trossachs</em></h1>
    <p>A charming restaurant with rooms in the heart of Callander. Locally-sourced Scottish cuisine in a beautifully restored Georgian townhouse.</p>
    <div class="hero-buttons">
      <a href="#" class="btn-primary">Reserve a Table &#8594;</a>
      <a href="#" class="btn-secondary">View Menu</a>
    </div>
  </div>
</section>

<div class="features-strip"><div class="inner">
  <div class="feature-item"><div class="icon">&#127860;</div><h4>Locally Sourced</h4><p>The best Scottish produce</p></div>
  <div class="feature-item"><div class="icon">&#11088;</div><h4>4.6 Stars</h4><p>199 glowing reviews</p></div>
  <div class="feature-item"><div class="icon">&#127968;</div><h4>Boutique Rooms</h4><p>Stay in a Georgian townhouse</p></div>
  <div class="feature-item"><div class="icon">&#127863;</div><h4>Wine &amp; Whisky</h4><p>Curated Scottish selection</p></div>
</div></div>

<section class="about-section">
  <div class="section-inner about-grid">
    <div class="about-image">"Where Scottish produce meets culinary artistry"</div>
    <div class="about-text">
      <h2 class="serif">A Taste of the Trossachs</h2>
      <p>Callander Meadows brings together the finest local ingredients with skilled, passionate cooking. Our ever-changing menu reflects what's fresh, what's seasonal, and what's exciting.</p>
      <p>Set in a beautifully restored Georgian townhouse, we also offer charming rooms for guests who want to extend their Trossachs experience.</p>
      <div class="highlight">
        <div><div class="number">199</div><div class="label">Reviews</div></div>
        <div><div class="number">4.6</div><div class="label">Stars</div></div>
        <div><div class="number">10+</div><div class="label">Years</div></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">Dining</div>
      <h2 class="serif">From Our Kitchen</h2>
      <p>Seasonal menus celebrating the best of Scotland</p>
    </div>
    <div class="cards-grid">
      <div class="card"><div class="card-img">Lunch</div><div class="card-body"><h3>Lunch Menu</h3><p>Two or three courses of seasonal Scottish cooking. Perfect after a morning walk in the Trossachs.</p><div class="price">From &pound;18 / 2 courses</div></div></div>
      <div class="card"><div class="card-img">Dinner</div><div class="card-body"><h3>Evening Menu</h3><p>Our signature experience. Five courses of creative Scottish cuisine with optional wine pairing.</p><div class="price">From &pound;45 / 5 courses</div></div></div>
      <div class="card"><div class="card-img">Stay</div><div class="card-body"><h3>Dinner, Bed &amp; Breakfast</h3><p>The complete Callander Meadows experience. Dine, rest and wake to a full Scottish breakfast.</p><div class="price">From &pound;160 / couple</div></div></div>
    </div>
  </div>
</section>

<section class="testimonials">
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">Reviews</div>
      <h2 class="serif">What Our Guests Say</h2>
    </div>
    <div class="testimonial-grid">
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"An absolute gem. The tasting menu was outstanding and the service was impeccable."</p><div class="author">Google Review</div></div>
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Best meal we've had in Scotland. Worth the drive from Glasgow, easily."</p><div class="author">TripAdvisor</div></div>
      <div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Charming rooms and the breakfast alone is worth staying for. A real hidden gem."</p><div class="author">Google Review</div></div>
    </div>
  </div>
</section>

<section class="cta-banner">
  <h2 class="serif">Experience Callander Meadows</h2>
  <p>Reserve your table or book a stay in our Georgian townhouse.</p>
  <a href="#" class="btn-primary">Book Now &#8594;</a>
</section>

<footer><div class="inner">
  <div><div class="brand serif">Callander Meadows</div><p>Restaurant &amp; Rooms in the heart of Callander, gateway to the Trossachs.</p></div>
  <div><h4>Dining</h4><a href="#">Lunch Menu</a><br><a href="#">Evening Menu</a><br><a href="#">Wine List</a></div>
  <div><h4>Stay</h4><a href="#">Rooms</a><br><a href="#">DB&amp;B Packages</a><br><a href="#">Gift Vouchers</a></div>
  <div><h4>Contact</h4><p>Main Street, Callander</p><p>mail@callandermeadows.co.uk</p><p>01877 381467</p></div>
</div><div class="bottom">Design concept by RAGA Marketing &mdash; ragamarketing.com</div></footer>"""
    },
    {
        "slug": "ochil-arms",
        "name": "The Ochil Arms",
        "tagline": "The Inn at Dollar",
        "primary": "#2e4028",
        "primary_dark": "#1a2818",
        "accent": "#c5a55a",
        "bg": "#f9f8f5",
        "bg_alt": "#f0ede6",
        "text": "#1a2818",
        "text_light": "#5a6a50",
        "hero_gradient": "#3a5530",
        "body": """
<nav><div class="inner">
  <div class="logo serif">The <span>Ochil Arms</span></div>
  <ul><li><a href="#">Home</a></li><li><a href="#">Menu</a></li><li><a href="#">Rooms</a></li><li><a href="#">Events</a></li><li><a href="#">Contact</a></li></ul>
  <a href="#" class="cta-btn">Book Now</a>
</div></nav>

<section class="hero">
  <div class="hero-content">
    <div class="hero-badge">Dollar, Clackmannanshire</div>
    <h1 class="serif">A proper <em>Scottish</em> inn</h1>
    <p>Great food, real ales and a warm welcome in the shadow of the Ochil Hills. Your home from home in Dollar.</p>
    <div class="hero-buttons">
      <a href="#" class="btn-primary">Book a Table &#8594;</a>
      <a href="#" class="btn-secondary">See Our Menu</a>
    </div>
  </div>
</section>

<div class="features-strip"><div class="inner">
  <div class="feature-item"><div class="icon">&#127860;</div><h4>Hearty Food</h4><p>Proper pub grub done right</p></div>
  <div class="feature-item"><div class="icon">&#127866;</div><h4>Real Ales</h4><p>Scottish craft &amp; cask ales</p></div>
  <div class="feature-item"><div class="icon">&#127968;</div><h4>Cosy Rooms</h4><p>Stay in the heart of Dollar</p></div>
  <div class="feature-item"><div class="icon">&#9968;</div><h4>Ochil Hills</h4><p>Perfect base for hillwalking</p></div>
</div></div>

<section class="about-section">
  <div class="section-inner about-grid">
    <div class="about-image">"Where the Ochil Hills meet proper Scottish hospitality"</div>
    <div class="about-text">
      <h2 class="serif">Welcome to Dollar</h2>
      <p>The Ochil Arms sits at the heart of Dollar, one of Clackmannanshire's most beautiful villages. Whether you're here for a pint after a walk in the Ochils, a family meal, or a cosy overnight stay, we've got you covered.</p>
      <p>Our kitchen serves honest, hearty Scottish food using local suppliers. No pretensions, just great cooking.</p>
      <div class="highlight">
        <div><div class="number">5.0</div><div class="label">Star Rating</div></div>
        <div><div class="number">7</div><div class="label">Days a Week</div></div>
        <div><div class="number">&#9825;</div><div class="label">Dog Friendly</div></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">Food &amp; Drink</div>
      <h2 class="serif">From Our Kitchen</h2>
    </div>
    <div class="cards-grid">
      <div class="card"><div class="card-img">Pub Classics</div><div class="card-body"><h3>Pub Classics</h3><p>Fish &amp; chips, steak pie, burgers &mdash; done properly with fresh ingredients and generous portions.</p></div></div>
      <div class="card"><div class="card-img">Sunday Roast</div><div class="card-body"><h3>Sunday Roast</h3><p>A Dollar tradition. Slow-roasted meats, crispy roasties and all the trimmings. Booking advised.</p></div></div>
      <div class="card"><div class="card-img">Ale Trail</div><div class="card-body"><h3>Real Ales &amp; Whisky</h3><p>Rotating Scottish guest ales, premium gins and a whisky selection that does Scotland proud.</p></div></div>
    </div>
  </div>
</section>

<section class="cta-banner">
  <h2 class="serif">Your table is waiting in Dollar</h2>
  <p>Book online or give us a call. Walk-ins always welcome.</p>
  <a href="#" class="btn-primary">Book a Table &#8594;</a>
</section>

<footer><div class="inner">
  <div><div class="brand serif">The Ochil Arms</div><p>A proper Scottish inn in the heart of Dollar, Clackmannanshire.</p></div>
  <div><h4>Menu</h4><a href="#">Food</a><br><a href="#">Drinks</a><br><a href="#">Sunday Roast</a></div>
  <div><h4>Stay</h4><a href="#">Rooms</a><br><a href="#">Book Online</a></div>
  <div><h4>Contact</h4><p>Dollar, Clackmannanshire</p><p>info@theinnatdollar.com</p><p>01259 764842</p></div>
</div><div class="bottom">Design concept by RAGA Marketing &mdash; ragamarketing.com</div></footer>"""
    },
    {
        "slug": "mill-cafe",
        "name": "The Mill Cafe",
        "tagline": "Coffee &amp; Kitchen &mdash; Tillicoultry",
        "primary": "#5a4a3a",
        "primary_dark": "#342a20",
        "accent": "#c49a6c",
        "bg": "#faf8f5",
        "bg_alt": "#f2ece4",
        "text": "#2a2018",
        "text_light": "#7a6a58",
        "hero_gradient": "#6a5a48",
        "body": """
<nav><div class="inner">
  <div class="logo serif">The <span>Mill</span> Cafe</div>
  <ul><li><a href="#">Home</a></li><li><a href="#">Menu</a></li><li><a href="#">About</a></li><li><a href="#">Find Us</a></li></ul>
  <a href="#" class="cta-btn">Visit Us</a>
</div></nav>

<section class="hero">
  <div class="hero-content">
    <div class="hero-badge">Tillicoultry</div>
    <h1 class="serif">Great coffee, <em>great food</em></h1>
    <p>A welcoming cafe in the heart of Tillicoultry. Fresh-baked treats, hearty lunches and the best coffee in the Hillfoots.</p>
    <div class="hero-buttons">
      <a href="#" class="btn-primary">See Our Menu &#8594;</a>
      <a href="#" class="btn-secondary">Find Us</a>
    </div>
  </div>
</section>

<div class="features-strip"><div class="inner">
  <div class="feature-item"><div class="icon">&#9749;</div><h4>Speciality Coffee</h4><p>Freshly roasted, expertly brewed</p></div>
  <div class="feature-item"><div class="icon">&#11088;</div><h4>4.1 Stars</h4><p>281 reviews on Google</p></div>
  <div class="feature-item"><div class="icon">&#127856;</div><h4>Fresh Baking</h4><p>Homemade cakes &amp; pastries daily</p></div>
  <div class="feature-item"><div class="icon">&#127869;</div><h4>Hearty Lunches</h4><p>Soups, sandwiches &amp; hot dishes</p></div>
</div></div>

<section class="about-section">
  <div class="section-inner about-grid">
    <div class="about-image">"Where Tillicoultry comes for great food and a warm welcome"</div>
    <div class="about-text">
      <h2 class="serif">More Than Just Coffee</h2>
      <p>The Mill Cafe is Tillicoultry's go-to spot for a proper coffee, a homemade lunch, or a slice of something sweet. We're proud to be part of the Hillfoots community.</p>
      <p>Everything is made fresh, from our soups to our cakes. Pop in for a takeaway or settle in for a catch-up with friends.</p>
      <div class="highlight">
        <div><div class="number">281</div><div class="label">Reviews</div></div>
        <div><div class="number">7</div><div class="label">Days Open</div></div>
        <div><div class="number">&#9825;</div><div class="label">Family Friendly</div></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">Our Menu</div>
      <h2 class="serif">Fresh Every Day</h2>
    </div>
    <div class="cards-grid">
      <div class="card"><div class="card-img">Breakfast</div><div class="card-body"><h3>Breakfast &amp; Brunch</h3><p>Start your day right with a full Scottish, eggs benny, or a warm bacon roll with fresh coffee.</p></div></div>
      <div class="card"><div class="card-img">Lunch</div><div class="card-body"><h3>Lunch</h3><p>Homemade soups, toasties, salads and daily specials. Something for everyone.</p></div></div>
      <div class="card"><div class="card-img">Cakes</div><div class="card-body"><h3>Cakes &amp; Bakes</h3><p>All baked in-house. Scones, traybakes, celebration cakes and seasonal specials.</p></div></div>
    </div>
  </div>
</section>

<section class="cta-banner">
  <h2 class="serif">Come say hello</h2>
  <p>We're right in the heart of Tillicoultry. No booking needed, just pop in.</p>
  <a href="#" class="btn-primary">Get Directions &#8594;</a>
</section>

<footer><div class="inner">
  <div><div class="brand serif">The Mill Cafe</div><p>Great coffee, fresh food and warm welcomes in Tillicoultry.</p></div>
  <div><h4>Menu</h4><a href="#">Breakfast</a><br><a href="#">Lunch</a><br><a href="#">Cakes</a></div>
  <div><h4>Info</h4><a href="#">Opening Hours</a><br><a href="#">Find Us</a></div>
  <div><h4>Contact</h4><p>Tillicoultry</p><p>millcafe@sterlingfurniture.co.uk</p><p>01259 755191</p></div>
</div><div class="bottom">Design concept by RAGA Marketing &mdash; ragamarketing.com</div></footer>"""
    },
]

output_dir = os.path.dirname(__file__)
for biz in businesses:
    html = template
    html = html.replace('{{BUSINESS_NAME}}', biz['name'])
    html = html.replace('{{TAGLINE}}', biz['tagline'])
    html = html.replace('{{PRIMARY_COLOR}}', biz['primary'])
    html = html.replace('{{PRIMARY_DARK}}', biz['primary_dark'])
    html = html.replace('{{ACCENT_COLOR}}', biz['accent'])
    html = html.replace('{{BG_COLOR}}', biz['bg'])
    html = html.replace('{{BG_ALT}}', biz['bg_alt'])
    html = html.replace('{{TEXT_COLOR}}', biz['text'])
    html = html.replace('{{TEXT_LIGHT}}', biz['text_light'])
    html = html.replace('{{HERO_GRADIENT_END}}', biz['hero_gradient'])
    html = html.replace('{{BODY_CONTENT}}', biz['body'])

    filepath = os.path.join(output_dir, f"{biz['slug']}.html")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created: {biz['slug']}.html")

print(f"\nAll {len(businesses)} mockups generated!")
