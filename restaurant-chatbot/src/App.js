import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [userInput, setUserInput] = useState('');
  const [messages, setMessages] = useState([]);

  const handleInputChange = (event) => {
    setUserInput(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    // Add user's message to the chat
    setMessages([...messages, { text: userInput, sender: 'user' }]);

    try {
      // Send the user input to the FastAPI backend
      const response = await axios.post('http://127.0.0.1:8000/chat', { message: userInput });

      let botMessage = response.data.message; // Default to the general message

      // Check if the bot returned a menu or a list of restaurants
      if (response.data.menu) {
        botMessage = "Menu: " + response.data.menu.map(item => item.item_name).join(", "); // Adjust according to your menu item structure
      } else if (response.data.restaurants) {
        botMessage = "Restaurants: " + response.data.restaurants.map(restaurant => restaurant.name).join(", "); // Adjust according to your restaurant structure
      }

      // Add the bot's response to the chat
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: botMessage, sender: 'bot' },
      ]);
    } catch (error) {
      console.error('Error communicating with the backend:', error);
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: 'Error communicating with the bot.', sender: 'bot' },
      ]);
    }

    // Clear the input field
    setUserInput('');
  };

  return (
    <div className="App">
      <h1>Restaurant Chatbot</h1>
      <div className="chat-container">
        <div className="messages">
          {messages.map((msg, index) => (
            <div key={index} className={msg.sender}>
              {msg.text}
            </div>
          ))}
        </div>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={userInput}
            onChange={handleInputChange}
            placeholder="Type your message..."
          />
          <button type="submit">Send</button>
        </form>
      </div>
    </div>
  );
}

export default App;
