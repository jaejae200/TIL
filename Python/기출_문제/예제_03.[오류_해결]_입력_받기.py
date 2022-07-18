try:
    numbers = map(int, input().split()) # 정수로 변환시킨 값을 입력받음으로서 오류 해결!
    print(sum(numbers)) # sum 숫자만 가능함
except:
    print('숫자가 아닙니다') # sum 숫자만 가능함

# 타입 불일치로 생겨난 오류
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
