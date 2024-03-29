from django.contrib import admin
from django.utils.safestring import mark_safe
from .forms import DesktopAdminForm, LaptopAdminForm
from .models import Category, Component, Desktop, Laptop, DesktopOrder, LaptopOrder, ShippingOrder

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
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return None


admin.site.register(DesktopOrder, DesktopOrderAdmin)


class LaptopOrderAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return None


admin.site.register(LaptopOrder, LaptopOrderAdmin)


class ShippingOrderAdmin(admin.ModelAdmin):
    exclude = ("user",)
    list_display = (
        "first_name", "last_name", "address", "city", "region", "postal_code", "phone_number", "email", "desktop",
        "laptop",
    )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


admin.site.register(ShippingOrder, ShippingOrderAdmin)
