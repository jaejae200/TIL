import sys

sys.stdin = open('1936.txt', 'r')

A, B = map(int, input().split())

if A == 1:
    if B == 2:
        print('B')
    if B == 3:
        print('A')

if A == 2:
    if B == 1:
        print('A')
    if B == 3:
        print('B')

if A == 3:
    if B == 1:
        print('B')
    if B == 2:
        print('A')
