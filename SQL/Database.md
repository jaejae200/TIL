# Database 🗃

- #### 체계화된 데이터의 모임 👨‍👩‍👧‍👧

- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합

- 논리적으로 연관된 자료 모음

- #### 몇 개의 자료 파일을 조직적으로 통합

  - 자료 항목의 중복을 없앤다.

  - 자료를 구조화하여 기억한다.

  - 자료의 집합체이다.

    

## 📝 RDB 

- ### 관계형 데이터베이스 (Relational Database)

  - 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형

  - `key`와 ` value `들의 간단한 관계를 표 형태로 정리한 데이터베이스

    | 고유 번호 (Primary key) |  이름  | 주소 | 나이 |
    | :---------------------: | :----: | :--: | :--: |
    |            1            | 홍길동 | 제주 |  20  |
    |            2            | 김길동 | 서울 |  30  |
    |            3            | 박길동 | 독도 |  40  |

- #### 스키마 (schema)

  - 자료의 구조, 표현 방법, 관계 등 전반적인 명세를 기술한 것



## 📝 RDBMS

- #### 관계형 데이터베이스 관리 시스템

  - #### SQLite
    
    - ##### 비교적 가벼운 데이터베이스
    - 로컬에서 간단한 DB 구성 가능, 오픈 소스 프로젝트이기 때문에 자유롭다 💡

### ⭐ SQLite Data Type ⭐

1.  `NULL` 💡

   - 아무것도 없는 상태

2.  `INTEGER` 💡

   - 크기에 따라  0, 1, 2, 3, 4, 5, 6 또는 8 바이트에 저장된 부호 있는 정수

3. `REAL` 💡

   - 8 바이트 부동 소수점 숫자로 저장된 부동 소수점 값

4.  `TEXT` 💡

5.  `BLOB` 💡

   -  입력된 그대로 정확히 저장된 데이터 (별다른 타입 없이 그대로 저장)

     

## 📝 SQL

데이터 관리를 위해 설계된 특수 목적으로 만들어진 프로그래밍 언어

### ✔ SQL Keywords - Data Manipulation  Language

- #### `INSERT` : 새로운 데이터 삽입 (추가) ⭐

- #### `SELECT` : 저장되어있는 데이터 조회 ⭐

- #### `UPDATE` : 저장되어있는 데이터 갱신 ⭐

- #### `DELETE` : 저장되어있는 데이터 삭제 ⭐



## 📝 테이블 생성 및 삭제

```sqlite
-- 데이터베이스 생성하기

$ sqlite3 tutorial.sqlite3
sqlite> .database

-- csv 파일을 table로 만들기
==================================
sqlite> .mode csv
sqlite> .import hellodb.csv examples
sqlite> .tables
examples

==================================
-- 테이블 생성 및 삭제 ⭐
SELECT * FROM examples;

==================================

-- SELECT 확인하기 ⭐
sqlite> SELECT * FROM examples;

'''
SELECT 문은 특정 테이블의 레코드(행) 정보를 반환!
'''
```



- #### 테이블 생성 및 삭제 statement

```sqlite
-- CREATE
CREATE TABLE classmates(
id INTEGER PRIMARY KEY,
name TEXT
);

==================================
-- 테이블 생성 및 확인하기
sqlite> CREATE TABLE calssmates(
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT
   ...> );
sqlite> .tables
classmates examples  # CREATE는 테이블을 생성한다!

==================================
-- 특정 테이블의 schema 조회

sqlite> .schema classmates
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);
```

```sqlite
-- DROP 
-- TABLE을 버린다.

DROP TABLE classmate;

sqlite> DROP TABLE classmate;
sqlite> .tables
examples
```



## 📝 필드 제약 조건

- ### `NOT NULL` : `NULL` 값 입력 금지
- #### `UNIQUE` : 중복 값 입력 금지 (`NULL` 값은 중복 입력 가능)
- #### `PRIMARY KEY` : 테이블에서 반드시 하나. `NOT NULL + UNIQUE`
- #### `FOREIGN KEY` : 외래키. 다른 테이블의 KEY
- #### `CHECK` : 조건으로 설정된 값만 입력 허용
- #### `DEFAULT` : 기본 설정 값



## 📝 CRUD

### ✔ CREATE

- ##### INSERT ⭐

  - ##### *'insert a single row into a table'*

  - 테이블에 단일 행 삽입

    ```sqlite
    INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);
    ```

  - 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력

    ```sqlite
    INSERT INTO 테이블_이름 VALUES (값1, 값2, 값3);		
    ```



### ✔ READ

- #### SELECT 

  - #####  *"query data from a table"*
  - #### 🔎 테이블에서 데이터를 조회
  - #### SELECT 문은 SQLite에서 가장 기본이 되는 문, 다양한 절와 함께 사용한다
    
    - #### ```ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY ...```

  

- #### LIMIT 

  - ##### *"constranin the number of rows returned by a query"*
  - #### 🔎 쿼리에서 반환되는 행 수를 제한
  - #### 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용하기도 한다.

  

- #### WHERE 

  - ##### *"specify the search condition for rows returned by the query"*

  - #### 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정

  - #### 여러 비교 연산자들이 존재 (후에 서술)

  

- #### SELECT DISTINCT 

  - ##### *"remove duplicate rows in the result set"*
  - #### 🔎 조회 결과에서 중복 행을 제거
  - #### DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함

  

- #### OFFSET 

  - ##### 처음부터 주어진 요소나 지점까지의 차이를 나타낸다
  - ##### 문자열 'abcdef' 에서 문자 'c' 는 시작점 'a' 에서 2의 OFFSET



####  WHERE절에서 사용할 수 있는 연산자

- #### 비교 연산자

  - ##### `=, > , >=, <, <=` 는 숫자 혹은 문자 값의 대/소 동일 여부를 확인하는 연산자

  

- #### 논리 연산자

  - ##### `AND`

    - 앞에 오는 조건과 뒤에 오는 조건이 모두 참인 경우

  - ##### `OR`

    - 앞의 조건이나 뒤의 조건이 모두 참인 경우

  - ##### `NOT`

    - 뒤에 오는 조건과 반대로

  - ##### `BETWEEN (값1 AND 값2)`

    - 값1과 값2 사이의 비교 (값1 <= 비교값 <= 값2)

  - ##### `IN (값1, 값2, ...)`

    - 목록 중에 값이 하나라도 일치하면 성공

  - ##### `LIKE`

    - 비교 문자열과 형태 일치
    - 와일드카드 (% : 0개 이상 문자, _ : 1개 단일 문자)

  - ##### `IS NULL / IS NOT NULL`

    - NULL 여부를 확인할 떄는 항상 = **대신에 IS를 활용**

  

- #### 부정 연산자

  - 같지 않다 ` (!=, ^=, <>)`
  - ~와 같지 않다 ` (NOT 칼럼명 =)`

  

- #### 연산자 우선순위

  - 1순위 : 괄호 ()
  
  - 2순위 : NOT
  
  - 3순위 : 비교 연산자, SQL
  
  - 4순위 : AND
  
  - 5순위 : OR 
