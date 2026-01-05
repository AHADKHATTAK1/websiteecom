import React from 'react';
import { BarChart3 } from 'lucide-react';

const Analytics = () => {
    return (
        <div className="animate-fade-in">
            <h1 className="page-title">Analytics</h1>
            <p className="page-subtitle">View business insights and metrics</p>
            <div className="card" style={{ marginTop: '2rem', padding: '3rem', textAlign: 'center' }}>
                <BarChart3 size={64} style={{ margin: '0 auto 1rem', color: 'var(--primary-400)' }} />
                <h2>Analytics Dashboard</h2>
                <p style={{ color: 'var(--text-secondary)', marginTop: '0.5rem' }}>
                    Analytics interface coming soon
                </p>
            </div>
        </div>
    );
};

export default Analytics;
