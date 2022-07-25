N = int(input())

for i in range(1, N+1):
    print(' '*(N-i) + '*' * i) # 끝 자리 수 N에서 i를 뺀 수를 공백으로 출력 후 i 수 만큼 * 출력