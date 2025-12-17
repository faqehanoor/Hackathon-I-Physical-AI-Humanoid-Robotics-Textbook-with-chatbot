import React, { useState } from 'react';
import styles from './ChatWidget.module.css';

interface Message {
  id: string;
  text: string;
  sender: 'user' | 'bot';
  timestamp: Date;
}

const ChatWidget: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState('');

  const handleSend = () => {
    if (inputValue.trim()) {
      // Add user message
      const newUserMessage: Message = {
        id: Date.now().toString(),
        text: inputValue,
        sender: 'user',
        timestamp: new Date()
      };

      setMessages(prev => [...prev, newUserMessage]);
      setInputValue('');

      // Simulate bot response after a delay
      setTimeout(() => {
        const botMessage: Message = {
          id: (Date.now() + 1).toString(),
          text: `I received your message: "${inputValue}". This is a simulated response.`,
          sender: 'bot',
          timestamp: new Date()
        };
        setMessages(prev => [...prev, botMessage]);
      }, 1000);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className={styles.chatContainer}>
      {/* Chat widget header */}
      <div
        className={`${styles.chatHeader} ${isOpen ? styles.open : ''}`}
        onClick={() => setIsOpen(!isOpen)}
      >
        <span className={styles.headerTitle}>AI Assistant</span>
        <span className={styles.toggleButton}>{isOpen ? '−' : '+'}</span>
      </div>

      {/* Chat messages panel */}
      {isOpen && (
        <div className={styles.chatPanel}>
          <div className={styles.messagesContainer}>
            {messages.length === 0 ? (
              <div className={styles.welcomeMessage}>
                Hello! I'm your AI assistant for robotics and physical AI. How can I help you today?
              </div>
            ) : (
              messages.map((message) => (
                <div
                  key={message.id}
                  className={`${styles.message} ${styles[message.sender]}`}
                >
                  <div className={styles.messageText}>{message.text}</div>
                  <div className={styles.timestamp}>
                    {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </div>
                </div>
              ))
            )}
          </div>

          {/* Input area */}
          <div className={styles.inputContainer}>
            <textarea
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Type your message here..."
              className={styles.textInput}
              rows={2}
            />
            <button
              onClick={handleSend}
              disabled={!inputValue.trim()}
              className={`${styles.sendButton} ${!inputValue.trim() ? styles.disabled : ''}`}
            >
              Send
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ChatWidget;