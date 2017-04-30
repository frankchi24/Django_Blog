from django import forms
from .models import Post
from pagedown.widgets import PagedownWidget

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget())
    class Meta:
        model = Post
        fields = [
        'title',
        'subtitle',
        'content'
        ]
        exclude = ["user"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Title'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control','placeholder':'Subtitle'}),
            # 'content': forms.Textarea(attrs={'class': 'form-control','rows': 5,'placeholder':'Content'}),
        }
