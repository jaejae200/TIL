# Grid system  

*web design*

- 요소들의 디자인과 배치에 도움을 주는 시스템
- 기본 요소
  - `Column`
    -  실제 컨텐츠를 포함하는 부분
  - `Gutter `
    - 칼럼 사이의 공간 (간격)
  - `Container`
    - 칼럼들을 담고 있는 공간



## Bootstrap grid System 📋

- `flexbox`로 제작됐다

- `container`, `rows`, `column`으로 컨텐츠를 배치하고 정렬

- ⭐ 중요 ⭐

  - `12개의 column`
  - `6개의 grid breakpoints`

  ```html
  <div class="container">
      <div class="row">
          <div class="col"></div>
          <div class="col"></div>
          <div class="col"></div>
      </div>
  </div>
  ```

  ```css
  @media (min-width: 576px) {
  .container-sm, .container {
  max-width: 540px;
  }
  }
  @media (min-width: 768px) {
  .container-md, .container-sm, .container {
  max-width: 720px;
  }
  }
  @media (min-width: 992px) {
  .container-lg, .container-md, .container-sm, .container {
  max-width: 960px;
  }
  }
  @media (min-width: 1200px) {
  .container-xl, .container-lg, .container-md, .container-sm, .container {
  max-width: 1140px;
  }
  }
  @media (min-width: 1400px) {
  .container-xxl, .container-xl, .container-lg, .container-md, .container-sm, .container {
  max-width: 1320px;
  }
  }
  ```

  