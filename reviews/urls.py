from django.urls import path
from . import views


urlpatterns = [
    # * using class based view
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view())
]
