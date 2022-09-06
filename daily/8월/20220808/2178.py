from re import M
import sys

sys.stdin = open('2178.txt', 'r')

# 우 하 우상 우하
dy = [0, 1, -1, 1]
dx = [1, 0, 1, 1]

BLACK = 1
WHITE = 2
N = 19

board = []


# 오목판 상황
for _ in range(N):
    # 하나의 행을 입력
    temp_list = list(map(int, input().split()))
    board.append(temp_list)
    answer = 0 

# 이중 반복문

for y in range(N):
    for x in range(N):
        # 검은색 돌이나 흰색 돌일 때만 델타 탐색을 수행
        if board[y][x] == BLACK or WHITE:

            # 델타 탐색
            for d in range(4):
                # 방향이 바뀔 때마다 돌의 개수가 갱신
                stone_count = 1
                
                # 다음 좌표 탐색 
                ny = y + dy[d]
                nx = x + dx[d]

                while True:
                # 인덱스 조건
                    if not(-1 < ny < N and -1 < nx < N):
                        break
                            
                    # 같은 값인지 확인하는 조건
                    if not(board[y][x] == board[ny][nx]):
                        break

                    stone_count += 1

                # 같은 방향 다음 좌표를 탐색

                    ny = ny + dy[d]
                    nx = nx + dx[d]
                
            # 돌의 개수가 5개라면 
            if stone_count == 5:
                # 이전 좌표
                prev_y = y - dy[d]
                prev_x = x - dx[d]

                # 육목인지 판단
                # 조건 1. 이전 좌표가 범위를 벗어나면 오목
                if not(-1 < prev_y < N and -1 < prev_x < N) or board[y][x] != board[prev_x][prev_y]:
                    # answer 값 갱신
                    answer = board[y][x] 
                    # 현재 돌의 색을 출력
                    print(board[y][x])
                    # 현재 돌의 좌표를 출력
                    print(y + 1, x + 1)


# 전체를 반복했는데 무승부.
if answer == 0 :
    print(answer)