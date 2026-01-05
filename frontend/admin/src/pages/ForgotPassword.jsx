import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './ForgotPassword.css';

function ForgotPassword() {
    const [email, setEmail] = useState('');
    const [submitted, setSubmitted] = useState(false);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        // Simulate API call for now (implement in backend later)
        setTimeout(() => {
            setSubmitted(true);
            setLoading(false);
        }, 1500);
    };

    return (
        <div className="admin-forgot-container">
            <div className="glass-morphism forgot-card">
                {!submitted ? (
                    <>
                        <div className="forgot-header">
                            <div className="admin-icon">🔑</div>
                            <h1>Restore Access</h1>
                            <p>Enter your email to receive reset instructions</p>
                        </div>

                        <form onSubmit={handleSubmit} className="admin-form">
                            <div className="form-input-group">
                                <label>Email Address</label>
                                <input
                                    type="email"
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                    placeholder="admin@example.com"
                                    required
                                />
                            </div>

                            <button type="submit" className="btn-primary" disabled={loading}>
                                {loading ? 'Sending Request...' : 'Send Reset Link'}
                            </button>
                        </form>
                    </>
                ) : (
                    <div className="success-state">
                        <div className="success-icon">📧</div>
                        <h1>Check Your Email</h1>
                        <p>If an account exists for <strong>{email}</strong>, you will receive password reset instructions shortly.</p>
                        <Link to="/login" className="btn-secondary">Return to Login</Link>
                    </div>
                )}

                <div className="forgot-footer">
                    <Link to="/login">Back to Login</Link>
                </div>
            </div>
        </div>
    );
}

export default ForgotPassword;
