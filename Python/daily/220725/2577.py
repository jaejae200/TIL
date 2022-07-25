A = int(input())    # 정수 입력받음
B = int(input())    # 정수 입력받음
C = int(input())    # 정수 입력받음
result = list(str(A * B * C))   # 입력받은 A*B*C 정수를 곱한 후 문자열로 변환하고 다시 list 변환 = 글자가 쪼개짐

for i in range(10):             # range 0 ~ 9 까지 임시변수 i에 저장
    print(result.count(str(i))) 
    # 0 ~ 9 까지 몇 개가 존재하는지 count한 후 출력, (즉 result 안의 숫자 개수를 세어본다)
    # result 결과가 문자열이기 때문에 임시변수 i도 str 변환하여 타입을 맞춰줘야 함!