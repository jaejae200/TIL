import sys

sys.stdin = open('11652.txt', 'r')

N = int(sys)
# 시간초과의 늪..

result = []

for _ in range(N):
    num = int(input())
    result.append(num)

result_a = set()

max = 0

for i in result:
    if result.count(i) > max:
        max = result.count(i)
    
for j in result:
    if max == result.count(j):
        result_a.add(j)

print(min(result_a))
    





