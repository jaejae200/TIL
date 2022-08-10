N = int(input())

pc = [0 for _ in range(101)]
client = map(int, input().split())

cnt = 0                             # 거절 받는 손님 수

for i in client:                    # 고객을 i로 순회
    if pc[i] == 0:                  # pc 인덱스 위치가 0이라면
        pc[i] = i                   # 고객을 앉힌다.
    else:                           # 아닐경우 거절손님 + 1
        cnt += 1

# 출력문
print(cnt)
