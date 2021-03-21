from reviews.models import ReviewModel
from django.views import View
from reviews.forms import ReviewForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView,CreateView
# from .models import ReviewModel
# Create your views here.


class ReviewView(CreateView):
    model = ReviewModel
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = "reviews/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # * Here we can pass data to the HTML template
        context["message"] = "This is Works"
        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = ReviewModel
    context_object_name = "reviews"

    # # * we dont need query_set for displaying
    # #  ? it is only mean for filtering
    # def get_queryset(self):
    #     base_queryset = super().get_queryset()
    #     # ? Here we can filter the data we should return to the HTML template
    #     return base_queryset.filter(rating__gt=2)


class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = ReviewModel
    context_object_name = "review"
