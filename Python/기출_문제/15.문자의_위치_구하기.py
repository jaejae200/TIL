# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

# word = input() # 문자열 word

# first_a = 0
# cnt = 0 
# for i in word :
#     if i == 'a':
#         print(first_a + cnt)
#         break
#     else:
#         cnt + 1

# if first_a == 0:
#     print(-1)

word = input()

for char in word:
# 문자로 순회하는 것이 아니라!
# 인덱스로 접근하자
# 원하는 숫자 0, 1, 2, 3
# 얻는 방법은? range(len(word)) => range(6) => 0 ~ 5
 for i in range(len(word)):
    print(i, word[i])
    # 알파벳이 a일때
    if word[i] == 'a':
        print(i)
        break
# for문을 다 돌았다는 뜻은
# 한번도 break에 안걸렸다.
# 'a'는 없었다.
else:
    print(-1)


# 2. for
# a 가 있었냐? 없었냐? (boolean)
is_a = False 
for i in range(len(word)):
    print(i, word[i])
    if word[i] == 'a':
        print(i)
        break

if is_a == False:
    print(-1)