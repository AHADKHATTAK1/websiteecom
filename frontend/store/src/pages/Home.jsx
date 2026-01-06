import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight, Sparkles, ShoppingBag, Zap } from 'lucide-react';
import { getThemeSettings } from '../services/api';
import './Home.css';

const Home = () => {
    const [theme, setTheme] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchTheme = async () => {
            try {
                const response = await getThemeSettings();
                setTheme(response.data);

                // Apply colors to root
                if (response.data) {
                    document.documentElement.style.setProperty('--primary-color', response.data.primary_color);
                    document.documentElement.style.setProperty('--secondary-color', response.data.secondary_color);
                }
            } catch (error) {
                console.error("Error fetching theme:", error);
            } finally {
                setLoading(false);
            }
        };
        fetchTheme();
    }, []);

    const featuredProducts = [
        // ... (remaining featuredProducts)
    ]; // Note: I will only replace the top part to show logic

    return (
        <div className="home">
            {/* Hero Section */}
            <section className="hero">
                <div className="container">
                    <div className="hero-content">
                        <div className="hero-badge">
                            <Sparkles size={16} />
                            <span>ERP-Powered Recycling</span>
                        </div>
                        <h1 className="hero-title">
                            Transforming E-Waste into
                            <span className="gradient-text"> Sustainable Value</span>
                        </h1>
                        <p className="hero-subtitle">
                            We provide an ERP-powered electronic recycling system that ensures secure data destruction, compliance, and environmentally responsible e-waste management.
                        </p>
                        <div className="hero-actions">
                            <Link to="/services" className="btn btn-primary">
                                Get Started
                                <ArrowRight size={18} />
                            </Link>
                            <Link to="/contact" className="btn btn-secondary">
                                Contact Our Experts
                            </Link>
                        </div>
                    </div>
                    <div className="hero-image">
                        <div className="hero-card">
                            <span className="hero-emoji"> 🛍️</span>
                        </div>
                    </div>
                </div>
            </section>

            {/* Features Section */}
            <section className="features">
                <div className="container">
                    <div className="grid grid-3">
                        <div className="feature-card">
                            <div className="feature-icon">
                                <Sparkles size={32} />
                            </div>
                            <h3>Electronic Waste Recycling</h3>
                            <p>Comprehensive recycling for computers, phones, servers, and all electronics</p>
                        </div>
                        <div className="feature-card">
                            <div className="feature-icon">
                                <ShoppingBag size={32} />
                            </div>
                            <h3>Secure Data Destruction</h3>
                            <p>Certified data wiping and physical destruction with compliance reporting</p>
                        </div>
                        <div className="feature-card">
                            <div className="feature-icon">
                                <Zap size={32} />
                            </div>
                            <h3>ERP-Powered Tracking</h3>
                            <p>Real-time asset tracking and automated compliance documentation</p>
                        </div>
                    </div>
                </div>
            </section>


            {/* Trending Categories */}
            <section className="categories-section">
                <div className="container">
                    <h2 className="section-title">Trending Categories</h2>
                    <div className="categories-grid">
                        <Link to="/products?cat=batteries" className="category-card">
                            <div className="category-icon">🔋</div>
                            <h3>Laptop Batteries</h3>
                        </Link>
                        <Link to="/products?cat=chargers" className="category-card">
                            <div className="category-icon">🔌</div>
                            <h3>Chargers</h3>
                        </Link>
                        <Link to="/products?cat=keyboards" className="category-card">
                            <div className="category-icon">⌨️</div>
                            <h3>Keyboards</h3>
                        </Link>
                        <Link to="/products?cat=ram" className="category-card">
                            <div className="category-icon">💾</div>
                            <h3>RAM</h3>
                        </Link>
                        <Link to="/products?cat=screens" className="category-card">
                            <div className="category-icon">🖥️</div>
                            <h3>Screens</h3>
                        </Link>
                        <Link to="/products?cat=hubs" className="category-card">
                            <div className="category-icon">🔗</div>
                            <h3>Type-C Hubs</h3>
                        </Link>
                        <Link to="/products?cat=audio" className="category-card">
                            <div className="category-icon">🎧</div>
                            <h3>Audio</h3>
                        </Link>
                        <Link to="/products?cat=storage" className="category-card">
                            <div className="category-icon">💽</div>
                            <h3>Storage</h3>
                        </Link>
                    </div>
                </div>
            </section>

            {/* Recycling Services */}
            <section className="services-section">
                <div className="container">
                    <h2 className="section-title">Our Recycling Services</h2>
                    <div className="grid grid-3">
                        <div className="service-card">
                            <div className="service-icon">♻️</div>
                            <h3>E-Waste Pickup</h3>
                            <p>Schedule free pickup for your old electronics</p>
                            <Link to="/services" className="service-link">Learn More →</Link>
                        </div>
                        <div className="service-card">
                            <div className="service-icon">🔒</div>
                            <h3>Data Destruction</h3>
                            <p>Certified secure data wiping & physical destruction</p>
                            <Link to="/services" className="service-link">Learn More →</Link>
                        </div>
                        <div className="service-card">
                            <div className="service-icon">📜</div>
                            <h3>Recycling Certificates</h3>
                            <p>Get compliance certificates for corporate recycling</p>
                            <Link to="/services" className="service-link">Learn More →</Link>
                        </div>
                    </div>
                </div>
            </section>

            {/* CTA Section */}
            <section className="cta-section">
                <div className="container">
                    <div className="cta-card">
                        <h2>Ready to Recycle or Shop?</h2>
                        <p>Browse quality laptop parts or schedule your e-waste pickup today</p>
                        <div className="cta-buttons">
                            <Link to="/products" className="btn btn-primary btn-lg">
                                Shop Products <ArrowRight size={20} />
                            </Link>
                            <Link to="/contact" className="btn btn-secondary btn-lg">
                                Schedule Pickup
                            </Link>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    );
};

export default Home;
