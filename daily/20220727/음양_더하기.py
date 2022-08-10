def solution(absolutes, signs):         # 입력받을 두 함수 정의
    answer = 0                          # 결과 기본값 0
    for i in range(len(absolutes)):     # 입력받는 absolutes의 개수 만큼 for문 진행
        if signs[i] == True:            # if signs이 True면
            answer += absolutes[i]      # 결과에 입력받은 정수를 더한다.
        else:                           # 포함되지 않는 값 [false]
            answer += absolutes[i] * -1 # 음수로 변환해서 더해준다.

    return answer                       # 결과를 반환
        
