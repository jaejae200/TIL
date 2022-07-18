N = 10
answer = [] # 해결! : tuple 형식이 아닌 list 형식으로 바꿔서 값들을 저장!
for number in range(N + 1):
    answer.append(number * 2)

print(answer)

# AttributeError: 'tuple' object has no attribute 'append'
# tuple 개체에 append 존재하지 않음!