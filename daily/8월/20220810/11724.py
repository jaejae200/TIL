'''
dfs 다듬는 법
'''

import sys

sys.stdin = open('11724.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]        # 그래프 만들어 줄 빈 리스트 만들기

for _ in range(m):                      # 인접 리스트 만들기
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)               # 방문 리스트 만들기
cnt = 0                                 # 연결 요소 저장해주는 변수

for i in range(1, n+1):                 # 1~n 까지
    
    if visited[i] == False:             # visited[i]의 값이 False일 때만 아래 DFS 실행
        def dfs(start):                                
            stack = [start]                            
            visited[start] = True                     

            while stack:                               
                cur = stack.pop()                       

                for adj in graph[cur]:               
                    if not visited[adj]:               
                        visited[adj] = True            
                        stack.append(adj)
        dfs(i)                         # dfs는 1~n까지 증가
        cnt += 1                       # 조건문 안에 들어오면 요소를 구하는 변수 증가

print(cnt)      
                               
                            