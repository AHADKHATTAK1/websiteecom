"""
Product Models
"""
from django.db import models
from django.contrib.auth import get_user_model
from core.base_models import TimeStampedModel, SoftDeleteModel

User = get_user_model()


class Category(TimeStampedModel):
    """Product categories"""
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Product(TimeStampedModel, SoftDeleteModel):
    store = models.ForeignKey('core.Store', on_delete=models.CASCADE, related_name='products', null=True) 
    """Products"""
    
    # Basic info
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=500, blank=True)
    
    # Category
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    
    # Pricing
    price = models.DecimalField(max_digits=10, decimal_places=2)
    compare_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Inventory
    sku = models.CharField(max_length=100, unique=True)
    barcode = models.CharField(max_length=100, blank=True)
    track_inventory = models.BooleanField(default=True)
    stock_quantity = models.IntegerField(default=0)
    low_stock_threshold = models.IntegerField(default=10)
    
    # Status
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    
    # SEO
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=500, blank=True)
    meta_keywords = models.CharField(max_length=500, blank=True)
    
    # Additional
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dimensions = models.JSONField(default=dict)  # {length, width, height}
    tags = models.JSONField(default=list)
    
    class Meta:
        db_table = 'products'
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['sku']),
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        return self.name
    
    @property
    def is_on_sale(self):
        return self.compare_price and self.price < self.compare_price
    
    @property
    def discount_percentage(self):
        if self.is_on_sale:
            return int(((self.compare_price - self.price) / self.compare_price) * 100)
        return 0
    
    @property
    def is_in_stock(self):
        if not self.track_inventory:
            return True
        return self.stock_quantity > 0
    
    @property
    def is_low_stock(self):
        if not self.track_inventory:
            return False
        return 0 < self.stock_quantity <= self.low_stock_threshold


class ProductImage(TimeStampedModel):
    """Product images"""
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    position = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'product_images'
        ordering = ['position']
    
    def __str__(self):
        return f"{self.product.name} - Image {self.position}"


class ProductVariant(TimeStampedModel):
    """Product variants (size, color, etc.)"""
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    
    name = models.CharField(max_length=100)  # e.g., "Red - Large"
    sku = models.CharField(max_length=100, unique=True)
    
    # Variant attributes
    attributes = models.JSONField(default=dict)  # {color: red, size: large}
    
    # Pricing
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Inventory
    stock_quantity = models.IntegerField(default=0)
    
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'product_variants'
    
    def __str__(self):
        return f"{self.product.name} - {self.name}"


class ProductReview(TimeStampedModel):
    """Product reviews"""
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    rating = models.IntegerField()  # 1-5
    title = models.CharField(max_length=200, blank=True)
    comment = models.TextField()
    
    is_verified = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=True)
    
    helpful_count = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'product_reviews'
        unique_together = ['product', 'user']
    
    def __str__(self):
        return f"{self.user.email} - {self.product.name} ({self.rating}*)"
