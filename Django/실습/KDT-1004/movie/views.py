from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.


def index(request):
    # 게시글을 가져와서 id 역순으로 정렬
    articles = Article.objects.order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "movie/index.html", context)


# def new(request):
#     return render(request, "movie/new.html")


def create(request):
    # 전송된 form의 method가 POST인지 확인
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        # 전송받은 데이터가 유효한지 확인 => DB에 저장 후 index 페이지로 리다이렉트
        if article_form.is_valid():
            article_form.save()
            return redirect("movie:index")
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }
    return render(request, "movie/new.html", context)


def detail(request, pk):
    # 특정 pk 값의 db 객체를 가져온다.
    article = Article.objects.get(pk=pk)
    # 객체 정보 전달
    context = {
        "article": article,
    }
    return render(request, "movie/detail.html", context)


def update(request, pk):
    # 객체 id
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        # POST가 들어왔을 때 동작
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사, 값을 저장해서 db에 반영
            article_form.save()
            return redirect("movie:detail", article.pk)
    # 유효하지 않으면 오류메시지 담긴 article_form 랜더링
    else:
        # Form 제공
        article_form = ArticleForm(instance=article)

    context = {
        "article_form": article_form,
    }
    return render(request, "movie/update.html", context)
