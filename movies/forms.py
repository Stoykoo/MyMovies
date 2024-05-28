from django import forms
from .models import MovieReview


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
class MovieReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')],
                                label='Rating')

    class Meta:
        model = MovieReview
        fields = ['rating', 'review']
        
