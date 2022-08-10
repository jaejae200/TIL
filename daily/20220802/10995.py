N = int(input())

if N == 1:
    print('*')                      #N = 1이면 * 출력
    
else:
    for n in range(N):              #N만큼 출력
        if n % 2 == 0:              # 2로 나눈 나머지가 0일때
            a = print('* ' * N)     # 0 = * *
        else:
            b = print(' *' * N)     # 1 =  * *