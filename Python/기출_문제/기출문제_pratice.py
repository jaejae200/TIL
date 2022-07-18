#.1

# num = int(input())

# if num %3==0:
#     if num %2==0:
#         print('참')
#     else:
#         print('거짓')


#.2

# word = input()
# j = 0
# for i in word:
#     j += 1
# print(j)

#.3

# num = int(input())
# n = 0 
# result = 0

# while n < num:
#     n += 1
#     result += n
# print(result)

#.3-1

# num = int(input())
# result = 0

# for i in range(1, num+1):
#     result += i 

# print(result)

#.4

# num = int(input())
# n = 0 
# result = 1

# while n < num:
#     n += 1
#     result *= n
# print(result)

#.4-1

# num = int(input())
# result = 1

# for i in range(1, num+1):
#     result *= i 

# print(result)

# 5
# numbers = [3, 10, 20] # 1. 문제 제공

# cnt = 0  # 2. 값 초기화
# result = 0 

# for i in numbers: # 3. 반복
#     cnt += 1
#     result += i
# print(int(result)/cnt)

# 6

# numbers = [200, 20, 100, 50, 250, 50, 150] 
# j = numbers[0]
# for i in numbers:
#     if i>j:
#         j=i
# print(j)

# 7 
# numbers = [0, 20, 100]
# j = numbers[0]
# for i in numbers:
#     if i<j:
#         j=i
# print(j)

# 8

# numbers = [0, 20, 100, 50,] 

# if numbers[0]>numbers[1]: #리스트 1번에 있는 숫자가 2번 보다 크다면
#     first = numbers[0] # 1번째로 제일 큰 숫자로 할당
#     second = numbers[1] # 2번째로 제일 큰 숫자로 할당
# else: #반대로 2번에 있는 숫자가 1번 보다 크다면 
#     first = numbers[1] # 2번에 있는 숫자를 제일 큰 숫자로 할당
#     second = numbers[0] # 1번에 있는 숫자를 제일 큰 숫자로 할당

# for i in numbers[2:]: #numbers 3번째부터의 값을 i에 할당
#     if i > second: # 할당된 numbers의 2번째 값이 i보다 작다면
#         if i > first:
#             second = first
#             first = i
#         else:
#             second = i

# print(second)
    

numbers = [0, 20, 100, 40]
# 1. 전체 숫자를 반복
max_number = numbers[0]
second_number = numbers[0]
for n in numbers:
    #만약에, n이 최대보다 크다면
    if max_number < n:
        # 최대값이었던 것이 두번째로 큰 수
        second_number = max_number
        max_number = n
    elif second_number < n < max_number:
    # elif second_number < n and n < max_number:
        second_number = n
print(second_number)


    



