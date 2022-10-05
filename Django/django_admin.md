# Django admin 👨‍💻



## Admin site 💻

- **Django의 가장 강력한 기능 중 하나**
- 관리자 페이지
  - 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
  - 모델 `class`를 `admin.py`에 **등록하고 관리**





### admin 계정 생성 ⚙

```bash
$ python manage.py createsuperuser
```

- `ID`
- `e-mail`
- `password` (2번 입력)



### admin model class 🔎

- 모델의 `record`를 보기 위해서는 `admin.py` 등록 필요

  ```python
  # articles/admin.py
  from django.contrib import admin
  from .models import Article
  
  class postAdmin(admin.ModelAdmin):
      fields = ["title", "content"]
  
  admin.site.register(Article)
  ```

  



