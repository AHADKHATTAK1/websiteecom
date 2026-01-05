import React, { useState, useEffect } from 'react';
import api from '../services/api';
import './ThemeEditor.css';

// Popular Google Fonts
const GOOGLE_FONTS = [
    'Inter', 'Roboto', 'Open Sans', 'Lato', 'Montserrat', 'Poppins',
    'Playfair Display', 'Merriweather', 'Lora', 'Raleway', 'Nunito',
    'Ubuntu', 'Work Sans', 'Fira Sans', 'Mukta', 'Quicksand'
];

function ThemeEditor() {
    const [theme, setTheme] = useState(null);
    const [presets, setPresets] = useState([]);
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);
    const [message, setMessage] = useState('');
    const [previewDevice, setPreviewDevice] = useState('desktop');
    const [activeTab, setActiveTab] = useState('colors');

    useEffect(() => {
        fetchTheme();
        fetchPresets();
        loadGoogleFonts();
    }, []);

    const fetchTheme = async () => {
        try {
            const response = await api.get('/admin/theme/');
            setTheme(response.data);
        } catch (error) {
            console.error('Error fetching theme:', error);
        } finally {
            setLoading(false);
        }
    };

    const fetchPresets = async () => {
        try {
            const response = await api.get('/admin/theme/presets/');
            setPresets(response.data);
        } catch (error) {
            console.error('Error fetching presets:', error);
        }
    };

    const loadGoogleFonts = () => {
        const link = document.createElement('link');
        link.href = `https://fonts.googleapis.com/css2?${GOOGLE_FONTS.map(f => `family=${f.replace(/ /g, '+')}:wght@300;400;600;700`).join('&')}&display=swap`;
        link.rel = 'stylesheet';
        document.head.appendChild(link);
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setTheme(prev => ({ ...prev, [name]: value }));
    };

    const handleSave = async () => {
        setSaving(true);
        setMessage('');
        try {
            await api.post('/admin/theme/update/', theme);
            setMessage('✅ Theme saved successfully!');
            setTimeout(() => setMessage(''), 3000);
        } catch (error) {
            setMessage('❌ Error saving theme.');
        } finally {
            setSaving(false);
        }
    };

    const applyPreset = async (presetId) => {
        try {
            const response = await api.post('/admin/theme/apply-preset/', { preset_id: presetId });
            setTheme(response.data);
            setMessage(`✅ Applied ${presetId} preset!`);
            setTimeout(() => setMessage(''), 3000);
        } catch (error) {
            setMessage('❌ Error applying preset.');
        }
    };

    const handleImageUpload = async (e, type) => {
        const file = e.target.files[0];
        if (!file) return;

        const formData = new FormData();
        formData.append('file', file);
        formData.append('type', type);

        try {
            const response = await api.post('/admin/theme/upload/', formData, {
                headers: { 'Content-Type': 'multipart/form-data' }
            });
            setTheme(response.data);
            setMessage(`✅ ${type} uploaded!`);
            setTimeout(() => setMessage(''), 3000);
        } catch (error) {
            setMessage(`❌ Error uploading ${type}.`);
        }
    };

    if (loading) return <div className="loading">Loading Editor...</div>;

    const deviceSizes = {
        desktop: { width: '100%', label: '🖥️ Desktop' },
        tablet: { width: '768px', label: '📱 Tablet' },
        mobile: { width: '375px', label: '📱 Mobile' }
    };

    return (
        <div className="advanced-theme-editor">
            <div className="editor-sidebar">
                <div className="sidebar-header">
                    <h2>🎨 Theme Customizer</h2>
                    <p>Professional design controls</p>
                </div>

                {/* Tab Navigation */}
                <div className="tab-nav">
                    <button className={activeTab === 'colors' ? 'active' : ''} onClick={() => setActiveTab('colors')}>Colors</button>
                    <button className={activeTab === 'typography' ? 'active' : ''} onClick={() => setActiveTab('typography')}>Fonts</button>
                    <button className={activeTab === 'layout' ? 'active' : ''} onClick={() => setActiveTab('layout')}>Layout</button>
                    <button className={activeTab === 'presets' ? 'active' : ''} onClick={() => setActiveTab('presets')}>Presets</button>
                </div>

                {/* Colors Tab */}
                {activeTab === 'colors' && (
                    <div className="tab-content">
                        <h3>Brand Colors</h3>
                        <div className="field">
                            <label>Primary Color</label>
                            <div className="color-picker-group">
                                <input type="color" name="primary_color" value={theme?.primary_color || '#6366f1'} onChange={handleChange} />
                                <span>{theme?.primary_color}</span>
                            </div>
                        </div>
                        <div className="field">
                            <label>Secondary Color</label>
                            <div className="color-picker-group">
                                <input type="color" name="secondary_color" value={theme?.secondary_color || '#4f46e5'} onChange={handleChange} />
                                <span>{theme?.secondary_color}</span>
                            </div>
                        </div>
                        <div className="field">
                            <label>Accent Color</label>
                            <div className="color-picker-group">
                                <input type="color" name="accent_color" value={theme?.accent_color || '#f59e0b'} onChange={handleChange} />
                                <span>{theme?.accent_color}</span>
                            </div>
                        </div>
                    </div>
                )}

                {/* Typography Tab */}
                {activeTab === 'typography' && (
                    <div className="tab-content">
                        <h3>Typography</h3>
                        <div className="field">
                            <label>Heading Font</label>
                            <select name="heading_font" value={theme?.heading_font || 'Inter'} onChange={handleChange} style={{ fontFamily: theme?.heading_font }}>
                                {GOOGLE_FONTS.map(font => (
                                    <option key={font} value={font} style={{ fontFamily: font }}>{font}</option>
                                ))}
                            </select>
                        </div>
                        <div className="field">
                            <label>Body Font</label>
                            <select name="body_font" value={theme?.body_font || 'Inter'} onChange={handleChange} style={{ fontFamily: theme?.body_font }}>
                                {GOOGLE_FONTS.map(font => (
                                    <option key={font} value={font} style={{ fontFamily: font }}>{font}</option>
                                ))}
                            </select>
                        </div>
                        <div className="field">
                            <label>Heading Size: {theme?.heading_size || '2.5rem'}</label>
                            <input type="range" name="heading_size" min="1.5" max="4" step="0.1" value={parseFloat(theme?.heading_size) || 2.5} onChange={(e) => handleChange({ target: { name: 'heading_size', value: e.target.value + 'rem' } })} />
                        </div>
                        <div className="field">
                            <label>Logo Upload</label>
                            <input type="file" accept="image/*" onChange={(e) => handleImageUpload(e, 'logo')} />
                            {theme?.logo && <img src={theme.logo} alt="Logo" className="logo-preview" />}
                        </div>
                    </div>
                )}

                {/* Layout Tab */}
                {activeTab === 'layout' && (
                    <div className="tab-content">
                        <h3>Layout & Style</h3>
                        <div className="field">
                            <label>Border Radius: {theme?.border_radius || '12px'}</label>
                            <input type="range" name="border_radius" min="0" max="24" value={parseInt(theme?.border_radius) || 12} onChange={(e) => handleChange({ target: { name: 'border_radius', value: e.target.value + 'px' } })} />
                        </div>
                        <div className="field">
                            <label>Button Radius: {theme?.button_radius || '8px'}</label>
                            <input type="range" name="button_radius" min="0" max="30" value={parseInt(theme?.button_radius) || 8} onChange={(e) => handleChange({ target: { name: 'button_radius', value: e.target.value + 'px' } })} />
                        </div>
                        <div className="field">
                            <label>Banner Text</label>
                            <textarea name="banner_text" value={theme?.banner_text || ''} onChange={handleChange} rows="3" />
                        </div>
                    </div>
                )}

                {/* Presets Tab */}
                {activeTab === 'presets' && (
                    <div className="tab-content">
                        <h3>Theme Presets</h3>
                        <div className="presets-grid">
                            {presets.map(preset => (
                                <div key={preset.id} className="preset-card" onClick={() => applyPreset(preset.id)}>
                                    <h4>{preset.name}</h4>
                                    <p>{preset.description}</p>
                                    <button className="btn-apply">Apply</button>
                                </div>
                            ))}
                        </div>
                    </div>
                )}

                <div className="editor-footer">
                    {message && <div className="status-msg">{message}</div>}
                    <button className="save-btn" onClick={handleSave} disabled={saving}>
                        {saving ? 'Saving...' : '💾 Publish Changes'}
                    </button>
                </div>
            </div>

            <div className="editor-preview">
                <div className="preview-header">
                    <span>👁️ Live Preview</span>
                    <div className="device-selector">
                        {Object.entries(deviceSizes).map(([key, { label }]) => (
                            <button key={key} className={previewDevice === key ? 'active' : ''} onClick={() => setPreviewDevice(key)}>
                                {label}
                            </button>
                        ))}
                    </div>
                </div>
                <div className="preview-container" style={{ maxWidth: deviceSizes[previewDevice].width }}>
                    <div className="preview-browser" style={{
                        fontFamily: theme?.body_font || 'Inter',
                        borderRadius: theme?.border_radius || '12px'
                    }}>
                        <div className="browser-navbar" style={{ background: theme?.primary_color }}>
                            <div className="nav-logo" style={{ fontFamily: theme?.heading_font }}>{theme?.site_name || 'My Store'}</div>
                        </div>
                        <div className="browser-hero" style={{
                            background: `linear-gradient(45deg, ${theme?.primary_color}, ${theme?.secondary_color})`,
                            fontFamily: theme?.heading_font
                        }}>
                            <h1 style={{ fontSize: theme?.heading_size }}>{theme?.banner_text || 'Welcome'}</h1>
                            <p>{theme?.banner_subtext || 'Shop amazing products'}</p>
                            <button className="shop-btn" style={{
                                borderRadius: theme?.button_radius,
                                background: theme?.accent_color
                            }}>Shop Now</button>
                        </div>
                        <div className="browser-content">
                            <h3 style={{ fontFamily: theme?.heading_font }}>Featured Products</h3>
                            <div className="mock-grid">
                                {[1, 2, 3].map(i => (
                                    <div key={i} className="mock-card" style={{
                                        borderRadius: theme?.border_radius,
                                        boxShadow: theme?.card_shadow
                                    }}>
                                        <div className="mock-img"></div>
                                        <div className="mock-text"></div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default ThemeEditor;
