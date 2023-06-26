from django.contrib import admin
from django.utils.safestring import mark_safe
from .forms import DesktopAdminForm, LaptopAdminForm
from .models import Category, Component, Desktop, Laptop, DesktopOrder

# Register your models here.
admin.site.register(Category)


class ComponentAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "platform", "category", "image_display")

    def image_display(self, obj):
        image_url = obj.image.url if obj.image else None
        return mark_safe(f'<img src="{image_url}" style="max-width:50px;max-height:50px" />')  # Renders the image

    image_display.short_description = 'Image'


admin.site.register(Component, ComponentAdmin)


class DesktopAdmin(admin.ModelAdmin):
    form = DesktopAdminForm
    list_display = ("name", "type", "image_display")

    def image_display(self, obj):
        image_url = obj.image.url if obj.image else None
        return mark_safe(f'<img src="{image_url}" style="max-width:50px;max-height:50px" />')  # Renders the image

    image_display.short_description = 'Image'


admin.site.register(Desktop, DesktopAdmin)


class LaptopAdmin(admin.ModelAdmin):
    form = LaptopAdminForm
    list_display = ("name", "type", "image_display")

    def image_display(self, obj):
        image_url = obj.image.url if obj.image else None
        return mark_safe(f'<img src="{image_url}" style="max-width:50px;max-height:50px" />')  # Renders the image

    image_display.short_description = 'Image'


admin.site.register(Laptop, LaptopAdmin)


class DesktopOrderAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        return None


admin.site.register(DesktopOrder, DesktopOrderAdmin)
