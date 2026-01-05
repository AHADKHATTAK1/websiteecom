import React, { useState } from 'react';
import {
    CreditCard,
    Mail,
    MessageSquare,
    Truck,
    Plus,
    CheckCircle,
    XCircle,
    Eye,
    Settings,
    Loader
} from 'lucide-react';
import './APIConfiguration.css';

const APIConfiguration = () => {
    const [selectedCategory, setSelectedCategory] = useState('all');
    const [showAddModal, setShowAddModal] = useState(false);
    const [testingAPI, setTestingAPI] = useState(null);

    const categories = [
        { id: 'all', label: 'All APIs', icon: Settings },
        { id: 'payment', label: 'Payment', icon: CreditCard },
        { id: 'shipping', label: 'Shipping', icon: Truck },
        { id: 'email', label: 'Email', icon: Mail },
        { id: 'sms', label: 'SMS', icon: MessageSquare }
    ];

    const apiProviders = [
        {
            id: 1,
            name: 'Stripe',
            category: 'payment',
            description: 'Accept payments online',
            logo: '💳',
            configured: true,
            status: 'active',
            lastTested: '2 hours ago'
        },
        {
            id: 2,
            name: 'PayPal',
            category: 'payment',
            description: 'PayPal payment gateway',
            logo: '🅿️',
            configured: false,
            status: 'inactive'
        },
        {
            id: 3,
            name: 'SendGrid',
            category: 'email',
            description: 'Email delivery service',
            logo: '📧',
            configured: true,
            status: 'active',
            lastTested: '1 day ago'
        },
        {
            id: 4,
            name: 'Twilio',
            category: 'sms',
            description: 'SMS notifications',
            logo: '💬',
            configured: true,
            status: 'active',
            lastTested: '3 hours ago'
        },
        {
            id: 5,
            name: 'FedEx',
            category: 'shipping',
            description: 'Shipping & tracking',
            logo: '📦',
            configured: false,
            status: 'inactive'
        },
        {
            id: 6,
            name: 'Mailgun',
            category: 'email',
            description: 'Email API service',
            logo: '✉️',
            configured: false,
            status: 'inactive'
        }
    ];

    const filteredAPIs = selectedCategory === 'all'
        ? apiProviders
        : apiProviders.filter(api => api.category === selectedCategory);

    const handleTestConnection = (apiId) => {
        setTestingAPI(apiId);
        setTimeout(() => {
            setTestingAPI(null);
            alert('Connection successful!');
        }, 2000);
    };

    return (
        <div className="api-configuration animate-fade-in">
            <header className="dashboard-header">
                <div>
                    <h1 className="page-title">API Configuration</h1>
                    <p className="page-subtitle">Manage all your third-party integrations</p>
                </div>
                <button className="btn-primary" onClick={() => setShowAddModal(true)}>
                    <Plus size={18} />
                    Add New API
                </button>
            </header>

            <div className="category-tabs">
                {categories.map(cat => {
                    const Icon = cat.icon;
                    return (
                        <button
                            key={cat.id}
                            className={`category-tab ${selectedCategory === cat.id ? 'active' : ''}`}
                            onClick={() => setSelectedCategory(cat.id)}
                        >
                            <Icon size={18} />
                            {cat.label}
                        </button>
                    );
                })}
            </div>

            <div className="api-grid">
                {filteredAPIs.map(api => (
                    <div key={api.id} className={`api-card card ${api.configured ? 'configured' : ''}`}>
                        <div className="api-card-header">
                            <div className="api-logo">{api.logo}</div>
                            <div className={`api-status badge-${api.status === 'active' ? 'success' : 'error'}`}>
                                {api.status === 'active' ? (
                                    <>
                                        <CheckCircle size={12} />
                                        Active
                                    </>
                                ) : (
                                    <>
                                        <XCircle size={12} />
                                        Inactive
                                    </>
                                )}
                            </div>
                        </div>

                        <div className="api-card-body">
                            <h3 className="api-name">{api.name}</h3>
                            <p className="api-description">{api.description}</p>
                            <span className={`api-category badge badge-${api.category === 'payment' ? 'primary' : api.category === 'email' ? 'warning' : 'success'}`}>
                                {api.category}
                            </span>
                        </div>

                        <div className="api-card-footer">
                            {api.configured ? (
                                <>
                                    {api.lastTested && (
                                        <p className="last-tested">
                                            Last tested {api.lastTested}
                                        </p>
                                    )}
                                    <div className="api-actions">
                                        <button
                                            className="btn-secondary"
                                            onClick={() => handleTestConnection(api.id)}
                                            disabled={testingAPI === api.id}
                                        >
                                            {testingAPI === api.id ? (
                                                <><Loader size={16} className="spinning" /> Testing...</>
                                            ) : (
                                                <><CheckCircle size={16} /> Test</>
                                            )}
                                        </button>
                                        <button className="btn-secondary">
                                            <Settings size={16} />
                                            Configure
                                        </button>
                                    </div>
                                </>
                            ) : (
                                <button className="btn-configure">
                                    <Plus size={16} />
                                    Configure Now
                                </button>
                            )}
                        </div>
                    </div>
                ))}
            </div>

            {showAddModal && (
                <div className="modal-overlay" onClick={() => setShowAddModal(false)}>
                    <div className="modal" onClick={e => e.stopPropagation()}>
                        <div className="modal-header">
                            <h2>Add New API Integration</h2>
                            <button className="modal-close" onClick={() => setShowAddModal(false)}>×</button>
                        </div>
                        <div className="modal-body">
                            <div className="form-group">
                                <label>API Provider</label>
                                <select>
                                    <option>Select Provider</option>
                                    <option>Stripe</option>
                                    <option>PayPal</option>
                                    <option>Razorpay</option>
                                </select>
                            </div>
                            <div className="form-group">
                                <label>API Key</label>
                                <input type="password" placeholder="Enter your API key" />
                            </div>
                            <div className="form-group">
                                <label>API Secret (optional)</label>
                                <input type="password" placeholder="Enter API secret" />
                            </div>
                        </div>
                        <div className="modal-footer">
                            <button className="btn-secondary" onClick={() => setShowAddModal(false)}>
                                Cancel
                            </button>
                            <button className="btn-primary">
                                <CheckCircle size={16} />
                                Save Configuration
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default APIConfiguration;
