from foods.forms import Reviewform, ProfileForm, CommentForm
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView, FormView, View
from django.views.generic.detail import SingleObjectMixin
from datetime import datetime
from allauth.account.views import PasswordChangeView
from allauth.account.models import EmailAddress
from foods.models import Review, User
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from foods.functions import confirmation_required_redirect

from rest_framework.generics import ListAPIView
from foods.serializers import ReviewSerializer

# Create your views here.


class IndexView(ListView):
    model = Review
    ordering = ['-created_date']
    context_object_name = "reviews"
    paginated_by = 10

class FoodListAPIView(ListAPIView):
    
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(DetailView):
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def get_success_url(self):
        return reverse('review-detail', kwargs={'pk': self.object.id})



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


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = Reviewform

    raise_exception = True

    def get_success_url(self):
        return reverse('review-detail', kwargs={'pk': self.object.id})

    def test_func(self, user):
        review = self.get_object()
        return review.author == user


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review

    raise_exception = True

    def get_success_url(self):
        return reverse('review-list')

    def test_func(self, user):
        review = self.get_object()
        return review.author == user


class ProfileView(DetailView):
    model = User
    template_name = 'foods/profile.html'
    pk_url_kwarg = "pk"
    context_object_name = "profile_user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get("pk")
        context["user_reviews"] = Review.objects.filter(
            author_id=user_id).order_by("-created_date")
        return context


class UserReviewListView(ListView):
    model = Review
    template_name = "foods/user_review_list.html"
    context_object_name = "user_reviews"
    paginate_by = 4

    def get_queryset(self):
        user_id = self.kwargs.get("pk")
        return Review.objects.filter(author_id=user_id).order_by("-created_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["profile_user"] = get_object_or_404(
            User, id=self.kwargs.get("pk"))
        return context


class ProfileSetView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "foods/profile_set_form.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("index")


class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "foods/profile_update_form.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.request.user.id})


class CustomPasswordChangeView(LoginRequiredMixin,PasswordChangeView):
    def get_success_url(self):
        return reverse('profile', kwargs={"pk": self.request.user.id} )


class ReviewComment(SingleObjectMixin, FormView):
    model = Review
    form_class = CommentForm
    template_name = 'foods/review_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(ReviewComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    

    def get_success_url(self):
        review = self.get_object()
        return reverse('review-detail', kwargs={'pk': self.object.id}) + '#comments'


class ReviewDisplay(DetailView):
    model = Review
    template_name = 'foods/review_detail.html'
    context_object_name = 'review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    

    def get_success_url(self):
        return reverse('review-detail', kwargs={'pk': self.object.id})


class ReviewDetailView(View):

    def get(self, request, *args, **kwargs):
        view = ReviewDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ReviewComment.as_view()
        return view(request, *args, **kwargs)