from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    '''Класс формы отзыва'''
    text = forms.CharField(widget=forms.Textarea, label='Отзыв')

    class Meta(object):
        model = Review
        fields = ('text',)
