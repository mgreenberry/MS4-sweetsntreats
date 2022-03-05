from django.contrib import admin
from .models import Product, Category, Reviews


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
        'is_favourite',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_title', 'review_body', 'author', 'product')

    class Meta:
        verbose_name_plural = 'Reviews'


admin.site.register(Reviews, ReviewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
