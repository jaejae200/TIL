# 기본 함수와 TABLE



## 🔨 SQLite Aggregate Functions

- ### 집계 함수

  - **값 집합에 대한 계산을 수행하고 단일 값을 반환**

    - 여러 행으로부터 하나의 결과값을 반환하는 함수

  - ##### `SELECT` 구문에서만 사용된다.

  - ##### 예시

    - 테이블 전체 행 수를 구하는 `COUNT(*)`
    - age 컬럼 전체 평균 값을 구하는 `AVG(age)`

  

- ### Functions

  - #### `COUNT`

    - **그룹의 항목 수**를 가져온다.

  - #### `AVG`

    - 모든 값의 **평균**을 계산

  - #### `MAX`

    - 그룹에 있는 모든 값의 **최댓값**을 가져온다.

  - #### `MIN`

    - 그룹에 있는 모든 값으 **최솟값**을 가져온다.

  - #### `SUM`

    - **모든 값의 합**을 계산한다.

      

## 🔎 LIKE

- *'query data based on pattern matching'*

- **패턴 일치**를 기반으로 **데이터를 조회**하는 방법

  

- SQLite는 패턴 구성을 위한 2개의 **`wildcards`** 제공

  - #### `%` (percent sign)

    - 0개 이상의 문자

  - #### `_ ` (underscore)

    - 임의의 단일 문자

  

- wildcards 사용 예시

```sqlite
SELECT * FROM 테이블 WHERE 컬럼 LIKE '패턴';
```

| 와일드 카드 패턴 | 의미                                          |
| ---------------- | --------------------------------------------- |
| `2%`             | 2로 시작하는 값                               |
| `%2`             | 2로 끝나는 값                                 |
| `%2%`            | 2가 들어가는 값                               |
| `_2%`            | 아무 값이 하나 있고 두 번째가 2로 시작하는 값 |
| `1___`           | 1로 시작하고 총 4자리인 값                    |
| `2_%_% / 2__% `  | 2로 시작하고 적어도 3자리인 값                |



## 🔎 ORDER BY

- *'sort a result set of a query'*

- 조회 결과 집합을 정렬

- ##### SELECT 문에 추가하여 사용

  

- 정렬 순서를 위한 **2개의 keyword 제공**

  - ##### `ASC` - 오름차순 (default)

  - ##### `DESC` - 내림차순

```sqlite
-- users 나이 순으로 오름차순 정렬하여 상위 10개의 이름만 조회
SELECT first_name FROM users ORDER BY age ASC LIMIT 10;

-- 나이, 성 순으로 오름차순 정렬
SELECT * users ORDER BY age, last_name LIMIT 10;

-- 계좌 잔액 순으로 내림차순 정렬 성과 이름 10개 조회
SELECT last_name, first_name ORDER BY balance DESC, last_name ASC LIMIT 10; 
```



## 📝 기본 함수

### ✔ 문자열 함수

- ##### `SUBSTR` (문자열, start, length) :
  
  - 문자열 자르기
  - 시작 인덱스는 1, 마지막 인덱스는 -1
- ##### `TRIM` (문자열), `LTRIM` (문자열), `RTRIM` (문자열)
  
  - 문자열 공백 제거
- ##### `LENGTH` (문자열) 
  
  - 문자열 길이
- ##### `REPLACE` (문자열, 패턴, 변경값)

  - 패턴에 일치하는 부분을 변경

- ##### `UPPER` (문자열), `LOWER` (문자열)

  - 대, 소문자 변경

- ##### `||`

  - 문자열 합치기 (concatenation)

  

### ✔ 숫자 함수

- ##### `ABS` (숫자)

  - 절대 값

- ##### `SIGN` (숫자)

  - 부호 (양수 1, 음수 -1, 0 0)

- ##### `MOD` (숫자1, 숫자2) 

  - 숫자 1을 숫자 2로 나눈 나머지

- ##### `CEIL` (숫자), `FLOOR` (숫자), `ROUND` (숫자, 자리)

  - 올림, 내림, 반올림

- ##### `POWER` (숫자1, 숫자2)

  - 숫자 1의 숫자 2 제곱

- ##### `SQRT` (숫자)

  - 제곱근
  
  

### ✔ 산술 연산자

- ##### `+`,` -`, `*`, `/`와 같은 산술 연산자와 우선 순위를 지정하는 `() `기호를 연산에 활용할 수 있다.

```sqlite
SELECT age+1 FROM users;
```



## 📝 GROUP BY

### ✔ GROUP BY

- *"make a set of summary rows from a set of rows"*

- `SELECT` 문의 `optional` 절

- 행 집합에서 요약 행 집합을 만든다

- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만든다

  

- GROUP BY 절에 명시하지 않은 컬럼은 별도로 지정할 수 없음.

  - 그룹마다 하나의 행을 출력하게 되므로 집계 함수 등을 활용해야 함

  

-  GROUP BY의 결과 는 정렬되지 않음

  - 기존의 순서와 바뀌는 모습도 있음
  - 원칙적으로 관계형 데이터베이스에서는 ORDER BY를 통해 정렬

  

- #### ⭐ 문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성해야 한다 ⭐

  ```sqlite
  SELECT * FROM 테이블 GROUP BY 컬럼1, 컬럼2;
  ```

  ```sqlite
  -- 집계함수와 활용하였을 때 의미가 있다! 💡
  
  SELECT * FROM users GROUP BY last_name;
  
  -- 그룹화된 각각의 그룹이 하나의 집합으로 집계함수의 인수로 넘겨진다. (아래 표 참조)
  ```

  | id   | last_name | id   | last_name |
  | ---- | --------- | ---- | --------- |
  | 1    | 김        | 1    | 김        |
  | 2    | 김        | 3    | 박        |
  | 3    | 박        | 4    | 이        |
  | 4    | 이        |      |           |



 ### ✔ Aggregate Function (집계 함수) 다시 보기

  - 값 집합에 대한 계산을 수행하고 단일 값을 반화 

    - 여러 행으로부터 하나의 결괏값을 반환하는 함수
    
  - #### ⭐ SELECT 구문에서만 사용된다 ⭐

  - 예시

    - 테이블 전체 행 수를 구하는 `COUNT (*)`
    
    - age 컬럼 전체 평균을 구하는 `AVG (age)`
    
      

### ✔ ALIAS

- 컬럼명이나 테이블명이 너무 길거나 다른 명칭으로 확인하고 싶을 때 `ALIAS` 활용

- `AS`를 생략하여 공백으로 표현 가능

- 별칭에 공백, 특수문자 등이 있는 경우 따옴표로 묶어서 표기

  ```sqlite
  SELECT last_name 성 FROM users;
  SELECT last_name AS 성 FROM users;
  SELECT last_name AS 성 FROM users; WHERE 성 = '김';
  ```




### ✔ HAVING

- 집계함수는 `WHERE` 절의 조건식에서는 사용할 수 없음 (실행 순서에 의함)

  - `WHERE`로 처리하는 것이 `GROUP BY` 그룹화보다 순서상 앞서 있기 때문

- 집계 결과에서 조건에 맞는 값을 따로 활용하기 위해서`HAVING`을 활용

  ```sqlite
  SELECT * FROM 테이블 GROUP BY 컬럼1, 컬럼2 HAVING 그룹 조건;
  ```



###  ✔ SELECT 문장 실행 순서

- #### `FROM`  👉 `WHERE`  👉 `GROUP BY` 👉 `HAVING` 👉 `SELECT` 👉 ` ORDER BY`

  - `FROM` 🔎 테이블을 대상으로
  - `WHERE` 🔎 제약 조건에 맞춰 뽑아서
  - `GROUP BY` 🔎 그룹화한다.
  - `HAVING` 🔎 그룹 중에 조건과 맞는 것을
  - `SELECT` 🔎 조회하며
  - `ORDER BY` 🔎 정렬하고
  - `LIMIT /  OFFSET` 🔎 특정 위치의 값을 가져온다



## 📝 ALTER TABLE

###  ✔ ALTER TABLE

```sqlite
-- 1. 테이블 이름 변경
ALTER TABLE table_name
RENAME TO new_name;

-- 2. 새로운 컬럼 추가
ALTER TABLE table_name
ADD COLUMN column_definition;

'''
💡 테이블에 있던 기존 레코드들에는 새로 추가할 필드에 대한 정보가 없다면
   NOT NULL 형태의 컬럼은 추가가 불가능하다

해결 방법 2가지 ⭐
1. NOT NULL 없이 공백으로 추가하기
2. 기본 값 (DEFAULT) 설정하기
'''

-- 3. 컬럼 이름 수정
ALTER TABLE table_name
RENAME COLUMN current_name TO new_name

-- 4. 컬럼 삭제
ALTER TABLE table_name
DROP COLUMN column_name;
```

## 📝 CASE

- ##### `CASE` 문은 특정 상황에서 데이터를 변환하여 활용할 수 있음

- ##### `ELSE`를 생략하는 경우 `NULL` 값이 지정됨.

  ```sqlite
  CASE
  	WHEN 조건식 THEN 식
  	WHEN 조건식 THEN 식
  	ELSE 식
  END
  
  -- gender가 1인 경우는 남자를 gender가 2인 경우에는 여자를 출력하시오.
  
  SELECT
  	id,
  	CASE
  		WHEN gender = 1 THEN '남자'
  		WHEN gender = 2 THEN '여자'
  	END
  FROM healthcare
  ```



## 📝 서브 쿼리

- 특정한 값을 메인 쿼리에 반환하여 활용

- 실제 테이블에 없는 기준을 이용한 검색이 가능

- 소괄호로 감싸서 사용, 메인 쿼리의 칼럼을 모두 사용할 수 있음

- 반대로 , 메인 쿼리는 서브 쿼리의 칼럼을 이용할 수 없음

  ```sqlite
  SELECT *
  FROM 테이블
  WHERE 칼럼1 = (
  	SELECT 칼럼1
  	FROM 테이블
  );
  ```



#### ✔ 단일행 서브쿼리

- 서브쿼리의 결과가 0또는 1개인 경우

- 단일행 비교 연산자와 함께 사용 `(=, <, <=, >=, >, <>)`

  

- #### `WHERE` 에서 활용

  ```sqlite
  -- users에서 가장 나이가 작은 사람의 수는?
  
  SELECT age, COUNT(*)
  FROM users 
  WHERE age = (SELECT MIN(age) FROM users);
  ```



- #### `SELECT` 에서 활용

  ```sqlite
  -- 전체 인원과 평균 연봉, 평균 나이를 출력하세요.
  
  SELECT
      (SELECT COUNT(*) FROM users) AS "전체 인원",
      (SELECT AVG(balance) FROM users) AS "평균 연봉",
      (SELECT AVG(age) FROM users) AS "평균 나이"
      ;
  ```

  

- #### `UPDATE` 에서 활용

  ```sqlite
  -- users의 balance를 AVG(balance) 수정
  UPDATE users
  SET balance = (SELECT AVG(balance) FROM users);
  ```

  

#### ✔ 다중행 서브쿼리

- 서브쿼리 결과가 2개 이상인 경우

- 다중행 비교 연산자와 함께 사용(IN, EXISTS 등)

  ```sqlite
  -- Q. users에서 이은정과 같은 지역에 사는 사람의 수는? 
  
  SELECT COUNT(*)
  FROM users
  WHERE country IN (
      SELECT country
      FROM users
      WHERE first_name = '은정' AND last_name='이'
  );
  ```

  

#### ✔ 다중컬럼 서브쿼리

```sqlite
-- Q. 특정 성씨에서 가장 어린 사람들의 이름과 나이

SELECT last_name, first_name, age 
FROM users 
WHERE (last_name, age) IN (
    SELECT last_name, MIN(age) 
    FROM users 
    GROUP BY last_name) 
ORDER BY last_name;
```

