from django.shortcuts import render , redirect, reverse
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView, UpdateView

# Class based view
class PostList(ListView):
    model=Post
    
class PostDetail(DetailView):
    model=Post

class PostUpdate(UpdateView):
    model=Post
    fields=['title','content']
    success_url = '/blog/cbv'

# Function based view
def all_posts(request):
    all_posts = Post.objects.all()
    
    return render(request,'post/all_posts.html',{'posts':all_posts})

def single_post(request,id):
    single_post = Post.objects.get(id=id)
    return render(request,'post/single_post.html',{'post':single_post})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse ('blog:blog_list'))
    else:
        form=PostForm()
    return render(request,'post/new.html',{'form':form})

def edit_post(request,id):
    single_post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES, instance=single_post)
        if form.is_valid():
            form.save()
            return redirect(reverse ('blog:blog_list'))
    else:
        form=PostForm(instance=single_post)
    return render(request,'post/new.html',{'form':form})