while True :
  value = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']        # 찾을 모음 대문자 소문자
  
  word = input()        # 입력
  
  if word == '#' :                                                  # #을 만나면 종료
    break
  
  cnt = 0               # 모음을 셀 변수

  for i in word:        # word를 한 글자씩 i에 할당
    if i in value:      # i가 value 안에 있으면
        cnt += 1        # cnt 증가

  print(cnt)