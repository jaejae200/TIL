import sys

sys.stdin=open('9455.txt', 'r')

M, N = 5, 4 #열, 행

box = [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 1, 0]
]

for i in range(N): 
    for j in range(M): 
        