word = input()

word_list = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

result = []

for i in word:
    if i not in word_list:
        result.append(i)

print(*result, sep='')