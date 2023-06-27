from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Desktop, Laptop, Component, Category, DesktopOrder, LaptopOrder
from django.contrib.auth.decorators import login_required
from .forms import DesktopForm, LaptopForm, ShippingForm


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
    if desktop is None:
        return redirect('browse_desktops')

    if request.method == "POST":
        form = DesktopForm(request.POST)
        if form.is_valid():
            desktop_save = DesktopOrder(
                processor=form.data['processor'],
                motherboard=form.data['motherboard'],
                graphics_card=form.data['graphics_card'],
                memory=form.data['memory'],
                power_supply=form.data['power_supply'],
                extra_case_fans=form.data['extra_case_fans'],
                storage_drive=form.data['storage_drive'],
                operating_system=form.data['operating_system'],
                price=form.data['price'],
                image=desktop.image,
                user=request.user,
            )
            desktop_save.save()
            return redirect("checkout", platform="desktop", id=desktop_save.pk)

    values_all = [
        {'label': 'Processor', 'value': Component.objects.filter(
            category=Category.objects.filter(name="Processor").first(), platform="desktop"),
         'class': 'processor'},
        {'label': 'Motherboard', 'value': Component.objects.filter(
            category=Category.objects.filter(name="Motherboard").first(), platform="desktop"), 'class': 'motherboard'},
        {'label': 'Graphics Card', 'value': Component.objects.filter(
            category=Category.objects.filter(name="Graphics Card").first(), platform="desktop"),
         'class': 'graphics_card'},
        {'label': 'Memory', 'value': Component.objects.filter(
            category=Category.objects.filter(name="Memory").first(), platform="desktop"),
         'class': 'memory'},
        {'label': 'Power Supply', 'value': Component.objects.filter(
            category=Category.objects.filter(name="Power Supply").first(), platform="desktop"),
         'class': 'power_supply'},
        {'label': 'Storage Drive', 'value': Component.objects.filter(
            category=Category.objects.filter(name="Storage Drive").first(), platform="desktop"),
         'class': 'storage_drive'},
        {'label': 'Extra Case Fans', 'value': Component.objects.filter(
            category=Category.objects.filter(name="Extra Case Fans").first(), platform="desktop"),
         'class': 'extra_case_fans'},
        {'label': 'Operating System', 'value': Component.objects.filter(
            category=Category.objects.filter(name="Operating System").first(), platform="desktop"),
         'class': 'operating_system'},
    ]

    context = {
        "desktop": desktop,
        "form": DesktopForm,
        "values_all": values_all,
    }
    return render(request, "customize_desktops.html", context=context)


@login_required(login_url="/members/login_user")
def customize_laptop(request, id):
    laptop = Laptop.objects.filter(pk=id).first()
    if laptop is None:
        return redirect('browse_laptops')

    starting_price = laptop.start_price

    if request.method == "POST":
        form = LaptopForm(request.POST)
        if form.is_valid():
            laptop_save = LaptopOrder(
                start_price=starting_price,
                exterior_color=form.data['exterior_color'],
                memory=form.data['memory'],
                operating_system_drive=form.data['operating_system_drive'],
                additional_storage_drive=form.data['additional_storage_drive'],
                operating_system=form.data['operating_system'],
                price=form.data['price'],
                image=laptop.image,
                user=request.user,
            )
            laptop_save.save()
            return redirect("checkout", id=laptop_save.pk, platform="laptop")

    values_all = [
        {
            'label': 'Exterior Color', 'value': Component.objects.filter(
            category=Category.objects.filter(name="Exterior Color").first(), platform="laptop"),
            'class': 'exterior_color'
        }, {
            'label': 'Memory', 'value': Component.objects.filter(
                category=Category.objects.filter(name="Memory").first(), platform="laptop"),
            'class': 'memory'
        }, {
            'label': 'Operating System Drive', 'value': Component.objects.filter(
                category=Category.objects.filter(name="Operating System Drive").first(), platform="laptop"),
            'class': 'operating_system_drive'
        }, {
            'label': 'Additional Storage Drive', 'value': Component.objects.filter(
                category=Category.objects.filter(name="Additional Storage Drive").first(), platform="laptop"),
            'class': 'additional_storage_drive'
        }, {
            'label': 'Operating System', 'value': Component.objects.filter(
                category=Category.objects.filter(name="Operating System").first(), platform="laptop"),
            'class': 'operating_system'
        },
    ]

    context = {
        "laptop": laptop,
        "form": LaptopForm,
        "values_all": values_all,
        "start_price": starting_price,
    }
    return render(request, "customize_laptops.html", context=context)


def browse_laptops(request):
    # laptop_list = Laptop.objects.all().order_by("?")
    laptop_list = Laptop.objects.all()

    for laptop in laptop_list:
        laptop.calculate_price()

    context = {
        "laptop_list": laptop_list,
    }
    return render(request, "browse_laptops.html", context=context)


@login_required(login_url="/members/login_user")
def checkout_page(request, platform, id):
    order = None
    if platform == "desktop":
        order = DesktopOrder.objects.filter(pk=id, user=request.user).first()
        if order is None:
            return redirect('home')

    elif platform == "laptop":
        order = LaptopOrder.objects.filter(pk=id, user=request.user).first()
        if order is None:
            return redirect('home')

    initial_data = {
        'first_name': order.user.first_name,
        'last_name':  order.user.last_name,
        'email':  order.user.email,
    }

    form = ShippingForm(initial=initial_data)
    context = {
        "platform": platform,
        "order": order,
        "form": form
    }
    return render(request, "checkout.html", context=context)

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
