# 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
# count() 메서드 사용 금지


word = input() # # 문자열 word가 주어질 때
cnt = 0 # 개수를 구하세요.

# char는 이름 붙이기
# word의 요소를 하나씩 char 바인딩
for char in word:
    if char == 'a': # 해당 문자열에서 
        cnt += 1 # 개수를 구하세요.
    
    
print(cnt)
    