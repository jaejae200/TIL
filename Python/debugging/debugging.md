# 디버깅(Debugging) ✒️

- ### branches
  
  - 모든 조건이 원하는대로 동작하는가?

- ### for loops
  
  - 반복문에 진입하는지 , 원하는 횟수만큼 실행되는지

- ### while loops
  
  - for loops와 동일, 종료조건이 제대로 동작하는지

- ### function
  
  - 함수 호출시, 함수 파라미터, 함수 결과

## 📌 활용 방법

- ### print 함수 활용

- ### 개발 환경에서 제공하는 기능 활용

- ### Python tutor 활용 (단, 단순한 Python 코드)

- ### 머리로 생각하고 눈으로 버그없애기
  
  - 에러 메세지가 발생하는 경우
    
    - 해당하는 위치를 찾아 메시지를 해결
  
  - 로직 에러가 발생하는 경우
    
    - 명시적인 에러 메세지 없이 다른 결과가 나온 경우
      
      - 어디까지 정상 작동하는지 확인 
      
      - 전체 코드를 살펴보기
      
      - 누군가에게 설명해보기

## 📌 에러와 예외

### 문법 에러(Syntax Error)

- #### SyntaxError가 발생하면 Python program 실행이 되지 않음

- ```python
  if else
  
  File "<ipython-input-1-f8a097d0a685>", line 1
  if else ^ # 문제가 발생한 위치를 표현
  SyntaxError: invalid syntax
  ```

### 예외(Exception)

- #### 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
  
  - 문장이나 표현식이 올바르더라도 발생하는 에러

- #### 실행 중에 감지되는 에러들을 예외라고 부름

- #### 예외는 여러 Type 으로 나타나고, 메시지의 일부로 출력

- #### 모든 내장 예외는 Exception Class를 상속받아 이뤄짐

- #### 사용자 정의 예외를 만들어 관리할 수 있음
  
  - 파이썬 내장 예외(built-in-exceptions)
    
    ![](C:\Users\kj310\AppData\Roaming\marktext\images\2022-07-18-16-29-20-image.png)

### 📌 예외 처리

- ### try 문(statement)
  
  - 오류가 발생할 가능성이 있는 코드를 실행
  
  - 예외가 발생하지 않으면 except 없이 실행 종료

- ### except 문
  
  - 예외가 발생하면 실행
  
  - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함

- ### 처리 순서

![](C:\Users\kj310\AppData\Roaming\marktext\images\2022-07-18-16-31-05-image.png)

- #### 작성 방법
  
  ```python
  try:
      try 명령문
  except 예외그룹-1 as 변수-1 :
      예외 처리 명령문 1 #except 는 여러 그룹으로 설정 가능
  finally:
      finally 명령문
  ```

### 📌 정리

- ### try
  
  - 코드를 실행함

- ### except
  
  - try 문에서 예외가 발생 시 실행함

- ### else
  
  - try 문에서 예외가 발생하지 않으면 실행함

- ### finally
  
  - 예외 발생 여부와 관계없이 항상 실행함 (Thank you for wathing)

## 📌 예외 발생 시키기

### raise statement

- ### raise를 통해 예외를 강제로 발생
  
  ```python
  raise <표현식> (메시지)
  ```
