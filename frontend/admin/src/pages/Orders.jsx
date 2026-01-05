import React from 'react';
import { ShoppingCart } from 'lucide-react';

const Orders = () => {
    return (
        <div className="animate-fade-in">
            <h1 className="page-title">Orders</h1>
            <p className="page-subtitle">Manage customer orders</p>
            <div className="card" style={{ marginTop: '2rem', padding: '3rem', textAlign: 'center' }}>
                <ShoppingCart size={64} style={{ margin: '0 auto 1rem', color: 'var(--primary-400)' }} />
                <h2>Order Management</h2>
                <p style={{ color: 'var(--text-secondary)', marginTop: '0.5rem' }}>
                    Order management interface coming soon
                </p>
            </div>
        </div>
    );
};

export default Orders;
