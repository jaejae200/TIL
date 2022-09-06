import sys

sys.stdin=open('25304.txt', 'r')

X = int(input())
N = int(input())
sum_ = 0 
for i in range(N):
    a, b = map(int, input().split())
    price = a * b
    sum_ += price

if sum_ == X:
    print('Yes')
else:
    print('No') 
