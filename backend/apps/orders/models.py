"""
Order Models
"""
from django.db import models
from django.contrib.auth import get_user_model
from core.base_models import TimeStampedModel
from apps.products.models import Product, ProductVariant

User = get_user_model()


class Order(TimeStampedModel):
    """Customer orders"""
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded'),
    ]
    
    # Customer
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders')
    
    # Order details
    order_number = models.CharField(max_length=50, unique=True, db_index=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Pricing
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Shipping address
    shipping_name = models.CharField(max_length=200)
    shipping_email = models.EmailField()
    shipping_phone = models.CharField(max_length=20)
    shipping_address = models.CharField(max_length=500)
    shipping_city = models.CharField(max_length=100)
    shipping_state = models.CharField(max_length=100)
    shipping_zip = models.CharField(max_length=20)
    shipping_country = models.CharField(max_length=100)
    
    # Notes
    customer_notes = models.TextField(blank=True)
    admin_notes = models.TextField(blank=True)
    
    class Meta:
        db_table = 'orders'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Order #{self.order_number}"


class OrderItem(TimeStampedModel):
    """Order line items"""
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    variant = models.ForeignKey(ProductVariant, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Product details (snapshot at time of order)
    product_name = models.CharField(max_length=200)
    product_sku = models.CharField(max_length=100)
    variant_name = models.CharField(max_length=100, blank=True)
    
    # Pricing
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'order_items'
    
    def __str__(self):
        return f"{self.product_name} x {self.quantity}"


class Payment(TimeStampedModel):
    """Payment records"""
    
    PAYMENT_METHOD_CHOICES = [
        ('stripe', 'Stripe'),
        ('paypal', 'PayPal'),
        ('razorpay', 'Razorpay'),
        ('cod', 'Cash on Delivery'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    
    # External reference
    transaction_id = models.CharField(max_length=200, blank=True)
    payment_intent_id = models.CharField(max_length=200, blank=True)
    
    # Metadata
    metadata = models.JSONField(default=dict)
    
    class Meta:
        db_table = 'payments'
    
    def __str__(self):
        return f"Payment for Order #{self.order.order_number}"


class Shipment(TimeStampedModel):
    """Shipment tracking"""
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='shipments')
    
    carrier = models.CharField(max_length=100)  # FedEx, UPS, DHL
    tracking_number = models.CharField(max_length=200)
    tracking_url = models.URLField(blank=True)
    
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    
    notes = models.TextField(blank=True)
    
    class Meta:
        db_table = 'shipments'
    
    def __str__(self):
        return f"Shipment {self.tracking_number}"
