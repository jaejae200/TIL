T = int(input())

for tc in range(1, T+1):
    option_result = 0                    #옵션 가격의 결과 
    s = int(input())                     
    option = int(input())
    
    for _ in range(option):             
        q, p = map(int, input().split())
        option_result += p * q      # 옵션 개수와 가격을 곱해서 저장

    # 출력문 (자동차 + 옵션값)
    print(s + option_result)