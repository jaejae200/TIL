import sys

sys.stdin=open('2857.txt', 'r')
name = []

for i in range(5):
    name.append(input())
    
FBI = []

for i in range(len(name)):
    if 'FBI' in name[i]:
        FBI.append(i+1)

if FBI == [] : 
    print('HE GOT AWAY!')
else:
    print(*FBI)



