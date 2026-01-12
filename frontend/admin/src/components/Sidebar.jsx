import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import {
    LayoutDashboard,
    ShoppingBag,
    ShoppingCart,
    Plug,
    Bot,
    BarChart3,
    Settings,
    Zap,
    Menu,
    X,
    Paintbrush
} from 'lucide-react';
import './Sidebar.css';

const Sidebar = ({ isOpen, onToggle }) => {
    const location = useLocation();

    const menuItems = [
        { path: '/dashboard', icon: LayoutDashboard, label: 'Dashboard' },
        { path: '/products', icon: ShoppingBag, label: 'Products' },
        { path: '/orders', icon: ShoppingCart, label: 'Orders' },
        { path: '/integrations', icon: Plug, label: 'Integrations' },
        { path: '/ai-configuration', icon: Bot, label: 'AI Chatbot' },
        { path: '/analytics', icon: BarChart3, label: 'Analytics' },
        { path: '/customize', icon: Paintbrush, label: 'Customize' },
    ];

    return (
        <aside className={`sidebar ${isOpen ? 'open' : 'closed'}`}>
            <div className="sidebar-header">
                <div className="logo">
                    <span className="logo-icon">🏗️</span>
                    {isOpen && <span className="logo-text">AL DAR Admin</span>}
                </div>
                <button className="toggle-btn" onClick={onToggle}>
                    {isOpen ? <ChevronLeft size={20} /> : <ChevronRight size={20} />}
                </button>
            </div>

            <nav className="sidebar-nav">
                {menuItems.map((item) => {
                    const Icon = item.icon;
                    const isActive = location.pathname === item.path;

                    return (
                        <Link
                            key={item.path}
                            to={item.path}
                            className={`nav-item ${isActive ? 'active' : ''}`}
                        >
                            <Icon size={20} className="nav-icon" />
                            {isOpen && <span className="nav-label">{item.label}</span>}
                            {isActive && <div className="active-indicator" />}
                        </Link>
                    );
                })}
            </nav>

            <div className="sidebar-footer">
                <div className="user-profile">
                    <div className="avatar">
                        <span>A</span>
                    </div>
                    {isOpen && (
                        <div className="user-info">
                            <p className="user-name">Admin</p>
                            <p className="user-email">admin@example.com</p>
                        </div>
                    )}
                </div>
            </div>
        </aside>
    );
};

export default Sidebar;
