from .models import Comment
from django import forms

class ComentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
