# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지
word = input()

for char in word: 
    print(chr(ord(char)-32), end='')
# 1. 알파벳을 숫자로 바꾸고
# 2. 그 숫자를 -32 하고
# 3. 다시 숫자를 알파벳으로 바꾼다.

# word = input()

# for char in word:
#     number = ord(char)
#     number = number-32
#     result += chr(number)