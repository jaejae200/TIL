n = int(input())

while True:
    if len(str(n)) == str(n).count('4') + str(n).count('7'):            # 문자열로 변환한 n의 길이가 n의 4 + 7의 개수와 같다면
        
        '''
        97이면 len(str(n)) = 2
        str(n).count('4') + str(n).count('7') = 1
        77이면 len(str(n)) = 2
        tr(n).count('4') + str(n).count('7') = 2
        '''
        print(n)    # 출력하고 종료
        break
    
    n -= 1          # 큰 수를 찾기 위해 입력받은 값에서부터 빼준다.