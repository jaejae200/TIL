from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count: 
        fruit_count[fruit] = 1 # 딕셔너리 값을 계속 바꾸고 있음,  list를 더해준다고 생각하면서 바꾸면 해결!
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

#  fruit_count[fruit] = fruit_count.get(fruit, 0) + 1  = 한 줄 요약