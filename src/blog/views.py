from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView
from .forms import PostModelForm
from django.urls import reverse_lazy

# Create your views here.

class PostCreate(CreateView):
    model = Post
    form_class = PostModelForm
    template_name ='blog/create_post.html'
    success_url = reverse_lazy('blog:archives')

    def form_valid(self,form):
    		form.instance.user = self.request.user
    		return super(PostCreate, self).form_valid(form)


def post(request, pk=None):
    obj = Post.objects.get(pk=pk)
    context ={
    'object':obj
    }
    return render(request, "blog/single_page.html", context)

def archives(request):
    queryset = Post.objects.order_by("-timestamp").all()
    object_list = {
    'object_list':queryset
    }
    return render(request, "blog/archives.html", object_list)
