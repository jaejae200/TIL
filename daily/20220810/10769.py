import sys

sys.stdin = open('10769.txt', 'r')

word = input()


if word.count(':-)') > word.count(':-('):   
    print('happy')
elif word.count(':-)') < word.count(':-('):
    print('sad')
elif word.count(':-)') == word.count(':-('):
    print('unsure')
elif word.count(':-)') == 0 and word.count(':-(') == 0:
    print('none')









