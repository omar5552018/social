from django import forms
from .models import Post

class UploadPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('image',)