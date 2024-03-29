# 힙, 셋 (Heap, Set) ✒

- #### 🔎 우선순위 큐(Priority Queue) 

  - 가중치가 있는 데이터
  - 작업 스케줄링
  - 네트워크 

- #### ⭐ 우선순위를 기준으로 가장 높은 데이터가 먼저 나가는 방식 ⭐

- 우선순위 큐를 구현하는 방법

  - 배열 (Array)
  - 연결 리스트 (Linked List)
  - 힙 (Heap)  ⭐

  | 연산 종류           | Enqueue (추가) | Dequeue (제거) |
  | ------------------- | -------------- | -------------- |
  | 배열                | O(1)           | O(N)           |
  | (정렬된 배열)       | O(N)           | O(1)           |
  | 연결 리스트         | O(1)           | O(N)           |
  | (정렬된 연결리스트) | O(N)           | O(1)           |
  | 힙                  | O(logN)        | O(logN)        |

  

## 📝 힙(Heap)

### 📌 힙의 특징

- **최대값 또는 최소값을 빠르게 찾아**내도록 만들어진 데이터구조

- #### 이진 트리의 형태로 느슨한 정렬 상태를 지속적으로 유지 ⭐

- 중복값을 허용

### 📌 Heap 언제 사용해야할까 ? 

- 데이터가 **지속적으로 정렬되야 하는 경우**
- 데이터에 **삽입/삭제가 빈번할 때**

### 📌 파이썬의 heapq 모듈 

- 최소 힙으로 구현되어 있음
- **삽입 삭제 수정 조회 연산 속도가 리스트보다 빠르다 **⭐

## 📝 셋(Set)

- #### Set은 수학에서의 '집합'을 나타내는 데이터 구조이다.

- 탐색, 제거가 빠르다.

### 📌 Set 언제 사용해야할까?

- **데이터의 중복이 없어야 할 때** (고유값들로 이루어진 데이터가 필요할 때)

- #### 정수가 아닌 데이터의 삽입, 삭제, 탐색이 빈번할 때

 