while True:                             # 값이 참일 때까지 반복
    A, B = map(int, input().split())    # int로 정수 입력받음
    if A == 0 and B == 0:               # A와 B가 0일때
        break                           # 반복문 종료
    else:                               # 아닌 경우 
        print(A + B)                    # A+B 값을 출력