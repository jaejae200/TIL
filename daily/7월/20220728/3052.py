R_list = []                 # 나머지 리스트

for _ in range(10):         # 반복문 10번
    num = int(input())      # 정수 입력받음
    R_list.append(num % 42) # 입력받은 정수 % 42 = 나머지 리스트에 추가 

print(len(set(R_list)))     # 충복 제거 후 요소 출력    