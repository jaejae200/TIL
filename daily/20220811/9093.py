import sys

sys.stdin = open('9093.txt', 'r')

T = int(input())

for _ in range(T):
    word = list(map(str, input().split()))
    result = []
    for i in range(len(word)):  
        result.append(word[i][::-1])

    print(*result)
