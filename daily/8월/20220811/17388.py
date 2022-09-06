result = list(map(int, input().split()))

if sum(result) < 100:
    if min(result) == result[0]:
        print('Soongsil')
    if min(result) == result[1]:
        print('Korea')
    if min(result) == result[2]:
        print('Hanyang')
else:
    print('OK')

