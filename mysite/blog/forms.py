from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        fields = ('title', 'text')
        model = Post