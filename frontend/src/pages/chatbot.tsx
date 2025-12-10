import React, { useState } from 'react';
import Layout from '@theme/Layout';

function Chatbot() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSendMessage = async () => {
    if (input.trim() === '') return;

    const userMessage = { text: input, sender: 'user' };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setInput('');
    setLoading(true);

    try {
      // TODO: Replace with actual API call to your FastAPI backend
      const response = await fetch('http://localhost:8000/chat', { // Assuming http://localhost:8000 is your backend endpoint
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: input }),
      });
      const data = await response.json();
      const botMessage = { text: data.response, sender: 'bot' }; // Adjust based on your backend response structure
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage = { text: 'Sorry, something went wrong.', sender: 'bot' };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout title="Chatbot" description="Chat with the book's content">
      <div style={{ display: 'flex', flexDirection: 'column', height: '80vh', maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
        <h1 style={{ textAlign: 'center' }}>Chat with the Book</h1>
        <div style={{ flexGrow: 1, border: '1px solid #ccc', borderRadius: '8px', padding: '10px', overflowY: 'auto', marginBottom: '10px' }}>
          {messages.map((msg, index) => (
            <div key={index} style={{ textAlign: msg.sender === 'user' ? 'right' : 'left', margin: '5px 0' }}>
              <span style={{
                display: 'inline-block',
                padding: '8px 12px',
                borderRadius: '15px',
                backgroundColor: msg.sender === 'user' ? '#007bff' : '#f1f1f1',
                color: msg.sender === 'user' ? 'white' : 'black',
              }}>
                {msg.text}
              </span>
            </div>
          ))}
          {loading && (
            <div style={{ textAlign: 'left', margin: '5px 0' }}>
              <span style={{ display: 'inline-block', padding: '8px 12px', borderRadius: '15px', backgroundColor: '#f1f1f1', color: 'black' }}>
                Typing...
              </span>
            </div>
          )}
        </div>
        <div style={{ display: 'flex' }}>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === 'Enter') {
                handleSendMessage();
              }
            }}
            style={{ flexGrow: 1, padding: '10px', border: '1px solid #ccc', borderRadius: '8px', marginRight: '10px' }}
            placeholder="Ask me about the book..."
            disabled={loading}
          />
          <button
            onClick={handleSendMessage}
            style={{ padding: '10px 15px', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '8px', cursor: 'pointer' }}
            disabled={loading}
          >
            Send
          </button>
        </div>
      </div>
    </Layout>
  );
}

export default Chatbot;