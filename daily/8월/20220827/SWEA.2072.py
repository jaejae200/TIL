import sys

sys.stdin=open('2072.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    num_list = list(map(int, input().split()))
    result = []
    for i in num_list:
        if i % 2 == 1:
            result.append(i)
    print(f'#{tc} {sum(result)}')


