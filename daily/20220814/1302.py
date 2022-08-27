import sys

sys.stdin = open('1302.txt', 'r')

N = int(input())

dict_ = {}

for _ in range(N):
    book = input()

    if book not in dict_:
        dict_[book] = 1
    else:
        dict_[book] += 1

my_list = []

num = max(dict_.values())

for i in dict_:
    if num == dict_[i]:
        my_list.append(i)

my_list.sort()
print(my_list[0])


    
    