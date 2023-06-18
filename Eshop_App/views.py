from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html", {})


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
