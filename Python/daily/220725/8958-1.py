T = int(input()) # Test_case 받아옴

for test_case in range(1, T + 1): # test_case에 문제 받을 개수 저장
    
    grade = input()             # 채점받은 결과를 입력받는다 ex = OXOXXO
    total_grade = list(grade)   # 채점받은 결과를 모아서 list로 만들어준다 ex = [O,X,O,X,X,O]
    score = 0                   # 누적되는 점수
    count = 0                  # 정답을 맞췄을 때 받는 점수

    for i in total_grade:
        if i == 'O':
            count += 1
            score += count
        else:
            count = 0

    print(score)