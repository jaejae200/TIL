# 백준은 통과하는데 실행이 안돼요..

import sys

word = sys.stdin.readline()                         # input (찾아서 적용했음.)
word = word.replace('\n', '').replace(' ', '')

small = [0]*26                  # 인덱스 값 만들어주는 변수 저장

for i in word:
    small[ord(i)-97] += 1       # word 입력받은 값을 순회하면서 i에 할당

'''
ord 사용해서 유니코드 변환하고 a = 97 이므로
index 값을 맞춰주기 위해 -97을 해줌
index 값 + 1
'''

for j in range(26):              # samll의 index만큼 반복문 순회
    if small[j] == max(small):      # if samll의 index에 저장된 값과 small의 max  값이 같다면
        print(chr(97+j), end ='')   # 아스키코드로 변환된 숫자를 다시 소문자로 만들어주고 end 이용 = 출력 조건