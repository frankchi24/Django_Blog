from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PostModelForm
from django.urls import reverse_lazy
from .mixins import FormUserNeededMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator # for class based views
# Create your views here.


class PostCreate(SuccessMessageMixin,FormUserNeededMixin,CreateView):
    model = Post
    form_class = PostModelForm
    template_name ='blog/create_post.html'
    success_url = reverse_lazy('blog:archives')
    success_message = "\"%(title)s\" was created successfully"
    def form_valid(self,form):
    		form.instance.user = self.request.user
    		return super(PostCreate, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostCreate, self).dispatch(*args, **kwargs)



class PostUpdate(SuccessMessageMixin,UpdateView):
    queryset = Post.objects.all()
    form_class = PostModelForm
    template_name ='blog/update_post.html'
    success_url = reverse_lazy('blog:archives')
    success_message = "\"%(title)s\" was updated"

    def form_valid(self,form):
    		form.instance.user = self.request.user
    		return super(PostUpdate, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:archives')
    success_message = "The post was deleted"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDelete, self).delete(request, *args, **kwargs)



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
