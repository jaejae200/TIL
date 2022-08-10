result = 0                                             # 결과값 0 할당                              

for i in range(1, 11):                                 # 1번부터 10번까지 (버섯)
    score = int(input())                               # (버섯) 점수 입력받음
    before_result = result                             # 전에 실행한 결과값 저장
    
    result += score                                    # result에 점수 누적
    
    if result >= 100:                                  # result = 100보다 크거나 같으면
        if (result - 100) > (100 - before_result):     # result - 100 값보다  100 - 이전 결과가 크다면 (>) 미만으로 같은 수라도 더 큰 수인 result 기준
            result = before_result                     # result에 이전 결과를 넣는다
        break                                          # 반복문 종료

print(result)                                          # result 출력
    