import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = True
for _ in range(m):
    i = int(input())
    k = list(map(int, input().split()))
    for j in range(i-1):
        if k[j] < k[j+1]:
            p = False
            break
    if not p: break

print('Yes' if p else 'No')










import sys

sys.stdin = open('23253.txt', 'r')

N, M = map(int, input().split())

my_list = [_ for _ in range(1, N+1)]

num1 = int(input())
dummy1 = list(map(int, input().split()))

num2 = int(input())
dummy2 = list(map(int, input().split()))

result = [] 

for i in range(1, N+1):
    if dummy1 != []:
        if dummy1[-1] == i:
            result.append(dummy1.pop())

    if dummy2 != []:
        if dummy2[-1] == i:
            result.append(dummy2.pop())


if result == my_list:
    print('Yes')
else:
    print('No')



