# CSS 기초 🌱

*Cascading Style Sheets*

**스타일을 지정하기 위한 언어**

우리가 눈으로 보는 잘 꾸며진 웹사이트



## CSS 시작하기 전 📖

**주로 활용하는 속성 위주로 기억하면 편하다.**



## CSS 구문 📝

```css
h1 {
    color : blue;
    font-size : 15px;
}
```

- `CSS` 구문은 선택자를 통해 스타일을 지정할 `HTML` 요소를 선택한다.
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미 
  - ##### 속성 (`Property`) : 어떤 스타일 기능을 변경할지 결정 
  - ##### 값 (`Value`) : 어떻게 스타일 기능을 변경할지 결정



## CSS 정의 방법 💡

- 인라인 (`inline`)  

- 내부 참조 (`embedding`)

  ```css
  <style>
  	h1 {
      	color: blue;
          font-size: 100px;
      }
  </style>
  ```

  

- 외부 참조 (`link file`) : 분리된` CSS` 파일

  - 외부 `CSS` 파일을 `<head>`내 `<link>`를 통해 불러온다.



## CSS 기초 선택자 ✔

- 요소 선택자 

  - `HTML 태그`를 직접 선택 

  

- 클래스(`class`) 선택자

  - 마침표(`.`)문자로 시작하며, 해당 클래스가 적용된 항목을 선택

  

- 아이디(`id`) 선택자 

  - `#` 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용 
  - 여러 번 사용해도 동작하지만, 단일 `id`를 사용하는 것을 권장



## CSS with 개발자 도구 🔨

- `styles` : 해당 요소에 선언된 모든 `CSS `
- `computed` : 해당 요소에 최종 계산된 `CSS`













