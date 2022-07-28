A, B = map(int, input().split())    # map 사용 띄어쓰기로 구분하는 input 값을 정수로 변환해서 받아온다

reverse_A = int(str(A)[::-1])       # A를 뒤집을 변수를 만듬 =  str 변경 후 슬라이싱해서 뒤집는다. 그 결과를 다시 정수로 변환
reverse_B = int(str(B)[::-1])       # B를 뒤집을 변수를 만듬 =  str 변경 후 슬라이싱해서 뒤집는다. 그 결과를 다시 정수로 변환

print(max(reverse_A, reverse_B))    # 뒤집은 변수 중에서 max(최댓값) 찾아 출력한다


