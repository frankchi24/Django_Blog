from django import forms
from .models import Post, Comment
from pagedown.widgets import PagedownWidget




class PostModelForm(forms.ModelForm):
    tags = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':64,'class': 'form-control','placeholder':'Tags'}))
    content = forms.CharField(widget=PagedownWidget(attrs={'placeholder':'Content'}))
    subtitle = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Subtitle'})),
    class Meta:
        model = Post
        fields = [
        'title',
        'subtitle',
        'content',
        'image'
        ]
        exclude = ['user','tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Title'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control','placeholder':'Tell Me Your Name'}),
            'content': forms.Textarea(attrs={'class': 'form-control','rows': 3,'placeholder':'What you think?'}),
        }
