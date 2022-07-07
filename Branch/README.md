# Branch ✒️

| branch                          | 주요 특징                                                    |
| ------------------------------- | ------------------------------------------------------------ |
| `master (main)`                 | 배포 가능한 상태의 코드                                      |
| `develop (main)`                | **feature branch**로 나뉘어지거나, 발생된 버그 수정 등 개발 진행, 개발 이후 **release branch**로 갈라짐. |
| `feature branches (supporting)` | 기능별 개발 브랜치(topic branch) 기능이 반영되거나 드랍되는 경우 브랜치 삭제 |
| `release branches (supporting)` | 개발 완료 이후 **QA/Test** 등을 통해 얻어진 다음 배포 전 **minor bug fix** 등 반영 |
| `hotfixes (supporting)`         | 긴급하게 반영 해야하는 **bug fix**, **release branch**는 다음 버전을 위한 것<br/>이라면, **hotfix branch**는 현재 버전을 위한 것 |

## 📋 Branch 명령어

`(master) $ git branch [branch name]` 

- 브랜치 생성

`(master) $ git checkout [branch name}]`

- 브랜치 이동

`(master) $ git checkout -b [branch name]`

- 브랜치 생성 및 이동

`(master) $ git branch`

- 브랜치 목록

`(master) $ git branch -d [branch name]`

- 브랜치 삭제

`(master) $ git merge [branch name]`

- 브랜치 병합 

## 🔎 Branch 병합 시나리오

 [Branch 병합 시나리오 예시](Branch_example.md)



## 📄 Feature Branch Workflow 활용 예

**Shared repository model (저장소의 소유권이 있는 경우)**

1. `clone` 을 통해 **저장소**를 **로컬**에 **복제**

2. 기능 추가를 위해 `branch` **생성** 및 **기능** 구현

3. 기능 구현 후 **원격 저장소**에 `branch` 반영

4. `master branch`에 병합 후 병합 완료 된 `branch` 삭제

5. 병합된 `master`의 내용을 `pull`

6. 원격 저장소에서 병합 완료 된 **로컬** `branch` 삭제

7. 새로운 기능 추가를 위해 `branch` **생성 및 과정 반복**

   

### 📄 Forking Workflow 활용 예

**Fork & Pull model (저장소의 소유권이 없는 경우)**

1. 소유권이 없는 **원격 저장소**를 `fork`를 통해 **복제**
2. `clone` 을 통해 **저장소**를 **로컬**에 **복제**
3. 추후 **로컬 저장소**를 **원본 원격 저장소**와 **동기화**하기 위해 **URL**을 연결
4. 기능 추가를 위해 `branch` **생성** 및 **기능** 구현
5. 기능 구현 후 **원격 저장소**에 `branch` 반영
6. 병합 완료 된 `branch` 삭제
7. 병합된 `master`의 내용을 원본 저장소에 `pull`
8. 새로운 기능 추가를 위해 `branch` **생성 및 과정 반복** 





