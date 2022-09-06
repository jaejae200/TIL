import sys

sys.stdin=open('2776.txt', 'r')

N = int(input())

for _ in range(N):
    note_1 = int(input())
    numlist_1 = set(map(int, input().split()))
    note_2 = int(input())
    numlist_2 = list(map(int, input().split()))     # 결과값을 위해서 set 사용하지 않았음

    result = []                                     # 결과값 넣어줄 리스트

    for i in numlist_2:
        if i in numlist_1:                          # numlist_2의 원소가 numlist_1 안에 있다면
            result.append(1)                        # result에 1을 추가해준다
        else:
            result.append(0)                        # 아닌 경우 0을 추가

    for j in result:
        print(j, end='\n')