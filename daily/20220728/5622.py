# 1 = 2초 2 = 3초 ... 
# ABC = 2 DEF = 3 어떻게 표현할까..?
# 추가    2       3      4      5 dial 
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'] # 다이얼 리스트
# 추가    0       1      2      3 index
# 추가    3       4      5      6 second
time_sec = 0 # 총 걸리는 시간

word = input()                                      # 입력을 받음 
for char in word:                                   # i에 word 저장 [W, A]
    for dial_list in dial:                          # j에 다이얼 리스트 저장 
        if char in dial_list:                       # dial_list에 char가 있으면
            time_sec += dial.index(dial_list) + 3   # char가 존재하는 index 위치에 +3(초) 더한 값을 넣어준다
            

print(time_sec)