import sys

sys.stdin = open('4949.txt', 'r')

while True:
   
    word = input()
    if word == '.':
        break
    
    stack = []
    temp = True
    for i in word:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                temp = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                temp = False
                break
            elif stack[-1] == '[':
                stack.pop()     

    if temp == True and not stack:
        print('yes')
    else:
        print('no')   
            


