# 스택, 큐 (Stack, Queue)✒

## 📝 스택

자료구조의 대표 동작 ⭐ 

- `push` 스택에 새로운 데이터를 삽입하는 행위 

- `pull` 스택의 가장 마지막 데이터를 가져오는 행위

- Python은 List로 스택을 간편하게 사용할 수 있다

  ![image-20220801105139618](C:\Users\kj310\AppData\Roaming\Typora\typora-user-images\image-20220801105139618.png)

### 📌 Stack을 써야하는 이유

- ### 뒤집기, 되돌리기, 되돌아가기 ⭐

- ### 마무리 되지 않은 일을 임시 저장 ⭐

- 괄호 매칭

- 함수 호출(재귀 호출)

- 백트래킹

- DFS(깊이 우선 탐색)

## 📝 큐(Queue)

Queue는 한 쪽 끝에서 데이터를 넣고, 다른 한 쪽에서만 데이터를 뺄 수 있는 자료구조 가장 먼저 들어온 데이터가 가장 먼저 나가므로 

- FIFO(First-in, First-out, 선입선출) 방식

`[dequeue]`👈 `가장 먼저 들어온 데이터` 👈 `data`  👈  `가장 최신의 데이터` `[enqueue]`

### 📌 덱 자료구조

- == 양 방향으로 삽입과 삭제가 자유로운 큐
- 덱은 양 방향 삽입, 추출이 모두 큐보다 훨씬 빠르다.
- `from collections import`  함수 호출
- `popleft( )`⭐
  - 가장 오래된 자료를 뺀다.