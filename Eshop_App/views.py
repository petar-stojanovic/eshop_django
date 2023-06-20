from django.shortcuts import render
from .models import Desktop, Laptop
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    desktop_list = Desktop.objects.all().order_by("?")[:6]

    for desktop in desktop_list:
        desktop.calculate_price()

    laptop_list = Laptop.objects.all().order_by("?")[:6]

    for laptop in laptop_list:
        laptop.calculate_price()

    context = {
        "desktop_list": desktop_list,
        "laptop_list": laptop_list
    }

    return render(request, "index.html", context=context)


def browse_desktops(request):
    # desktop_list = Desktop.objects.all().order_by("?")
    desktop_list = Desktop.objects.all()

    for desktop in desktop_list:
        desktop.calculate_price()

    context = {
        "desktop_list": desktop_list,
    }
    return render(request, "browse_desktops.html", context=context)


@login_required(login_url="/members/login_user")
def customize_desktop(request, id):
    desktop = Desktop.objects.filter(pk=id).first()

    values = [
        {'label': 'Processor', 'value': desktop.processor, 'class': 'processor'},
        {'label': 'Motherboard', 'value': desktop.motherboard, 'class': 'motherboard'},
        {'label': 'Graphics Card', 'value': desktop.graphics_card, 'class': 'graphics_card'},
        {'label': 'Memory', 'value': desktop.memory, 'class': 'memory'},
        {'label': 'Power Supply', 'value': desktop.power_supply, 'class': 'power_supply'},
        {'label': 'Storage Drive', 'value': desktop.storage_drive, 'class': 'storage_drive'},
    ]

    context = {
        "desktop": desktop,
        "values": values
    }
    return render(request, "customize_desktops.html", context=context)


@login_required(login_url="/members/login_user")
def customize_laptop(request, id):
    return render(request, "customize_desktops.html", context={})


def browse_laptops(request):
    # laptop_list = Laptop.objects.all().order_by("?")
    laptop_list = Laptop.objects.all()

    for laptop in laptop_list:
        laptop.calculate_price()

    context = {
        "laptop_list": laptop_list,
    }
    return render(request, "browse_laptops.html", context=context)

# def create_component(request):
#     if request.method == 'POST':
#         form = ComponentForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = ComponentForm()
#
#     return render(request, 'components/create.html', {'form': form})
