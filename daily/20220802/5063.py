import sys

sys.stdin=open('5063.txt', 'r')

N = int(input())

for _ in range(N):
    AD = list(map(int, input().split()))
    
    if (AD[0]+AD[2]) == AD[1]: # 기본 수익 + 광고료가 = 광고 후 수입과 같음
        print('does not matter') # 상관없다 출력
    
    if (AD[0]+AD[2]) < AD[1]: # 기본 수익 + 광고료가 = 광고 후 수입보다 적음
        print('advertise')  # 광고를 해야한다 출력
    
    if (AD[0]+AD[2]) > AD[1]: # 기본 수익 + 광고료가 = 광고 후 수입보다 많음
        print('do not advertise') # 광고를 하지 말아야한다 출력
