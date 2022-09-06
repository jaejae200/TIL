import sys

sys.stdin = open('2897.txt', 'r')

R, C = map(int, input().split())

parking = [list(input()) for _ in range(R)]     # 주차장

zero = 0        # 차를 부수는 경우를 세주는 변수
one = 0 
two = 0
three = 0
four = 0 

for i in range(R-1):
    for j in range(C-1):
        
        base = parking[i][j]        # [0,0] # 2행 2열
        x = parking[i][j+1]         # [0,1]
        y = parking[i+1][j]         # [1,0]
        z = parking[i+1][j+1]       # [1,1]

        result = base + x + y + z   # 내가 필요한 공간의 요소를 전부 더해준다.

        if '#' in result:           # result 안에 빌딩 '#' 존재시 
            continue                # 아래 if문 순회하지 않음

        if result.count('.') == 4:      # 공간이 4개라면 차를 부수지 않아도 괜찮기 때문에 zero + 1
            zero += 1
        elif result.count('.') == 3:    # 공간이 3개라면 차를 1개 부숴야 하기 때문에 one + 1 
            one += 1
        elif result.count('.') == 2:    # 공간이 2개..
            two += 1
        elif result.count('.') == 1:
            three += 1
        elif result.count('.') == 0:
            four += 1  


print(zero, one, two, three, four, sep='\n')   # 모든 변수를 개행으로 출력




        