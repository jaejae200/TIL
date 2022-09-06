# 너무 많이 돌아가서 풀이 참조했음 *

N, M = map(int, input().split())
# 5 21
card_list = list(map(int, input().split()))
# 5 6 7 8 9

max_ = 0                                         # M이하 제일 큰 수를 넣어줄 변수

for i in range(N-2):                             # range 범위 지정 3개  N=5 index = (0,1,2) 
    for j in  range(i+1,N-1):                    # i를 기준으로 다음 카드의 순번과 마지막 제외 index = (1,2,3)
        for k in range(j+1 , N):                 # j를 기준으로 다음 카드의 순번과 마지막 카드까지 index = (2,3,4)
            total = card_list[i] + card_list[j] + card_list[k]      # 카드 3개를 더한 수

            if total == M:                       # 카드 3개를 더한 수가 M과 같다면 max_에 할당하고 반복문 종료
                max_ = total
                break
            
            if max_ < total <= M:                # M 이하인 total이 max_보다 크다면 max_에 total을 할당
                max_ = total

            

    # 출력문
print(max_)