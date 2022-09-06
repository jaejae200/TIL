import sys

sys.stdin = open('2592.txt', 'r')

num = [int(input()) for _ in range(10)]

print(int(sum(num)/len(num)))
print(max(num, key = num.count))

