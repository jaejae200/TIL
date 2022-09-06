import sys

sys.stdin=open('1100.txt', 'r')

matrix =[list(input()) for _ in range(8)]           #8 * 8의 리스트를 만듦

cnt = 0                                             # 흰칸 위에 있는 F수를 넣어줄 변수
for i in range(8):                                  # 하나하나 탐색할 반복문
    for j in range(8):
        if matrix[i][j] == 'F':                     # 만약 matrix에 i열 j행에 F가 있다면
            if (i + j) % 2 == 0:                    # 또, 인덱스 위치를 숫자로 나타내고 2로 나눴을 때 나머지가 0이라면
                cnt += 1                            # cnt 를 1 증가시켜준다

print(cnt)

