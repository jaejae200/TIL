
N = int(input())                            # 총 카드 숫자 ex 7 = 1 ~ 7
card_list = []                              # 카드 저장할 리스트
delete_card = []                            # 버릴 카드 저장할 리스트
for i in range(1, N+1):                     # 카드 저장할 리스트에 카드 넣어줌
    card_list.append(i)

while len(card_list) != 1:                  # while card_list에 len 길이가 1이 아닐 때까지
    delete_card.append(card_list.pop(0))    # delete_card에 append 추가 card_list의 첫번째 데이터를 꺼내면서(pop) = 버린 카드 리스트
    card_list.append(card_list.pop(0))      # card_list에 append 추가 card_list의 첫번째 데이터를 꺼내면서(pop) = 첫번째 데이터를 맨 아래 데이터로 넣어주기

print(*delete_card, *card_list)             # *이용해서 출력 조작 버린 카드들과 남은 카드 출력
