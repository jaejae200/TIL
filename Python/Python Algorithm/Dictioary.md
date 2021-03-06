# 딕셔너리 (Dictioary) ✒

Python에는 딕셔너리(dict) 자료구조가 내장 되어 있다.

```python
# Non-sequence & Key-Value+ 쌍으로 이루어진 자료구조.
# Key는 변경 불가능하다 (immutable) Value는 변경 가능하다

info = {
    'name' : 'kim'
    'gender' : 'male'
    'address' : 'seoul'
}
```

해시 함수와 해시 테이블을 이용하기 때문에 삽입, 삭제, 수정, 조회 연산 속도가 리스트보다 빠르다.



## 💡 딕셔너리 언제 사용해야할까?

1. 리스트 사용하기 힘든 경우

2. 데이터에 대한 **빠른 접근 탐색**이 필요한 경우

3. 현실적인 데이터 관리를 위해서

   

## 📝 해시 테이블 

	### 📌 해시 함수

임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수

```python
# 'happy'
    	👇
# 489f719cadf919094ddb38e7654de153ac33c02febb5de91e5345cbe372cf4a0
```

### 📌 해시

함수를 통해 얻어진 임의의 값



## 📝 딕셔너리 연산의 시간 복잡도

`Get item`  		  #O(1)

`insert item`  	#O(1)

`Updata item` 	 #O(1)

`Delete item` 	 #O(1)

`Search item`	  #O(1)



## 🔎 딕셔너리 기본 문법

```python
# ==================================================================================
# 1. 선언

<dict> = {
    key : key_value # key = value 선언
}

# ==================================================================================
# 2. 삽입 / 수정

<dict>['key'] = 'new_value' # 기존 key = value 값 수정
<dict>['new_key'] = 'new_value' # 새로운 key = value 삽입

# ==================================================================================
# 3. 삭제

key = <dict>.pop('key')  # 내부의 존재하는 key의 value 삭제 및 반환
		          # 존재하지 않는 key = keyerror 발생

key = <dict>.pop('key', 'default') # 두 번째 인자로 기본 값을 지정하여 keyError 방지 가능

# ==================================================================================
# 4. 조회
	# key에 해당하는 value 반환

<dict>.get('key') # key가 없는 경우 None을 반환한다.
<dict>[key] 		# key가 없는 경우 error 반환한다.

# ==================================================================================
```

### 🔎 딕셔너리 메서드

```python
# ================================================================

<dict>.keys() # dict에서 모든 key를 반환한다 <class 'dict_keys'>
				# 리스트와 비슷하게 사용해도 ⭕
    
# ================================================================

<dict>.values() # dict에서 모든 value를 반환한다

# ================================================================

<dict>.items() # dict에서 key와 value를 같이 반환한다
				# (key, value) = tuple

# ================================================================
```

