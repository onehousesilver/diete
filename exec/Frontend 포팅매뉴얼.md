# Frontend 포팅매뉴얼

## 소개

diète Frontend 빌드 매뉴얼

## 기술스택 및 라이브러리

| Project              | Version | Description              |
| -------------------- | ------- | ------------------------ |
| animate.css          | 4.1.1   |                          |
| apexcharts           | 3.33.2  |                          |
| axios                | 0.26.1  |                          |
| core-js              | 3.8.3   |                          |
| gsap                 | 3.9.1   |                          |
| hover.css            | 2.3.2   |                          |
| jquery               | 3.6.0   |                          |
| jwt-decode           | 3.1.2   | IDE                      |
| lodash               | 4.17.21 |                          |
| password-validator   | 5.2.1   |                          |
| sass-loader          | 12.6.0  | SCSS Compiler            |
| scrollmagic          | 2.0.8   |                          |
| sweet-modal-vue      | 2.0.0   |                          |
| swiper               | 5.3.7   |                          |
| vue                  | 2.6.14  |                          |
| vue-apexcharts       | 1.6.2   |                          |
| vue-awesome-swiper   | 4.1.1   |                          |
| vue-js-toggle-button | 1.3.3   |                          |
| vue-moment           | 4.1.0   |                          |
| vue-router           | 3.5.1   | Vue3 Official Router     |
| vue-sweetalert2      | 5.0.2   |                          |
| vuetify              | 2.6.0   |                          |
| vuex                 | 3.6.2   | State Management Library |
| vuex-persistedstate  | 4.1.0   |                          |
| VScode               | 1.64.2  | IDE                      |

## 개발 환경 구성

1. 프로젝트 다운로드

   ```shell
   git clone <repo URL> <folder-name>
   ```

2. frontend 폴더로 이동

   ```shell
   cd <folder-name>/Client
   ```

3. 패키지 설치

   ```shell
   npm install
   ```

4. 프로젝트 실행

   ```shell
   npm run serve
   ```

## 디렉토리 구조

```plaintext
.
└─src
    ├─api
    ├─assets  /* image, css, js 등의 리소스 */
    ├─components  /* 컴포넌트 단위의관련 Vue 파일 */
    ├─js  /* API 경로 설정 파일 */
    ├─plugins  
    ├─router  /* 컴포넌트 단위의 Vue 파일 */
    ├─store  /* Vuex 관련 파일 */
    └─views  /* 페이지 단위의 Vue 파일 */
```

