# 문자열 word가 주어질 때, Dictionary를 활용해서 
# 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

word = input () # 문자열 word

result = {}
for char in word:
    # 딕셔너리에 키가 없으면?
    if not char in result.keys():
        # 키랑 값을 1으로 초기화한다.
        result[char] = 1
    # 딕셔너리에 키가 있으면?
    else:
        result[char] = result[char] + 1

print(result)


result = {}
for char in word:
    # result['a'] 없으면 KeyError
    # result.get('a') 기본값이 None
    # result.get('a', 0) 기본값이 0
    result[char] = result.get(char, 0) + 1
print(result)

# 출력부분
for key in result:
    print(key, result[key])

