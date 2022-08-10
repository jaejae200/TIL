import sys
sys.stdin=open('2669.txt', 'r')

plane = [[0]* 100 for _ in range(101)]              # 빈 도화지 생성 100 * 100

for _ in range(4):
    x, y, x_end, y_end = map(int, input().split())  # 4번 좌표를 받아서 도화지에 표시해준다.
    for i in range(x+1, x_end+1):                   # x y 안의 색칠된 공간을 구해줘야 함, 따라서 코드에서는 받은 좌표의 +1의 값부터 색칠
        for j in range(y+1, y_end+1):
            plane[i][j] = 1                         # 색칠할 공간 1로 바꿔주기

print(sum(map(sum, plane)))                         # 파이써닉한 방법으로 1로 색칠한 값들 더해줌

