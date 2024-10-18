import sqlite3
import json

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('restaurants.db')
cursor = conn.cursor()


# Load the JSON data (replace 'your_data.json' with your actual file path)
data = '''
{
  "restaurants": [
    {
      "id": 1,
      "name": "Burger Palace",
      "location": "Downtown",
      "cuisine": "Fast Food",
      "menu_items": [
        { "id": 1, "item_name": "Cheeseburger", "price": 5.99, "category": "Burgers" },
        { "id": 2, "item_name": "Bacon Burger", "price": 6.99, "category": "Burgers" },
        { "id": 3, "item_name": "Fries", "price": 2.99, "category": "Sides" }
      ]
    },
    {
      "id": 2,
      "name": "Pizza Hub",
      "location": "Uptown",
      "cuisine": "Italian",
      "menu_items": [
        { "id": 4, "item_name": "Margherita Pizza", "price": 8.99, "category": "Pizza" },
        { "id": 5, "item_name": "Pepperoni Pizza", "price": 9.99, "category": "Pizza" },
        { "id": 6, "item_name": "Garlic Bread", "price": 3.99, "category": "Sides" }
      ]
    },
    {
      "id": 3,
      "name": "Sushi World",
      "location": "City Center",
      "cuisine": "Japanese",
      "menu_items": [
        { "id": 7, "item_name": "California Roll", "price": 10.99, "category": "Sushi" },
        { "id": 8, "item_name": "Spicy Tuna Roll", "price": 12.99, "category": "Sushi" },
        { "id": 9, "item_name": "Miso Soup", "price": 3.99, "category": "Soup" }
      ]
    },
    {
      "id": 4,
      "name": "Taco Fiesta",
      "location": "Suburb",
      "cuisine": "Mexican",
      "menu_items": [
        { "id": 10, "item_name": "Beef Tacos", "price": 7.99, "category": "Tacos" },
        { "id": 11, "item_name": "Chicken Quesadilla", "price": 6.99, "category": "Quesadillas" },
        { "id": 12, "item_name": "Guacamole", "price": 4.99, "category": "Sides" }
      ]
    },
    {
      "id": 5,
      "name": "Pasta Heaven",
      "location": "Midtown",
      "cuisine": "Italian",
      "menu_items": [
        { "id": 13, "item_name": "Spaghetti Bolognese", "price": 11.99, "category": "Pasta" },
        { "id": 14, "item_name": "Penne Alfredo", "price": 10.99, "category": "Pasta" },
        { "id": 15, "item_name": "Garlic Bread", "price": 3.99, "category": "Sides" }
      ]
    },
    {
      "id": 6,
      "name": "Indian Spice",
      "location": "Downtown",
      "cuisine": "Indian",
      "menu_items": [
        { "id": 16, "item_name": "Butter Chicken", "price": 12.99, "category": "Main Course" },
        { "id": 17, "item_name": "Naan Bread", "price": 2.99, "category": "Sides" },
        { "id": 18, "item_name": "Samosa", "price": 3.99, "category": "Appetizers" }
      ]
    },
    {
      "id": 7,
      "name": "Seafood Delight",
      "location": "Coastal",
      "cuisine": "Seafood",
      "menu_items": [
        { "id": 19, "item_name": "Grilled Salmon", "price": 15.99, "category": "Main Course" },
        { "id": 20, "item_name": "Fish and Chips", "price": 12.99, "category": "Main Course" },
        { "id": 21, "item_name": "Shrimp Cocktail", "price": 9.99, "category": "Appetizers" }
      ]
    },
    {
      "id": 8,
      "name": "Vegan Bites",
      "location": "Uptown",
      "cuisine": "Vegan",
      "menu_items": [
        { "id": 22, "item_name": "Vegan Burger", "price": 8.99, "category": "Burgers" },
        { "id": 23, "item_name": "Quinoa Salad", "price": 7.99, "category": "Salads" },
        { "id": 24, "item_name": "Sweet Potato Fries", "price": 3.99, "category": "Sides" }
      ]
    },
    {
      "id": 9,
      "name": "BBQ Nation",
      "location": "Midtown",
      "cuisine": "American",
      "menu_items": [
        { "id": 25, "item_name": "BBQ Ribs", "price": 16.99, "category": "Main Course" },
        { "id": 26, "item_name": "Pulled Pork Sandwich", "price": 9.99, "category": "Sandwiches" },
        { "id": 27, "item_name": "Coleslaw", "price": 2.99, "category": "Sides" }
      ]
    },
    {
      "id": 10,
      "name": "The Deli Spot",
      "location": "Downtown",
      "cuisine": "Deli",
      "menu_items": [
        { "id": 28, "item_name": "Turkey Sandwich", "price": 7.99, "category": "Sandwiches" },
        { "id": 29, "item_name": "Roast Beef Sandwich", "price": 8.99, "category": "Sandwiches" },
        { "id": 30, "item_name": "Potato Salad", "price": 3.99, "category": "Sides" }
      ]
    },
    {
      "id": 11,
      "name": "Noodle House",
      "location": "Chinatown",
      "cuisine": "Chinese",
      "menu_items": [
        { "id": 31, "item_name": "Beef Chow Mein", "price": 9.99, "category": "Noodles" },
        { "id": 32, "item_name": "Pork Dumplings", "price": 5.99, "category": "Appetizers" },
        { "id": 33, "item_name": "Egg Drop Soup", "price": 3.99, "category": "Soup" }
      ]
    },
    {
      "id": 12,
      "name": "Mediterranean Grill",
      "location": "Suburb",
      "cuisine": "Mediterranean",
      "menu_items": [
        { "id": 34, "item_name": "Chicken Shawarma", "price": 9.99, "category": "Main Course" },
        { "id": 35, "item_name": "Falafel", "price": 6.99, "category": "Main Course" },
        { "id": 36, "item_name": "Hummus", "price": 4.99, "category": "Sides" }
      ]
    },
    {
      "id": 13,
      "name": "Dessert Dream",
      "location": "Uptown",
      "cuisine": "Desserts",
      "menu_items": [
        { "id": 37, "item_name": "Chocolate Cake", "price": 5.99, "category": "Cakes" },
        { "id": 38, "item_name": "Cheesecake", "price": 6.99, "category": "Cakes" },
        { "id": 39, "item_name": "Ice Cream", "price": 3.99, "category": "Ice Cream" }
      ]
    },
    {
      "id": 14,
      "name": "Kebab King",
      "location": "City Center",
      "cuisine": "Middle Eastern",
      "menu_items": [
        { "id": 40, "item_name": "Lamb Kebab", "price": 11.99, "category": "Main Course" },
        { "id": 41, "item_name": "Chicken Kebab", "price": 10.99, "category": "Main Course" },
        { "id": 42, "item_name": "Tabbouleh", "price": 4.99, "category": "Sides" }
      ]
    },
    {
      "id": 15,
      "name": "French Bistro",
      "location": "Midtown",
      "cuisine": "French",
      "menu_items": [
        { "id": 43, "item_name": "Croque Monsieur", "price": 8.99, "category": "Sandwiches" },
        { "id": 44, "item_name": "French Onion Soup", "price": 6.99, "category": "Soup" },
        { "id": 45, "item_name": "Crepes", "price": 7.99, "category": "Desserts" }
      ]
    },
    {
      "id": 16,
      "name": "Thai Taste",
      "location": "Suburb",
      "cuisine": "Thai",
      "menu_items": [
        { "id": 46, "item_name": "Pad Thai", "price": 9.99, "category": "Main Course" },
        { "id": 47, "item_name": "Green Curry", "price": 11.99, "category": "Main Course" },
        { "id": 48, "item_name": "Spring Rolls", "price": 4.99, "category": "Appetizers" }
      ]
    },
    {
      "id": 17,
      "name": "Korean BBQ House",
      "location": "City Center",
      "cuisine": "Korean",
      "menu_items": [
        { "id": 49, "item_name": "Bulgogi", "price": 13.99, "category": "Main Course" },
        { "id": 50, "item_name": "Kimchi", "price": 3.99, "category": "Sides" },
        { "id": 51, "item_name": "Bibimbap", "price": 11.99, "category": "Main Course" }
      ]
    },
    {
      "id": 18,
      "name": "Steak House",
      "location": "Downtown",
      "cuisine": "American",
      "menu_items": [
        { "id": 52, "item_name": "Sirloin Steak", "price": 19.99, "category": "Main Course" },
        { "id": 53, "item_name": "Ribeye Steak", "price": 24.99, "category": "Main Course" },
        { "id": 54, "item_name": "Mashed Potatoes", "price": 4.99, "category": "Sides" }
      ]
    },
    {
      "id": 19,
      "name": "Lebanese Delights",
      "location": "Midtown",
      "cuisine": "Lebanese",
      "menu_items": [
        { "id": 55, "item_name": "Shish Tawook", "price": 10.99, "category": "Main Course" },
        { "id": 56, "item_name": "Baba Ganoush", "price": 4.99, "category": "Appetizers" },
        { "id": 57, "item_name": "Fattoush", "price": 5.99, "category": "Salads" }
      ]
    },
    {
      "id": 20,
      "name": "Healthy Bites",
      "location": "Uptown",
      "cuisine": "Health Food",
      "menu_items": [
        { "id": 58, "item_name": "Grilled Chicken Salad", "price": 9.99, "category": "Salads" }

      ]
    }
  ]
}

'''
# Parse the JSON data
restaurant_data = json.loads(data)

# Insert restaurant data
for restaurant in restaurant_data['restaurants']:
    cursor.execute('''
    INSERT INTO restaurants (id, name, location, cuisine)
    VALUES (?, ?, ?, ?)
    ''', (restaurant['id'], restaurant['name'], restaurant['location'], restaurant['cuisine']))
    
    # Insert menu items
    for item in restaurant['menu_items']:
        cursor.execute('''
        INSERT INTO menu_items (id, restaurant_id, item_name, price, category)
        VALUES (?, ?, ?, ?, ?)
        ''', (item['id'], restaurant['id'], item['item_name'], item['price'], item['category']))

# Commit changes and close the connection
conn.commit()
conn.close()
