import sys

sys.stdin = open('1547.txt', 'r')

M = int(input())
stack = [1]
for _ in range(M):
    x, y = map(int, input().split())

    if x in stack:
        stack.pop()
        stack.append(y)
        continue
    
    if y in stack:
        stack.pop()
        stack.append(x)


print(*stack)
    
