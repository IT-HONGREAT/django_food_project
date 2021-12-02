from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.urls import reverse
from datetime import datetime
from allauth.account.views import PasswordChangeView
from foods.models import Menu

# Create your views here.


def index(request):
    context = dict()
    today = datetime.today().date()
    menus = Menu.objects.all()

    context["date"] = today
    context["menus"] = menus
    return render(request, 'foods/index.html', context=context)


def food_detail(request, pk):
    context = dict()
    menu = Menu.objects.get(id=pk)
    context["menu"] = menu
    return render(request, 'posts/detail.html', context=context)


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')
