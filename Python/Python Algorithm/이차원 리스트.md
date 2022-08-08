# 이차원 리스트 ✒

- list를 원소로 가지는 리스트일 뿐이다.

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix[0][0])
>>> 1
print(matrix[1][2])
>>> 6
print(matrix[2][0])
>>> 7

# 슬라이싱에 익숙해져라!
```

- ### ⭐ 특정 값으로 정해진 이차원 리스트 만들기 ⭐

  1. 직접 작성 (추천하지 않음)

     ```python
     matrix = [
         [0,0,0]
         [0,0,0]
         [0,0,0]
     ]
     ```

  2. 반복문으로 작성 ⭐

     ```python
     # 1.
     matrix = []
     
     for _ in range(10):
         matrix.append([0] * 10)
     
     pprint(matrix)
     >>> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,] # * 10줄
     # ================================================
     # 2.
     n = 4 #행 (가로)
     m = 3 #열 (세로)
     
     matrix = []
     
     for _ in range(n):
         matrix.append([0] * m)
     # ================================================
     # 3.
     n = 10 # 행
     m = 10 # 열
     ⭐ matrix = [[0] * m for _ in range(n)] ⭐ # 익숙해져야 할 코딩
     
     # 제일 중요한 입력받는 2차원 리스트 만들기!
     ⭐⭐ mtrix = [ist(map(int, input().split())) for _ in range(n)] ⭐⭐
     
     ```
  

## 📝 순회

1. 이중 for문을 이용한 행 우선 순회 ✔

   ```python
   for i in range(n): # 행
       for j in range(m): # 열
           print(matrix[i][j])
   ```

2.  이중 for문을 이용한 열 우선 순회 ✔

   ```python
   for i in range(m): # 열
       for j in range(n): #행
           print(matrix[j][i])
   ```

3. Pythonic한 방법 ✔

   ```python
   total = sum(map(sum, matrix))
   ```

4. Pythonic한 방법으로 최대값 최소값 구하기 ✔ 

   ```python
   # 복잡도는 같다는 것을 숙지하고 있어야 함 !
   
   max_value = max(map(max, matrix))
   min_value = min(map(min, matrix))
   ```


##  📝 회전

 1. 90도 회전하기 ✔

    ```python
    matrix = [
        [1, 2, 3]
        [4, 5, 6]
        [7, 8, 9]
    ]
    
    n = 3 
    rotated_matrix = [[0] * n for _ in range(n)]
    	
        # 왼쪽 								
    for i in range(n):
        for j in range(n):
            rotated_matrix[i][j] = ⭐ matrix[j][n-i-1]
        							# 길이 - 인덱스 - 인덱스를 맞춰주는 수
        # 오른쪽 
    for i in range(n):
        for j in range(n):
            rotated_matrix[i][j] = ⭐ matrix[n-j-i][i]
            
    # 과정을 기억하자 직접 생각해보자 
    ```

    

    

