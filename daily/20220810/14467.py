import sys

sys.stdin = open('14467.txt', 'r')

N = int(input())

cow_list = {}  # cow의 번호와 (key) 위치 (value)입력받음
cnt = 0


for _ in range(N):
    
    cow, place = map(int, input().split()) # 소와 위치 정보 입력받음

    if cow in cow_list and cow_list[cow] != place: # if cow(번호)가 딕셔너리 안에 있고 place 위치(0 or 1) 이 같지 않다면
        cnt += 1                                   # cnt 증가 > 다리를 건넜음.
    cow_list[cow] = place   # 소의 정보(번호)와 위치 저장 >>> 딕셔너리에

# 출력
print(cnt)
