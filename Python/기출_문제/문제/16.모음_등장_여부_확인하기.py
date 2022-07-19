# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

word = input()
vowels = 0
# 지금은 인덱스가 필요없어서
# 그냥 char를 받을게요!
for char in word:
    if char in ['a', 'e', 'i', 'o', 'u']: #'aeiou' 가능
        vowels = vowels + 1
    
print(vowels)
