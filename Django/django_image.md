# django-image 🖼

- `ImageField`
  - 이미지 업로드에 사용하는 모델 필드
  - 사용하려면 반드시 `Pillow` 라이브러리가 필요



## URL 설정 ⚙

- `ettings.py` `MEDIA_ROOT`, `MEDIA_URL` 설정

  - `MEDIA_ROOT`

    - 사용자가 **업로드 한 파일(미디어 파일)들을 보관**할 디렉토리의 절대 경로

    - ```python
      MEDIA_ROOT = BASE_DIR / 'media'
      ```

  - `MEDIA_URL`

    - `MEDIA_ROOT`에서 제공되는 미디어를 처리하는 `URL`

    - ```python
      MEDIA_URL = '/media/'
      ```

      

- 업로드 된 파일의 경로는 `django`가 제공하는 `url` 속성을 통해 얻을 수 있음

  ```django
  <img src="{{ article.image.url }}">
  ```

  

- 개발 단계에서 사용자가 **업로드 한 파일 제공하기**

   ```python
   # urls.py
   
   from django.conf.urls.static import static
   
   urlpatterns = [
       path (...)
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```



## 이미지 업로드 📤

- `blank`
  - 기본 값 : `False`
    - `True`인 경우 필드를 비워 둘 수 있음
  - **유효성 검사에서 사용됨 `(is_valid)`**
- `null`
  - 기본 값 : `False`
    - `True`면 빈 값을` DB에 NULL`로 저장



### HTML 설정 ⚙

- 게시글 작성 **`form enctype`** 속성 지정

  ```html
  <Form enctype="multipart/form-data">
      ...
  </Form>
  ```



- `enctype`(인코딩) 속성
  - `multipart/form-data` ⭐
    - **파일/이미지 업로드 시에 반드시 사용**
  - `application/x-www-form-urlencoded`
    - (기본값) 모든 문자 인코딩
  - `text/plain `
    - 인코딩을 하지 않은 문자 상태로 전송



### view 설정 ⚙

- 업로드 한 파일은 `request.FILES` 객체로 전달됨

  ```python
  request.FILES
  ```



## 이미지 리사이징 📏

***Django-imagekit***



```bash
$pip install Pillow
```

```bash
$pip install django-imagekit
```

```python
# settings.py

INSTALLED_APP = [
    ...
    'imagekit',
]
```

```python
# models.py

from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Article(models.Model):
    image = ProcessedImageField(
    	blank=True,
        processors=[Thumbnail(n,n)],
        format='JPEG', 
        options={'quality': 90}, 
    )
```

