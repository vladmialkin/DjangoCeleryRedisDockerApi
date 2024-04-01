from django.contrib import admin
from .models import Category, Product


# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')
    ordering = ('name',)

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'brand', 'slug', 'price', 'available', 'created_at', 'updated_at',)
    list_filter = ('available', 'created_at', 'updated_at',)
    ordering = ('title',)

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}
