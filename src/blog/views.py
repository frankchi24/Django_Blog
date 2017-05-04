from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Tag
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
        the_post = form.save(commit=False)
        # use the save(commit=False) before saving many-to-many field
        the_post.save()
        tag_names = form.cleaned_data['tags'].split(',')
        for tag in tag_names:
            print(tag)
            tag, created = Tag.objects.get_or_create(tag_name=tag)
            the_post.tags.add(tag)
        the_post.save()
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
        the_post = form.save(commit=False)

        self.object.tags.all().delete()
        the_post.save()
        # clean out tags of the post

        tag_names = form.cleaned_data['tags'].split(',')
        # split tags from the form cleaned data

        for tag in tag_names:
            print(tag)
            tag, created = Tag.objects.get_or_create(tag_name=tag)
            the_post.tags.add(tag)
        the_post.save()
        return super(PostUpdate, self).form_valid(form)

    def get_initial(self):
        tag_list = ''
        for tag in self.object.tags.all():
            tag_list = tag_list  + tag.tag_name + ','
        return { 'tags': tag_list}

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



def Posts_for_Tag(request,page_slug=None):
    queryset = Post.objects.order_by("-timestamp").all().filter(tags__tag_name__contains=page_slug)
    paginator = Paginator(queryset, 3)
    page = request.GET.get('page')
    try:
        paginated = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated = paginator.page(paginator.num_pages)
    object_list = {
    'object_list':paginated,
    'title':'Tags: \"' + page_slug + "\""
    }
    return render(request, "blog/archives.html", object_list)

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
    'object_list':contacts,
    'title':'Post Archives'
    }
    return render(request, "blog/archives.html", object_list)
