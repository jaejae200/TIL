import sys

sys.stdin=open('10871.txt', 'r')


N, X = map(int, input().split())        

num = map(int, input().split())

my_list = []                        # True 저장해줄 리스트

for i in num: 
    if i < X:                       # i가 x보다 작다면 True 반환
        my_list.append(i)           # my_list에 i값 저장

print(*my_list)

