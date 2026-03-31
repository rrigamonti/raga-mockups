import os

TEMPLATE_CSS = open("template.html", "r", encoding="utf-8").read()
# Extract just the CSS part (lines 1-121)
css_lines = TEMPLATE_CSS.split("\n")
css_end = css_lines.index("</style>") + 1
CSS_BLOCK = "\n".join(css_lines[9:css_end])  # Just the style rules

businesses = [
    {
        "slug": "the-croft-and-creel",
        "name": "The Croft and Creel",
        "town": "Falkirk",
        "category": "Restaurant",
        "primary": "#1a3a4a",
        "primary_dark": "#0f2530",
        "accent": "#e8a838",
        "bg": "#faf9f6",
        "bg_alt": "#f0ede7",
        "text": "#1a2a30",
        "text_light": "#5a6a70",
        "hero_end": "#2a5a6a",
        "tagline": "Scottish Seafood &amp; Grill",
        "hero_title": "Fresh Scottish Seafood &amp; <em>Fine Dining</em> in Falkirk",
        "hero_desc": "Locally sourced seafood and premium cuts, served in a warm and inviting setting in the heart of Falkirk.",
        "nav_items": "Home|Menu|Wine List|Private Dining|Contact",
        "cta": "Book a Table",
        "features": [
            ("&#127843;", "Fresh Seafood", "Locally sourced daily"),
            ("&#11088;", "Top Rated", "Exceptional reviews"),
            ("&#127863;", "Fine Wines", "Curated wine list"),
            ("&#127860;", "Private Dining", "Events and celebrations"),
        ],
        "about_quote": "\"Where Scottish land meets sea on every plate\"",
        "about_title": "A Taste of Scotland",
        "about_p1": "The Croft and Creel brings the finest Scottish seafood and grill to Falkirk. Our kitchen champions local fishermen and farmers, delivering dishes that celebrate the best of what Scotland has to offer.",
        "about_p2": "Whether it is a relaxed lunch or a special evening out, our warm hospitality and thoughtfully crafted menu make every visit memorable.",
        "cards_overline": "Our Menu",
        "cards_title": "From Sea &amp; Land",
        "cards_desc": "Fresh Scottish produce, expertly prepared",
        "cards": [
            ("Seafood Platter", "A selection of the finest Scottish shellfish and fish, beautifully presented with seasonal accompaniments."),
            ("Grill Menu", "Premium Scottish cuts cooked over charcoal. From ribeye to fillet, every steak is a celebration."),
            ("Sunday Lunch", "A Croft and Creel tradition. Three courses of comfort with all the trimmings."),
        ],
        "testimonials": [
            ("\"Absolutely stunning seafood. Best we have had in central Scotland.\"", "Google Review"),
            ("\"The atmosphere is wonderful and the service impeccable. A real gem in Falkirk.\"", "Google Review"),
            ("\"We keep coming back for the grill menu. Never disappoints.\"", "Google Review"),
        ],
        "cta_title": "Reserve your table",
        "cta_desc": "Book online for lunch, dinner, or a private dining experience in Falkirk.",
        "footer_desc": "Scottish Seafood &amp; Grill in Falkirk.",
        "footer_menu": "Lunch|Dinner|Seafood|Wine List",
        "footer_col2_title": "Visit",
        "footer_col2": "Reservations|Private Dining|Gift Vouchers",
        "footer_address": "Falkirk",
        "footer_phone": "01324 635843",
    },
    {
        "slug": "house-of-olives",
        "name": "House of Olives",
        "town": "Falkirk",
        "category": "Cafe",
        "primary": "#5a7a2a",
        "primary_dark": "#3a5a1a",
        "accent": "#e8c83a",
        "bg": "#fafaf5",
        "bg_alt": "#f0f0e8",
        "text": "#2a3a1a",
        "text_light": "#5a6a4a",
        "hero_end": "#7a9a4a",
        "tagline": "Mediterranean Cafe",
        "hero_title": "Fresh Mediterranean <em>Flavours</em> in Falkirk",
        "hero_desc": "Authentic Mediterranean cuisine made with love. Fresh olives, vibrant salads and homemade dishes to brighten your day.",
        "nav_items": "Home|Menu|About|Gallery|Contact",
        "cta": "View Menu",
        "features": [
            ("&#127813;", "Fresh Ingredients", "Mediterranean produce daily"),
            ("&#11088;", "4.9 Stars", "51 reviews on Google"),
            ("&#9749;", "Great Coffee", "Specialty brews"),
            ("&#127838;", "Homemade", "Everything made fresh"),
        ],
        "about_quote": "\"A little taste of the Mediterranean in Falkirk\"",
        "about_title": "Our Story",
        "about_p1": "House of Olives brings the warmth and flavour of Mediterranean cuisine to Falkirk. Every dish is made with passion, using the freshest ingredients and traditional recipes.",
        "about_p2": "From hearty breakfasts to vibrant lunch plates, we offer a dining experience that transports you straight to the sun-soaked shores of the Med.",
        "cards_overline": "Our Menu",
        "cards_title": "Mediterranean Delights",
        "cards_desc": "Fresh, vibrant and full of flavour",
        "cards": [
            ("Breakfast", "Start your day with our Mediterranean-inspired breakfast. Fresh bread, eggs, olives and more."),
            ("Lunch Plates", "Colourful salads, wraps and meze boards. Light, fresh and packed with flavour."),
            ("Sweet Treats", "Homemade baklava, pastries and cakes paired with specialty coffee."),
        ],
        "testimonials": [
            ("\"Delicious food, lovely atmosphere and helpful staff.\"", "Google Review"),
            ("\"Best Mediterranean food in Falkirk, hands down.\"", "Google Review"),
            ("\"Everything tastes homemade and fresh. Love this place.\"", "Google Review"),
        ],
        "cta_title": "Visit us today",
        "cta_desc": "Pop in for breakfast, lunch or a coffee in the heart of Falkirk.",
        "footer_desc": "Mediterranean Cafe in Falkirk.",
        "footer_menu": "Breakfast|Lunch|Drinks|Desserts",
        "footer_col2_title": "Info",
        "footer_col2": "About Us|Gallery|Catering",
        "footer_address": "30 Cow Wynd, Falkirk",
        "footer_phone": "01324 868871",
    },
    {
        "slug": "the-coppertop",
        "name": "The Coppertop",
        "town": "Falkirk",
        "category": "Restaurant",
        "primary": "#8a4a2a",
        "primary_dark": "#5a3018",
        "accent": "#d4943a",
        "bg": "#faf8f5",
        "bg_alt": "#f2ede6",
        "text": "#3a2a1a",
        "text_light": "#6a5a4a",
        "hero_end": "#a06a3a",
        "tagline": "Restaurant &amp; Bar",
        "hero_title": "Dine &amp; Drink at <em>The Coppertop</em>",
        "hero_desc": "A welcoming restaurant and bar in the heart of Falkirk. Great food, craft drinks and a warm atmosphere.",
        "nav_items": "Home|Food Menu|Drinks|Events|Contact",
        "cta": "Book Now",
        "features": [
            ("&#127860;", "Fresh Food", "Seasonal menus daily"),
            ("&#127867;", "Craft Drinks", "Cocktails, wine &amp; beer"),
            ("&#127926;", "Live Events", "Music &amp; entertainment"),
            ("&#11088;", "Highly Rated", "Loved by locals"),
        ],
        "about_quote": "\"Where copper warmth meets Falkirk charm\"",
        "about_title": "Welcome to The Coppertop",
        "about_p1": "The Coppertop is Falkirk's go-to spot for great food and craft drinks. Our menu celebrates Scottish produce with a modern twist, while our bar serves up creative cocktails and local ales.",
        "about_p2": "Whether you are catching up with friends or celebrating a special occasion, our warm copper-toned interior and friendly team make every visit special.",
        "cards_overline": "Our Menu",
        "cards_title": "Food &amp; Drink",
        "cards_desc": "Something for every taste",
        "cards": [
            ("Starters &amp; Sharing", "Perfect plates to share with friends. From loaded nachos to Scottish charcuterie."),
            ("Mains", "Hearty dishes from gourmet burgers to pan-seared fish. All made with local ingredients."),
            ("Cocktails", "Our bartenders craft signature cocktails using premium spirits and fresh ingredients."),
        ],
        "testimonials": [
            ("\"Great food, brilliant cocktails and lovely atmosphere. Our new favourite spot.\"", "Google Review"),
            ("\"The burger here is the best in Falkirk. Will definitely be back.\"", "Google Review"),
            ("\"Perfect for a night out. The staff are so friendly and welcoming.\"", "Google Review"),
        ],
        "cta_title": "Your table awaits",
        "cta_desc": "Book online for lunch, dinner or drinks in Falkirk.",
        "footer_desc": "Restaurant &amp; Bar in Falkirk.",
        "footer_menu": "Food|Drinks|Cocktails|Desserts",
        "footer_col2_title": "Events",
        "footer_col2": "Live Music|Private Hire|Functions",
        "footer_address": "Falkirk",
        "footer_phone": "01324 622667",
    },
    {
        "slug": "black-bull-polmont",
        "name": "Black Bull Polmont",
        "town": "Polmont",
        "category": "Pub",
        "primary": "#2a2a2a",
        "primary_dark": "#1a1a1a",
        "accent": "#c8963a",
        "bg": "#faf9f6",
        "bg_alt": "#f0ede8",
        "text": "#2a2a2a",
        "text_light": "#5a5a5a",
        "hero_end": "#3a3a3a",
        "tagline": "Traditional Scottish Pub",
        "hero_title": "A True <em>Scottish Pub</em> in Polmont",
        "hero_desc": "Real ales, hearty pub grub and a warm welcome. The Black Bull has been the heart of Polmont for generations.",
        "nav_items": "Home|Food|Drinks|Events|Contact",
        "cta": "View Menu",
        "features": [
            ("&#127866;", "Real Ales", "Cask ales on tap"),
            ("&#127860;", "Pub Grub", "Hearty Scottish classics"),
            ("&#127941;", "Live Sport", "Big screen action"),
            ("&#11088;", "Local Favourite", "Loved by the community"),
        ],
        "about_quote": "\"The heart and soul of Polmont\"",
        "about_title": "Your Local",
        "about_p1": "The Black Bull is more than a pub. It is the beating heart of Polmont, where friends meet, families gather and great memories are made over a pint and a plate of comfort food.",
        "about_p2": "Our kitchen serves up honest Scottish pub classics, from fish and chips to steak pie, all made with quality local ingredients.",
        "cards_overline": "On the Menu",
        "cards_title": "Pub Classics",
        "cards_desc": "Hearty food done right",
        "cards": [
            ("Fish &amp; Chips", "Beer-battered haddock with chunky chips, mushy peas and homemade tartare sauce."),
            ("Steak Pie", "Slow-cooked Scottish beef in rich gravy, topped with golden puff pastry."),
            ("Sunday Roast", "A proper Sunday roast with all the trimmings. Booking recommended."),
        ],
        "testimonials": [
            ("\"Best pub grub in the area. The steak pie is incredible.\"", "Google Review"),
            ("\"Friendly staff, great atmosphere and proper real ales. What more could you want?\"", "Google Review"),
            ("\"Our go-to Sunday lunch spot. Never lets us down.\"", "Google Review"),
        ],
        "cta_title": "Pop in for a pint",
        "cta_desc": "Food served daily. Live sport on the big screen every weekend.",
        "footer_desc": "Traditional Scottish Pub in Polmont.",
        "footer_menu": "Food|Drinks|Real Ales|Whisky",
        "footer_col2_title": "What's On",
        "footer_col2": "Live Sport|Quiz Night|Events",
        "footer_address": "Polmont, Falkirk",
        "footer_phone": "01324 716610",
    },
    {
        "slug": "the-riverside-dunblane",
        "name": "The Riverside",
        "town": "Dunblane",
        "category": "Pub",
        "primary": "#2a4a3a",
        "primary_dark": "#1a3028",
        "accent": "#d4a848",
        "bg": "#f8faf8",
        "bg_alt": "#eef2ee",
        "text": "#1a2a20",
        "text_light": "#4a5a4a",
        "hero_end": "#3a6a4a",
        "tagline": "Bar &amp; Restaurant by the Allan Water",
        "hero_title": "Eat, Drink &amp; <em>Relax</em> by the River",
        "hero_desc": "A stunning riverside setting in the heart of Dunblane. Great food, local ales and a warm Scottish welcome.",
        "nav_items": "Home|Menu|Drinks|Beer Garden|Contact",
        "cta": "Book a Table",
        "features": [
            ("&#127860;", "Fresh Menu", "Seasonal Scottish dishes"),
            ("&#11088;", "Highly Rated", "Loved on Google"),
            ("&#127795;", "Beer Garden", "Riverside outdoor seating"),
            ("&#127866;", "Local Ales", "Scottish craft beers"),
        ],
        "about_quote": "\"Where great food meets the gentle flow of the Allan Water\"",
        "about_title": "By the Water",
        "about_p1": "The Riverside sits in one of Dunblane's most beautiful spots, right on the banks of the Allan Water. Our kitchen serves up seasonal Scottish dishes while our bar pours local craft ales and fine wines.",
        "about_p2": "In summer, our riverside beer garden is the perfect spot to unwind. In winter, cosy up by the fire with a dram and hearty comfort food.",
        "cards_overline": "Our Menu",
        "cards_title": "From Our Kitchen",
        "cards_desc": "Fresh, seasonal and proudly Scottish",
        "cards": [
            ("Lunch", "Light bites, soups and fresh salads. The perfect riverside lunch in Dunblane."),
            ("Dinner", "Evening dishes that celebrate the best of Scottish produce. Booking recommended."),
            ("Beer Garden", "Al fresco dining by the Allan Water. Scottish sunshine and good vibes."),
        ],
        "testimonials": [
            ("\"What a setting! Lovely food and the beer garden is stunning in summer.\"", "Google Review"),
            ("\"Best pub in Dunblane. Great food, great atmosphere, great staff.\"", "Google Review"),
            ("\"The riverside location makes it so special. Food is excellent too.\"", "Google Review"),
        ],
        "cta_title": "Your riverside table awaits",
        "cta_desc": "Book online for lunch, dinner or drinks in Dunblane.",
        "footer_desc": "Bar &amp; Restaurant in Dunblane.",
        "footer_menu": "Lunch|Dinner|Drinks|Desserts",
        "footer_col2_title": "Visit",
        "footer_col2": "Beer Garden|Private Hire|Functions",
        "footer_address": "Dunblane, Perthshire",
        "footer_phone": "01786 823318",
    },
    {
        "slug": "beech-tree-cafe",
        "name": "Beech Tree Cafe",
        "town": "Dunblane",
        "category": "Cafe",
        "primary": "#6a4a2a",
        "primary_dark": "#4a3018",
        "accent": "#d4a44a",
        "bg": "#faf8f4",
        "bg_alt": "#f2ede4",
        "text": "#3a2a18",
        "text_light": "#6a5a48",
        "hero_end": "#8a6a3a",
        "tagline": "Coffee &amp; Homemade Food",
        "hero_title": "Coffee, Cake &amp; <em>Community</em> in Dunblane",
        "hero_desc": "A cosy neighbourhood cafe serving specialty coffee, homemade cakes and freshly prepared food. Your happy place in Dunblane.",
        "nav_items": "Home|Menu|Coffee|Cakes|Contact",
        "cta": "View Menu",
        "features": [
            ("&#9749;", "Specialty Coffee", "Expertly brewed"),
            ("&#127856;", "Homemade Cakes", "Baked fresh daily"),
            ("&#127860;", "Breakfast &amp; Lunch", "Made from scratch"),
            ("&#11088;", "5 Star Reviews", "Loved by locals"),
        ],
        "about_quote": "\"Your cosy corner in Dunblane\"",
        "about_title": "Our Wee Cafe",
        "about_p1": "The Beech Tree Cafe is Dunblane's favourite spot for great coffee and homemade food. Everything is made from scratch using quality local ingredients, from our morning pastries to our lunchtime specials.",
        "about_p2": "Pop in for a flat white and a slice of cake, or settle in for a leisurely brunch. We are your home from home in Dunblane.",
        "cards_overline": "What We Do",
        "cards_title": "Coffee, Food &amp; Cake",
        "cards_desc": "All homemade, all delicious",
        "cards": [
            ("Breakfast", "Start your morning right with our full Scottish or lighter options. Served until noon."),
            ("Lunch", "Soups, sandwiches, salads and daily specials. All freshly made."),
            ("Cakes &amp; Coffee", "Homemade cakes, scones and traybakes paired with specialty coffee."),
        ],
        "testimonials": [
            ("\"Best coffee in Dunblane. The cakes are incredible too.\"", "Google Review"),
            ("\"Such a lovely wee cafe. Everything is homemade and delicious.\"", "Google Review"),
            ("\"Our favourite brunch spot. Friendly staff and great food.\"", "Google Review"),
        ],
        "cta_title": "Pop in for a coffee",
        "cta_desc": "Open daily for breakfast, lunch and the best cake in Dunblane.",
        "footer_desc": "Coffee &amp; Homemade Food in Dunblane.",
        "footer_menu": "Breakfast|Lunch|Coffee|Cakes",
        "footer_col2_title": "Info",
        "footer_col2": "About Us|Catering|Gift Cards",
        "footer_address": "Dunblane, Perthshire",
        "footer_phone": "01786 823451",
    },
    {
        "slug": "dunmar-house",
        "name": "Dunmar House Hotel",
        "town": "Alloa",
        "category": "Hotel",
        "primary": "#3a2a4a",
        "primary_dark": "#28183a",
        "accent": "#c8a05a",
        "bg": "#faf8fc",
        "bg_alt": "#f0edf4",
        "text": "#2a1a3a",
        "text_light": "#5a4a6a",
        "hero_end": "#5a3a6a",
        "tagline": "Boutique Hotel &amp; Events",
        "hero_title": "Elegance &amp; <em>Charm</em> in the Heart of Alloa",
        "hero_desc": "A beautiful boutique hotel offering stylish accommodation, exceptional dining and stunning event spaces in Clackmannanshire.",
        "nav_items": "Home|Rooms|Dining|Weddings|Events|Contact",
        "cta": "Book a Room",
        "features": [
            ("&#127968;", "Boutique Rooms", "Elegantly appointed"),
            ("&#127860;", "Fine Dining", "Scottish cuisine"),
            ("&#128141;", "Weddings", "Your perfect day"),
            ("&#11088;", "Highly Rated", "Exceptional reviews"),
        ],
        "about_quote": "\"Where timeless elegance meets modern comfort\"",
        "about_title": "A Clackmannanshire Gem",
        "about_p1": "Dunmar House Hotel is a beautifully restored boutique hotel in Alloa, offering a perfect blend of historic charm and modern luxury. Our elegant rooms, fine dining restaurant and stunning grounds make it the ideal destination.",
        "about_p2": "Whether you are planning a romantic getaway, a special celebration or a memorable wedding, Dunmar House provides an unforgettable setting.",
        "cards_overline": "Experience",
        "cards_title": "Stay, Dine &amp; Celebrate",
        "cards_desc": "Something special for every occasion",
        "cards": [
            ("Accommodation", "Beautifully appointed rooms combining period features with modern comforts."),
            ("Dining", "Our restaurant serves seasonal Scottish cuisine in an elegant setting."),
            ("Weddings &amp; Events", "Create lasting memories in our stunning grounds and function rooms."),
        ],
        "testimonials": [
            ("\"Absolutely beautiful hotel. The rooms are gorgeous and the staff are wonderful.\"", "Google Review"),
            ("\"We had our wedding here and it was perfect. Could not recommend more highly.\"", "Google Review"),
            ("\"The dining experience was exceptional. A hidden gem in Alloa.\"", "Google Review"),
        ],
        "cta_title": "Plan your stay",
        "cta_desc": "Book a room, reserve a table or enquire about weddings and events.",
        "footer_desc": "Boutique Hotel &amp; Events in Alloa.",
        "footer_menu": "Rooms|Dining|Bar|Afternoon Tea",
        "footer_col2_title": "Events",
        "footer_col2": "Weddings|Corporate|Private Dining",
        "footer_address": "Alloa, Clackmannanshire",
        "footer_phone": "01259 214339",
    },
    {
        "slug": "the-royal-oak-alloa",
        "name": "The Royal Oak",
        "town": "Alloa",
        "category": "Pub",
        "primary": "#4a2a1a",
        "primary_dark": "#301810",
        "accent": "#d4943a",
        "bg": "#faf8f5",
        "bg_alt": "#f2ede6",
        "text": "#2a1a10",
        "text_light": "#5a4a3a",
        "hero_end": "#6a4a2a",
        "tagline": "Traditional Pub &amp; Kitchen",
        "hero_title": "Good Food, Great <em>Craic</em> in Alloa",
        "hero_desc": "A proper Scottish pub with hearty food, real ales and a warm community atmosphere. The Royal Oak has been an Alloa institution for generations.",
        "nav_items": "Home|Food|Drinks|Events|Contact",
        "cta": "View Menu",
        "features": [
            ("&#127866;", "Real Ales", "Cask ales on tap"),
            ("&#127860;", "Pub Food", "Hearty Scottish classics"),
            ("&#127926;", "Live Music", "Regular entertainment"),
            ("&#11088;", "Community Hub", "Heart of Alloa"),
        ],
        "about_quote": "\"Alloa's home from home\"",
        "about_title": "A Proper Local",
        "about_p1": "The Royal Oak is the kind of pub every town needs. A place where the welcome is warm, the pints are well-poured and the food is honest and hearty.",
        "about_p2": "From our famous steak pie to our lively quiz nights, there is always a reason to visit. Come for a pint, stay for the craic.",
        "cards_overline": "On the Menu",
        "cards_title": "Pub Favourites",
        "cards_desc": "Honest food, done well",
        "cards": [
            ("Bar Bites", "Perfect with a pint. Loaded fries, wings, and our famous haggis bon bons."),
            ("Mains", "From fish and chips to a 10oz Scottish ribeye. Proper pub portions."),
            ("Sunday Roast", "A Royal Oak tradition. Slow-roasted with all the trimmings."),
        ],
        "testimonials": [
            ("\"The best pub in Alloa. Great food, great beer, great people.\"", "Google Review"),
            ("\"Love the quiz nights here. Such a fun atmosphere.\"", "Google Review"),
            ("\"Steak pie is absolutely top class. We come back every week.\"", "Google Review"),
        ],
        "cta_title": "Pop in for a pint",
        "cta_desc": "Food served daily. Live music and events every weekend.",
        "footer_desc": "Traditional Pub &amp; Kitchen in Alloa.",
        "footer_menu": "Bar Bites|Mains|Drinks|Desserts",
        "footer_col2_title": "What's On",
        "footer_col2": "Live Music|Quiz Night|Events",
        "footer_address": "Alloa, Clackmannanshire",
        "footer_phone": "01259 929587",
    },
    {
        "slug": "cesars-paradise",
        "name": "Cesars Paradise",
        "town": "Grangemouth",
        "category": "Pub",
        "primary": "#1a2a4a",
        "primary_dark": "#101830",
        "accent": "#d4a04a",
        "bg": "#f8f9fc",
        "bg_alt": "#eef0f6",
        "text": "#1a2030",
        "text_light": "#4a5060",
        "hero_end": "#2a3a5a",
        "tagline": "Bar &amp; Entertainment",
        "hero_title": "Your <em>Paradise</em> in Grangemouth",
        "hero_desc": "Great drinks, live entertainment and a buzzing atmosphere. Cesars Paradise is Grangemouth's go-to night out.",
        "nav_items": "Home|Drinks|Events|Gallery|Contact",
        "cta": "See What's On",
        "features": [
            ("&#127867;", "Great Drinks", "Cocktails, pints &amp; spirits"),
            ("&#127926;", "Live Entertainment", "DJs &amp; events"),
            ("&#127941;", "Live Sport", "Big screen action"),
            ("&#11088;", "Top Atmosphere", "Grangemouth's favourite"),
        ],
        "about_quote": "\"Where every night is a great night\"",
        "about_title": "Welcome to Paradise",
        "about_p1": "Cesars Paradise is the beating heart of Grangemouth's nightlife. Whether you are watching the big game, enjoying live entertainment or just having a few drinks with friends, we have got you covered.",
        "about_p2": "Our friendly staff, buzzing atmosphere and great drinks make every visit a good time. Come and find your paradise.",
        "cards_overline": "What's On",
        "cards_title": "Entertainment &amp; Events",
        "cards_desc": "Something happening every week",
        "cards": [
            ("Live Sport", "Every big match on the big screen. The best atmosphere in Grangemouth."),
            ("DJ Nights", "Weekend DJ sets to keep the party going until late."),
            ("Live Music", "Regular live bands and acoustic sessions. Check our events page."),
        ],
        "testimonials": [
            ("\"Best bar in Grangemouth. Great atmosphere and friendly staff.\"", "Google Review"),
            ("\"Love watching the football here. Great pints and a buzzing crowd.\"", "Google Review"),
            ("\"Our go-to place for a night out. Never disappoints.\"", "Google Review"),
        ],
        "cta_title": "Join the party",
        "cta_desc": "Live sport, DJs and events every weekend in Grangemouth.",
        "footer_desc": "Bar &amp; Entertainment in Grangemouth.",
        "footer_menu": "Cocktails|Beers|Spirits|Shots",
        "footer_col2_title": "Events",
        "footer_col2": "Live Sport|DJs|Live Music",
        "footer_address": "Grangemouth",
        "footer_phone": "01324 485100",
    },
    {
        "slug": "cooks-bar-and-kitchen",
        "name": "Cook's Bar and Kitchen",
        "town": "Grangemouth",
        "category": "Restaurant",
        "primary": "#4a3a2a",
        "primary_dark": "#302418",
        "accent": "#c89848",
        "bg": "#faf8f5",
        "bg_alt": "#f2ede6",
        "text": "#2a2018",
        "text_light": "#5a4a3a",
        "hero_end": "#6a5a3a",
        "tagline": "Bar &amp; Kitchen",
        "hero_title": "Fresh Food &amp; <em>Good Times</em> in Grangemouth",
        "hero_desc": "A modern bar and kitchen serving fresh, flavourful food and great drinks in a warm and welcoming setting.",
        "nav_items": "Home|Food Menu|Drinks|Events|Contact",
        "cta": "Book a Table",
        "features": [
            ("&#127860;", "Fresh Food", "Made to order daily"),
            ("&#127867;", "Craft Drinks", "Cocktails &amp; local ales"),
            ("&#11088;", "Highly Rated", "Top reviews"),
            ("&#127926;", "Events", "Private hire available"),
        ],
        "about_quote": "\"Where good food brings people together\"",
        "about_title": "Our Kitchen",
        "about_p1": "Cook's Bar and Kitchen is all about fresh, honest food and a great atmosphere. Our chefs prepare everything from scratch using quality ingredients, creating dishes that are full of flavour.",
        "about_p2": "Whether you are in for a quick lunch, a family dinner or drinks with friends, our modern setting and friendly team make every visit enjoyable.",
        "cards_overline": "Our Menu",
        "cards_title": "From the Kitchen",
        "cards_desc": "Fresh, flavourful and made with care",
        "cards": [
            ("Starters", "From soup of the day to sharing platters. Great ways to start your meal."),
            ("Mains", "Burgers, steaks, pasta and more. Something to satisfy every appetite."),
            ("Desserts", "Homemade puddings and sweet treats to finish on a high."),
        ],
        "testimonials": [
            ("\"Really good food in a nice setting. The burgers are fantastic.\"", "Google Review"),
            ("\"Great place for a family meal. Kids menu is excellent too.\"", "Google Review"),
            ("\"Lovely cocktails and the food is always spot on. Highly recommend.\"", "Google Review"),
        ],
        "cta_title": "Your table is ready",
        "cta_desc": "Book online for lunch, dinner or drinks in Grangemouth.",
        "footer_desc": "Bar &amp; Kitchen in Grangemouth.",
        "footer_menu": "Starters|Mains|Desserts|Kids",
        "footer_col2_title": "Info",
        "footer_col2": "Reservations|Private Hire|Functions",
        "footer_address": "Grangemouth",
        "footer_phone": "01324 877115",
    },
]

# Read template CSS
with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

for biz in businesses:
    # Build the CSS variables
    css = template.replace("{{PRIMARY_COLOR}}", biz["primary"])
    css = css.replace("{{PRIMARY_DARK}}", biz["primary_dark"])
    css = css.replace("{{ACCENT_COLOR}}", biz["accent"])
    css = css.replace("{{BG_COLOR}}", biz["bg"])
    css = css.replace("{{BG_ALT}}", biz["bg_alt"])
    css = css.replace("{{TEXT_COLOR}}", biz["text"])
    css = css.replace("{{TEXT_LIGHT}}", biz["text_light"])
    css = css.replace("{{HERO_GRADIENT_END}}", biz["hero_end"])
    css = css.replace("{{BUSINESS_NAME}}", biz["name"])
    css = css.replace("{{TAGLINE}}", biz["tagline"])

    # Build nav
    nav_links = "".join(f'<li><a href="#">{item}</a></li>' for item in biz["nav_items"].split("|"))

    # Build features
    features_html = ""
    for icon, title, desc in biz["features"]:
        features_html += f'<div class="feature-item"><div class="icon">{icon}</div><h4>{title}</h4><p>{desc}</p></div>\n'

    # Build cards
    cards_html = ""
    for title, desc in biz["cards"]:
        cards_html += f'<div class="card"><div class="card-img">{title}</div><div class="card-body"><h3>{title}</h3><p>{desc}</p></div></div>\n'

    # Build testimonials
    testimonials_html = ""
    for quote, author in biz["testimonials"]:
        testimonials_html += f'<div class="testimonial"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>{quote}</p><div class="author">{author}</div></div>\n'

    # Build footer menu
    footer_menu = "".join(f'<a href="#">{item}</a><br>' for item in biz["footer_menu"].split("|"))
    footer_col2 = "".join(f'<a href="#">{item}</a><br>' for item in biz["footer_col2"].split("|"))

    # Name split for logo
    name_parts = biz["name"].split(" ", 1)
    logo_first = name_parts[0]
    logo_rest = name_parts[1] if len(name_parts) > 1 else ""

    body = f"""
<nav><div class="inner">
  <div class="logo serif">{logo_first} <span>{logo_rest}</span></div>
  <ul>{nav_links}</ul>
  <a href="#" class="cta-btn">{biz["cta"]}</a>
</div></nav>

<section class="hero">
  <div class="hero-content">
    <div class="hero-badge">{biz["town"]}</div>
    <h1 class="serif">{biz["hero_title"]}</h1>
    <p>{biz["hero_desc"]}</p>
    <div class="hero-buttons">
      <a href="#" class="btn-primary">{biz["cta"]} &#8594;</a>
      <a href="#" class="btn-secondary">Learn More</a>
    </div>
  </div>
</section>

<div class="features-strip"><div class="inner">
{features_html}</div></div>

<section class="about-section">
  <div class="section-inner about-grid">
    <div class="about-image">{biz["about_quote"]}</div>
    <div class="about-text">
      <h2 class="serif">{biz["about_title"]}</h2>
      <p>{biz["about_p1"]}</p>
      <p>{biz["about_p2"]}</p>
    </div>
  </div>
</section>

<section>
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">{biz["cards_overline"]}</div>
      <h2 class="serif">{biz["cards_title"]}</h2>
      <p>{biz["cards_desc"]}</p>
    </div>
    <div class="cards-grid">
{cards_html}    </div>
  </div>
</section>

<section class="testimonials">
  <div class="section-inner">
    <div class="section-header">
      <div class="overline">Reviews</div>
      <h2 class="serif">What People Are Saying</h2>
    </div>
    <div class="testimonial-grid">
{testimonials_html}    </div>
  </div>
</section>

<section class="cta-banner">
  <h2 class="serif">{biz["cta_title"]}</h2>
  <p>{biz["cta_desc"]}</p>
  <a href="#" class="btn-primary">{biz["cta"]} &#8594;</a>
</section>

<footer><div class="inner">
  <div><div class="brand serif">{biz["name"]}</div><p>{biz["footer_desc"]}</p></div>
  <div><h4>Menu</h4>{footer_menu}</div>
  <div><h4>{biz["footer_col2_title"]}</h4>{footer_col2}</div>
  <div><h4>Contact</h4><p>{biz["footer_address"]}</p><p>{biz["footer_phone"]}</p></div>
</div><div class="bottom">Design concept by RAGA Marketing &mdash; ragamarketing.com</div></footer>"""

    html = css.replace("{{BODY_CONTENT}}", body)

    filepath = f"{biz['slug']}.html"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: {filepath}")

print(f"\nDone! {len(businesses)} mockups generated.")
