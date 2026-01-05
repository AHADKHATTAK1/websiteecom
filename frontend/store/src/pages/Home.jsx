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
                            <span>welcome to our store</span>
                        </div>
                        <h1 className="hero-title">
                            {theme?.banner_text || "Shop Smarter with"}
                            {!theme?.banner_text && <span className="gradient-text"> AI Intelligence</span>}
                        </h1>
                        <p className="hero-subtitle">
                            {theme?.banner_subtext || "Discover quality products at competitive prices. Fast shipping, secure payments, and excellent customer service guaranteed."}
                        </p>
                        <div className="hero-actions">
                            <Link to="/products" className="btn btn-primary">
                                Start Shopping
                                <ArrowRight size={18} />
                            </Link>
                            <button className="btn btn-secondary">
                                Learn More
                            </button>
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
                            <h3>informative </h3>
                            <p>Get personalized product suggestions based on your preferences</p>
                        </div>
                        <div className="feature-card">
                            <div className="feature-icon">
                                <ShoppingBag size={32} />
                            </div>
                            <h3>Easy Shopping</h3>
                            <p>Browse and buy with our intuitive, user-friendly interface</p>
                        </div>
                        <div className="feature-card">
                            <div className="feature-icon">
                                <Zap size={32} />
                            </div>
                            <h3>Fast Delivery</h3>
                            <p>Quick and reliable shipping to your doorstep</p>
                        </div>
                    </div>
                </div>
            </section>

            {/* Featured Products */}
            <section className="featured-products">
                <div className="container">
                    <div className="section-header">
                        <h2>Featured Products</h2>
                        <Link to="/products" className="view-all">
                            View All <ArrowRight size={18} />
                        </Link>
                    </div>
                    <div className="grid grid-4">
                        {featuredProducts.map(product => (
                            <Link to={`/product/${product.id}`} key={product.id} className="product-card card">
                                <div className="product-badge badge badge-success">{product.badge}</div>
                                <div className="product-image">{product.image}</div>
                                <h3 className="product-name">{product.name}</h3>
                                <div className="product-footer">
                                    <span className="product-price">${product.price}</span>
                                    <button className="btn-quick-add">Add to Cart</button>
                                </div>
                            </Link>
                        ))}
                    </div>
                </div>
            </section>

            {/* CTA Section */}
            <section className="cta-section">
                <div className="container">
                    <div className="cta-card">
                        <h2>Experience AI-Powered Shopping Today</h2>
                        <p>Join thousands of happy customers and discover a smarter way to shop</p>
                        <Link to="/products" className="btn btn-primary btn-lg">
                            Browse Products <ArrowRight size={20} />
                        </Link>
                    </div>
                </div>
            </section>
        </div>
    );
};

export default Home;
