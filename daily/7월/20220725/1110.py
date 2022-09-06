# 0~99 input < 10 

N = int(input())
num = N
cnt = 0 

while True:
    a = num // 10   # num을 10으로 나눈 몫 26) 2
    b = num % 10    # num을 10으로 나눈 나머지 26) 6
    c = (a+b) % 10  # 2+6 = 8 값을 10으로 나눈 나머지 = 오른쪽 끝 자리 수를 구하는 공식
    num = (b * 10) + c # 결과는 나머지를 십의 자리 수로 만들고 오른쪽 끝자리를 더해준다.

    cnt += 1         # 사이클 추가
    if num == N:     # 원점으로 돌아왔다면
        print(cnt)  # 출력하고 break
        break