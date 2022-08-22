## Join 📥

- ##### 관계형 데이터베이스의 가장 큰 장점이자 핵심적인 기능
- 일반적으로 데이터베이스에는 하나의 테이블에 많은 데이터를 저장하는 것이 아니라
  **여러 테이블로 나눠 저장하게 되며, 여러 테이블을 결합 (Join) 출력하여 활용**
- ##### 일반적으로 레코드는 ⭐ 기본키(PK)나 ⭐ 외래키(FK) 값의 관계에 의해 결합함  👨‍👩‍👧‍👦 👈 👩‍👧‍👦

![image-20220823051757879](C:\Users\kj310\AppData\Roaming\Typora\typora-user-images\image-20220823051757879.png)



### 🔎 대표적인 JOIN

#### ✔ INNER JOIN : 두 테이블에 모두 일치하는 행만 반환

```sqlite
SELECT *
FROM 테이블_1 [INNER] JOIN 테이블2
	ON 테이블1.칼럼 = 테이블2.칼럼;

-- [INNER] 생략
SELECT *

-- 실습
-- 0 
SELECT *
FROM user JOIN role
	ON user.role_id = role.id
-- 1 

SELECT *
FROM user JOIN role
	ON user.role_id = role.id
WHERE role.id = 2;

-- 2 이름을 내림차순으로
SELECT *
FROM user JOIN role
	ON user.role_id = role.id
WHERE role.id = 2 ORDER BY users.name DESC;
	
```

#### ✔ OUTER JOIN : 동일한 값이 없는 행도 반환

```sqlite
SELECT * 
FROM 테이블_1 [LEFT|RIGHT|FULL] OUTER JOIN 테이블_2
	ON 테이블_1.칼럼 = 테이블_2.칼럼
	
-- 0.
SELECT * 
FROM articles LEFT OUTER JOIN user
	ON articls.user_id = user.id;
	
-- 1.
SELECT * 
FROM articles LEFT OUTER JOIN user
	ON articls.user_id = user.id
WHERE articls.user_id IS NOT NULL;

-- FULL
SELECT * 
FROM articles FULL OUTER JOIN user
	ON articls.user_id = user.id
```

#### CROSS JOIN : 모든 데이터의 조합

```sqlite
SELECT *
FROM users CROSS JOIN role;
```



- ### 관계 정리 💡

  ![image-20220823055328797](C:\Users\kj310\AppData\Roaming\Typora\typora-user-images\image-20220823055328797.png)

