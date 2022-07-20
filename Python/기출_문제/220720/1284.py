# A = 1L당 요금 P = 9
# B = RL이하 요금 100 Q RL= 20 기준 1L당 요금 S = 3
# 종민이가 사용하는 물 W = 10

# 내가 풀은 것
# t = int(input())
# for test in range(1, t+1):
    
#     water = 250
#     if water > 100 :
#         j = (water - 100) * 10
#     else:
#         j = 0
#     a = water * 8
#     b = 300 + j
    

# print(min(a, b))

import sys
sys.stdin = open("1284.input.txt", "r")

# A : 사용량 * P원
# B :
#   R이하 : Q
#   R초과 : Q + S*(사용량-R)

T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    # print(P, Q, R, S, W)
    A = W * P
    if R > W:
        B = Q
    else:
        B = Q + S * (W - R)
    print(f'#{test_case} {min(A, B)}')
    