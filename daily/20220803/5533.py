import sys

sys.stdin=open('5533.txt', 'r')

N = int(input())
score = [[], [], []]                         # 빈 리스트 3개 만들어줌 
sum_ = []                                     # 결과 더해줄 리스트       
    
for _ in range(N):
    a, b, c = (map(int, input().split()))
    score[0].append(a)                       # 게임.1 의 결과
    score[1].append(b)                       # 게임.2 의 결과
    score[2].append(c)                       # 게임.3 의 결과

for i in range(N):
    get = 0                                  # 게임에서 점수를 가져갈 때 값을 넣어줄 변수
    for j in range(3):                       
        if score[j].count(score[j][i]) == 1:        # j = 0 일때 게임.1의 결과를 가져오고 score[0]에 저장된 데이터가 score에 하나만 있을 때
            get += score[j][i]                      # get에 부른 값을 더해준다
    sum_.append(get)                                 # sum에 총 점수를 append

for i in sum_:                              # 출력 
    print(i)




