from django.shortcuts import render
from blog.models import Post

def home(request):
	queryset = Post.objects.order_by("-timestamp")[:3]
	object_list = {
	'object_list':queryset
	}
	return render(request,"home.html",object_list)


def contact(request):
	return render(request,"contact.html",{})

def about(request):
	return render(request,"about.html",{})


def post(request):
	return render(request,"post.html",{})
