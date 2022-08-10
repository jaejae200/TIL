x = int(input())
y = int(input())

if x < 0:           # x가 음수일 때
    if y > 0:       # y = 양수
        print('2')
    if y < 0:       # y = 음수
        print('3')

if x > 0:            # x가 양수일 때
    if y > 0:           # y = 양수
        print('1')
    if y < 0:           # y = 음수 
        print('4')
    