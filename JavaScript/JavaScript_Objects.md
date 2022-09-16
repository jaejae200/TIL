# JavaScript Objects



## 객체의 정의와 특징

- 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현

- key는 문자열 타입만 가능

  - key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현

-  value는 모든 타입(함수포함) 가능

- 객체 요소 접근은 점 또는 대괄호로 가능

  - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

  ```js
  const me = {
      name: 'jack',
      phoneNumber: '01012345678',
      'samsung products': {
          buds: 'Galaxy Buds pro',
          galaxy: 'Galaxy s20’,
      },
  }
  
  console.log(me.name)
  console.log(me.phoneNumber)
  console.log(me['samsung products'])
  console.log(me['samsung products'].buds)
  ```

  

- 메서드는 객체의 속성이 참조하는 함수

- 객체.메서드명() 으로 호출 가능

- 메서드 내부에서는 this 키워드가 객체를 의미함

  ```js
  const me = {
      firstName: 'John',
      lastName: 'Doe' , 
      getFullName: function () {
          return this.firstName + this.lastName
      }
  }
  ```

  

## 객체 관련 ES6 문법 익히기

- ES6에 새로 도입된 문법들로 객체 생성 및 조작에 유용하게 사용 가능
  - 속성명 축약
  - 메서드명 축약
  - 계산된 속성명 사용하기
  - 구조 분배 할당
    - 구조 분배 할당은 배열도 가능하다
  - 객체 전개 구문



## JSON

*JavaScript Object Notation*



- key-value쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포맷
- 자바스크립트의 객체와 유사하게 생겼으나 실제로는 문자열 타입
  - 따라서 JS의 객체로써 조작하기 위해서는 구문 분석(parsing)이 필수



- 자바스크립트에서는 JSON을 조작하기 위한 두 가지 내장 메서드를 제공
  - JSON.parse()
    - JSON => 자바스크립트 객체
  - JSON.stringify()
    - • 자바스크립트 객체 => JSON

