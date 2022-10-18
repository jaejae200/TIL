#  RDB 🔗

**관계형 데이터베이스**

외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계



## RDB에서의 관계 🔗

- `1:1`
  - *One-to-one relationships*
  - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우
- `1:N`
  - *one-to-many relationships*
  - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
- `M:N`
  - *Many-to-many relationships*
  - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
  - 양쪽 모두에서 `1:N` 관계를 가짐



## Foreign Key 🔑 

- **관계형 데이터베이스에서 다른 테이블의 행을 식별**할 수 있는 키
-  참조되는 테이블의 기본 키(`Primary Key`)를 가리킴
- 키를 사용하여 **부모 테이블의 유일한 값을 참조** (참조 무결성)



### 1:N 

- 게시판의 게시글와 `1:N` 관계를 나타낼 수 있는 댓글 구현
- `1:N` 관계에서 댓글을 담당할 `Article` 모델은 1, `Comment` 모델은 N이 될 것
- **2개의 필수 위치 인자가 필요**
  - 참조하는 `model class`
  - `on_delete` 옵션

### on_delete 🗑

- 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할 지를 정의

- `on_delete` 옵션 값
  - `CASCADE` 
    - 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
  - `PROTECT`, `SET_NULL`, `SET_DEFAULT` … 등 여러 옵션 값들이 존재



### Comment 모델 정의 🗃

- 외래 키 필드는 `ForeignKey` 클래스를 **작성하는 위치와 관계없이 필드의 마지막에 작성됨**

  ```python
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  ```





## 관계 모델 참조 📑

```python
article.comment_set.method()
```

- `Article` 모델이 `Comment` 모델을 참조(역참조)할 때 사용하는 매니저
- `article.comment` 형식으로는 댓글 객체를 참조 **할 수 없음**
- 대신 `comment_set manager`를 자동으로 생성해 `article.comment_set` 형태로 **댓글 객체를 참조할 수 있음**



### related_name 🔖

- `ForeignKey` 클래스의 선택 옵션

- 역참조 시 사용하는 매니저 이름(`model_set manager`)을 변경할 수 있음

- **작성 후 다시 원래 코드로 복구**

  ```python
  # models.py
  
  class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE, 		 											related_name='comments')
  ...
  ```



### admin site 등록 📝

- 새로 작성한 `Comment` 모델을 `admin site`에 등록하기

  ```python
  # admin.py
  from .models import Article, Comment
  
  admin.site.register(Article)
  admin.site.register(Comment)
  ```



## Comment 구현 🗨

### CREATE ⚙

- `save` 메서드의 `commit` 옵션을 사용해 `DB`에 저장되기 전 `article` 객체 저장하기

  ```python
  # views.py
  
  def comments_create(request, pk):
  	article = Article.objects.get(pk=pk)
  	comment_form = CommentForm(request.POST)
  	if comment_form.is_valid():
  		comment = comment_form.save(commit=False)
  		comment.article = article
  		comment.save()
  		return redirect('articles:detail', article.pk)
  ```

  

- `article`의 모든 댓글을 가져온 후 `context` 추가

  ```python
  # views.py
  from .models import Article, Comment
  
  def detail(request, pk):
  	article = Article.objects.get(pk=pk)
  	comment_form = CommentForm()
  	comments = article.comment_set.all()
  	context = {
  		'article': article,
  		'comment_form': comment_form,
  		'comments': comments,
  	}
  	return render(request, 'articles/detail.html', context)
  ```



### READ 📖

-  `detail` 템플릿에서 **댓글 목록 출력**하기

  ```python
  <!-- articles/detail.html -->
  {% extends 'base.html' %}
  {% block content %}
      ...
      <a href="{% url 'articles:index' %}">back</a>
      <hr>
      <h4>댓글 목록</h4>
      <ul>
      	{% for comment in comments %}
      		<li>{{ comment.content }}</li>
      	{% endfor %}
      </ul>
      <hr>
      ...
  {% endblock content %}
  ```

  

### DELETE 🗑

- 댓글 삭제 구현

  ```python
  # urls.py
  urlpatterns = [
  ...,
  	path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, 			name='comments_delete'),
  ]
  ```

  ```python
  # views.py
  def comments_delete(request, article_pk, comment_pk):
  	comment = Comment.objects.get(pk=comment_pk)
  	comment.delete()
  	return redirect('articles:detail', article_pk)
  ```



- 댓글 삭제 버튼

  ```html
  <!-- articles/detail.html -->
  {% block content %}
      ...
      <h4>댓글 목록</h4>
      <ul>
          {% for comment in comments %}
          <li>
          {{ comment.content }}
              <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" 					method="POST">
                  {% csrf_token %}
                  <input type="submit" value="DELETE">
              </form>
          </li>
          {% endfor %}
      </ul>
      <hr>
      ...
  {% endblock content %}
  ```

  



## 번외 🔍

### 댓글 개수 출력 💡

- `DTL filter - length` 사용

  ```django
  {{ comments|length }}
  
  {{ article.comment_set.all|length }}
  ```

- `Queryset API - count()` 사용

  ```django
  {{ comments.count }}
  
  {{ article.comment_set.count }}
  ```



### 댓글이 없는 경우 대체 컨텐츠 출력 💡

- `DTL for empty` 활용

  ```django
  {% empty %}
  	<p>댓글이 없음</p>
  ```

  