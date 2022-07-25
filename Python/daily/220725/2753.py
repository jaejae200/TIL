year = int(input())

if year % 4 ==0 and year % 100 !=0 or year % 400 == 0:  #if year 4로 나눴을때 0이 되면서(and) 100의 배수가 아닐 때 또는(or) 400의 배수일 때
    print('1')                                          # 1을 출력한다
else:                                                   # false 일 경우
    print('0')                                          # 0을 출력한다
