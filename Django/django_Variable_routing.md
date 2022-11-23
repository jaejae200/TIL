# Variable routing 📥

- `URL 주소`를 **변수로 사용하는 것**
- `URL`의 일부를 변수로 지정하여 `view` 함수의 인자로 넘길 수 있음
- **변수 값에 따라 하나의 `path()`에 여러 페이지를 연결 시킬 수 있음**



## Variable routing 작성 📝

- **변수는 “`<>`” 에 정의**

- 기본 타입은 `string` 또한 **5가지 타입**으로 명시가 가능하다

  - `str`
    - `/` 를 제외하고 비어 있지 않은 모든 문자열
  - ` int`
    - 0 또는 양의 정수와 매치
  - `slug`
  - `uuid`
  - `path`

- 예시

  ```python
  # articles/views.py
  def hello(request, name):
  	context = {
  		'name': name,
  	}
  	return render(request, 'hello.html', context)
  
  
  <!-- articles/templates/hello.html -->
  {% extends 'base.html' %}
  
  {% block content %}
  
  	<h1>만나서 반가워요 {{ name }}님!</h1>
      
  {% endblock %
  ```

  

  