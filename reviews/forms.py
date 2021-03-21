from reviews.models import ReviewModel
from django import forms


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=100,
#                                 error_messages={
#                                     "required": "your name must not be empty",
#                                     "max_length": "Please enter a shorter name!"
#                                 })
#     review_text = forms.CharField(
#         label="Your FeedBack", max_length=200, widget=forms.Textarea)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        # ?Here we connecting ReviewModel with Form
        model = ReviewModel
        # ?here we can explicitly set which model field should be render in html
        # fields = ['user_name', 'review_text', 'rating']
        # ?here we set to all fields
        fields = '__all__'
        # *If we used __all__ we can use exclude
        # exclude = ['some_field']
