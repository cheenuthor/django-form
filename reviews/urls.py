from django.urls import path
from . import views


urlpatterns = [
    # * using class based view
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewListView.as_view()),
    path("reviews/<int:id>", views.ReviewDetailView.as_view(),)
]
