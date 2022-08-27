import sys

sys.stdin = open('1076.txt', 'r')

colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
values = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9]
mult = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

value_1 = input()
value_2 = input()
value_3 = input()


result = ((values[colors.index(value_1)] * 10) + values[colors.index(value_2)]) * mult[colors.index(value_3)]

print(result)