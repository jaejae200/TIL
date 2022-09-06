text = input().upper()                                      # input 알파벳을 모두 대문자로 받는다
text_list = list(set(text))                                 # list로 만들어주고 set 활용해서 중복을 제거한다 (count 위함)

max_count = []                                              # 문자 개수를 저장해줄 리스트
for i in text_list:                                         # 중복 제거한 알파벳을 i에 저장
    max_count.append(text.count(i))                         # i에 있는 알파벳 기준 input/count 값을 max_count에 추가

if max_count.count(max(max_count)) > 1:                     # max_count의 최댓값이 1개 이상이라면 '?' 출력
    print('?')
else:                   
    print(text_list[(max_count.index(max(max_count)))])     
    # max_count의 최댓값 인덱스 위치를 찾고 text_list에 같은 인덱스의 위치한 알파벳을 출력한다


