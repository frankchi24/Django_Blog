from django.shortcuts import render, redirect
from blog.models import Post
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
	queryset = Post.objects.order_by("-timestamp")[:3]
	object_list = {
	'object_list':queryset
	}
	# messages.success(request, 'Hello world!')
	return render(request,"to_be_frank/home.html",object_list)


def contact(request):
	return render(request,"to_be_frank/contact.html",{})

def about(request):
	return render(request,"to_be_frank/about.html",{})


def post(request):
	return render(request,"to_be_frank/post.html",{})
