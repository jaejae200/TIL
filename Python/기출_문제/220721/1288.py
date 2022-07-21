import sys
sys.stdin = open("1288.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    
    n = int(input())
    cnt = 1
    result = set()
    
    while True:
        if len(result) == 10:
            break
        else:
            num = n * cnt
            result.update(str(num))
            cnt += 1
    
    print(f'#{test_case} {num}')