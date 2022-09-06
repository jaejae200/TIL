# https://www.acmicpc.net/problem/10101

triangle = [] 

for _ in range(3):
    triangle.append(int(input()))

if triangle[0] + triangle[1] + triangle[2] == 180:          # 입력받은 세 값의 합이 180 인지
    if triangle.count(60) == 3:                             # 60이 3개 있으면
        print('Equilateral')
    elif triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[0] == triangle[2]:    # 0과 1 1과 0 0과 2 중 하나라도 같으면
        print('Isosceles')
    else:       # 3 각이 모두 틀린 경우
        print('Scalene')
else:   # 180이 아닌 경우
    print('Error')

