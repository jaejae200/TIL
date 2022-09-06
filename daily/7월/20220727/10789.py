import sys

sys.stdin = open('10789.txt', 'r')

result = []                     # 단어들이 모이는 리스트
max_ = []                       # range를 맞추기 위한 단어들의 길이

for i in range(5):              # 5문장을 받을 것
    word = input()        
    result.append(word)         # 문장은 result에 append
    max_.append(len(word))      # 글자수는 max_ 함수에 append

rst = ''        # 공백 문자 

for i in range(max(max_)):      # max 최대 수 만큼 반복 (range 나가지 않기 위해 )
    for j in range(5):          # 5 단어를 순회
        if i < max_[j]:         # max_[j]가 i보다 큰 경우만
            rst += result[j][i] # rst에 단어를 세로로 적립.

print(rst)
            

    


