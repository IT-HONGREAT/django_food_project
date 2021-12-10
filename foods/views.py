from foods.forms import Reviewform
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
from datetime import datetime
from allauth.account.views import PasswordChangeView
from foods.models import Menu, Review
from braces.views import LoginRequiredMixin

# Create your views here.


class IndexView(ListView):
    model = Review
    ordering = ['-created_date']
    context_object_name = "reviews"
    paginated_by = 10


class ReviewDetailView(DetailView):
    model = Review


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = Reviewform
    template_name = 'foods/review_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('review-detail', kwargs={'pk': self.object.id})


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = Reviewform

    def get_success_url(self):
        return reverse('review-detail', kwargs={'pk': self.object.id})


class ReviewDeleteView(DeleteView):
    model = Review

    def get_success_url(self):
        return reverse('review-list')


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')
