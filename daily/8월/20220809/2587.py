
num = [int(input()) for _ in range(5)]      # 5개 정수를 받고
num.sort()                                  # 정렬 후 

average = int(sum(num) / len(num))          # 평균 값 계산 식

print(average, num[2])                      # 문제에선 5개의 정수'만' 받는다고 했으니 평균과 가운데 인덱스 출력





