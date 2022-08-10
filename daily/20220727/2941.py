word = input()
char_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in char_list:
    count = word.replace(i, '*')
    word = count

print(len(count))
