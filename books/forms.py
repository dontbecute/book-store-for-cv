from django.forms import ModelForm
from .models import Books , Review

class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = ['title' , 'auth', 'ratings', 'discreption' , 'image' ,'price']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review' , 'rating'  , 'auth' ,'book']

        