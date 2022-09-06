import sys

sys.stdin = open('11945.txt', 'r')

N, M = map(int, input().split())

snack = [input() for _ in range(N)]
result = []
for i in range(N):
    result.append(snack[i][::-1])

print(*result)
