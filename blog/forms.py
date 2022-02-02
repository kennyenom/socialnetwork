from pyexpat import model
from django import forms
from .models import *

class Post(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title','content']
        # widgets = {
        #   'content': forms.Textarea(attrs={'rows':4, 'cols':5}),
        # }

class Postimage(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['image']

class PostEdit(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title','content']

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='comment ',widget=forms.TextInput(attrs={'placeholder':'add a comment'}))
    class Meta:
        model = Comment
        fields = ['content']
