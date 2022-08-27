import sys
sys.stdin=open('10546.txt', 'r')

N = int(sys.stdin.readline())

dic = {}

for _ in range(2*N-1):
    name = sys.stdin.readline().rstrip()

    if dic.get(name) is None:
        dic[name] = 1
    else:
        del(dic[name])

print(*dic)

    


