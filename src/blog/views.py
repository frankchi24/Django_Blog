from django.shortcuts import render
from .models import Post
# Create your views here.
def post(request, pk=None):
    obj = Post.objects.get(pk=pk)
    context ={
    'object':obj
    }
    return render(request, "blog/single_page.html", context)

def archives(request):
    queryset = Post.objects.all()
    object_list = {
    'object_list':queryset
    }
    return render(request, "blog/archives.html", object_list)
