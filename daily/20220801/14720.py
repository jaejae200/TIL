N = int(input())
road = list(map(int, input().split()))              # 가게들 리스트
cnt = 0                                             # 딸기 초코 바나나 순서 만들어줄 변수
result = 0                                          # 먹을 수 있는 우유의 수
for i in road:                                      
    if i == cnt:                                    # 만나는 가게가 cnt 와 같다면 0 = 딸기
        cnt += 1                                    # cnt + 1 = 초코로 바꿔줌
        result += 1                                 # 먹을 수 있는 우유도 증가

    if cnt > 2:                                     # cnt가 2를 넘어가면 0으로 초기화
        cnt = 0

print(result)
    
    