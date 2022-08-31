import sys

sys.stdin=open('11718.txt', 'r')

while True :
    try :
        print(input())
    except EOFError:
        break