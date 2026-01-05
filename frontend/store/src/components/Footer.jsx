import React from 'react';

const Footer = () => {
    return (
        <footer style={{
            background: '#1e293b',
            color: 'white',
            padding: '4rem 0 2rem',
            marginTop: 'auto'
        }}>
            <div className="container">
                <div style={{
                    display: 'grid',
                    gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
                    gap: '3rem',
                    marginBottom: '3rem'
                }}>
                    <div>
                        <h3 style={{ marginBottom: '1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                            <span>♻️</span>
                            ERP E-Recycle Solutions
                        </h3>
                        <p style={{ color: '#94a3b8', lineHeight: '1.7', marginBottom: '1rem' }}>
                            Smart ERP Solutions for Responsible E-Waste Recycling. Protecting the planet through technology-driven recycling.
                        </p>
                        <div style={{ display: 'flex', gap: '1rem', fontSize: '1.5rem' }}>
                            <a href="#" aria-label="Facebook">📘</a>
                            <a href="#" aria-label="Instagram">📷</a>
                            <a href="#" aria-label="Twitter">🐦</a>
                        </div>
                    </div>

                    <div>
                        <h4 style={{ marginBottom: '1.5rem' }}>Shop</h4>
                        <ul style={{ listStyle: 'none', padding: 0 }}>
                            <li style={{ marginBottom: '0.75rem' }}>
                                <a href="/products" style={{ color: '#cbd5e1', textDecoration: 'none' }}>All Products</a>
                            </li>
                            <li style={{ marginBottom: '0.75rem' }}>
                                <a href="/products?category=electronics" style={{ color: '#cbd5e1', textDecoration: 'none' }}>Electronics</a>
                            </li>
                            <li style={{ marginBottom: '0.75rem' }}>
                                <a href="/products?category=fashion" style={{ color: '#cbd5e1', textDecoration: 'none' }}>Fashion</a>
                            </li>
                            <li style={{ marginBottom: '0.75rem' }}>
                                <a href="/products?featured=true" style={{ color: '#cbd5e1', textDecoration: 'none' }}>Featured Items</a>
                            </li>
                        </ul>
                    </div>

                    <div>
                        <h4 style={{ marginBottom: '1.5rem' }}>Support</h4>
                        <ul style={{ listStyle: 'none', padding: 0 }}>
                            <li style={{ marginBottom: '0.75rem' }}>
                                <a href="/help" style={{ color: '#cbd5e1', textDecoration: 'none' }}>Help Center</a>
                            </li>
                            <li style={{ marginBottom: '0.75rem' }}>
                                <a href="/shipping" style={{ color: '#cbd5e1', textDecoration: 'none' }}>Shipping & Returns</a>
                            </li>
                            <li style={{ marginBottom: '0.75rem' }}>
                                <a href="/track-order" style={{ color: '#cbd5e1', textDecoration: 'none' }}>Track Order</a>
                            </li>
                            <li style={{ marginBottom: '0.75rem' }}>
                                <a href="/contact" style={{ color: '#cbd5e1', textDecoration: 'none' }}>Contact Us</a>
                            </li>
                        </ul>
                    </div>

                    <div>
                        <h4 style={{ marginBottom: '1.5rem' }}>Contact</h4>
                        <ul style={{ listStyle: 'none', padding: 0 }}>
                            <li style={{ marginBottom: '0.75rem', color: '#cbd5e1' }}>
                                📧 support@khattakstore.com
                            </li>
                            <li style={{ marginBottom: '0.75rem', color: '#cbd5e1' }}>
                                📞 +92 300 1234567
                            </li>
                            <li style={{ marginBottom: '0.75rem', color: '#cbd5e1' }}>
                                📍 Islamabad, Pakistan
                            </li>
                        </ul>
                    </div>
                </div>

                <div style={{
                    borderTop: '1px solid #334155',
                    paddingTop: '2rem',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    flexWrap: 'wrap',
                    gap: '1rem',
                    color: '#64748b',
                    fontSize: '0.875rem'
                }}>
                    <span>© 2026 Khattak Inc. All rights reserved.</span>
                    <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
                        <a href="/privacy" style={{ color: '#64748b', textDecoration: 'none' }}>Privacy Policy</a>
                        <span>•</span>
                        <a href="/terms" style={{ color: '#64748b', textDecoration: 'none' }}>Terms of Service</a>
                        <span>•</span>
                        <a href="/cookies" style={{ color: '#64748b', textDecoration: 'none' }}>Cookie Policy</a>
                    </div>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
