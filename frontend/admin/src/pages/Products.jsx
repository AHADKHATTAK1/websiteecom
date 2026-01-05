import React from 'react';
import { Package } from 'lucide-react';

const Products = () => {
    return (
        <div className="animate-fade-in">
            <h1 className="page-title">Products</h1>
            <p className="page-subtitle">Manage your product catalog</p>
            <div className="card" style={{ marginTop: '2rem', padding: '3rem', textAlign: 'center' }}>
                <Package size={64} style={{ margin: '0 auto 1rem', color: 'var(--primary-400)' }} />
                <h2>Product Management</h2>
                <p style={{ color: 'var(--text-secondary)', marginTop: '0.5rem' }}>
                    Product management interface coming soon
                </p>
            </div>
        </div>
    );
};

export default Products;
