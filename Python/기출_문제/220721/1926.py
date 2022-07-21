# 숫자 1부터 순서대로 3,6,9 말하지 않음 대신 박수를 침 해당 숫자가 들어간 개수만큼 쳐야함
# 박수 - 두번 --

n = int(input())                # 정수 입력받음
game = ['3', '6', '9']          # 369 룰

for i in range(1, n+1):         # i 안에 주어진 숫자만큼 
    num = (str(i))              # game 비교를 위해 문자열로 변환
    count = 0                   # 3 6 9가 포함된 숫자 세기 위한 저장소
    for j in range(len(num)):   # j에 변환한 num의 자릿수 넣음 1, 2, 3, 4
        if num[j] in game:      # if num[j] 안에 3 6 9 가 있다면 
            count += 1          # count 1 증가
    if count > 0:               # 만약 count 가 1보다 크다면
        num = '-' * count       # num은 '-' * count 만큼! 333 이라면 ---
    
    print(num, end=' ')         # num 결과 출력
    



