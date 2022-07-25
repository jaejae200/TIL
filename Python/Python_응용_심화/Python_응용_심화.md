# Python 응용/심화

## 📝 추가 문법

### 📌 List Comprehension

  - 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

    ```python
    [<expression> for <변수> in <iterable>]
    [<expression> for <변수> in <iterable> if <조건식>]
    ```

### 📌 Dictionary Comprehension

  - 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

    ```python
    {key: value for <변수> in <iterable>}
    {key: value for <변수> in <iterable> if <조건식>}
    ```

### 📌lambda [parameter] : 표현식

  #### 	🔖 람다함수

- 표현식을 계산한 결과값을 반환하는 함수

- 이름이 없는 함수 = 익명 함수

#### 🔖 특징

- `return` 문을 가질 수 없음
- 간편 조건문 외 조건문이나 반복문을 가질 수 없음

#### 🔖 장점

- 함수를 정의해서 사용하는 것보다 간결함
- `def`를 사용할 수 없는 곳에서도 사용 

#### 🔖 filter

- 순회 가능한 데이터구조의 모든 요소에 함수 적용
- 그 결과가 `True`인 것들을 `filter object`로 반환

``` python
def odd(n):
    return n % 2
numbers = [1, 2, 3]
result = filter(odd, numbers)
print(result, type(result))

# <filter object at [] <class 'filter'>

list(result)

[1, 3]
```

## 📝 Python Standard Library, PSL

- Python에서 기본적으로 설치된 모듈과 함수
  - ex) `random.py = import random`

## 📌 Python Package index, PIP

- PyPI에 저장된 외부 package들을 설치하도록 도와주는 package 관리 시스템

- package 설치

  `$ pip install SomePackage`  최신 버전

  `$ pip install SomePackage == 1.0.5` 특정 버전

  `$ pip install SomePackage >= 1.0.4` 최소 버전

  - `bash`나 `cmd` 환경에서 가능하다.
  - `$pip list` 사용하여 설치된 pip 목록을 확인할 수 있다.
  - `$ pip freeze` list와 비슷한 목록을 만들지만 txt로 만들어서 관리함
    - `$ pip freeze > requirements.txt`

## 📌 venv

- #### 가상 환경을 만들고 관리하는데 사용하는 모듈

- #### 특정 Directory에 가상 환경을 만들고, 고유한 Python Package 집합을 가질 수 있다


