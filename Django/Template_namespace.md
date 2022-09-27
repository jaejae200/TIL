# Template namespace 💻

각각의 `urls` 를 맵핑하고 `Templates` 나눴을 때 경로를 설정해주는 방법

- 전까지 `urls`를 각 앱에 만들고 `path`를 나눴을 것이다, 주문을 받았을 때 구분된 `Templates`을 반환하는 방법을 설명한다.

```python
# [app]/views.py

return render(request, '[app]/index.html')
```

- 각 `app` 템플릿 안에 `app` 이름의 폴더를 만들어준 후 상위 폴더를 지정해서 반환해주면 된다!