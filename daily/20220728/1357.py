# 함수 X

X, Y = map(int, input().split())                            # 두 정수 입력받음
reversed_sum = (int(str(X)[::-1])) + (int(str(Y)[::-1]))    # 두 정수를 뒤집은 값을 더해서 reversed에 저장
print(int(str(reversed_sum)[::-1]))                         # 뒤집은 값을 다시 뒤집어서 출력

# 함수 O

def Rev(num):                                               # 함수 정의 rev(num)
    return int(str(num)[::-1])                              # rev 사용 시 num의 문자를 뒤집는 로직을 반환

X, Y = map(int, input().split())                            # 두 정수 입력받음 
print(Rev(Rev(X)+Rev(Y)))                                   # 두 정수를 뒤집은 값을 더해서 뒤집어서 출력
                                                        