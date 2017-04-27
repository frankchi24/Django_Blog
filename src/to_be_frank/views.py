from django.shortcuts import render


def home(request):
	return render(request,"home.html",{})


def contact(request):
	return render(request,"contact.html",{})

def about(request):
	return render(request,"about.html",{})


def post(request):
	return render(request,"post.html",{})
