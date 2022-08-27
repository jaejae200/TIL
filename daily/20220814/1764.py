import sys

sys.stdin = open('1764.txt', 'r')

N, M = map(int, input().split())

result = []



N_list = [input().strip() for _ in range(N)]
M_list = [input().strip() for _ in range(M)]

# 교차하는 이름들을 찾는다
duplicate = list(set(N_list) & set(M_list))

print(len(duplicate))
for name in sorted(duplicate):
    print(name)





# for _ in range(N):
#     hear = input()
#     result.append(hear)

# for _ in range(M):
#     see = input()
#     result.append(see)

# result.sort()

# dic = {}

# for i in result:

#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1

# print(result.count(max(result)))

# for k, v in dic.items():
#     if v == 2:
#         print(k)
        




