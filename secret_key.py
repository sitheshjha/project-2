#see in this project only this file secret_key.py execute the whole code and output if your 
#working with open api key then use the four files of this project by including open ai key
# but if your doing it manually use only this files and run (streamlit run secret_key.py) in terminal to see the output
import importlib
import random

try:
    st = importlib.import_module("streamlit")
except ImportError:
    raise ImportError(
        "Streamlit is required to run this application. Install it with: pip install streamlit"
    )

# Page config
st.set_page_config(page_title="Restaurant Generator", page_icon="🍽", layout="wide")

restaurant_image_url = "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=1800&q=80"

# Custom styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
    color: white;
}
h1, h2, h3 {
    text-align: center;
}
.card {
    background-color: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
}
.image-card {
    border-radius: 20px;
    overflow: hidden;
    margin: 0 auto 20px;
    width: 100%;
    max-width: 100%;
}
.stButton>button {
    color: #ffffff !important;
    background-color: #ff6f61 !important;
    border: 1px solid rgba(255, 255, 255, 0.6) !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2) !important;
    border-radius: 12px !important;
    padding: 0.7rem 1.2rem !important;
}
.stButton>button:hover {
    background-color: #ff856f !important;
}
.stButton>button:focus {
    outline: 2px solid #ffffff !important;
    outline-offset: 2px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="image-card">
    <img src="{restaurant_image_url}" alt="restaurant ambience" style="width:100%; max-width:100%; height:auto; border-radius:20px; display:block;" />
</div>
""", unsafe_allow_html=True)

# Side navigation
st.sidebar.title("Restaurant Hub")
st.sidebar.markdown("Choose a page and cuisine to generate a restaurant name with menu items.")
page = st.sidebar.radio("Navigate", ["Home", "Generator", "About"])

cuisines = (
    "Indian", "Italian", "Mexican", "American", "Arabic", "Chinese",
    "Japanese", "French", "Thai", "Greek", "Spanish"
)
sidebar_cuisine = st.sidebar.selectbox("Pick a cuisine 🍜", cuisines)

# Data
data = {
    "Indian": {
        "names": [
            "Spice Paradise", "Curry Delight", "Tandoori Treat", "Masala Mansion", "Naan & Nirvana",
            "Saffron Story", "Royal Rasoi", "Samosa Station", "Kebab Court", "Mughal Magic",
            "Biryani Bazaar", "Heritage Haveli", "Curry Carnival", "Chaat Chateau", "Paneer Palace",
            "Madras Melody", "Bombay Bistro", "Delhi Dine", "Garam Ghar", "Mumbai Masala"
        ],
        "menu": [
            "Butter Chicken", "Garlic Naan", "Chicken Biryani", "Paneer Tikka",
            "Aloo Gobi", "Chole Bhature", "Rogan Josh", "Dal Makhani",
            "Tandoori Chicken", "Palak Paneer", "Gulab Jamun", "Samosa",
            "Idli Sambhar", "Dosa", "Fish Curry", "Mutton Korma",
            "Lassi", "Mango Chutney", "Pav Bhaji", "Masala Dosa",
            "Rajma", "Chicken 65", "Navratan Korma", "Jeera Rice",
            "Bhindi Masala", "Malai Kofta", "Kadhi Pakora", "Prawn Masala",
            "Beetroot Raita", "Matar Paneer"
        ]
    },
    "Italian": {
        "names": [
            "Bella Pasta", "Roma Delight", "La Trattoria", "Venice Vibes", "Tuscan Table",
            "Piazza del Gusto", "Mamma Mia Ristorante", "Ciao Bella Bistro", "Dolce Vita Dine",
            "Pasta Piazza", "Vino e Cucina", "Gondola Grill", "Sorrento Sizzle", "Capri Corner",
            "Florence Feast", "Napoli Nook", "Amore al Forno", "Trattoria Toscana", "Basilico Bistro",
            "Pomodoro Palace", "Villa Venezia"
        ],
        "menu": [
            "Margherita Pizza", "Fettuccine Alfredo", "Spaghetti Carbonara", "Lasagna",
            "Penne Arrabbiata", "Risotto ai Funghi", "Bruschetta", "Caprese Salad",
            "Gnocchi al Pesto", "Osso Buco", "Tiramisu", "Panna Cotta",
            "Seafood Linguine", "Calzone", "Prosciutto e Melone", "Polenta",
            "Minestrone", "Saltimbocca", "Melanzane alla Parmigiana", "Ravioli",
            "Focaccia", "Antipasto", "Zuppa Toscana", "Cannoli",
            "Aglio e Olio", "Cacio e Pepe", "Gamberi Fra Diavolo", "Bistecca Fiorentina",
            "Affogato", "Panzanella", "Ciabatta"
        ]
    },
    "Mexican": {
        "names": [
            "El Sabor", "Taco Fiesta", "Casa Mexicana", "Cantina Caliente", "Aztec Avenue",
            "Baja Bites", "Sombrero Grill", "Salsa Street", "La Cocina Viva", "Mariachi Market",
            "Fiesta Fresca", "Nacho Nook", "Tortilla Terrace", "Tequila Tavern", "Plaza Picante",
            "Puebla Palace", "Olé Oasis", "Margarita Mesa", "Chili Charm", "Viva Veracruz",
            "Guacamole Garden", "Rancho Rey"
        ],
        "menu": [
            "Carne Asada", "Fish Tacos", "Chicken Enchiladas", "Chili Con Carne",
            "Guacamole", "Street Tacos", "Quesadillas", "Chilaquiles",
            "Carnitas", "Tamales", "Mole Poblano", "Pozole",
            "Fajitas", "Sopa de Lima", "Elote", "Nachos",
            "Pico de Gallo", "Tostadas", "Burritos", "Huevos Rancheros",
            "Salsa Verde", "Ceviche", "Chile Rellenos", "Camarones al Ajillo",
            "Arroz Mexicano", "Frijoles Charros", "Crema", "Queso Fundido",
            "Plantains", "Mexican Rice"
        ]
    },
    "American": {
        "names": [
            "Burger Hub", "Grill Nation", "BBQ House", "Patriot Plates", "Route 66 Diner",
            "Liberty Lunch", "City Smokehouse", "Stars & Stripes Grill", "Main Street Eats", "Garage Gourmet",
            "Skyline Steakhouse", "Backyard BBQ", "Diner Deluxe", "American Table", "Vintage Grill",
            "The Brat Barn", "Hot Dog Haven", "Cattleman's Catch", "Soul Food Station", "Freedom Fare",
            "Harbor House"
        ],
        "menu": [
            "Cheeseburger", "BBQ Ribs", "Buffalo Wings", "Mac and Cheese",
            "Grilled Steak", "Fried Chicken", "Pulled Pork Sandwich", "Caesar Salad",
            "Club Sandwich", "Cobb Salad", "Cornbread", "Meatloaf",
            "Shrimp Po' Boy", "Clam Chowder", "Bacon Cheeseburger", "Chicken Alfredo",
            "Sliders", "Texas Brisket", "Waffles", "Pancakes",
            "Apple Pie", "Mashed Potatoes", "Coleslaw", "Onion Rings",
            "Hot Dog", "Philly Cheesesteak", "Lobster Roll", "Grilled Salmon",
            "Chili Bowl", "Fried Shrimp", "Caramelized Onion Burger"
        ]
    },
    "Arabic": {
        "names": [
            "Desert Feast", "Arabian Nights", "Falafel House", "Oasis Grill", "Sands & Spices",
            "Casablanca Kitchen", "Sultan's Table", "Mediterranean Mezze", "Bedouin Bites", "Palace of Shawarma",
            "Lebanese Lounge", "Cedar Cafe", "Zaatar & Co.", "Mosaic Meals", "Golden Dune",
            "Spice Souk", "Mint & Pita", "Cairo Corner", "Hummus House", "Saffron Oasis",
            "Marhaba Meals"
        ],
        "menu": [
            "Falafel", "Hummus", "Shawarma", "Kebab",
            "Tabbouleh", "Fattoush", "Baba Ganoush", "Mansaf",
            "Kibbeh", "Stuffed Grape Leaves", "Lamb Kofta", "Muhammara",
            "Labneh", "Mujaddara", "Stuffed Eggplant", "Chicken Kabsa",
            "Baklava", "Kunafa", "Pita Bread", "Tahini Sauce",
            "Spiced Rice", "Foul Medames", "Maaloubeh", "Sujuk",
            "Shish Taouk", "Arabic Coffee", "Zaatar Manakeesh", "Harira",
            "Sambousek", "Lamb Shawarma", "Date Milkshake"
        ]
    },
    "Chinese": {
        "names": [
            "Dragon Bowl", "Wok Master", "Golden Panda", "Imperial Wok", "Lotus Lantern",
            "Dynasty Dine", "Silk Road Kitchen", "Red Dragon House", "Panda Pavilion", "Beijing Bistro",
            "Mandarin Magic", "Shanghai Spice", "Great Wall Grill", "Forbidden Feast", "Lucky Lotus",
            "Jade Garden", "Rice & Noodle", "Oriental Orchard", "Dragonfly Delight", "Tea House Tavern",
            "Golden Dynasty"
        ],
        "menu": [
            "Noodles", "Fried Rice", "Dumplings", "Spring Rolls",
            "Kung Pao Chicken", "Sweet and Sour Pork", "Mapo Tofu", "Peking Duck",
            "Chow Mein", "Hot and Sour Soup", "Szechuan Beef", "Char Siu",
            "Ma Po Eggplant", "Sesame Chicken", "Wonton Soup", "Egg Foo Young",
            "General Tso's Chicken", "Dim Sum", "Beef and Broccoli", "Moo Shu Pork",
            "Steamed Buns", "Crispy Duck", "Sichuan Hotpot", "Scallion Pancakes",
            "Honey Walnut Shrimp", "Salt and Pepper Squid", "Cantonese Fish", "Braised Pork Belly",
            "Prawn Toast", "Lo Mein", "Spring Chicken"
        ]
    },
    "Japanese": {
        "names": [
            "Sakura Bistro", "Tokyo Table", "Ninja Noodles", "Kyoto Kitchen", "Shogun Sushi",
            "Samurai Sushi", "Zen Garden", "Bento Boulevard", "Osaka Oven", "Wasabi Way",
            "Harajuku House", "Mount Fuji Cafe", "Edo Eats", "Kawaii Kitchen", "Yokohama Yakitori",
            "Miso Market", "Origami Dine", "Ukiyo Grill", "Nikko Nook", "Cherry Blossom Cafe"
        ],
        "menu": [
            "Sushi Platter", "Ramen", "Tempura", "Teriyaki Chicken",
            "Udon Noodles", "Sashimi", "Katsu Curry", "Okonomiyaki",
            "Gyoza", "Miso Soup", "Donburi", "Yakitori",
            "Seaweed Salad", "Matcha Ice Cream", "Takoyaki", "Unagi Don",
            "Tonkatsu", "Chirashi", "Oyakodon", "Green Tea Mochi",
            "Shabu Shabu", "Soba", "Natto", "Pocky Dessert",
            "Kaiseki Set", "Eel Sushi", "Japanese Curry", "Rice Balls",
            "Beef Tataki", "Agedashi Tofu", "Amazake"
        ]
    },
    "French": {
        "names": [
            "Parisian Plate", "Le Bistro", "Café de la Rue", "Maison du Fromage", "Chateau Cuisine",
            "Belle Époque", "Baguette & Brie", "Rue Royale", "Lyonnais Lounge", "Montmartre Meals",
            "Provence Pantry", "Nice Nosh", "Versailles View", "Gourmet Garçon", "Petit Paris",
            "Brasserie Belle", "Lavender Bistro", "Côte d'Azur Cafe", "Soleil Supper", "Le Gourmet"
        ],
        "menu": [
            "Croissant", "Coq au Vin", "Boeuf Bourguignon", "Ratatouille",
            "Quiche Lorraine", "French Onion Soup", "Escargots", "Duck Confit",
            "Crepes", "Bouillabaisse", "Steak Frites", "Niçoise Salad",
            "Mousse au Chocolat", "Tarte Tatin", "Crème Brûlée", "Pain au Chocolat",
            "Cassoulet", "Soufflé", "Croque Monsieur", "Cheese Platter",
            "Madeleines", "Sole Meunière", "Pissaladière", "Magret de Canard",
            "Rillettes", "Gateau Basque", "Profiteroles", "Salon de Thé",
            "Macarons", "Galette"
        ]
    },
    "Thai": {
        "names": [
            "Bangkok Bites", "Siam Spice", "Thai Terrace", "Lotus Leaf", "Bangkok Bistro",
            "Pad Thai Place", "Green Curry Garden", "Elephant Eatery", "Mango Sticky Cafe", "Thai Treasure",
            "Chiang Mai Kitchen", "Saffron Siam", "Temple Taste", "Thai Silk Table", "Phuket Flavor",
            "Spice of Siam", "Lemongrass Lounge", "Bamboo Bistro", "Sawasdee Supper", "Golden Pavilion"
        ],
        "menu": [
            "Pad Thai", "Green Curry", "Tom Yum Soup", "Massaman Curry",
            "Mango Sticky Rice", "Papaya Salad", "Satay", "Thai Spring Rolls",
            "Thai Basil Chicken", "Panang Curry", "Tom Kha Gai", "Stir-Fried Morning Glory",
            "Pineapple Fried Rice", "Chicken Cashew", "Coconut Soup", "Crab Fried Rice",
            "Fish Cakes", "Thai Iced Tea", "Sticky Rice", "Khao Soi",
            "Pad See Ew", "Som Tum", "Duck Curry", "Thai Noodles",
            "Sweet Chili Shrimp", "Bangkok Beef", "Larb Gai", "Curry Puff",
            "Thai Mango Salad", "Red Curry"
        ]
    },
    "Greek": {
        "names": [
            "Santorini Spice", "Athens Table", "Olive & Ouzo", "Mediterranean Muse", "Poseidon Plates",
            "Mykonos Meals", "Parthenon Pantry", "Acropolis Eatery", "Aegean Aroma", "Zeus Zest",
            "Agora Grill", "Hellenic House", "Thessaloniki Tavern", "Greek Garden", "Sparta Supper",
            "Olive Grove", "Ionian Inn", "Ouzo Oasis", "Feta Feast", "Gyro Garden"
        ],
        "menu": [
            "Moussaka", "Souvlaki", "Greek Salad", "Spanakopita",
            "Tzatziki", "Gyro", "Dolmades", "Baklava",
            "Lamb Kleftiko", "Greek Lemon Chicken", "Feta Pie", "Octopus Salad",
            "Avgolemono Soup", "Pita Bread", "Keftedes", "Halloumi",
            "Greek Yogurt", "Fasolada", "Seafood Platter", "Olive Tapenade",
            "Pastitsio", "Mediterranean Rice", "Greek Mezze", "Stuffed Peppers",
            "Lemon Potatoes", "Honey Cake", "Grilled Fish", "Cretan Salad",
            "Tirokafteri", "Plaki"
        ]
    },
    "Spanish": {
        "names": [
            "Tapas Terrace", "Madrid Munch", "Barcelona Bistro", "La Fiesta", "Sangria Salsa",
            "Paella Palace", "Olé Olé", "Casa de Tapas", "Flamenco Feast", "Costa Cocina",
            "Seville Suppers", "Catalan Kitchen", "Ibiza Eats", "Andalusia Alcove", "Madrid Market",
            "La Mancha Lounge", "Tapas Tango", "El Toro", "Ronda Restaurant", "La Rambla",
            "Plaza Plate"
        ],
        "menu": [
            "Paella", "Patatas Bravas", "Gazpacho", "Churros",
            "Jamón Ibérico", "Tortilla Española", "Pulpo a la Gallega", "Croquetas",
            "Pimientos de Padrón", "Sangria", "Tapas Platter", "Calamares",
            "Pulpo", "Empanadas", "Coca de Trampo", "Pollo al Ajillo",
            "Seafood Paella", "Manchego Cheese", "Chorizo", "Pisto",
            "Albóndigas", "Pa amb Tomàquet", "Gambas al Ajillo", "Fabada Asturiana",
            "Crema Catalana", "Torrijas", "Sopa de Ajo", "Chocolate con Churros",
            "Arroz Negro", "Bacalao"
        ]
    }
}

# Page content
if page == "Home":
    st.subheader("Build your restaurant concept with us")
    st.write("Use the side navigation to browse the generator, choose cuisines, and discover unique restaurant names.")
    st.markdown("---")
    st.write("### What you can do")
    st.write("- Select a cuisine from the sidebar")
    st.write("- Generate unique restaurant names")
    st.write("- Explore menus with 30 curated items per cuisine")
    st.write("- Enjoy a responsive website-like layout")

elif page == "Generator":
    cuisine = sidebar_cuisine
    st.subheader(f"Generate a {cuisine} restaurant")
    if st.button("✨ Generate Restaurant"):
        selected = data[cuisine]
        name = random.choice(selected["names"])
        menu = random.sample(selected["menu"], min(10, len(selected["menu"])))

        st.markdown(f"<div class='card'><h2>{name}</h2></div>", unsafe_allow_html=True)
        st.markdown("<div class='card'><h3>🍽 Sample Menu</h3>", unsafe_allow_html=True)
        for item in menu:
            st.write(f"• {item}")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("Click the Generate button to create a new restaurant name and curated sample menu.")

else:
    st.subheader("About this app")
    st.write("This restaurant generator uses a sidebar layout to feel more like a website.")
    st.write("It supports multiple cuisines and now includes new country styles like Japanese, French, Thai, Greek, and Spanish.")
    st.write("Each cuisine has 20 unique restaurant names and 30+ menu items to make the generator more useful.")
    st.markdown("---")
    st.write("Built with Streamlit in Python.")

# Footer
st.markdown("---")
st.caption("🚀 Built with Streamlit | No API needed")