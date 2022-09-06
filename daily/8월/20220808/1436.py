N = int(input())

title = 0
i = 666

while True :
    if '666' in str(i) : # 증가하는 i 값에 666이 존재할 경우에
        title += 1       # 다음 원하는 회차를 구해줌
    if title == N :      # 내가 원하는 회차에 접근하면
        print(i)         # 지금까지 쌓았던 i값을 출력하고
        break            # 반복문 탈출
    i += 1           
    # 조건이 해당되지 않으면 계속 i를 1 더한다