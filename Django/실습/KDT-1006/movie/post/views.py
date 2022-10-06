from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts
    }
    return render(request, 'post/index.html', context)

def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('post:index')
    else: 
        post_form = PostForm()
    
    context = {
        'post_form': post_form
    }
    return render(request, 'post/new.html', context=context)

def detail(request, pk):
    # 특정 글을 가져온다.
    post = Post.objects.get(pk=pk)
    # template에 객체 전달
    context = {
        'post' : post
    }
    return render(request, 'post/detail.html', context)

def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('post:detail', post.pk)
    else:
        post_form = PostForm(instance=post)
    
    context = {
        'post_form': post_form ,
        'post' : post
    }
    return render(request, 'post/update.html', context)


def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()

    return redirect('post:index')