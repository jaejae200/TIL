from django.shortcuts import render, redirect
from .models import post
from .forms import postForm

# Create your views here.


def index(request):
    posts = post.objects.order_by("-pk")

    context = {
        "posts": posts,
    }
    return render(request, "post/index.html", context)


def create(request):
    if request.method == "POST":
        post_form = postForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect("post:index")
    else:
        post_form = postForm()

    context = {
        "post_form": post_form,
    }

    return render(request, "post/new.html", context)


def detail(request, pk):
    Post = post.objects.get(pk=pk)

    context = {
        "post": Post,
    }
    return render(request, "post/detail.html", context)


def update(request, pk):
    Post = post.objects.get(pk=pk)

    if request.method == "POST":
        post_form = postForm(request.POST, instance=Post)
        if post_form.is_valid():
            post_form.save()
            return redirect("post:detail", Post.pk)
    else:
        post_form = postForm(instance=Post)

    context = {
        "post_form": post_form,
        "post": Post,
    }

    return render(request, "post/update.html", context)


def delete(request, pk):
    Post = post.objects.get(pk=pk)
    Post.delete()

    return redirect("post:index")
