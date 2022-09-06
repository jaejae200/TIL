import sys

sys.stdin=open('10816.txt', 'r')

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

my_dict = {}

for i in N_list:
    if i in my_dict:            # 모든 값을 dic에 추가하는 반복문
        my_dict[i] += 1
    else:       
        my_dict[i] = 1

# M_list 를 기준으로 my_dict 탐색

for j in range(M):
    if M_list[j] in my_dict:
        print(my_dict[M_list[j]], end = ' ')
    else:
        print(0, end=' ')


# for i in N_list:
#     if i in M_list:
#         if i not in my_dict:  
#             my_dict[i] = 1
#         else:
#             my_dict[i] += 1

# print(my_dict)