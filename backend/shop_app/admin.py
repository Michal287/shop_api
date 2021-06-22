from django.contrib import admin
from .models import Product, Category, Favorite, Image


class PropertyImageInline(admin.TabularInline):
    model = Image
    extra = 1


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline, ]


admin.site.register(Product, PropertyAdmin)
admin.site.register(Category)
admin.site.register(Favorite)
admin.site.register(Image)