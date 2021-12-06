from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
from datetime import datetime
from allauth.account.views import PasswordChangeView
from foods.models import Menu, Review

# Create your views here.


class IndexView(ListView):
    model = Review
    ordering = ['-created_date']
    context_object_name = "reviews"
    paginated_by = 10


class FoodsDetailView(DetailView):
    model = Review


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')
