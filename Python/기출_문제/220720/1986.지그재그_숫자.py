t = int(input())
for test in range(1, t+1):
    
    number = int(input())
    total = 1
    for i in range(2, number+1):

        if i % 2:
            total += i
            print(i)
        else:
            total -= i
    
    print(f'#{test} {total}')