import React from 'react';
import {
    TrendingUp,
    ShoppingCart,
    DollarSign,
    Users,
    ArrowUp,
    ArrowDown,
    Activity
} from 'lucide-react';
import './Dashboard.css';

const Dashboard = () => {
    const stats = [
        {
            label: 'Total Revenue',
            value: '$45,231',
            change: '+20.1%',
            trend: 'up',
            icon: DollarSign,
            color: 'success'
        },
        {
            label: 'Orders',
            value: '2,456',
            change: '+15.3%',
            trend: 'up',
            icon: ShoppingCart,
            color: 'primary'
        },
        {
            label: 'Customers',
            value: '12,345',
            change: '+8.2%',
            trend: 'up',
            icon: Users,
            color: 'accent'
        },
        {
            label: 'Conversion Rate',
            value: '3.24%',
            change: '-2.1%',
            trend: 'down',
            icon: TrendingUp,
            color: 'warning'
        }
    ];

    return (
        <div className="dashboard animate-fade-in">
            <header className="dashboard-header">
                <div>
                    <h1 className="page-title">Dashboard</h1>
                    <p className="page-subtitle">Welcome back! Here's what's happening with your store.</p>
                </div>
                <button className="btn-primary">
                    <Activity size={18} />
                    View Reports
                </button>
            </header>

            <div className="stats-grid">
                {stats.map((stat, index) => {
                    const Icon = stat.icon;
                    const TrendIcon = stat.trend === 'up' ? ArrowUp : ArrowDown;

                    return (
                        <div key={index} className={`stat-card card stat-${stat.color}`}>
                            <div className="stat-header">
                                <div className={`stat-icon-wrapper stat-icon-${stat.color}`}>
                                    <Icon size={24} />
                                </div>
                                <div className={`stat-badge badge-${stat.trend === 'up' ? 'success' : 'error'}`}>
                                    <TrendIcon size={12} />
                                    {stat.change}
                                </div>
                            </div>
                            <div className="stat-body">
                                <h3 className="stat-value">{stat.value}</h3>
                                <p className="stat-label">{stat.label}</p>
                            </div>
                            <div className="stat-footer">
                                <div className="progress-bar">
                                    <div
                                        className={`progress-fill progress-${stat.color}`}
                                        style={{ width: `${Math.abs(parseFloat(stat.change))}%` }}
                                    />
                                </div>
                            </div>
                        </div>
                    );
                })}
            </div>

            <div className="dashboard-grid">
                <div className="card">
                    <h2 className="card-title">Recent Orders</h2>
                    <div className="table-container">
                        <table className="data-table">
                            <thead>
                                <tr>
                                    <th>Order ID</th>
                                    <th>Customer</th>
                                    <th>Status</th>
                                    <th>Amount</th>
                                </tr>
                            </thead>
                            <tbody>
                                {['#ORD-001', '#ORD-002', '#ORD-003', '#ORD-004', '#ORD-005'].map((id, i) => (
                                    <tr key={id}>
                                        <td><span className="text-primary">{id}</span></td>
                                        <td>Customer {i + 1}</td>
                                        <td>
                                            <span className={`badge badge-${i % 2 === 0 ? 'success' : 'warning'}`}>
                                                {i % 2 === 0 ? 'Delivered' : 'Processing'}
                                            </span>
                                        </td>
                                        <td className="font-semibold">${(Math.random() * 500 + 50).toFixed(2)}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>

                <div className="card">
                    <h2 className="card-title">Quick Actions</h2>
                    <div className="quick-actions">
                        <button className="action-btn">
                            <ShoppingCart size={20} />
                            <span>New Order</span>
                        </button>
                        <button className="action-btn">
                            <Users size={20} />
                            <span>Add Customer</span>
                        </button>
                        <button className="action-btn">
                            <TrendingUp size={20} />
                            <span>View Analytics</span>
                        </button>
                        <button className="action-btn">
                            <Activity size={20} />
                            <span>Generate Report</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Dashboard;
