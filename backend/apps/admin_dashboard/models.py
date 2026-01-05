from django.db import models
from core.base_models import BaseModel


class ThemeSettings(BaseModel):
    """Store theme customization settings"""

    site_name = models.CharField(max_length=255, default="My AI Store")
    logo = models.ImageField(upload_to="themes/logos/", null=True, blank=True)
    favicon = models.ImageField(upload_to="themes/favicons/", null=True, blank=True)

    # Colors
    primary_color = models.CharField(max_length=20, default="#6366f1")
    secondary_color = models.CharField(max_length=20, default="#4f46e5")
    accent_color = models.CharField(max_length=20, default="#f59e0b")
    background_color = models.CharField(max_length=20, default="#ffffff")
    text_color = models.CharField(max_length=20, default="#1e293b")

    # Gradient Support
    enable_gradients = models.BooleanField(default=False)
    primary_gradient = models.CharField(
        max_length=200, default="linear-gradient(135deg, #6366f1 0%, #4f46e5 100%)"
    )
    hero_gradient = models.CharField(
        max_length=200, default="linear-gradient(135deg, #f59e0b 0%, #f97316 100%)"
    )

    # Dark Mode
    enable_dark_mode = models.BooleanField(default=False)
    dark_background = models.CharField(max_length=20, default="#0f172a")
    dark_text = models.CharField(max_length=20, default="#f1f5f9")

    # Typography
    heading_font = models.CharField(max_length=100, default="Inter")
    body_font = models.CharField(max_length=100, default="Inter")
    heading_size = models.CharField(max_length=10, default="2.5rem")
    body_size = models.CharField(max_length=10, default="1rem")
    font_weight_bold = models.IntegerField(default=700)
    font_weight_normal = models.IntegerField(default=400)
    line_height = models.CharField(max_length=10, default="1.6")

    # Layout & Spacing
    border_radius = models.CharField(max_length=10, default="12px")
    button_radius = models.CharField(max_length=10, default="8px")
    card_shadow = models.CharField(max_length=100, default="0 4px 12px rgba(0,0,0,0.1)")
    spacing_unit = models.CharField(max_length=10, default="1rem")
    container_width = models.CharField(max_length=10, default="1280px")

    # Section Configuration (JSON)
    header_config = models.JSONField(default=dict, blank=True)
    footer_config = models.JSONField(default=dict, blank=True)
    hero_config = models.JSONField(default=dict, blank=True)

    # Button Styles
    button_style = models.CharField(
        max_length=20,
        default="solid",
        choices=[("solid", "Solid"), ("outline", "Outline"), ("ghost", "Ghost")],
    )
    button_size = models.CharField(
        max_length=20,
        default="medium",
        choices=[("small", "Small"), ("medium", "Medium"), ("large", "Large")],
    )

    # Typography Advanced
    letter_spacing = models.CharField(max_length=10, default="0px")
    heading_line_height = models.CharField(max_length=10, default="1.2")
    body_line_height = models.CharField(max_length=10, default="1.6")

    # Banner
    banner_text = models.CharField(
        max_length=500, default="Find Everything You Need with AI"
    )
    banner_subtext = models.CharField(
        max_length=500,
        default="Experience the future of shopping with our zero-human automated platform.",
    )
    banner_image = models.ImageField(upload_to="themes/banners/", null=True, blank=True)

    # Contact
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Theme: {self.site_name}"

    class Meta:
        verbose_name_plural = "Theme Settings"
