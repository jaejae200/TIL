dwarf_list = []                         # 난쟁이 리스트

for _ in range(9):
    dwarf_list.append(int(input()))

list_total = sum(dwarf_list)            # 난쟁이들의 키를 더한 수

for i in range(8):                      # range를 벗어나지 않기 위해 범위 조정
    for j in range(i+1,9):
        if list_total - (dwarf_list[i] + dwarf_list[j]) == 100:      # (키의 총 합) - ((거짓말 난쟁이) + (거짓말 난쟁이)) == 100과 같다면
            liar1 = dwarf_list[i]
            liar2 = dwarf_list[j]

dwarf_list.remove(liar1)                # 찾은 요소를 난쟁이 리스트에 지운다
dwarf_list.remove(liar2)            

dwarf_list.sort()                       # 정렬 *낮은 순서대로

# 출력문
for i in dwarf_list:        
    print(i)