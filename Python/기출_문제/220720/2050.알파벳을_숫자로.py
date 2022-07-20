My_list = list(input()) # 알파벳 list 받기

for i in range(len(My_list)): # 알파벳 개수 i에 넣기
    print(ord(My_list[i])-64, end = '') # ord 변환 = 숫자 대문자 A =65 따라서 -64 후 순서대로 출력
    