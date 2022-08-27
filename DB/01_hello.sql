-- SQLite
-- classmate table 생성
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT
    age INTEGER
    address TEXT
);

-- 테이블 목록 조회
.tables

-- 특정 테이블 스키마 조회
.schema classmates 

-- 값 추가
INSERT INTO classmates VALUES (1, '김재우');

INSERT INTO classmates VALUES (2, '김재우우');

-- 테이블 삭제