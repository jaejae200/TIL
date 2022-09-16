## JavaScript operator



## 할당 연산자

```js
lex x = 0

x += 10 
console.log(x) // 10

X -= 3
console.log(x) // 7

x *= 10
console.log(x) // 70

x /= 10
console.log(x) // 7

x++
console.log(x) // 8

x--
console.log(x) // 7
```



- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
- 다양한 연산에 대한 단축 연산자 지원
- Increment 및 Decrement 연산자
  - Increment(++): 피연산자의 값을 1 증가시키는 연산자
  - Decrement(--): 피연산자의 값을 1 감소시키는 연산자
  - Airbnb Style Guide에서는 ‘+=’ 또는 ‘-=’와 같이 더 분명한 표현으로 적을 것을 권장



## 비교 연산자

```js
const one = 1
const two = 100
console.log(one < two) 			// true

const charone = 'a'
const chartwo = 'z'
console.log(charone > chartwo) // false
```



- 피연산자를 비교하고 결과값을 boolean으로 반환하는 연산자
- 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교
  - 알파벳끼리 비교할 경우
    - 알파벳 순서상 후순위가 더 크다
    - 소문자가 대문자보다 더 크다 



## 동등 비교 연산자

```js
const a = 1004
const b = '1004'
console.log(a == b) // true

const c = 1
const d = true
console.log)(c == d) // true

// 자동 타입 변환 예시
console.log(a+b) // 10041004
console.log(c+b) // 2
```



- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음



## 일치 비교 연산자

```js
const a = 1004
const b = '1004'
console.log(a == b) // false

const c = 1
const d = true
console.log)(c == d) // false
```



- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음
  - 엄격한 비교: 두 비교 대상의 타입과 값 모두 같은지 비교



## 논리 연산자

- 세 가지 논리 연산자로 구성
  - and 연산
    - &&
  - or 연산
    - ||
  - not 연산
    - !
- 단축 평가 지원
  - `false && true => false`
  - `true || false => true`



## 삼항 연산자 

```js
console.log(true ? 1 : 2) // 1
console.log(false ? 1 : 2) // 2

const result = Math.PI > 4 ? 'Yes' : 'No'
console.log(result) // No
```



- 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
- 가장 왼쪽의 조건식이 참이면 콜론(:) 앞의 값을 사용하고 그렇지 않으면 콜론(:) 뒤의 값을 사용
- 삼항 연산자의 결과 값이기 때문에 변수에 할당 가능
- 한 줄에 표기하는 것을 권장





