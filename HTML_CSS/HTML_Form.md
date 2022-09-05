# HTML Form 📥

- 사용자와 웹사이트 또는 어플리케이션이 서로 상호 작용
- 하나 이상의 위젯을 설명하는 라벨과 같이 사용된다
  - `텍스트 필드 (한줄 또는 여러줄)`
  - `셀렉 박스`
  - `버튼`
  - `체크박스`
  - `라디오 버튼`



## From 요소 📖

```html
<from action="homepage" method="post">
</from>

<!-- form의 공식적인 형태 >
```

- `<div>` 나 `<p>` 요소와 같이 사용된다
- `form`이 동작하는 방식을 설정하는 속성들을 지정해야한다.
- 모든 속성은 선택이지만, ⭐ `action` 속성과 `method `속성 필수 ⭐



- `action`
  - 데이터를 보낼 `URL`을 지정한다
- `method`
  - 어떤 `HTTP` 방식을 사용할 것인지 지정 (`GET` or `POST`)

```html
<form action="/my-handling-form-page" method="post">
    <div>
        <label for="name">Name:</label>
        <input type="text" id="name" />
    </div>
    <div>
        <label for="mail">E-mail:</label>
        <input type="email" id="mail" />
    </div>
    <div>
        <label for="msg">Message:</label>
        <textarea id="msg"></textarea>
    </div>
</form>
```

- `input`

  - `type` 속성

  - 어떻게 입력 받을 것인지 정의 ⭐

  - `input` 태그는 자동 닫힘 태그

  - 요소가 끝날 때 `/` 추가

    ```html
    <input type="text" value="by default this element is filled with this text" />
    ```

- `button`

  - 데이터를 서버로 보낼 수 있게 만든다.
  - `submit`
    - 폼 데이터를 action 속성에 정의된 웹페이지에 전송
  - `reset`
    - 모든 폼 위젯을 기본 값으로 바꿈 
    - UX 관점에서 이 방법은 좋은 방법이 아니다.
  - `button`
    - 아무 행동도 하지 않는다.
    - js 사용시 유용하다.

  

