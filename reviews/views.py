from django.views import View
from reviews.forms import ReviewForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
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


# def review(request):
#     if request.method == 'POST':
#         # *For updating a existing_data we use that id and pass it as a Instance
#         # existing_data= ReviewModel.objects.get(pk=1)
#         form = ReviewForm(request.POST,
#                           # ?Here we pass is as instance of data
#                           # instance=existing_data
#                           )
#         if form.is_valid():
#             # * If we are using model form
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()
#     return render(request, "reviews/review.html",  {
#         "form": form
#     })


def thank_you(request):
    return render(request, "reviews/thankyou.html")
