from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import PostModelForm, CommentForm
from django.urls import reverse_lazy, reverse
from .mixins import FormUserNeededMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator # for class based views
# messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
#Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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



def PostDetail(request, pk=None):
    form = CommentForm()
    post = get_object_or_404(Post, pk=pk)
    success_message = 'Thanks for your input!'
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.post = post
            c.save()
            messages.success(request, success_message)
            return redirect(reverse('blog:PostDetail', kwargs={'pk':pk}))
        else:
            messages.success(request, 'Form is not valid~')
    context ={
    'object':post,
    'form':form
    }
    return render(request, 'blog/single_page.html', context)

# class PostDetail(DetailView):
#     model = Post
#     template_name = 'blog/single_page.html'
#
#     def get_context_data(self, **kwargs):
#         obj = super(PostDetail, self).get_context_data(**kwargs)
#         return obj
#
#     def get_form(self):
#         form = self.form_class(instance=self.object) # instantiate the form
#         return form





def archives(request):
    queryset = Post.objects.order_by("-timestamp").all()
    paginator = Paginator(queryset, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    object_list = {
    'object_list':contacts
    }
    return render(request, "blog/archives.html", object_list)
