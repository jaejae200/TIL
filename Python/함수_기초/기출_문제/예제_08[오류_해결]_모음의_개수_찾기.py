word = "HappyHacking"

count = 0

for char in word:
    if char in ['a','e','i','o','u']: # or 사용하여 모든 값이 count 되었음. (or = 하나만 참이라도 수행)
        count += 1

print(count)

# in 사용하여 모음이 word 안에 있다면 count 증가!