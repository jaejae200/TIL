# OOP 기초 ✒



## 📌 객체(object)의 특징

- #### 타입 `type` : 어떤 연산자 `operator` 와 조작 `method` 이 가능한가?

- #### 속성 `attribute` : 어떤 상태 ` 데이터`를 가지는가?

- #### 조작법 `method` : 어떤 행위 `함수` 를 할 수 있는가?

  

## 📌 기본 문법

- ```python
  # 클래스 정의
  class Myclass:
      pass 
  # 인스턴트 생성
  my_instance = MyClass()
  # 메서드 호출
  my_instance.my_method()
  # 속성
  my_instance.my_attribute
  ```

  
  
- #### 객체의 틀(Class) 을 가지고 객체(Instance) 를 생성한다

  - `class` : 객체들의 분류
  - `instance` : 하나하나의 실체나 예

  - **Python은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스이다!**

  

- ### 속성

  - ##### 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미

  

- ### methot

  - ##### 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)

  

- #### 객체 비교하기

  - `==`
    - 변수가 참조하는 객체가 동등한 경우 `True`
  - `is`
    - 두 변수가 동일한 객체를 가르키는 경우 `True`

  

- ### instance method 

  - `instance` 변수를 사용하거나, `instance` 변수에 값을 설정하는 `method`

  - `class`내부에서 정의되는 `method`의 기본

  - 호출 시, 첫번째 인자로 `instance` 자기 자신 `self` 전달됨

  - ```python
    class Myclass
    	def instance_method(self, arg1, ...)
    ```

  

- ### constructor method 

  - `instance` 객체가 생성될 떄 자동으로 호출되는 `method`
  - `instance` 변수들의 초기값을 설정
    - `instance` 생성
    - `__init__` `method` 자동 호출

  

- ### destructor method 

  - `instance` 객체가 소멸되기 직전에 호출되는 메소드
    - `__del__`

