# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input())    # 정수 입력받음
B = int(input())    # 정수 입력받음
C = int(input())    # 정수 입력받음
result = list(str(A * B * C))   # 입력받은 A*B*C 정수를 곱한 후 문자열로 변환하고 다시 list 변환 = 글자가 쪼개짐

for i in range(10):             # range 0 ~ 9 까지 임시변수 i에 저장
    print(result.count(str(i)))


