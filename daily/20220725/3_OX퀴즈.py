# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input()) # Test_case 받아옴

for test_case in range(1, T + 1): # test_case에 문제 받을 개수 저장
    
    grade = input()             # 채점받은 결과를 입력받는다 ex = OXOXXO
    total_grade = list(grade)   # 채점받은 결과를 모아서 list로 만들어준다 ex = [O,X,O,X,X,O]
    score = 0                   # 누적되는 점수
    answer = 1                  # 정답을 맞췄을 때 받는 점수
    
    for i in total_grade:   # 채점 결과를 반복
        if i == 'O':        # 저장소 i에 'O' 라는 문자가 있다면 = 정답!
            score += answer # 점수를 합산한다
            answer += 1     # 다음에 받는 점수가 늘어난다.
        
        else :              # 'O' 가 아닌 경우 (input 에선 'O'와 'X'를 받을 것이기 때문에 X가 포함된다.)
            answer = 1      # 점수를 합산하지 않고, 정답 시 받는 점수를 1점으로 초기화한다.

    print(score)            # 결과 누적 점수를 출력!
