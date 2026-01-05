import React, { useState } from 'react';
import { MessageCircle, X, Send, Minimize2 } from 'lucide-react';
import './ChatWidget.css';

const ChatWidget = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [isMinimized, setIsMinimized] = useState(false);
    const [messages, setMessages] = useState([
        {
            role: 'bot',
            content: 'Hi! 👋 I\'m your AI shopping assistant. How can I help you today?'
        }
    ]);
    const [inputMessage, setInputMessage] = useState('');

    const handleSendMessage = () => {
        if (!inputMessage.trim()) return;

        // Add user message
        setMessages([...messages, {
            role: 'user',
            content: inputMessage
        }]);

        // Simulate bot response
        setTimeout(() => {
            setMessages(prev => [...prev, {
                role: 'bot',
                content: 'I can help you find products, track orders, or answer any questions about our store. What would you like to know?'
            }]);
        }, 1000);

        setInputMessage('');
    };

    return (
        <>
            {/* Chat Button */}
            {!isOpen && (
                <button className="chat-button" onClick={() => setIsOpen(true)}>
                    <MessageCircle size={24} />
                    <span className="chat-button-badge">AI</span>
                </button>
            )}

            {/* Chat Window */}
            {isOpen && (
                <div className={`chat-widget ${isMinimized ? 'minimized' : ''}`}>
                    <div className="chat-header">
                        <div className="chat-header-info">
                            <div className="bot-avatar">🤖</div>
                            <div>
                                <h3>AI Assistant</h3>
                                <p className="status">Online</p>
                            </div>
                        </div>
                        <div className="chat-header-actions">
                            <button
                                className="header-btn"
                                onClick={() => setIsMinimized(!isMinimized)}
                            >
                                <Minimize2 size={18} />
                            </button>
                            <button
                                className="header-btn"
                                onClick={() => setIsOpen(false)}
                            >
                                <X size={18} />
                            </button>
                        </div>
                    </div>

                    {!isMinimized && (
                        <>
                            <div className="chat-messages">
                                {messages.map((msg, idx) => (
                                    <div key={idx} className={`message ${msg.role}`}>
                                        <div className="message-content">
                                            {msg.content}
                                        </div>
                                    </div>
                                ))}
                            </div>

                            <div className="chat-input">
                                <input
                                    type="text"
                                    placeholder="Type your message..."
                                    value={inputMessage}
                                    onChange={(e) => setInputMessage(e.target.value)}
                                    onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
                                />
                                <button className="send-btn" onClick={handleSendMessage}>
                                    <Send size={18} />
                                </button>
                            </div>

                            <div className="chat-footer">
                                <span>Powered by AI</span>
                            </div>
                        </>
                    )}
                </div>
            )}
        </>
    );
};

export default ChatWidget;
