import sqlite3
import json

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('restaurants.db')
cursor = conn.cursor()

# Create a table to store restaurant data
cursor.execute('''
CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY,
    name TEXT,
    location TEXT,
    cuisine TEXT
)
''')

# Create a table to store menu items
cursor.execute('''
CREATE TABLE IF NOT EXISTS menu_items (
    id INTEGER PRIMARY KEY,
    restaurant_id INTEGER,
    item_name TEXT,
    price REAL,
    category TEXT,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
)
''')

conn.commit()
