import sys
from pprint import pprint 

sys.stdin = open('2606.txt', 'r')

n = int(input())        # 컴퓨터 수
m = int(input())        # 연결 수

graph = [[] for i in range(n + 1)]              # 빈 리스트 만들어주기

for _ in range(m):                              # 리스트에 인접 요소를 넣어주는 반복문
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)                       # DFS 리스트를 만들어준다

def dfs(start):                                 # dfs (start) start 값 = 1번 컴퓨터
    stack = [start]                             # stack에 1번 컴퓨터를 넣고
    visited[start] = True                       # True로 바꿔줌 visited[1] = True

    while stack:                                # stack이 없을 때까지 반복
        cur = stack.pop()                       # stack에 있던 1을 꺼내고 cur에 저장

        for adj in graph[cur]:                  # graph[1] 값을 adj 순회 graph[1] = [2,5]
            if not visited[adj]:                # if vitised[2]가 False 라면
                visited[adj] = True             # visitied[1] = True 로 다녀왔음을 표시
                stack.append(adj)               # stack에 값을 넣어놓는다. (선입후출)
dfs(1)

result = sum(visited) - 1                       # 방문한 노드를 len으로 처리하는 방법 or True로 방문 처리된 index를 sum하는 방법

# 출력문
print(result)



