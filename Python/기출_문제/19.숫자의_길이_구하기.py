def number(n):
    cnt = 0
    while n:
        n //= 10
        cnt += 1

    return cnt

print(number(int(input())), type(number))

