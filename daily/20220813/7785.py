import sys

sys.stdin=open('7785.txt', 'r')

# N 출입 기록 수 'enter' 출근 'leave' 퇴근
# 회사에 남아있는 사람만 

N = int(input())

dic = {}

for _ in range(N):
    name, work = input().split()
    
    if work == 'enter':
        dic[name] = 'enter'

    else:
        if dic[name]:
            del dic[name]

for dict in sorted(dic, reverse=True):
    print(dict)