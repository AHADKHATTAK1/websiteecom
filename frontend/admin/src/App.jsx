import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import './App.css';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import APIConfiguration from './pages/APIConfiguration';
import AIConfiguration from './pages/AIConfiguration';
import Products from './pages/Products';
import Orders from './pages/Orders';
import Analytics from './pages/Analytics';
import Login from './pages/Login';
import Register from './pages/Register';
import ForgotPassword from './pages/ForgotPassword';
import ThemeEditor from './pages/ThemeEditor';
import Integrations from './pages/Integrations';

// Protected Route Component
const ProtectedRoute = ({ children }) => {
    const token = localStorage.getItem('admin_token');
    const user = JSON.parse(localStorage.getItem('admin_user') || '{}');

    if (!token || user.role !== 'admin') {
        return <Navigate to="/login" replace />;
    }

    return children;
};

function App() {
    const [sidebarOpen, setSidebarOpen] = useState(true);
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    useEffect(() => {
        const token = localStorage.getItem('admin_token');
        setIsAuthenticated(!!token);
    }, []);

    const MainLayout = ({ children }) => (
        <div className="app">
            <Sidebar isOpen={sidebarOpen} onToggle={() => setSidebarOpen(!sidebarOpen)} />
            <main className={`main-content ${sidebarOpen ? 'sidebar-open' : 'sidebar-closed'}`}>
                {children}
            </main>
        </div>
    );

    return (
        <Router>
            <Routes>
                {/* Auth Routes */}
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/forgot-password" element={<ForgotPassword />} />

                {/* Protected Admin Routes */}
                <Route path="/dashboard" element={<ProtectedRoute><MainLayout><Dashboard /></MainLayout></ProtectedRoute>} />
                <Route path="/integrations" element={<ProtectedRoute><MainLayout><Integrations /></MainLayout></ProtectedRoute>} />
                <Route path="/api-configuration" element={<ProtectedRoute><MainLayout><APIConfiguration /></MainLayout></ProtectedRoute>} />
                <Route path="/ai-configuration" element={<ProtectedRoute><MainLayout><AIConfiguration /></MainLayout></ProtectedRoute>} />
                <Route path="/products" element={<ProtectedRoute><MainLayout><Products /></MainLayout></ProtectedRoute>} />
                <Route path="/orders" element={<ProtectedRoute><MainLayout><Orders /></MainLayout></ProtectedRoute>} />
                <Route path="/analytics" element={<ProtectedRoute><MainLayout><Analytics /></MainLayout></ProtectedRoute>} />
                <Route path="/customize" element={<ProtectedRoute><MainLayout><ThemeEditor /></MainLayout></ProtectedRoute>} />

                {/* Redirects */}
                <Route path="/" element={<Navigate to="/dashboard" replace />} />
                <Route path="*" element={<Navigate to="/dashboard" replace />} />
            </Routes>
        </Router>
    );
}

export default App;
