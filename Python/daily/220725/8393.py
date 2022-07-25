N = int(input())         # 입력받는 정수
sum = 0                  # 저장소 할당

for i in range(1, N+1):  # i에 1부터 N까지 숫자를 저장
    sum += i             # sum 함수에 수를 합산!
    
print(sum)               # sum 출력