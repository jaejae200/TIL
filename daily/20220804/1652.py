import sys

sys.stdin=open('1652.txt', 'r')

N = int(input())

space = [list(input()) for _ in range(N)]

result_row = 0
result_col = 0

for i in range(N):
    cnt_row = 0                 # 연속된 2자리를 구해줄 cnt 변수
    cnt_col = 0 
    for j in range(N):
        # 가로
        if space[i][j] == '.':  # if 0.0 0.1 ... 행을 다 찾아보면서 '.' 있으면 
            cnt_row += 1        # cnt + 1
        else:                   # X가 있는 경우
            cnt_row = 0         # cnt를 초기화
        
        if cnt_row == 2:        # cnt가 2와 같아지는 조건에 충족하면
            result_row += 1     # 결과값에 + 1
# =================================
        # 세로
        if space[j][i] == '.':  # if 0.0 1.0 ... 열을 다 찾아보면서 '.' 있으면 
            cnt_col += 1        # cnt + 1 
        else:                   # X가 있는 경우
            cnt_col = 0         # cnt 초기화

        if cnt_col == 2:        # cnt가 2와 같아지면
            result_col += 1     # 결과값 + 1
 
print(result_row, result_col)
