import sys

sys.stdin=open('1206.txt', 'r')

T = 10

for _ in range(1, T+1):
    rol = int(input())
    rol_list = list(map(int, input().split()))
    cnt = 0
    for i in range(2, rol-2):
        def_2 = rol_list[i] - rol_list[i-2]
        def_1 = rol_list[i] - rol_list[i-1]
        def1 = rol_list[i] - rol_list[i+1]
        def2 = rol_list[i] - rol_list[i+2]
        if def_2 > 0 and def_1 > 0 and def1 > 0 and def2 > 0 :
            cnt += min(def_2, def_1, def1, def2)
    print(f'#{_} {cnt}')
        

