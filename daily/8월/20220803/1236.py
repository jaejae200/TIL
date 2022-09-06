import sys

sys.stdin=open('1236.txt', 'r')
# N = 열 M = 행
N, M = map(int, input().split())                       

matrix = [list(input()) for _ in range(N)]        # 세로 x 가로

guard_n = 0                                       # 열에 필요한 경호원 숫자
guard_m = 0                                       # 행에 필요한 경호원 숫자

for i in range(N):                                # 열을 기준으로 행을 다 뒤져본다.
    if 'X' not in matrix[i]:                      # [matrix[i] = 한 행]에 x가 없으면
        guard_m += 1                              # guard_m + 1 

for j in range(M):                                # 행을 기준으로 열을 뒤져본다.
    if 'X' not in [matrix[col][j] for col in range(N)]: #  가로 x 세로 #  열의 데이터로 행만큼 리스트를 만들어 준다
        guard_n += 1                                  

print(max(guard_n, guard_m))









# import sys

# sys.stdin=open('1236.txt', 'r')


# N, M = map(int, input().split())

# matrix = [list(input()) for _ in range(N)]

# guard = 0

# for i in range(max(N, M)):
    
#     if i == (N-1) :
#         if 'X' not in matrix[i][0:M]:
#             guard += 1
#             break
#         else:
#             break
    
#     if i < (N-1) :
#         if 'X' not in matrix[i][0:M]:
#             guard += 1


# print(guard)



# if 'X' not in matrix[0][0::N]:
    #guard += 1


    # for i in range(N):
#     for j in range(M):
#         if 'X' in matrix[i][j::M]:

#         if 'X' not in matrix[i][j::M]:
#             guard += 1

    
