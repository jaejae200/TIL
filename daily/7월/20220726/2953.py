import sys

sys.stdin = open('2953.txt', 'r') # 텍스트 파일 불러옴


score = []                                       # score 저장할 빈 리스트 생성

for i in range(1, 6):                            # 1  ~  6 까지 반복할 것 = 5번
    score.append(sum(map(int, input().split()))) # score 리스트에 append (추가) (공백으로 구분(split) 하는 정수의 입력(input) 값을 다 더해서)

maximum = max(score)                             # max 함수 이용 score 의 최댓값 저장
print(score.index(maximum) + 1, maximum)             # score의 최댓값 index 위치 찾기 , 최댓값 출력
