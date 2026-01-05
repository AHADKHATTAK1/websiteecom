import React from 'react';
import { Link } from 'react-router-dom';
import { ShoppingCart, Search, User, Menu } from 'lucide-react';
import './Header.css';

const Header = ({ cartCount }) => {
    const [theme, setTheme] = React.useState(null);

    React.useEffect(() => {
        const fetchTheme = async () => {
            try {
                // We'll import this dynamically or assume it's passed or available
                // For now let's use the API service logic directly or props
                // Better to use the hook pattern if available, but here we can just fetch
                const response = await fetch('http://localhost:8000/api/admin/theme/');
                const data = await response.json();
                setTheme(data);
            } catch (error) {
                console.error("Error fetching theme for header:", error);
            }
        };
        fetchTheme();
    }, []);

    return (
        <header className="header">
            <div className="container">
                <div className="header-content">
                    <Link to="/" className="logo">
                        {theme?.logo ? (
                            <img src={theme.logo} alt={theme.site_name} className="logo-image" style={{ height: '40px' }} />
                        ) : (
                            <span className="logo-icon">🛍️</span>
                        )}
                        <span className="logo-text" style={{ fontFamily: theme?.heading_font }}>
                            {theme?.site_name || "ERP E-Recycle"}
                        </span>
                    </Link>

                    <nav className="nav">
                        <Link to="/" className="nav-link">Home</Link>
                        <Link to="/products" className="nav-link">Products</Link>
                        <Link to="/about" className="nav-link">About</Link>
                        <Link to="/contact" className="nav-link">Contact</Link>
                    </nav>

                    <div className="header-actions">
                        <button className="icon-btn">
                            <Search size={20} />
                        </button>
                        <button className="icon-btn">
                            <User size={20} />
                        </button>
                        <Link to="/cart" className="icon-btn cart-btn">
                            <ShoppingCart size={20} />
                            {cartCount > 0 && <span className="cart-badge">{cartCount}</span>}
                        </Link>
                    </div>
                </div>
            </div>
        </header>
    );
};

export default Header;
