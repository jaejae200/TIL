import sys

sys.stdin=open('1209.txt', 'r')

T = 10

for _ in range(1, T+1):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    maximum = 0
    sum_ = 0
    sum_2 = 0
    sum_3 = 0
    sum_4 = 0
    
    for i in range(len(matrix)):
        if maximum < sum_:
            maximum = sum_
        if maximum < sum_2:
            maximum = sum_2
        sum_ = 0
        sum_2 = 0

        for j in range(len(matrix)):
            sum_ += matrix[i][j]
            sum_2 += matrix[j][i]

    for i in range(len(matrix)):
        sum_3 += matrix[i][i]
        sum_4 += matrix[i][99-i]

    if maximum < sum_3:
        maximum = sum_3
    if maximum < sum_4:
        maximum = sum_4

    print(f'#{_} {maximum}')


            
        






