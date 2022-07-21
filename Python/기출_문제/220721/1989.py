T = int(input())
for test_case in range(1, T + 1):
    word = input()
    reverse_word = word[::-1]
    # print(reverse_word)
    if word == reverse_word:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
