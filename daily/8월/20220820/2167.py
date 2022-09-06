import sys

N, M = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 계산받을 배열 받아옴

K = int(sys.stdin.readline())

for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    sum_ = 0
    
    for col in range(i-1, x):
        for row in range(j-1, y): 
            sum_ += matrix[col][row]  

    print(sum_)