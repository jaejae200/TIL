from ntpath import join
import sys

sys.stdin=open('2979.txt', 'r')

A, B, C = map(int, input().split())

time = [0] * 100                            # 입력으로 주어지는 시간 0부터 100 사이까지
result = 0                                  # 주차 비용 저장할 변수

for _ in range(3):                              # 3대니까 3번만
    arrival, leave = map(int, input().split())  # 들어온 시간, 나간 시간
    for i in range(arrival, leave):             # i는 시간의 범위 예제2) 입력값 
        '''
        i는 시간의 범위 
        예제2) 입력값 
        15 30
        25 50
        70 80

        time[15] ~ time[29] # 나가는 시간 제외
        time[25] ~ time[49]
        time[70] ~ time[79] 

        '''
        time[i] += 1 # 위에 해당한 인덱스에 +1 을 해준다

for j in time:      # time을 하나씩 돌면서
    if j == 1:          # index 값이 1이라면
        result += A     # 1인 수 만큼 result에 + A
    if j == 2:          # ...
        result += 2 * B
    if j == 3:
        result += 3 * C

# 출력문
print(result)

    

