number_list = [1, 23, 9, 6, 91, 59, 29]
max1 = max(number_list) # 내장 함수로 정의를 하다보니 실행할 때에 오류가 생김! 이름 수정하여 정상 출력

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

# type 에러! : int 객체를 호출할 수 없음!