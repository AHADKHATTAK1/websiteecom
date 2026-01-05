from django.core.management.base import BaseCommand
from apps.products.models import Product, Category
from apps.core.models import Store
from django.utils.text import slugify


class Command(BaseCommand):
    help = "Add more products to the store"

    def handle(self, *args, **kwargs):
        self.stdout.write("Adding professional products...")

        # Get default store
        store = Store.objects.first()

        # Get categories
        electronics = Category.objects.get(slug="electronics")
        fashion = Category.objects.get(slug="fashion")
        home = Category.objects.get(slug="home-living")
        ai = Category.objects.get(slug="ai-gadgets")

        # Professional product catalog
        products = [
            # Electronics
            {
                "name": '4K Ultra HD Smart TV 55"',
                "price": 649.99,
                "compare_price": 799.99,
                "category": electronics,
                "description": "Experience cinema-quality visuals with AI-enhanced picture processing and smart home integration.",
                "stock": 25,
                "is_featured": True,
            },
            {
                "name": "Wireless Gaming Mouse Pro",
                "price": 89.99,
                "category": electronics,
                "description": "Professional-grade wireless mouse with customizable RGB, 20K DPI sensor, and 100-hour battery.",
                "stock": 150,
                "is_featured": False,
            },
            {
                "name": "Mechanical Keyboard RGB",
                "price": 129.99,
                "compare_price": 159.99,
                "category": electronics,
                "description": "Premium mechanical keyboard with hot-swappable switches and per-key RGB lighting.",
                "stock": 80,
                "is_featured": True,
            },
            # Fashion
            {
                "name": "Premium Leather Jacket",
                "price": 299.99,
                "compare_price": 399.99,
                "category": fashion,
                "description": "Genuine leather jacket with modern slim fit. Perfect for casual and semi-formal occasions.",
                "stock": 45,
                "is_featured": True,
            },
            {
                "name": "Designer Denim Jeans",
                "price": 79.99,
                "category": fashion,
                "description": "Premium denim with stretch comfort. Available in multiple washes and sizes.",
                "stock": 200,
                "is_featured": False,
            },
            {
                "name": "Cashmere Sweater",
                "price": 149.99,
                "category": fashion,
                "description": "Luxurious 100% cashmere sweater. Ultra-soft and perfect for winter.",
                "stock": 60,
                "is_featured": False,
            },
            # Home & Living
            {
                "name": "Robot Vacuum Cleaner Pro",
                "price": 399.99,
                "compare_price": 499.99,
                "category": home,
                "description": "AI-powered robot vacuum with mapping, app control, and auto-empty base station.",
                "stock": 35,
                "is_featured": True,
            },
            {
                "name": "Smart Air Purifier",
                "price": 249.99,
                "category": home,
                "description": "HEPA filter air purifier with real-time quality monitoring and smartphone control.",
                "stock": 50,
                "is_featured": True,
            },
            {
                "name": "Luxury Bedding Set Queen",
                "price": 189.99,
                "category": home,
                "description": "Egyptian cotton bedding set with 1000 thread count. Hotel-quality comfort.",
                "stock": 75,
                "is_featured": False,
            },
            # AI Gadgets
            {
                "name": "AI Smart Display Hub",
                "price": 199.99,
                "category": ai,
                "description": "Central smart home hub with AI assistant, video calling, and entertainment features.",
                "stock": 100,
                "is_featured": True,
            },
            {
                "name": "AI Language Translator Earbuds",
                "price": 279.99,
                "compare_price": 329.99,
                "category": ai,
                "description": "Real-time language translation earbuds supporting 40+ languages.",
                "stock": 60,
                "is_featured": True,
            },
            {
                "name": "Smart Fitness Watch Pro",
                "price": 349.99,
                "category": ai,
                "description": "AI-powered fitness tracking with heart rate, SpO2, GPS, and personalized coaching.",
                "stock": 120,
                "is_featured": True,
            },
        ]

        added = 0
        for prod_data in products:
            slug = slugify(prod_data["name"])
            if not Product.objects.filter(slug=slug).exists():
                Product.objects.create(
                    store=store,
                    name=prod_data["name"],
                    slug=slug,
                    description=prod_data["description"],
                    price=prod_data["price"],
                    compare_price=prod_data.get("compare_price"),
                    category=prod_data["category"],
                    stock_quantity=prod_data["stock"],
                    is_featured=prod_data["is_featured"],
                    sku=f"SKU-{slug[:8].upper()}",
                )
                added += 1
                self.stdout.write(f"   + Added: {prod_data['name']}")

        self.stdout.write(
            self.style.SUCCESS(f"\n✅ Added {added} professional products!")
        )
