/**
 * Axios instance for API calls
 */
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Request interceptor for adding auth token
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// Response interceptor for handling errors
api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;

        // If 401 and not already retrying, try to refresh token
        if (error.response?.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;

            try {
                const refreshToken = localStorage.getItem('refresh_token');
                const response = await axios.post(`${API_BASE_URL}/api/auth/token/refresh/`, {
                    refresh: refreshToken,
                });

                const { access } = response.data;
                localStorage.setItem('access_token', access);

                originalRequest.headers.Authorization = `Bearer ${access}`;
                return api(originalRequest);
            } catch (refreshError) {
                // Refresh failed, redirect to login
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
                window.location.href = '/login';
                return Promise.reject(refreshError);
            }
        }

        return Promise.reject(error);
    }
);

export default api;

// API service functions
export const authAPI = {
    login: (email, password) => api.post('/api/auth/login/', { email, password }),
    register: (userData) => api.post('/api/auth/register/', userData),
    getProfile: () => api.get('/api/auth/profile/'),
};

export const apiIntegrationsAPI = {
    getProviders: () => api.get('/api/integrations/providers/'),
    getConfigurations: () => api.get('/api/integrations/configurations/'),
    createConfiguration: (data) => api.post('/api/integrations/configurations/', data),
    testConnection: (id) => api.post(`/api/integrations/configurations/${id}/test_connection/`),
    getLogs: (id) => api.get(`/api/integrations/configurations/${id}/logs/`),
};

export const chatbotAPI = {
    getConfig: () => api.get('/api/chatbot/config/'),
    createConfig: (data) => api.post('/api/chatbot/config/', data),
    testConnection: (id) => api.post(`/api/chatbot/config/${id}/test_connection/`),
    sendMessage: (data) => api.post('/api/chatbot/chat/', data),
};
