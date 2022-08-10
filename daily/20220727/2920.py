C_major = ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'C']
result = []
play = map(int, input().split())

for i in play:
    result.append(C_major[i-1])


if result == C_major:
    print('ascending')
elif result[::-1] == C_major:
    print('descending')
elif result != C_major:
    print('mixed')


