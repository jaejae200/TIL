word = input()
result = [] 
for i in range(len(word)):
    if word[i] == 'a':
        # 리스트에 추가해줘
        result.append(i)
print(result)

# 2. 그때 그때 출력
word = input()
result = []
for i in range(len(word)):
    if word[i] == 'a':
        print(i, end='')