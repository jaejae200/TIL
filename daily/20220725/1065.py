n = int(input())
han = 0 # 한수
for i in range(1, n + 1):   # 
    if i < 100:             # i가 100 이하라면
        han += 1            # 한수를 그대로 더해준다
    else:
        ns = list(map(int, str(i)))     
        if ns[0] - ns[1] == ns[1] - ns[2]:   # 입력 받은 i의 자리 수를 보고 0-1과 1-2 즉 수열을 이룬다면
            han += 1                        # 그 수가 한수이고 +1
print(han)