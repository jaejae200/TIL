N = int(input())                        # 입력받을 정수

for i in range(1, N + 1):               # 1부터 N까지 (문제 예 : 1부터 216 까지)
    num_list = list(map(int, str(i)))   # 분배합 리스트를 만들어준다 (정답 기준 [1, 9, 8])
    sum_ = i + sum(num_list)            # 순회하는 i (1 ~ 216)와 분배합 리스트를 더한 값(i를 쪼개서 더해줌)을 sum_에 저장한다
    if(sum_ == N):                      # 만약 (if) sum_ 값이 input 값과 같다면
        print(i)                        # result에 i의 값을 저장한다
        break                           # 끝 자리까지 순회를 돌 필요가 없기 때문에 break 이용해서 끊어준다!
    elif i >= N:
        print('0')                        # 결과를 출력