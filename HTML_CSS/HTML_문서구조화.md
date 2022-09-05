# HTML

## HTML 문서 구조화

- table의 각 영역을 명시하기 위해 `<thead>` `<tbody>` `<tfoot>` 요소를 활용한다.

  ![image-20220905145910725](C:\Users\kj310\AppData\Roaming\Typora\typora-user-images\image-20220905145910725.png)



- `<tr>`으로 가로 줄을 구성하고 내부에는 `<th>` 혹은 `<td>`로 셀을 구성

  ![image-20220905150000357](C:\Users\kj310\AppData\Roaming\Typora\typora-user-images\image-20220905150000357.png)



- `colspan` , `rowspan` 속성을 활용하여 셀 병합

  ![image-20220905150041585](C:\Users\kj310\AppData\Roaming\Typora\typora-user-images\image-20220905150041585.png)



- table 태그 기본 구성

  ```html
  <body>
      <table>
          <thead>
              <tr>
                  <th>ID</th>
                  <th>Name</th>
                  <th>Major</th>
              </tr>
          </thead>
          <tbody>
              <tr>
                  <td>1</td>
                  <td>홍길동</td>
                  <td>Computer Science</td>
              </tr>
              <tr>
                  <td>2</td>
                  <td>김철수</td>
                  <td>Business</td>
              </tr>
          </tbody>
          <tfoot>
              <tr>
                  <td>총계</td>
                  <td> colspan="2">2명</td>
              </tr>
          </tfoot>
          <caption>1반 학생 명단</caption>
      </table>
  </body>
  ```



## Form

정보를 서버에 전송하기 위해 사용하는 태그

### 기본 속성

- `action `
  - `form`을 처리할 서버의 `URL`
- `method`
  - `form` 을 제출할 때 사용할 `HTTP` 메서드
  - `GET` 혹은 `POST`
- `enctype`
  - `method`가 `post`인 경우 데이터의 유형
    - `application/x-www-form-urlencoded` : 기본값
    - `multipart/form-data` : 파일 전송 시 (`input type`이 `file`인 경우)



### input

다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공된다.



#### `<input>` 대표적인 속성

- name
  - fom control에 적용되는 이름 (name/value 페어로 전송)
- value
  - fom control에 적용되는 값 (name/value 페어로 전송)
- required, readonly, autofocus, autocomplete, disabled 등



### input label

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음

  - label을 읽어 내용을 쉽게 확인할 수 있도록 한다.

- `<input>`에 id 속성을, `<label>`에는 for 속성을 활용하여 상호 연관을 시킨다

  ```html
  <label for="agreement">개인정보 수집에 동의합니다.</label>
  <input type="checkbox" name="agreement" id="agreement">
  ```

  

### input 유형

일반적으로 입력을 받기 위하여 제공, 타입별로 HTML 기본 검정 혹은 추가 속성을 활용할 수 있다

- `text`
  - 일반 텍스트 입력
- `password`
  - 입력 시 값이 보이지 않고 문자를 특수기호(`*`)로 표현
- `email`
  - 이메일 형식이 아닌 경우 `form` 제출 불가 
- `number`
  - `min`, `max`, `step` 속성을 활용하여 숫자 범위 설정 가능
- `file`
  - `accept` 속성을 활용하여 파일 타입 지정 가능



#### 항목 중 선택

- 일반적으로` label` 태그와 함께 사용하여 선택 항목을 작성

- 동일 항목에 대하여는 `name`을 지정하고 선택된 항목에 대한 `value`를 지정

  - `checkbox`

    - 다중 선택

  - `radio`

    - 단일 선택

    ```html
    <div>
        <p>checkbox</p>
        <input id="html" type="checkbox" name="language" value="html">
        <label for="html">HTML</label>
        <input id="python" type="checkbox" name="language" value="python">
        <label for="python">파이썬</label>
        <input id="python" type="checkbox" name="language" value="java">
        <label for="java">자바</label>
        <hr>
    </div>
    ```

  

#### 기타

- 다양한 종류의 `input`을 위한 `picker`를 제공
  - `color`
    - `color picker`
  - `date`
    - `date picker`
- `hidden input`을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
  - `hidden`
    - 사용자에게 보이지 않는 `input`



