from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Component(models.Model):
    PLATFORM_CHOICES = [
        ('desktop', 'Desktop'),
        ('laptop', 'Laptop'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES, default="desktop")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.name


class Desktop(models.Model):
    TYPE = [
        ('small', 'Small Desktop'),
        ('premium', 'Premium Desktop'),
        ('elite', 'Elite Desktop'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE, default="small")

    processor = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='desktop_processor')
    motherboard = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='desktop_motherboard')
    graphics_card = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='desktop_graphics')
    memory = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='desktop_memory')
    power_supply = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='desktop_power')
    storage_drive = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='desktop_storage')
    extra_case_fans = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='desktop_case_fans')
    operating_system = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='desktop_os')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def calculate_price(self):
        components = [self.processor, self.motherboard, self.graphics_card, self.storage_drive, self.memory,
                      self.power_supply,
                      self.storage_drive, self.extra_case_fans, self.operating_system]
        total_price = sum(component.price for component in components if component)
        self.price = total_price
        self.save()

    # TODO: For filtering
    # category = Categories.objects.get(name='Storage Drive')
    # desktops = category.desktops_storage.all()
    def __str__(self):
        return self.name


class Laptop(models.Model):
    TYPE = [
        ('small', 'Small Laptop'),
        ('premium', 'Premium Laptop'),
        ('elite', 'Elite Laptop'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE, default="small")
    start_price = models.DecimalField(max_digits=8, decimal_places=2)

    exterior_color = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='laptop_color')
    memory = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='laptop_memory')
    operating_system_drive = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='laptop_os_drive')
    additional_storage_drive = models.ForeignKey(Component, on_delete=models.CASCADE,
                                                 related_name='laptop_additional_storage')
    operating_system = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='laptop_os')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def calculate_price(self):
        components = [self.exterior_color, self.memory, self.operating_system_drive,
                      self.additional_storage_drive,
                      self.operating_system]
        total_price = sum(component.price for component in components if component)
        total_price += self.start_price
        self.price = total_price
        self.save()

    def __str__(self):
        return self.name

class DesktopOrder(models.Model):
    processor = models.CharField(max_length=50)
    motherboard = models.CharField(max_length=50)
    graphics_card = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    power_supply = models.CharField(max_length=50)
    extra_case_fans = models.CharField(max_length=50)
    storage_drive = models.CharField(max_length=50)
    operating_system = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='orders/images')

    def __str__(self):
        return f"Desktop Order #{self.pk}"


class LaptopOrder(models.Model):
    start_price = models.DecimalField(max_digits=8, decimal_places=2)
    exterior_color = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    operating_system_drive = models.CharField(max_length=50)
    additional_storage_drive = models.CharField(max_length=50)
    operating_system = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='orders/images')

    def __str__(self):
        return f"Laptop Order #{self.pk}"
