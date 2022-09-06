import sys

sys.stdin=open('20001.txt', 'r', encoding = 'utf-8')

problem = []

while True:                  
    word = input()
    if word == '문제':
        problem.append(1)

    if word == '고무오리':
        if not problem:
            problem.append(1)
            problem.append(1)
        else:
            problem.pop()

    if word == '고무오리 디버깅 끝':
        break

if not problem:
    print('고무오리야 사랑해')
else:
    print('힝구')




                        