from django import forms
from .models import Post, Comment
from pagedown.widgets import PagedownWidget




class PostModelForm(forms.ModelForm):
    tags = forms.CharField(widget=forms.TextInput(attrs={'size':64}))
    content = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Post
        fields = [
        'title',
        'subtitle',
        'content',
        ]
        exclude = ['user','tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Title'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control','placeholder':'Subtitle'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control','placeholder':'Subtitle'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control','placeholder':'Tell Me Your Name'}),
            'content': forms.Textarea(attrs={'class': 'form-control','rows': 3,'placeholder':'What you think?'}),
        }
