import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('restaurants.db')
cursor = conn.cursor()

# Query to check restaurants
cursor.execute('SELECT * FROM restaurants')
restaurants = cursor.fetchall()
print("Restaurants:", restaurants)

# Query to check menu items
cursor.execute('SELECT * FROM menu_items')
menu_items = cursor.fetchall()
print("Menu Items:", menu_items)

# Close the connection
conn.close()
