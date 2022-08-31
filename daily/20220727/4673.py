my_list = set()

for i in range(1, 10001):
    i = i + sum(map(int, str(i)))
    my_list.add(i)

for j in range(1, 10001):
    if j not in my_list:
        print(j)

