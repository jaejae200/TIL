# 🔎 DFS 

**깊이 우선 탐색**

**시작 정점으로부터 갈 수 있는 하위 정점까지 가장 깊게 탐색**하고,

더이상 갈 곳이 없다면 마지막 갈림길로 돌아와서 다른 정점을 탐색하며 결국 모든 정점을 방문하는 순회 방법.



## 📝 그래프 탐색 알고리즘 (참고)

- 시작 정점에서 간선을 타고 이동할 수 있는 모든 정점을 찾는 알고리즘

- 깊이우선탐색 (DFS)
  - 그래프의 깊이를 우선으로 탐색하기 위해 활용
  - 스택 + 그래프
- 너비우선탐색 (BFS)
  - 그래프의 너비를 우선으로 탐색하기 위해 활용
  - 그래프 + 큐

## 📝 DFS ? 

- 미로 탈출을 생각하면 이해하기 쉽다.
  - 어느 한 쪽 길로 가장 깊에 들어갔다가 막히면 다시 돌아와서 다른 길을 탐색한다.

### 📌 DFS의 특징

- 모든 정점을 방문할 때 유리하다.
  - 경우의 수, 순열과 조합 문제에서 사용
- BFS에 비해 코드 구현이 간단하다.
  - 단, 모든 정점을 방문할 필요가 없거나 최단 거리를 구하는 경우는 BFS가 유리하다

## 📝 DFS의 동작 과정

- 탐색할 그래프가 먼저 필요하다.

  - 그래프는 **인접 행렬** 혹은 **인접 리스트** 방식으로 표현할 수 있다.

- 각 정점을 방문했는지 여부를 판별한 방문 체크 리스트가 필요하다.

  - visited 리스트를 따로 선언하여 각 정점을 방문했는지 체크한다.

  ```python
  visited = [false] * n # n은 정점의 개수
  ```

  |   정점 i   |    0    |    1    |    2    |    3    |    4    |    5    |    6    |
  | :--------: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
  | visited[i] | `false` | `false` | `false` | `false` | `false` | `false` | `false` |

​		인덱스는 각 정점의 번호

​		방문한 정점은 `True`, 방문하지 않은 정점은 `False`

- DFS의 사이클

  - 현재 정점 방문처리 
  - 인접한 모든 정점 확인
  - 방문하지 않은 인접 정점 이동

  ```python
  ⭐ 핵심 ⭐
  
  graph = [
      [1,2],
      [0,3,4],
      [0,4,5],
      [1],
      [1,2,6]
      [2],
      [4]
  ]
  
  visited = [False] * n					 # 방문 처리 리스트 만들기
  
  --------------------------
  # 현재 노드가 0일때
  #visited[0] = True						# 시작 정점 방문 처리
  #stack = [0]								# 돌아갈 곳을 기록
  
  # 함수로 만들기
  def dfs(start):							
      stack = [start]						 # 돌아갈 곳을 기록
      visited[start] = True 				 # 시작 정점 방문 처리
  --------------------------
  
      while len(stack) != 0:				# 스택이 빌 때까지 반복 (비어있지 않으면 계속 반복)
          cur = stack.pop()				# 현재 방문 정점(후입선출)
          
          for adj in graph[cur]:			# 인접한 모든 정점에 대해
              if not visited[adj]:		# 아직 방문하지 않은 정점이라면
                  visited[adj] = True		# True 방문 처리 후 스택에 append
                  stack.append(adj)
              
  ```

  ```python
  # 바이러스 문제
  
  n = int(input())	# 정점 개수 (컴퓨터)
  m = int(input())	# 간선 개수  
  
  graph [[] for _ in range(n + 1)]
  visited = [false] * (n + 1)
  total = 0
  
  #인접 리스트 만들기
  for _ in range(m):
      v1, v2 = map(int, input().split())
  	graph[v1].append(v2)
      graph[v2].append(v1)
      
  '''
  graph = [
  0	[],
  1	[2,5],
  2	[1,3,5],
  3	[2],
  4	[7],
  5	[1,2,6],
  6	[5],
  7	[4]
  ]
  '''
  
  # 1번 컴퓨터를 시작 정점으로 DFS 진행
  
  # visited = [False] * n
  
  def dfs(start):
      stack = [start]			# 1이라는 숫자가 들어감
      visited[start] = True	# 1을 True
      
      while stack:
          cur = stack.pop()	#  cur에 stack 첫번째 1이 먼저 나옴
          
          for adj in graph[cur]:		
              if not visited[adj]:
                  visited[adj] = True
                  stack.append(adj)
  dfs(1) # 1번 정점에서 시작
  
  # 정점을 리스트에 넣어서 len 출력도 가능
  
  result = sum(visited) - 1 # True = 1 False = 0 sum 진행 시 더해짐
  print(result)
  
  ```

  

  