i, j = map(int, input().split())

print(bool(i) and bool(not j) or bool(not i) and bool(j))