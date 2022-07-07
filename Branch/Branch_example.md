## Branch 병합 시나리오

### 상황 1. fast-foward

​		**fast-foward**는 `feature` 브랜치 생성된 이후 `master` 브랜치에 변경 사항이 없는 상황에서 이루어진다.

1. `feature/home branch` 생성 및 이동

2. 작업 완료 후 `commit`

3. `master branch` 이동

4. `master branch` 에 병합

5. 결과 : `fast-foward`

6. `feature/home branch` 삭제

   

### 상황 2. merge commit

**서로 다른 이력**`(commit)`을 **병합**`(merge)`하는 과정에서 **다른 파일이 수정**되어 있는 상황 **git**이 **auto merging**을 진행하고, 

**commit이 발생됨.**

1. `feature/about branch` 생성 및 이동

2. 작업 완료 후 `commit`

3. `master branch` 이동

4. `master branch`에 추가 `commit` 발생시키기!!

5. `master branch`에 병합

6. 결과 -> 자동으로 `merge commit` 발생

7. **커밋** 및 **그래프** 확인하기

8. `feature/about branch` 삭제

   

### 상황 3. merge commit 충돌

**서로 다른 이력**`(commit)`을 **병합**`(merge)`하는 과정에서 **같은 파일의 동일한 부분이 수정**되어 있는 상황

**git**이 **auto merging**을 하지 못하고, 충돌 메시지가 뜬다. 해당 파일의 위치에 **표준형식**에 따라 표시 해준다.

원하는 형태의 코드로 **직접 수정**을 하고 **직접** `commit`을 발생 시켜야 한다.

1. `feature/test branch` 생성 및 이동
2. 작업 완료 후 `commit`
3. `master branch` 이동
4. `master branch`에 추가 `commit` 이 발생시키기!!
5. `master branch`에 병합
6. 결과 -> `merge conflict`발생
7. **충돌 확인 및 해결**
8. `merge commit` 진행
9. **커밋 및 확인하기**
10. `feature/test branch` 삭제

