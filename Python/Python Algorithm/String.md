# 문자열(String) ✒

문자열은 **immutable** (변경 불가능한) 자료형



## 📝 문자열 슬라이싱

```python
txt = [a, b, c, d, e, f]

txt[2:5] # cde

txt[2:5:2] # ce

txt[2:5:-1] # error
txt[5:2:-1] # fed  # ⭐ -1, 반대로 갈 경우 역 순으로 index 넣어줌
				   # ⭐ 문자열을 뒤집어줄 때 많이 사용한다. 
    
txt[:3] #abc
txt[3:] #def

# TIP!!💡 -x index 앞에 전체 index를 대입해보면 쉽게 위치를 알 수 있다.
```

|       | a    | b    | c    | d    | e    | f    |
| ----- | ---- | ---- | ---- | ---- | ---- | ---- |
| index | 0    | 1    | 2    | 3    | 4    | 5    |
| index | -6   | -5   | -4   | -3   | -2   | -1   |



## 📝 문자열 메서드(method)

- `.split()`

  - 문자열을 **일정 기준으로 나누어** 리스트로 반환

- `.strip()`

  - 문자열 양쪽 끝에 있는 특정 문자를 모두 제거한 **새로운 문자열을 반환 공백 제거 유용**

- `.find()`

  - 특정 **문자가 나타나는 위치**(index)를 반환 
  - 문자가 없다면 **-1 반환** ⭐ (실행이 멈추지 않음)

- `.index()`

  - 특정 **문자가 나타나는 위치**(index)를 반환
  - 문자가 없다면 **오류 발생** ⭐ (실행이 멈춤)

- `.count()`

  - 문자열에서 **특정 문자가 몇 개**인지 반환
  - 문자열의 개수도 확인 가능하다

- `.replace()`

  - 문자열에서 **기존 문자를 새로운 문자로 수정**한 새로운 문자열 반환

- `.join()`

  - 각각 원소 사이에 **특정 문자를 삽입**한 새로운 문자열 반환

  - 공백 출력, 콤마 출력 등 **원하는 출력 형태**를 위해 사용

    

## 📝 아스키(ASCII) 코드

- ### 컴퓨터는 숫자만 이해할 수 있다

  - 비트(bit)
    - 0과 1 두 가지 정보만 표현
    
  - 바이트(byte)
    - 데이터를 저장하는 기본 단위
    
    - 1 byte == 8 bits
    
      

### 📌 아스키 코드란?

- #### 알파벳을 표현하는 대표 인코딩 방식

- 각 문자를 표현하는데 **1byte** 사용

  - 1bit : 통신 에러 검출용
  - 7bit : 문자 정보 저장 (총 128개)

- ```python
  ord() # 문자를 아스키코드로 변환 🔍
  
  chr() # 아스키코드를 문자로 변환 🔍
  
  	  # 시저 암호 문제 해결에 유용 ⭐
  ```

  
