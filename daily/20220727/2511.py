import sys

sys.stdin=open('2511.txt', 'r')

A = list(map(int, input().split())) # A의 카드 list
B = list(map(int, input().split())) # B.. 

result_A = 0                        # A의 점수
result_B = 0                        # B..

for i in range(len(A)):             # range에 10을 적어도 무방
    if A[i] > B[i]:                 # A가 B보다 크면
        result_A += 3               # A의 점수를 3점 +
    elif A[i] < B[i]:               # B가 A보다 크면
        result_B += 3               # B ...
    elif A[i] == B[i]:              # 둘이 같다면
        result_A += 1               # 둘 다 점수를 +1
        result_B += 1

print(result_A, result_B)           # 둘의 총 점수 출력

if result_A > result_B:             # 점수 결과를 비교해서 큰쪽을 출력 
    print('A')
if result_B > result_A:
    print('B')

if result_A == result_B:             # 동점인 경우
    for j in range(len(A)-1,-1,-1):  # 반대로 시작해서 큰 수를 가진 사람이 이기는 조건
        if A[j] > B[j]:              # 9번째 인덱스부터 나오는 값이 A가 더 크다면
            print('A')               # A의 승리로 마무리(break)
            break
        elif A[j] < B[j]:            # B의 승리 (break)
            print('B')
            break
        elif j == 1:                 # 마지막 인덱스까지 승부가 나지 않은 경우 
            if A[0] == B[0]:         # 최종 카드가 같다면 
                print('D')           # Drow 출력
                