from http import server
import sys

sys.stdin=open('1543.txt', 'r')

word = input()
search_ = input()

index = 0
result = 0 

while len(word) - index >= len(search_):                    # (전체 문자열) - index 결과가 search_ 문자열의 길이보다 많거나 같을 때까지
    if word[index:index+len(search_)] == search_:           # if word[index값 : index값 + search_ 문자의 길이] 
                                                            # 즉, ex)  word[0:2] 가 aa와 같은지 확인하는 if 문 (예제4 기준)
        result += 1                                         # 결과를 1 더하고
        index += len(search_)                               # index 값에 search_ 문자열 길이를 더한다 = 인덱스를 밀어줌 word[0:2] 존재 시 word[2:0] 으로 
    
    else:                                                   # 포함되지 않는 경우 index를 증가하면서 계속 비교해나감
        index += 1

# 출력문
print(result)


