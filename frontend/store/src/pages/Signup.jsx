import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import api from '../services/api';
import './Signup.css';

function Signup() {
    const [formData, setFormData] = useState({
        first_name: '',
        last_name: '',
        email: '',
        password: '',
        password2: ''
    });
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');

        // Validation
        if (formData.password !== formData.password2) {
            setError('Passwords do not match');
            return;
        }

        if (formData.password.length < 8) {
            setError('Password must be at least 8 characters');
            return;
        }

        setLoading(true);

        try {
            const response = await api.post('/auth/register/', {
                first_name: formData.first_name,
                last_name: formData.last_name,
                email: formData.email,
                password: formData.password
            });

            // Store tokens
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            localStorage.setItem('user', JSON.stringify(response.data.user));

            // Redirect to home
            navigate('/');
        } catch (err) {
            const errorMsg = err.response?.data?.email?.[0] ||
                err.response?.data?.detail ||
                'Signup failed. Please try again.';
            setError(errorMsg);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="signup-container">
            <div className="signup-box">
                <div className="signup-header">
                    <h1>Create Account 🎉</h1>
                    <p>Join us and start shopping</p>
                </div>

                {error && (
                    <div className="error-message">
                        <span className="error-icon">⚠️</span>
                        {error}
                    </div>
                )}

                <form onSubmit={handleSubmit} className="signup-form">
                    <div className="form-row">
                        <div className="form-group">
                            <label htmlFor="first_name">First Name</label>
                            <input
                                type="text"
                                id="first_name"
                                name="first_name"
                                value={formData.first_name}
                                onChange={handleChange}
                                placeholder="John"
                                required
                                autoFocus
                            />
                        </div>

                        <div className="form-group">
                            <label htmlFor="last_name">Last Name</label>
                            <input
                                type="text"
                                id="last_name"
                                name="last_name"
                                value={formData.last_name}
                                onChange={handleChange}
                                placeholder="Doe"
                                required
                            />
                        </div>
                    </div>

                    <div className="form-group">
                        <label htmlFor="email">Email Address</label>
                        <input
                            type="email"
                            id="email"
                            name="email"
                            value={formData.email}
                            onChange={handleChange}
                            placeholder="john.doe@example.com"
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="password">Password</label>
                        <input
                            type="password"
                            id="password"
                            name="password"
                            value={formData.password}
                            onChange={handleChange}
                            placeholder="At least 8 characters"
                            required
                            minLength="8"
                        />
                        <small className="password-hint">
                            Use 8+ characters with letters, numbers & symbols
                        </small>
                    </div>

                    <div className="form-group">
                        <label htmlFor="password2">Confirm Password</label>
                        <input
                            type="password"
                            id="password2"
                            name="password2"
                            value={formData.password2}
                            onChange={handleChange}
                            placeholder="Re-enter your password"
                            required
                        />
                    </div>

                    <div className="terms-checkbox">
                        <label>
                            <input type="checkbox" required />
                            <span>
                                I agree to the <a href="/terms">Terms of Service</a> and{' '}
                                <a href="/privacy">Privacy Policy</a>
                            </span>
                        </label>
                    </div>

                    <button type="submit" className="signup-btn" disabled={loading}>
                        {loading ? 'Creating account...' : 'Create Account'}
                    </button>
                </form>

                <div className="login-prompt">
                    Already have an account? <Link to="/login">Login</Link>
                </div>

                <div className="social-signup">
                    <div className="divider">
                        <span>Or sign up with</span>
                    </div>
                    <div className="social-buttons">
                        <button className="social-btn google-btn">
                            <span className="social-icon">🔵</span>
                            Google
                        </button>
                        <button className="social-btn facebook-btn">
                            <span className="social-icon">📘</span>
                            Facebook
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Signup;
