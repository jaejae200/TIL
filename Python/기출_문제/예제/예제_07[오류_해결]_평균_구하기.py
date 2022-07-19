number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1 # for문 안으로 들어가야 count 증가!

print(total / count) # //는 몫을 구하는 연산자이기 때문에 평균값을 정확하게 나눌 수 없음! # / 나누기로 변경하여 값 출력