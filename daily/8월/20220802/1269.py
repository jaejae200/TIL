# set
import sys

sys.stdin=open('1269.txt', 'r')


A, B = map(int, input().split())
a = set(map(int, input().split())) # set를 이용하면 차집합을 구할 수 있다 
b = set(map(int, input().split())) 

print(len(a-b)+len(b-a)) # 차집합 a-b = 1 b-a = 3 



# 시간 초과

# A, B = map(int, input().split())

# A_list = list(map(int, input().split()))
# B_list = list(map(int, input().split()))

# result = []

# for i in A_list:
#     if i in B_list:
#         None
#     elif i not in B_list:
#         result.append(i)
    
# for j in B_list:
#     if j in A_list:
#         None
#     elif j not in A_list:
#         result.append(j)

# print(len(result))



