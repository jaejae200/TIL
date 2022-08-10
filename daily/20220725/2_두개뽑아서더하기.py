# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers): 
    answer = set()
    for i in range(len(numbers)): #0 ~ numbers
        for j in range(i+1, len(numbers)): # 1 ~ numbers
            answer.add(numbers[i]+numbers[j]) # set에 number 값 두개 더한 정수를 입력
    answer = list(answer)  # 리스트로 변환
    answer.sort() # 정렬
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
