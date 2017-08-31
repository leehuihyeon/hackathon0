from django import forms
from .models import Comment, FreePost


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        
        fields  = ('author', 'message')
        
        
