import sys

sys.stdin=open('2167.txt', 'r')

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

# 계산받을 배열 받아옴

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    sum_ = 0
    
    for col in range(i-1, x):
        for row in range(j-1, y): 
            sum_ += matrix[col][row]  

    print(sum_)

    # matrix[i][j] ~ matrix[x][y] 값을 구하면 되는 문제


# 
# i, j, x, y
# 1  1  2  3
# 1  2  1  2
# 1  3  2  3 