from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import requests

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust according to your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('restaurants.db')
    conn.row_factory = sqlite3.Row  # Makes the cursor return dictionaries instead of tuples
    return conn

@app.get("/restaurants")
def get_restaurants():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM restaurants")
    restaurants = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in restaurants]

@app.get("/restaurants/{restaurant_id}/menu")
def get_menu(restaurant_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu_items WHERE restaurant_id = ?", (restaurant_id,))
    menu_items = cursor.fetchall()
    conn.close()
    
    if not menu_items:
        raise HTTPException(status_code=404, detail="Menu not found")
    
    return [dict(row) for row in menu_items]

@app.post("/order")
def place_order(order: dict):
    # You can implement the logic to place an order and store it in the database.
    # For now, just return a success message for the demo.
    return {"message": "Order placed successfully", "order": order}

@app.post("/chat")
def chat_with_bot(user_input: dict):  # Expect a dict for the user input
    # Send the user input to the Rasa model for intent recognition
    rasa_endpoint = "http://localhost:5005/model/parse"  # Adjust if your Rasa server is hosted differently
    response = requests.post(rasa_endpoint, json={"text": user_input["message"]})  # Access message from the dict

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error communicating with the Rasa model")

    intent = response.json().get("intent", {}).get("name")
    
    if intent == "order_food":
        return {"message": "Processing your order..."}
    elif intent == "get_menu":
        restaurant_id = extract_restaurant_id(user_input["message"])
        menu = get_menu(restaurant_id)
        print(menu)
        return {"menu": menu}  # Return the menu here
    elif intent == "get_restaurants":
        restaurants = get_restaurants()
        print(restaurants)
        return {"restaurants": restaurants}  # Return the restaurants here
    else:
        return {"message": "Sorry, I didn't understand that."}

# Helper function to extract restaurant ID (implement as needed)
def extract_restaurant_id(user_input: str):
    # Logic to extract the restaurant ID from the user input if applicable
    # For simplicity, returning a hardcoded ID for demo purposes
    return 1
