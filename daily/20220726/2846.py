import sys

sys.stdin = open('2846.txt', 'r')

N = int(input())                            # 측정한 높이의 수
road = list(map(int, input().split()))      # N개의 양의 정수
uphill = 0                                  # 오르막길 높이를 임시 저장할 변수
count = []                                  # 오르막길 높이를 최종적으로 넣어줄 리스트
for i in range(N - 1):                      # index 0부터 n의 -1 까지
    if road[i] < road[i + 1]:               # index 1이 0보다 크다면
        uphill += (road[i + 1] - road[i])   # uphill에 index[1]에서 index[0]을 뺀 수를 적립
    elif road[i] >= road[i + 1]:            # index 0이 1보다 크다면
        count.append(uphill)                # uphill에 있는 데이터를 count에 저장 (여러 오르막길이 나올 수 있음)
        uphill = 0                          # uphill 0으로 초기화

count.append(uphill)                        # 반복문이 종료된 후 uphill에 있는 결과를 최종 count에 삽입

print(max(count))                           # count 리스트 안의 최댓값을 print (제일 높았던 오르막길!)
