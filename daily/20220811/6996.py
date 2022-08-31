import sys

sys.stdin=open('6996.txt', 'r')

T = int(input())

for _ in range(T):
    a, b = input().split()
    a_list = sorted(a)
    b_list = sorted(b)

    if a_list == b_list:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')
