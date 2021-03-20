from reviews.forms import ReviewForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    form = ReviewForm()
    return render(request, "reviews/review.html",  {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thankyou.html")
