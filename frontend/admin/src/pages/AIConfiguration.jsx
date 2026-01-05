import React, { useState } from 'react';
import {
    Bot,
    Brain,
    MessageSquare,
    Settings,
    Sparkles,
    Play,
    CheckCircle,
    Loader
} from 'lucide-react';
import './AIConfiguration.css';

const AIConfiguration = () => {
    const [selectedProvider, setSelectedProvider] = useState('openai');
    const [testing, setTesting] = useState(false);
    const [showPreview, setShowPreview] = useState(false);

    const aiProviders = [
        {
            id: 'openai',
            name: 'OpenAI',
            icon: '🤖',
            models: ['gpt-4', 'gpt-4-turbo', 'gpt-3.5-turbo'],
            description: 'Advanced language model from OpenAI'
        },
        {
            id: 'claude',
            name: 'Anthropic Claude',
            icon: '🧠',
            models: ['claude-3-opus', 'claude-3-sonnet', 'claude-3-haiku'],
            description: 'Anthropic\'s powerful AI assistant'
        },
        {
            id: 'gemini',
            name: 'Google Gemini',
            icon: '✨',
            models: ['gemini-pro', 'gemini-pro-vision'],
            description: 'Google\'s multimodal AI model'
        }
    ];

    const handleTestConnection = () => {
        setTesting(true);
        setTimeout(() => {
            setTesting(false);
            alert('AI connection successful!');
        }, 2000);
    };

    return (
        <div className="ai-configuration animate-fade-in">
            <header className="dashboard-header">
                <div>
                    <h1 className="page-title">AI Chatbot Configuration</h1>
                    <p className="page-subtitle">Configure your AI-powered customer support chatbot</p>
                </div>
                <button className="btn-primary" onClick={() => setShowPreview(!showPreview)}>
                    <MessageSquare size={18} />
                    {showPreview ? 'Hide' : 'Preview'} Chatbot
                </button>
            </header>

            <div className="ai-config-grid">
                <div className="config-panel">
                    <div className="card">
                        <div className="card-header-custom">
                            <Bot size={24} className="text-primary" />
                            <h2 className="card-title">AI Provider</h2>
                        </div>

                        <div className="provider-grid">
                            {aiProviders.map(provider => (
                                <button
                                    key={provider.id}
                                    className={`provider-card ${selectedProvider === provider.id ? 'selected' : ''}`}
                                    onClick={() => setSelectedProvider(provider.id)}
                                >
                                    <div className="provider-icon">{provider.icon}</div>
                                    <div className="provider-info">
                                        <h3>{provider.name}</h3>
                                        <p>{provider.description}</p>
                                    </div>
                                    {selectedProvider === provider.id && (
                                        <CheckCircle className="selected-icon" size={20} />
                                    )}
                                </button>
                            ))}
                        </div>
                    </div>

                    <div className="card">
                        <div className="card-header-custom">
                            <Settings size={24} className="text-primary" />
                            <h2 className="card-title">Model Settings</h2>
                        </div>

                        <div className="form-group">
                            <label>Model</label>
                            <select>
                                {aiProviders.find(p => p.id === selectedProvider)?.models.map(model => (
                                    <option key={model} value={model}>{model}</option>
                                ))}
                            </select>
                        </div>

                        <div className="form-group">
                            <label>API Key</label>
                            <input type="password" placeholder="Enter your API key" />
                        </div>

                        <div className="form-group">
                            <label>System Prompt</label>
                            <textarea
                                rows="4"
                                placeholder="You are a helpful e-commerce assistant..."
                                defaultValue="You are a helpful e-commerce assistant. Help customers find products, track orders, and answer questions about our store."
                            />
                        </div>

                        <div className="form-row">
                            <div className="form-group">
                                <label>Temperature</label>
                                <input type="number" defaultValue="0.7" min="0" max="1" step="0.1" />
                            </div>
                            <div className="form-group">
                                <label>Max Tokens</label>
                                <input type="number" defaultValue="500" min="100" max="4000" step="100" />
                            </div>
                        </div>

                        <button
                            className="btn-test"
                            onClick={handleTestConnection}
                            disabled={testing}
                        >
                            {testing ? (
                                <>
                                    <Loader size={18} className="spinning" />
                                    Testing Connection...
                                </>
                            ) : (
                                <>
                                    <Play size={18} />
                                    Test Connection
                                </>
                            )}
                        </button>
                    </div>

                    <div className="card">
                        <div className="card-header-custom">
                            <Sparkles size={24} className="text-primary" />
                            <h2 className="card-title">Chatbot Features</h2>
                        </div>

                        <div className="feature-toggle">
                            <div className="toggle-item">
                                <div>
                                    <h4>Knowledge Base</h4>
                                    <p>Use custom training data</p>
                                </div>
                                <label className="switch">
                                    <input type="checkbox" defaultChecked />
                                    <span className="slider"></span>
                                </label>
                            </div>

                            <div className="toggle-item">
                                <div>
                                    <h4>Product Recommendations</h4>
                                    <p>Suggest products based on conversation</p>
                                </div>
                                <label className="switch">
                                    <input type="checkbox" defaultChecked />
                                    <span className="slider"></span>
                                </label>
                            </div>

                            <div className="toggle-item">
                                <div>
                                    <h4>Order Tracking</h4>
                                    <p>Allow customers to track their orders</p>
                                </div>
                                <label className="switch">
                                    <input type="checkbox" defaultChecked />
                                    <span className="slider"></span>
                                </label>
                            </div>
                        </div>
                    </div>

                    <div className="action-buttons">
                        <button className="btn-secondary">Cancel</button>
                        <button className="btn-primary">
                            <CheckCircle size={18} />
                            Save Configuration
                        </button>
                    </div>
                </div>

                {showPreview && (
                    <div className="preview-panel">
                        <div className="chat-preview card">
                            <div className="chat-header">
                                <Bot size={20} />
                                <span>AI Assistant</span>
                            </div>
                            <div className="chat-messages">
                                <div className="message bot-message">
                                    <div className="message-content">
                                        Hello! How can I help you today?
                                    </div>
                                </div>
                                <div className="message user-message">
                                    <div className="message-content">
                                        I'm looking for wireless headphones
                                    </div>
                                </div>
                                <div className="message bot-message">
                                    <div className="message-content">
                                        Great! I can help you find the perfect wireless headphones. We have several options:
                                        <br /><br />
                                        • Sony WH-1000XM5 - $399<br />
                                        • Bose QuietComfort 45 - $329<br />
                                        • Apple AirPods Max - $549
                                        <br /><br />
                                        What's your budget range?
                                    </div>
                                </div>
                            </div>
                            <div className="chat-input">
                                <input type="text" placeholder="Type a message..." disabled />
                                <button className="send-btn" disabled>Send</button>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default AIConfiguration;
