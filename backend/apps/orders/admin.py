"""
Admin configuration for orders
"""
from django.contrib import admin
from .models import Order, OrderItem, Payment, Shipment


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product_name', 'product_sku', 'unit_price', 'quantity', 'total_price']
    can_delete = False


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0
    readonly_fields = ['payment_method', 'status', 'amount', 'transaction_id', 'created_at']
    can_delete = False


class ShipmentInline(admin.TabularInline):
    model = Shipment
    extra = 0
    fields = ['carrier', 'tracking_number', 'tracking_url', 'shipped_at', 'delivered_at']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'customer', 'status', 'total', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['order_number', 'customer__email', 'shipping_email']
    readonly_fields = ['order_number', 'subtotal', 'tax', 'shipping_cost', 'discount', 'total', 'created_at', 'updated_at']
    inlines = [OrderItemInline, PaymentInline, ShipmentInline]
    
    fieldsets = (
        ('Order Info', {'fields': ('order_number', 'customer', 'status')}),
        ('Pricing', {'fields': ('subtotal', 'tax', 'shipping_cost', 'discount', 'total')}),
        ('Shipping Address', {'fields': ('shipping_name', 'shipping_email', 'shipping_phone', 
                                          'shipping_address', 'shipping_city', 'shipping_state', 
                                          'shipping_zip', 'shipping_country')}),
        ('Notes', {'fields': ('customer_notes', 'admin_notes')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order', 'payment_method', 'status', 'amount', 'created_at']
    list_filter = ['payment_method', 'status', 'created_at']
    search_fields = ['order__order_number', 'transaction_id']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['order', 'carrier', 'tracking_number', 'shipped_at', 'delivered_at']
    list_filter = ['carrier', 'shipped_at', 'delivered_at']
    search_fields = ['order__order_number', 'tracking_number']
    readonly_fields = ['created_at', 'updated_at']
