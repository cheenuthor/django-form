from reviews.models import ReviewModel
from django.views import View
from reviews.forms import ReviewForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
# from .models import ReviewModel
# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html",  {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "reviews/review.html",  {
            "form": form
        })


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

    # * we dont need query_set for displaying
    #  ? it is only mean for filtering
    def get_queryset(self):
        base_queryset = super().get_queryset()
        # ? Here we can filter the data we should return to the HTML template
        return base_queryset.filter(rating__gt=2)


class ReviewDetailView(TemplateView):
    template_name = "reviews/review_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = ReviewModel.objects.get(pk=review_id)
        context["review"] = selected_review
        return context
