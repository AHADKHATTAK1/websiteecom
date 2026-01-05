"""
Admin configuration for products
"""
from django.contrib import admin
from .models import Category, Product, ProductImage, ProductVariant, ProductReview


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'alt_text', 'is_primary', 'position']


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 0
    fields = ['name', 'sku', 'price', 'stock_quantity', 'is_active']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'category', 'price', 'stock_quantity', 'is_active', 'is_featured', 'created_at']
    list_filter = ['is_active', 'is_featured', 'category', 'created_at']
    search_fields = ['name', 'sku', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductVariantInline]
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Info', {'fields': ('name', 'slug', 'category', 'short_description', 'description')}),
        ('Pricing', {'fields': ('price', 'compare_price', 'cost_price')}),
        ('Inventory', {'fields': ('sku', 'barcode', 'track_inventory', 'stock_quantity', 'low_stock_threshold')}),
        ('Status', {'fields': ('is_active', 'is_featured')}),
        ('SEO', {'fields': ('meta_title', 'meta_description', 'meta_keywords')}),
        ('Additional', {'fields': ('weight', 'dimensions', 'tags')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'is_verified', 'is_approved', 'created_at']
    list_filter = ['rating', 'is_verified', 'is_approved', 'created_at']
    search_fields = ['product__name', 'user__email', 'title', 'comment']
    readonly_fields = ['created_at', 'updated_at']
