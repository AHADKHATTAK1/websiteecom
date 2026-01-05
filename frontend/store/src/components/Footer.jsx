import React from 'react';

const Footer = () => {
    const [theme, setTheme] = React.useState(null);

    React.useEffect(() => {
        const fetchTheme = async () => {
            try {
                const response = await fetch('http://localhost:8000/api/admin/theme/');
                const data = await response.json();
                setTheme(data);
            } catch (error) {
                console.error("Error fetching theme for footer:", error);
            }
        };
        fetchTheme();
    }, []);

    return (
        <footer style={{
            background: 'var(--text-dark)', // Inversed for footer
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
                        <h3 style={{
                            marginBottom: '1.5rem',
                            fontFamily: theme?.heading_font,
                            display: 'flex',
                            alignItems: 'center',
                            gap: '0.5rem'
                        }}>
                            {theme?.logo ? (
                                <img src={theme.logo} alt="Logo" style={{ height: '32px', filter: 'brightness(0) invert(1)' }} />
                            ) : (
                                <span>🛍️</span>
                            )}
                            {theme?.site_name || 'AI Store'}
                        </h3>
                        <p style={{ color: '#94a3b8', lineHeight: '1.7' }}>
                            {theme?.banner_subtext || "Your intelligent shopping destination powered by AI. Experience the future of e-commerce today."}
                        </p>
                    </div>
                    <div>
                        <h4 style={{ marginBottom: '1.5rem', fontFamily: theme?.heading_font }}>Shop</h4>
                        <ul style={{ listStyle: 'none', padding: 0 }}>
                            <li style={{ marginBottom: '0.75rem' }}>
                                <a href="/products" style={{ color: '#cbd5e1', textDecoration: 'none', transition: 'color 0.2s' }}>All Products</a>
                            </li>
                            <li style={{ marginBottom: '0.75rem' }}>
                                <a href="#" style={{ color: '#cbd5e1', textDecoration: 'none', transition: 'color 0.2s' }}>Featured Collections</a>
                            </li>
                            <li style={{ marginBottom: '0.75rem' }}>
                                <a href="#" style={{ color: '#cbd5e1', textDecoration: 'none', transition: 'color 0.2s' }}>New Arrivals</a>
                            </li>
                        </ul>
                    </div>
                    <div>
                        <h4 style={{ marginBottom: '1.5rem', fontFamily: theme?.heading_font }}>Support</h4>
                        <ul style={{ listStyle: 'none', padding: 0 }}>
                            <li style={{ marginBottom: '0.75rem' }}>
                                <a href="#" style={{ color: '#cbd5e1', textDecoration: 'none', transition: 'color 0.2s' }}>Help Center</a>
                            </li>
                            <li style={{ marginBottom: '0.75rem' }}>
                                <a href="#" style={{ color: '#cbd5e1', textDecoration: 'none', transition: 'color 0.2s' }}>Shipping & Returns</a>
                            </li>
                            <li style={{ marginBottom: '0.75rem' }}>
                                <a href="#" style={{ color: '#cbd5e1', textDecoration: 'none', transition: 'color 0.2s' }}>Contact Us</a>
                            </li>
                        </ul>
                    </div>
                    <div>
                        <h4 style={{ marginBottom: '1.5rem', fontFamily: theme?.heading_font }}>Contact</h4>
                        <ul style={{ listStyle: 'none', padding: 0 }}>
                            <li style={{ marginBottom: '0.75rem', color: '#cbd5e1' }}>
                                {theme?.contact_email || 'support@aistore.com'}
                            </li>
                            <li style={{ marginBottom: '0.75rem', color: '#cbd5e1' }}>
                                {theme?.contact_phone || '+1 (555) 123-4567'}
                            </li>
                            <li style={{ marginBottom: '0.75rem', color: '#cbd5e1' }}>
                                {theme?.address || '123 Innovation Dr, Tech City'}
                            </li>
                        </ul>
                    </div>
                </div>
                <div style={{
                    borderTop: '1px solid #334155',
                    paddingTop: '2rem',
                    textAlign: 'center',
                    color: '#64748b',
                    fontSize: '0.875rem',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    flexWrap: 'wrap',
                    gap: '1rem'
                }}>
                    <span>© {new Date().getFullYear()} {theme?.site_name || 'AI Store'}. All rights reserved.</span>
                    <span style={{ display: 'flex', gap: '1rem' }}>
                        <a href="#" style={{ color: '#64748b' }}>Privacy Policy</a>
                        <a href="#" style={{ color: '#64748b' }}>Terms of Service</a>
                    </span>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
