from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from .models import Article, Comment as Comment_model
from .forms import ArticleForm, CommentForm

# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else: 
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    
    context = {
        'article': article,
        'comments': article.comment_set.all(),
        'comment_form': comment_form,
    }

    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
    
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)

def comments_delete(request, article_pk, comment_pk):
    comment = Comment_model.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
