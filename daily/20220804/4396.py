import sys

sys.stdin=open('4396.txt', 'r')

# N 줄 M 폭탄 x 열린 칸 . 다른 모든 칸 

N = int(input())

board = [list(map(int, input())) for _ in range(N)]

