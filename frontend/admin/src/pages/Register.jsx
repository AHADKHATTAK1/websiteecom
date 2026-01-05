import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import api from '../services/api';
import './Register.css';

function Register() {
    const [formData, setFormData] = useState({
        first_name: '',
        last_name: '',
        email: '',
        password: '',
        password2: '',
        role: 'admin' // Forced for this registration page
    });
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (formData.password !== formData.password2) {
            setError('Passwords do not match');
            return;
        }
        setError('');
        setLoading(true);

        try {
            await api.post('/auth/register/', formData);
            navigate('/login');
        } catch (err) {
            setError(err.response?.data?.email?.[0] || err.response?.data?.password?.[0] || 'Registration failed.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="admin-register-container">
            <div className="glass-morphism register-card">
                <div className="register-header">
                    <div className="admin-icon">🧱</div>
                    <h1>Create Admin</h1>
                    <p>Register a new management account</p>
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
                    <span>or register with email</span>
                </div>

                <form onSubmit={handleSubmit} className="admin-form">
                    <div className="form-row">
                        <div className="form-input-group">
                            <label>First Name</label>
                            <input type="text" name="first_name" value={formData.first_name} onChange={handleChange} placeholder="John" required />
                        </div>
                        <div className="form-input-group">
                            <label>Last Name</label>
                            <input type="text" name="last_name" value={formData.last_name} onChange={handleChange} placeholder="Doe" required />
                        </div>
                    </div>

                    <div className="form-input-group">
                        <label>Email Address</label>
                        <input type="email" name="email" value={formData.email} onChange={handleChange} placeholder="admin@example.com" required />
                    </div>

                    <div className="form-input-group">
                        <label>Password</label>
                        <input type="password" name="password" value={formData.password} onChange={handleChange} placeholder="Password" required />
                    </div>

                    <div className="form-input-group">
                        <label>Confirm Password</label>
                        <input type="password" name="password2" value={formData.password2} onChange={handleChange} placeholder="Repeat password" required />
                    </div>

                    <button type="submit" className="btn-primary" disabled={loading}>
                        {loading ? 'Creating Account...' : 'Create Admin Account'}
                    </button>
                </form>

                <div className="register-footer">
                    <p>Already have an account? <Link to="/login">Sign In</Link></p>
                </div>
            </div>
        </div>
    );
}

export default Register;
