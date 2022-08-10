import sys          

sys.stdin=open('20220801/9012.txt', 'r')

T = int(input())                

for _ in range(1, T+1):
    vps = input()
    cnt = 0                 # 짝을 맞춰줄 cnt 변수
    for i in vps:           # 한 글자씩 순회
        if i == '(':        # '(' 면 cnt += 1 
            cnt += 1 
        if i == ')':        # ')' 면 cnt -+ 1 
            cnt -= 1    
        if cnt == -1 :      # cnt 가 -1 이면 VPS에 해당되지 않는 ')' 괄호가 하나 더 생기는 것이기 때문에 (())) = -1
            print('NO')     # 'No'를 출력하고 break
            break           
    
    if cnt >= 1:            # cnt가 1 이상이면 VPS에 해당하지 않기 때문에 'NO'
        print('NO')
    
    if cnt == 0:            # 위 조건에 해당하지 않고 cnt가 0이라면 VPS
        print('YES')        # YES를 출력

