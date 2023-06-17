from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Component

# Register your models here.
admin.site.register(Category)


class ComponentAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "platform", "image_display")

    def image_display(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-width:50px;max-height:50px" />')  # Renders the image

    image_display.short_description = 'Image'


admin.site.register(Component, ComponentAdmin)
