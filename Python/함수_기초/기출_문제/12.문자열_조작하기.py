# word = input()
# print(word.replace('a',''))
# - - - - - - - - - - - -

word = 'apple'
result = ''
# 반복! for
for char in 'apple':
    # 만약 a가 아닐 때
    if char != 'a':
        result = result + char
        # 반복문에서 아무것도 안하고 넘어가는 것
        # continue
print(result)