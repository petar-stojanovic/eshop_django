from django import forms
from .models import Component, Category, Desktop, Laptop, DesktopOrder, LaptopOrder


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


class DesktopForm(forms.Form):
    processor = forms.ModelChoiceField(queryset=Component.objects.filter(
        category=Category.objects.filter(name="Processor").first(), platform="desktop"))
    motherboard = forms.ModelChoiceField(queryset=Component.objects.filter(
        category=Category.objects.filter(name="Motherboard").first(), platform="desktop"))
    graphics_card = forms.ModelChoiceField(queryset=Component.objects.filter(
        category=Category.objects.filter(name="Graphics Card").first(), platform="desktop"))
    memory = forms.ModelChoiceField(queryset=Component.objects.filter(
        category=Category.objects.filter(name="Memory").first(), platform="desktop"))
    power_supply = forms.ModelChoiceField(queryset=Component.objects.filter(
        category=Category.objects.filter(name="Power Supply").first(), platform="desktop"))
    storage_drive = forms.ModelChoiceField(queryset=Component.objects.filter(
        category=Category.objects.filter(name="Storage Drive").first(), platform="desktop"))
    extra_case_fans = forms.ModelChoiceField(queryset=Component.objects.filter(
        category=Category.objects.filter(name="Extra Case Fans").first(), platform="desktop"))
    operating_system = forms.ModelChoiceField(queryset=Component.objects.filter(
        category=Category.objects.filter(name="Operating System").first(), platform="desktop"))

    def __init__(self, *args, **kwargs):
        super(DesktopForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control text-dark'


class LaptopForm(forms.Form):
    exterior_color = forms.ModelChoiceField(queryset=Component.objects.filter(
        category=Category.objects.filter(name="Exterior Color").first(), platform="laptop"))
    memory = forms.ModelChoiceField(queryset=Component.objects.filter(
        category=Category.objects.filter(name="Memory").first(), platform="laptop"))
    operating_system_drive = forms.ModelChoiceField(queryset=Component.objects.filter(
        category=Category.objects.filter(name="Operating System Drive").first(), platform="laptop"))
    additional_storage_drive = forms.ModelChoiceField(queryset=Component.objects.filter(
        category=Category.objects.filter(name="Additional Storage Drive").first(), platform="laptop"))
    operating_system = forms.ModelChoiceField(queryset=Component.objects.filter(
        category=Category.objects.filter(name="Operating System").first(), platform="laptop"))

    def __init__(self, *args, **kwargs):
        super(LaptopForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control text-dark'


class ShippingForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=50)
    address = forms.CharField(max_length=100)
    country = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    region = forms.CharField(max_length=50)
    postal_code = forms.IntegerField()
    payment_method = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super(ShippingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control fw-bold border-2'

        self.fields['first_name'].widget.attrs['placeholder'] = "First name"
        self.fields['last_name'].widget.attrs['placeholder'] = "Last name"
        self.fields['email'].widget.attrs['placeholder'] = "Email address"
        self.fields['phone_number'].widget.attrs['placeholder'] = "Phone number"
        self.fields['address'].widget.attrs['placeholder'] = "Street Address"
        self.fields['country'].widget.attrs['placeholder'] = "Country"
        self.fields['city'].widget.attrs['placeholder'] = "City"
        self.fields['region'].widget.attrs['placeholder'] = "Region"
        self.fields['postal_code'].widget.attrs['placeholder'] = "Postal code"
        self.fields['payment_method'].widget.attrs['placeholder'] = "Payment Method"

