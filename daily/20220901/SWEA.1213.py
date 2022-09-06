import sys

sys.stdin=open('1213.txt', 'rt', encoding='UTF8')

T = 10

for _ in range(1, T+1):
    tc = int(input())
    find = input()
    word = input()
    print(f'#{_} {word.count(find)}')
