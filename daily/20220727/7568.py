import sys

sys.stdin = open('7568.txt', 'r')

N = int(input())                         # 사람 수 input 

bulk_list = []                           # 사람들 몸무게 리스트를 만들어줌

for i in range(N):                       # 사람 수 만큼 index 진행
    x, y = map(int, input().split())     # x는 몸무게 y는 키 각각 입력받는다
    bulk_list.append((x,y))              # x와 y를 리스트 안의 리스트로 append

for j in bulk_list:                      # index j에 리스트 값 순회
    rank = 1                             # 순위를 1등으로 설정 
    for compare_j in bulk_list:          # index j와 비교할 compare_j 안에 리스트 값 넣어줌
        if j[0] < compare_j[0] and j[1] < compare_j[1]:  # 몸무게는 몸무게끼리 키는 키끼리 비교하면서 둘다 참인 경우
            rank += 1                                    # rank를 1 증가시켜준다
    
    print(rank, end=' ')                 # end = ' ' 이용 데이터 값마다 공백을 넣어줌 