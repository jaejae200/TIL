T = int(input())

for _ in range(1, T+1):
    count = 0 
    N, M = map(int, input().split())
    for i in range(N, M+1):  
        word = str(i)               # i를 문자열로 하나하나 쪼개보고
        count += word.count('0')    # 0이 있다면 count 증가
    print(count)
    


