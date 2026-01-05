from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.products.models import Category, Product
from apps.admin_dashboard.models import ThemeSettings
from django.utils.text import slugify

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with initial data for client demo'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database seeding...')

        # 0. Create Default Store
        from apps.core.models import Store
        store, created = Store.objects.get_or_create(
            subdomain='mystore',
            defaults={'name': 'My Awesome Store'}
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created Store: {store.name} (Subdomain: {store.subdomain})'))

        # 1. Create Superuser
        if not User.objects.filter(email='admin@mystore.local').exists():
            User.objects.create_superuser(
                email='admin@mystore.local',
                password='password123',
                first_name='Admin',
                last_name='User',
                store=store
            )
            self.stdout.write(self.style.SUCCESS('Superuser created (admin@mystore.local / password123)'))
        
        # 2. Create Categories
        categories_data = [
            {'name': 'Electronics', 'slug': 'electronics'},
            {'name': 'Fashion', 'slug': 'fashion'},
            {'name': 'Home & Living', 'slug': 'home-living'},
            {'name': 'AI Gadgets', 'slug': 'ai-gadgets'}
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={'name': cat_data['name']}
            )
            categories[cat_data['slug']] = category
            if created:
                self.stdout.write(f"   Created category: {cat_data['name']}")

        # 3. Create Products
        products_data = [
            {
                'name': 'Smart AI Speaker',
                'price': 99.99,
                'category': 'ai-gadgets',
                'description': 'Control your home with voice commands using our latest AI technology.',
                'stock': 50,
                'is_featured': True
            },
            # ... other products (omitted for brevity, assume loop uses data structure)
        ]
        
        # Define products data properly if not defined in previous scope or ensure it's available.
        # Restoring full product list to be safe:
        products_data = [
            {
                'name': 'Smart AI Speaker',
                'price': 99.99,
                'category': 'ai-gadgets',
                'description': 'Control your home with voice commands using our latest AI technology.',
                'stock': 50,
                'is_featured': True
            },
            {
                'name': 'Wireless Noise Cancelling Headphones',
                'price': 199.99,
                'compare_price': 249.99,
                'category': 'electronics',
                'description': 'Immerse yourself in music with industry-leading noise cancellation.',
                'stock': 30,
                'is_featured': True
            },
            {
                'name': 'Minimalist Cotton T-Shirt',
                'price': 25.00,
                'category': 'fashion',
                'description': 'Premium organic cotton t-shirt for everyday comfort.',
                'stock': 100,
                'is_featured': False
            },
            {
                'name': 'Smart Coffee Maker',
                'price': 129.50,
                'category': 'home-living',
                'description': 'Wake up to fresh coffee brewed exactly how you like it via app control.',
                'stock': 15,
                'is_featured': True
            }
        ]

        for prod_data in products_data:
            slug = slugify(prod_data['name'])
            if not Product.objects.filter(slug=slug).exists():
                Product.objects.create(
                    store=store,
                    name=prod_data['name'],
                    slug=slug,
                    description=prod_data['description'],
                    price=prod_data['price'],
                    compare_price=prod_data.get('compare_price'),
                    category=categories[prod_data['category']],
                    stock_quantity=prod_data['stock'],
                    is_featured=prod_data['is_featured'],
                    sku=f"SKU-{slug[:5].upper()}-{prod_data['stock']}"
                )
                self.stdout.write(f"   Created product: {prod_data['name']}")

        # 4. Create Theme Settings (if missing)
        if not ThemeSettings.objects.exists():
            ThemeSettings.objects.create(
                # store=store, # Add later when ThemeSettings is updated
                site_name="My Awesome Store",
                primary_color="#6366f1",
                secondary_color="#4f46e5",
                accent_color="#f59e0b",
                heading_font="Inter",
                body_font="Inter",
                banner_text="Welcome to the Future of Shopping",
                banner_subtext="Experience AI-powered commerce with seamless personalization."
            )
            self.stdout.write(self.style.SUCCESS('Default theme settings created'))

        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))
