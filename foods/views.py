from foods.forms import Reviewform
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
from datetime import datetime
from allauth.account.views import PasswordChangeView
from allauth.account.models import EmailAddress
from foods.models import Menu, Review
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from foods.functions import confirmation_required_redirect
# from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.


class IndexView(ListView):
    model = Review
    ordering = ['-created_date']
    context_object_name = "reviews"
    paginated_by = 10


class ReviewDetailView(DetailView):
    model = Review


class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Review
    form_class = Reviewform
    template_name = 'foods/review_form.html'

    redirect_unauthenticated_users = True
    raise_exception = confirmation_required_redirect

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('review-detail', kwargs={'pk': self.object.id})

    def test_func(self, user):
        return EmailAddress.objects.filter(user=user, verified=True).exists()


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
