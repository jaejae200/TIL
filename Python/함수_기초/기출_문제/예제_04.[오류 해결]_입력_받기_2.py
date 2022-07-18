words = list(map(str, input().split())) #int로 변환되었던 리스트를 문자열 str로 바꾸자.
print(words)

# ValueError: invalid literal for int() with base 10: "I'm"
# 값 에러 : int() 안에 10진수를 입력해주세요!