for _ in range(int(input())):
    n, string = input().split()
    n = int(n)
    print(string[:n-1], string[n:], sep='') # 슬라이스로 그 위치만 공백으로 변환




    