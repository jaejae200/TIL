

x, y = map(int, input().split())
x = x - 1   # 
y = y - 1 

w = abs(x // 4 - y // 4)    # 절대값
h = abs(x % 4 - y % 4)

print(w + h)    

