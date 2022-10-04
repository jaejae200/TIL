# Django Model Form 🔒

- 사용자가 입력한 값이 `DB`의 `데이터 형식`과 일치하는지를 확인하는 **유효성 검증이 반드시 필요**



## Model Form Class ✏

`Model` 을 통해 `Form Class`를 만들 수 있는 `helper class`

- `ModelForm`은 `Form`과 똑같은 방식으로 `View` 함수에서 사용



### Model Form 선언 🔍

- `forms` 라이브러리의 `ModelForm` 클래스를 상속받음

  ```python
  #[app]/forms.py
  
  from django import forms
  from .models import Article
  
  # 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정
  class ArticleForm(forms.ModelForm):
      # Meta 클래스를 선언
      class Meta: 
          model = Article
          # __all__ 모든 필드 포함, 물론 각각의 필드를 정의해줄 수 있음 ('title, ...')
          fields = '__all__'
          
         
  ```

  

### Model Form 활용 💡

```python
# articles/views.py
from .forms import ArticleForm
# forms.py 파일의 form을 import

def new(request):
    form = ArticleForm()
    context = {
   		'form': form,
    }
	return render(request, 'articles/new.html', context)
```

```html
<!-- articles/new.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}" method="POST">
        <!-- method가 POST일때 csrf_token 발급하여 유효성 검사 -->
        {% csrf_token %} 
        <!-- form 필드를 p 태그로 하나씩 area 생성해준다 -->
        {{ form.as_p }}
        <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```



- `as_p()`
  - 각 필드가 `<p>` 태그로 감싸져서 렌더링
- `as_ul()`
  -  각 필드가 목록 항목`<li>` 태그로 감싸져서 렌더링
  - `<ul>` 태그는 직접 작성해야 한다.
- ` as_table()`
  - 각 필드가 테이블 `<tr>` 태그 행으로 감싸져서 랜더링



#### 저장 및 활용 💾

```python
>>> from .models import Article
>>> from .forms import ArticleForm

# Create a form instance from POST data.
>>> f = ArticleForm(request.POST)

# Save a new Article object from the form's data.
# form 인스턴스에 바인딩 된 데이터를 통해 데이터베이스 객체를 만들고 저장
# 제공되지 않은 경우 save()는 지정된 모델의 새 인스턴스를 만든다(CREATE)
>>> new_article = f.save()

# Create a form to edit an existing Article, but
use POST data to populate the form.
>>> a = Article.objects.get(pk=1)
>>> f = ArticleForm(request.POST, instance=a)
>>> f.save()
```





## 유효성 검사 🔍

- `is_valid()`

  - 유효성 검사를 실행하고, 데이터가 유효한지 여부를 `boolean`으로 반환

  - 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 `is_valid()`를 제공하여 개발자의 편의를 도움

  - 유효성 검증을 실패 했을 때 사용자에게 **실패 결과 메세지**를 출력해줄 수 있음

    ```python
    # articles/views.py
    def create(request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        context = {
            'form': form,
        }
        return render(request, 'articles/new.html', context)
    ```

    

