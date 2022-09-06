import sys

sys.stdin=open('2750.txt', 'r')

N = int(input())

num = []                         # 정렬해줄 리스트
 
for _ in range(N):               # N 번만큼 숫자 입력받아서 num list에 넣어줌
    num.append(int(input()))

num.sort()                       # 리스트 sort 정렬

print(*num, sep='\n')            # num 언패킹 후 sep 이용 문자 끝마다 개행

