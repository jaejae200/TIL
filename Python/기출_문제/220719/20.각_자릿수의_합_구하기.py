# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

def number(n):
    answer = 0
    while n:
        answer += n%10 #answer 에 n에 10을 나눈 나머지를 더함
        n //= 10 
    return answer

print(number(int(input())))