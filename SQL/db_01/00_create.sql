-- 테이블 만들기
CREATE TABLE healthcare (
id PRIMARY KEY,
sido INTEGER NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,
va_left REAL NOT NULL,
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- csv import 하기
.mode csv 
.import health.csv healthcare

-- 10살보다 어린 사람 수 
SELECT COUNT(*) FROM healthcare WHERE age < 10;
-- 성별이 1인 사람 수 
SELECT COUNT(*) FROM healthcare WHERE gender=1;
-- smoking이 3이면서 dirinking이 1인 사람 수
SELECT COUNT(*) FROM healthcare WHERE smoking = 3 AND is_drinking = 1;
-- 양쪽 시력이 모두 2.0 이상인 사람 수 
SELECT COUNT(*) FROM healthcare WHERE va_left >= 2.0 AND va_right >= 2.0;
-- sido 중복 제외 모두 출력
SELECT DISTINCT sido FROM healthcare;

-- 개인적인 조합

-- 성별이 2면서 dirinking이 1인 사람 수 
SELECT COUNT(*) FROM healthcare WHERE gender = 2  AND is_drinking = 1
