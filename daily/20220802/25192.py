import sys

sys.stdin=open('25192.txt', 'r')

N = int(input())                                
dic = {}                                    # 유저 중복 확인할 딕셔너리
cnt = 0                                     # 곰곰티콘 사용 횟수
for _ in range(N):
    user = input()

    if user == 'ENTER':                     # ENTER가 들어오면         
        for key, value in dic.items():      # dic에 있는 key와 value를 가져오고
            if value == 1:                  # value가 1이라면 곰곰티콘을 사용했다는 cnt += 1
                cnt +=1
        dic = {}                            # 그리고 딕셔너리를 초기화한다.
        continue                            # 아래는 실행하지 않음 why? = ENTER는 딕셔너리에 들어갈 필요가 없어서 
    if user not in dic:                     #  user = input 값이 딕셔너리에 없으면 
        dic[user] = 1                       # key = user 와 value = 1을 넣어줌 지금 딕셔너리는 닉네임과 value값 하나씩 있는 상태

for key, value in dic.items():              # key와 value 가 
    if value == 1:                          # 1이라면
        cnt +=1                             # 곰곰티콘 사용 횟수 1을 증가시켜준다.

print(cnt)



# 0과 1로만 이루어져서 곰곰티콘을 확인하는 것
# 그 후에 채팅 기록은 확인하지 않음 = 곰곰티콘이 아닌 일반 채팅 첫 log가 중요

    


 
