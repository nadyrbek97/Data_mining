from django.shortcuts import render, redirect
from .forms import HomeForm
from .models import Home
from .data_test import Data
from django.contrib import messages
from django.views.generic import CreateView
from Data_mining.views import home
from django.http import HttpResponse
# Create your views here.


# class HomeCreateView(CreateView):
#     model = Home
#     fields = ('price', 'area', 'seria', 'rooms', 'floor', 'heating', 'hot_water')
#     template_name = 'home_form.html'
#
#     def post(self, request):
#         return redirect(home)

def home_view(request):
    next = request.GET.get('next')
    form = HomeForm(request.POST or None)
    if form.is_valid():
        area = form.cleaned_data.get('area')
        seria = form.cleaned_data.get('seria')
        rooms = form.cleaned_data.get('rooms')
        floor = form.cleaned_data.get('floor')
        heating = form.cleaned_data.get('heating')
        messages.success(request, f'Your parameters are valid')
        h = Home(area=area, seria=seria, rooms=rooms, floor=floor, heating=heating)
        a = []
        a.append(h.rooms)
        a.append(h.seria)
        a.append(h.heating)
        a.append(h.area)
        a.append(h.floor)

        e = []
        e.append(a)
        print(e)

        d = Data.data_min(e)
        prediction = int(d[0])
        print(type(d))
        h.save()
        messages.info(request, f'The Prediction is { prediction }$')
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'home_form.html', context)

