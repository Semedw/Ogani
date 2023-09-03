from django.contrib import admin
from .models import (
    Blog, ProductCategory, BlogCategory, Banner, Settings, Product,
    Discount_Product, Discount_category, Contact
)

admin.site.register(ProductCategory)
admin.site.register(BlogCategory)
admin.site.register(Banner)
admin.site.register(Settings)
admin.site.register(Discount_category)
admin.site.register(Contact)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'created_at',)
    search_fields = ('title', 'content')
    readonly_fields = ('comment', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at', 'created_at',)
    search_fields = ('name', 'content')
    ordering = ('-created_at', '-price' )
    readonly_fields = ('heart', 'retweet', )


@admin.register(Discount_Product)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at', 'created_at',)
    search_fields = ('name', 'content')
    ordering = ('-created_at', '-price' )
    readonly_fields = ('heart', 'retweet', )






# Django administration
admin.site.site_header = 'Ogani Master Administration'
admin.site.site_title = 'Ogani Master Administration'