from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Article
from .forms import ArticleForm

# Create your views here.


def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'post/index.html', context)

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('post:index')
    else: 
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'post/form.html', context=context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'post/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            messages.success(request, '글이 수정되었습니다.')
            return redirect('post:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'post/form.html', context)