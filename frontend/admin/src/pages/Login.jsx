import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import api from '../services/api';
import './Login.css';

function Login() {
    const [formData, setFormData] = useState({ email: '', password: '' });
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            const response = await api.post('/api/auth/login/', formData);
            localStorage.setItem('admin_token', response.data.tokens.access);
            localStorage.setItem('admin_refresh', response.data.tokens.refresh);
            localStorage.setItem('admin_user', JSON.stringify(response.data.user));

            if (response.data.user.role === 'admin') {
                navigate('/dashboard');
            } else {
                setError('Access denied. Admin privileges required.');
            }
        } catch (err) {
            setError(err.response?.data?.error || 'Login failed. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="admin-login-container">
            <div className="glass-morphism login-card">
                <div className="login-header">
                    <div className="admin-icon">🛍️</div>
                    <h1>Khattak Store Admin</h1>
                    <p>Merchant Management Portal</p>
                </div>


                {error && (
                    <div className="alert-error">
                        <span>❌</span> {error}
                    </div>
                )}

                <div className="social-login">
                    <button type="button" className="btn-social google">
                        <span className="social-icon">G</span> Continue with Google
                    </button>
                    <button type="button" className="btn-social apple">
                        <span className="social-icon"></span> Continue with Apple
                    </button>
                </div>

                <div className="divider">
                    <span>or continue with email</span>
                </div>

                <form onSubmit={handleSubmit} className="admin-form">
                    <div className="form-input-group">
                        <label>Email Address</label>
                        <input
                            type="email"
                            name="email"
                            value={formData.email}
                            onChange={handleChange}
                            placeholder="admin@example.com"
                            required
                        />
                    </div>

                    <div className="form-input-group">
                        <label>Password</label>
                        <input
                            type="password"
                            name="password"
                            value={formData.password}
                            onChange={handleChange}
                            placeholder="••••••••"
                            required
                        />
                    </div>

                    <div className="form-actions">
                        <Link to="/forgot-password">Forgot Password?</Link>
                    </div>

                    <button type="submit" className="btn-primary" disabled={loading}>
                        {loading ? 'Authenticating...' : 'Sign In'}
                    </button>
                </form>

                <div className="login-footer">
                    <p>Don't have an account? <Link to="/register">Create one</Link></p>
                </div>
            </div>
        </div>
    );
}

export default Login;
