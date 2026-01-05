"""
Pre-configured theme presets for quick styling
"""

THEME_PRESETS = {
    'modern': {
        'name': 'Modern',
        'description': 'Clean and contemporary design with vibrant colors',
        'settings': {
            'primary_color': '#6366f1',
            'secondary_color': '#4f46e5',
            'accent_color': '#f59e0b',
            'background_color': '#ffffff',
            'text_color': '#1e293b',
            'heading_font': 'Poppins',
            'body_font': 'Inter',
            'heading_size': '2.5rem',
            'body_size': '1rem',
            'font_weight_bold': 700,
            'font_weight_normal': 400,
            'line_height': '1.6',
            'border_radius': '12px',
            'button_radius': '8px',
            'card_shadow': '0 4px 12px rgba(0,0,0,0.1)',
            'spacing_unit': '1rem',
            'banner_text': 'Experience Modern Shopping',
            'banner_subtext': 'Discover the future of e-commerce with AI-powered recommendations',
        }
    },
    'classic': {
        'name': 'Classic',
        'description': 'Timeless elegance with sophisticated colors',
        'settings': {
            'primary_color': '#1e3a8a',
            'secondary_color': '#1e40af',
            'accent_color': '#d97706',
            'background_color': '#fafaf9',
            'text_color': '#292524',
            'heading_font': 'Playfair Display',
            'body_font': 'Lora',
            'heading_size': '2.75rem',
            'body_size': '1.05rem',
            'font_weight_bold': 700,
            'font_weight_normal': 400,
            'line_height': '1.75',
            'border_radius': '6px',
            'button_radius': '4px',
            'card_shadow': '0 2px 8px rgba(0,0,0,0.08)',
            'spacing_unit': '1.25rem',
            'banner_text': 'Premium Quality, Timeless Style',
            'banner_subtext': 'Curated collections for the discerning shopper',
        }
    },
    'vibrant': {
        'name': 'Vibrant',
        'description': 'Bold and energetic with bright color palette',
        'settings': {
            'primary_color': '#ec4899',
            'secondary_color': '#d946ef',
            'accent_color': '#f59e0b',
            'background_color': '#ffffff',
            'text_color': '#18181b',
            'heading_font': 'Montserrat',
            'body_font': 'Open Sans',
            'heading_size': '2.75rem',
            'body_size': '1rem',
            'font_weight_bold': 800,
            'font_weight_normal': 400,
            'line_height': '1.5',
            'border_radius': '16px',
            'button_radius': '24px',
            'card_shadow': '0 8px 24px rgba(236,72,153,0.15)',
            'spacing_unit': '1rem',
            'banner_text': 'Shop Bold, Shop Bright!',
            'banner_subtext': 'Express yourself with our vibrant collection',
        }
    },
    'minimal': {
        'name': 'Minimal',
        'description': 'Clean and understated monochrome design',
        'settings': {
            'primary_color': '#18181b',
            'secondary_color': '#27272a',
            'accent_color': '#71717a',
            'background_color': '#ffffff',
            'text_color': '#09090b',
            'heading_font': 'Roboto',
            'body_font': 'Roboto',
            'heading_size': '2.25rem',
            'body_size': '0.95rem',
            'font_weight_bold': 500,
            'font_weight_normal': 300,
            'line_height': '1.65',
            'border_radius': '2px',
            'button_radius': '0px',
            'card_shadow': '0 1px 3px rgba(0,0,0,0.05)',
            'spacing_unit': '0.875rem',
            'banner_text': 'Less is More',
            'banner_subtext': 'Simple. Refined. Exceptional.',
        }
    }
}

def get_preset(preset_name):
    """Get a specific preset by name"""
    return THEME_PRESETS.get(preset_name.lower())

def list_presets():
    """List all available presets"""
    return [{
        'id': key,
        'name': value['name'],
        'description': value['description']
    } for key, value in THEME_PRESETS.items()]
