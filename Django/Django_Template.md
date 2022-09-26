# Django Template 📜

데이터 표현을 제어하는 도구이자 표현에 관련된 로직



- *Django Template*을 이용한 **HTML 정적 부분**과 **동적 컨텐츠 삽입**
- *Template System*의 기본 목표를 숙지



## Django Template Language ⚙

*Django template*에서 사용하는 *built-in template system*

- **조건**, **반복**, **변수 치환**, **필터** 등의 기능을 제공

  - `Python`처럼 일부 프로그래밍 구조(`if`, `for` 등)를 사용할 수 있지만 이것은 `Python` 코드로 실행되는 것이 아님
  - `Django` 템플릿 시스템은 단순히 `Python`이 `HTML`에 포함 된 것이 아니니 주의

- #### 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것임을 명심할 것



### DTL Syntax 🔎

- `Variable` 

  - 변수명은 **영어**, **숫자와 밑줄(`_`)**의 조합으로 구성될 수 있으나 밑줄로는 시작 할 수 없음

  - `render()`의 세번째 인자로 `{'key': value}` 와 같이 딕셔너리 형태로 넘겨주며,  여기서 정의한 `key`에 해당하는 문자열이 `template`에서 사용 가능한 변수명이 된다.

    ```python
    # urls.py
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('index/', views.index),
        path('greeting/', views.greeting),
    ]
    
    # views.py
    def greeting(request):
        foods = ['apple', 'banana', 'coconut',]
        info = {
            'name': 'Alice'
        }
        context = {
            'foods': foods,
            'info': info,
        }
    	return render(request, 'greeting.html', context)
    ```

    ```html
    !-- articles/templates/greeting.html -->
    
    <p>저는 {{ foods.0 }}을 가장 좋아합니다.</p>
    <p>안녕하세요 저는 {{ info.name }} 입니다.</p>
    
    <a href="/index/">뒤로</a>
    ```

    

- `Filters`

  - 표시할 **변수를 수정할 때** 사용

  - `{{ name|lower }}`

    - `name` 변수를 모두 소문자로 출력

  - **일부 필터는 인자를 받는다**.

    ```python
    # urls.py
    urlpatterns = [
    		...,
    		path('dinner/', views.dinner),
    ]
    
    # articles/views.py
    import random
    from django.shortcuts import render
    
    ...
    
    def dinner(request):
        foods = ['족발', '햄버거', '치킨', '초밥',]
        pick = random.choice(foods)
        context = {
            'pick': pick,
            'foods': foods,
    	}
    	return render(request, 'dinner.html', context)
    ```

    ```python
    !-- articles/templates/dinner.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
    ...
    </head>
    <body>
        <p>{{ pick }}은 {{ pick|length }}글자</p>
        <p>{{ foods|join:", "}}</p>
        
        <a href="/index/">뒤로</a>
    </body>
    </html>
    ```

    

- `Tags`

  - 출력 텍스트를 만들거나, **반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행**

- `Comments`

  - *Django template*에서 **라인의 주석을 표현**하기 위해 사용

