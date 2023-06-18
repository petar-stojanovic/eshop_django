from django import forms
from .models import Component, Category, Desktop, Laptop


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ['name', 'price', 'platform', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.platform == 'desktop':
            self.fields['category'].queryset = Category.objects.filter(
                name__in=['processor', 'motherboard', 'graphics card', 'memory', 'power supply', 'storage drive',
                          'extra case fans', 'operating system'])
        else:
            self.fields['category'].queryset = Category.objects.filter(
                name__in=['exterior color', 'memory', 'operating system drive', 'additional storage drive'])


class DesktopAdminForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the choices for the storage_drive field based on the "Storage Drive" category
        # sd = Category.objects.filter(name="Storage Drive").first()
        self.fields['processor'].queryset = Component.objects.filter(
            category=Category.objects.filter(name="Processor").first(), platform="desktop")
        self.fields['motherboard'].queryset = Component.objects.filter(
            category=Category.objects.filter(name="Motherboard").first(), platform="desktop")
        self.fields['graphics_card'].queryset = Component.objects.filter(
            category=Category.objects.filter(name="Graphics Card").first(), platform="desktop")
        self.fields['memory'].queryset = Component.objects.filter(
            category=Category.objects.filter(name="Memory").first(), platform="desktop")
        self.fields['power_supply'].queryset = Component.objects.filter(
            category=Category.objects.filter(name="Power Supply").first(), platform="desktop")
        self.fields['storage_drive'].queryset = Component.objects.filter(
            category=Category.objects.filter(name="Storage Drive").first(), platform="desktop")
        self.fields['extra_case_fans'].queryset = Component.objects.filter(
            category=Category.objects.filter(name="Extra Case Fans").first(), platform="desktop")
        self.fields['operating_system'].queryset = Component.objects.filter(
            category=Category.objects.filter(name="Operating System").first(), platform="desktop")


class LaptopAdminForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the choices for the storage_drive field based on the "Storage Drive" category
        # sd = Category.objects.filter(name="Storage Drive").first()
        self.fields['exterior_color'].queryset = Component.objects.filter(
            category=Category.objects.filter(name="Exterior Color").first(), platform="laptop")
        self.fields['memory'].queryset = Component.objects.filter(
            category=Category.objects.filter(name="Memory").first(), platform="laptop")
        self.fields['operating_system_drive'].queryset = Component.objects.filter(
            category=Category.objects.filter(name="Operating System Drive").first(), platform="laptop")
        self.fields['additional_storage_drive'].queryset = Component.objects.filter(
            category=Category.objects.filter(name="Additional Storage Drive").first(), platform="laptop")
        self.fields['operating_system'].queryset = Component.objects.filter(
            category=Category.objects.filter(name="Operating System").first(), platform="laptop")
