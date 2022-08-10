A, B = map(int, input().split()) # 두 정수 입력받
result = []                      # 결과값 저장할 리스트

for i in range(1, B+1):           # 1부터 B까지 반복
    for j in range(i):            # cnt 수 만큼 j에 입력
        result.append(i)          # cnt 값 result에 추가

print(sum(result[A-1:B])) 