import sys
 
sys.stdin = open('5576.txt', 'r')

W = [int(input()) for _ in range(10)]

K = [int(input()) for _ in range(10)]

W.sort(reverse=True)      # 큰 순서대로 출력        
K.sort(reverse=True)

print(sum(W[:3]))         # 3개만 뽑아 더함
print(sum(K[:3]))