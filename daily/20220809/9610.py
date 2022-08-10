n = int(input())

cnt_Q1 = 0  # 값 저장할 변수들
cnt_Q2 = 0 
cnt_Q3 = 0 
cnt_Q4 = 0
AXIS = 0

for i in range(n):
    x, y = map(int, input().split())
       
    if x > 0 and y > 0:             # Q1~Q4 까지 조건들
        cnt_Q1 += 1
    elif x < 0 and y > 0:
        cnt_Q2 += 1
    elif x < 0 and y < 0:
        cnt_Q3 += 1
    elif x > 0 and y < 0:
        cnt_Q4 += 1
    else:
        AXIS += 1


# 출력문 

print(f'Q1: {cnt_Q1}')
print(f'Q2: {cnt_Q2}')
print(f'Q3: {cnt_Q3}')
print(f'Q4: {cnt_Q4}')
print(f'AXIS: {AXIS}')

    
