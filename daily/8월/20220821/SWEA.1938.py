import sys
import math

sys.stdin = open('1938.txt', 'r')

a, b = map(int, input().split())

print(a+b, a-b, a*b, math.trunc(a/b), sep='\n')

