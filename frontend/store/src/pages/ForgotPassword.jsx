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
        // Simulate API call for now
        setTimeout(() => {
            setSubmitted(true);
            setLoading(false);
        }, 1500);
    };

    return (
        <div className="store-forgot-container">
            <div className="glass-morphism forgot-card">
                {!submitted ? (
                    <>
                        <div className="forgot-header">
                            <div className="store-icon">✨</div>
                            <h1>Reset Password</h1>
                            <p>We'll send you instructions to reset your password</p>
                        </div>

                        <form onSubmit={handleSubmit} className="store-form">
                            <div className="form-input-group">
                                <label>Email Address</label>
                                <input
                                    type="email"
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                    placeholder="name@example.com"
                                    required
                                />
                            </div>

                            <button type="submit" className="btn-gradient" disabled={loading}>
                                {loading ? 'Sending...' : 'Send Reset Instructions'}
                            </button>
                        </form>
                    </>
                ) : (
                    <div className="success-state">
                        <div className="success-icon">💌</div>
                        <h1>Check Your Inbox</h1>
                        <p>We've sent a recovery link to <strong>{email}</strong>. Please check your email.</p>
                        <Link to="/login" className="btn-outline">Back to Login</Link>
                    </div>
                )}

                <div className="forgot-footer">
                    <p>Suddenly remembered? <Link to="/login">Sign In</Link></p>
                </div>
            </div>
        </div>
    );
}

export default ForgotPassword;
