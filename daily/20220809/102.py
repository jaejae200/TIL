from pprint import pprint

# 인접 행렬
n, m = map(int, input().split()
)
graph = [[0] * (n+1) for _ in range(n+1)] # n by n
graph_2 = [[] * (n+1) for _ in range(n+1)] # n by n

for edge in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    # graph[v2][v1] = 1
    
    graph_2[v1].append(v2)
    # graph_2[v2].append(v1)


pprint(graph)
print(graph_2)