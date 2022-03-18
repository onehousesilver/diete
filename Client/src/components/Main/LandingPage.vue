<template>
  <div id="body">
    <!-- 비회원일 때 랜딩 페이지 -->

    <div id="logout" v-if="isLogin">
      <!-- top -->
      <section class="top-section">
        <div class="top-title">diète</div>
        <div class="top-title">오늘 어떤 음식을 드시고 싶으신가요?</div>
        <div class="top-title">
          당신은 하루 칼로리 권장량을 준수하고 계신가요?
        </div>
        <div class="top-title">내 식단에 대한 분석이 필요하신가요?</div>
        <div class="top-title">내가 먹은 음식에 대한 자세한 정보와</div>
        <div class="top-title">어쩌고저쩌고를 할 수 있습니다.</div>
      </section>

      <!-- middle -->
      <section class="middle-section scroll-spy">
        <div class="inner">
          <img
            src="../../assets/main_logout/recommend_page.png"
            alt=""
            class="recommend_page back-to-position to-right delay-0"
          />

          <div class="text-group">
            <img
              src="../../assets/main_logout/main_title1.png"
              alt=""
              class="title back-to-position to-left delay-1"
            />
            <img
              src="../../assets/main_logout/main_description1.png"
              alt=""
              class="description back-to-position to-left delay-2"
            />
          </div>
        </div>
      </section>

      <section class="middle-section2 scroll-spy">
        <div class="inner">
          <img
            src="../../assets/main_logout/my_page.png"
            alt=""
            class="my_page back-to-position to-right delay-0"
          />

          <div class="text-group">
            <img
              src="../../assets/main_logout/middle2_title.png"
              alt=""
              class="title back-to-position to-left delay-1"
            />
            <img
              src="../../assets/main_logout/middle2_text.png"
              alt=""
              class="description back-to-position to-left delay-2"
            />
          </div>
        </div>
      </section>

      <!-- bottom -->
      <section class="bottom-section scroll-spy">
        <div class="inner">
          <div>
            <div class="text-group">
              <img
                src="../../assets/main_logout/bottom_title_bold.png"
                alt=""
                class="recommend_page back-to-position to-right delay-0"
              />
              <img
                src="../../assets/main_logout/bottom_description.png"
                alt=""
                class="recommend_page back-to-position to-right delay-1"
              />
            </div>
            <div class="more back-to-position to-right delay-2">
              <button
                class="bttn-unite bttn-md bttn-success start-btn"
                @click="goToJoin"
              >
                시작하기
              </button>
            </div>
          </div>
        </div>
      </section>
    </div>

    <!-- 회원일 때 랜딩 페이지 -->
    <div id="login" v-else>
      <div class="main-section-login">
        <div class="main-title">건강한 하루의 시작</div>
        <div class="main-sub-title">오늘 하루도 건강하게 시작해보세요!</div>
        <div class="card-section">
          <div class="menu-recommend-card">
            <router-link :to="{ name: 'menu' }">
              <div>음식추천</div>
              <span>나에게 꼭 맞는 식단을 추천해드립니다.</span>
              <img src="../../assets/recommend-card.svg" alt="" />
            </router-link>
          </div>

          <div class="menu-search-card">
            <router-link :to="{ name: 'search' }">
              <div>음식검색</div>
              <span>어떤 음식이든 검색해보세요!</span>
              <img src="../../assets/search-card.svg" alt="" />
            </router-link>
          </div>

          <div class="menu-record-card">
            <router-link :to="{ name: 'record' }">
              <div>나의기록</div>
              <span>내 기록을 남겨보세요.</span>
              <img src="../../assets/record-card.svg" alt="" />
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import goToTop from "../../js/goToTop.js";

export default {
  name: "MainDescription",
  data: function () {
    return {
      isLogin: true,
    };
  },
  // test를 필요한 이벤트에 넣음
  // created 될 때 test 실행
  methods: {
    test() {
      goToTop();
    },
    goToJoin() {
      // signup으로 감
    },
  },
  mounted() {
    this.test();
  },
};
</script>

<style scoped>
/* Logout 랜딩 페이지 */
#logout {
  /* margin: 0 6.25rem; */
}
.top-section {
  height: 700px;
  background-image: url("../../assets/main_logout/person.gif");
  background-size: contain;
  background-repeat: no-repeat;
}
.top-section .top-title {
  font-size: 50px;
  text-align: center;
}

.middle-section .inner {
  position: relative;
  height: 400px;
}
.middle-section .inner .recommend_page {
  display: block;
  width: 600px;
  margin-left: 300px;
}

.middle-section .text-group {
  position: absolute;
  top: 100px;
  right: 200px;
}

.middle-section .text-group .description {
  display: block;
}

/* middle-sction2 */
.middle-section2 {
  background-image: url("../../assets/main_logout/main_bg.png");
}
.middle-section2 .inner {
  position: relative;
  height: 400px;
}
.middle-section2 .inner .my_page {
  width: 600px;
  display: block;
  margin-left: 300px;
}

.middle-section2 .text-group {
  position: absolute;
  top: 100px;
  right: 200px;
}

.middle-section2 .text-group .description {
  display: block;
}

.bottom-section {
  height: 800px;
  background-attachment: fixed;
  background-color: #eaf7ee;
  background-image: url("../../assets/main_logout/main_bg2.png");
  background-position: right;
  background-repeat: no-repeat;
  background-position-x: 900px;
}

/* Login 랜딩 페이지 */
#login {
  margin: 0 6.25rem;
}
a {
  width: 100%;
  height: 100%;
}
.main-section-login .main-title {
  font-size: 2.3rem;
  font-weight: 700;
  margin-top: 1.875rem;
  color: #333;
}
.main-section-login .main-sub-title {
  font-size: 1.5rem;
  color: #333;
}

.card-section {
  display: flex;
  font-size: 2rem;
  justify-items: center;
  margin-top: 1.875rem;
  color: #333;
}
.card-section span {
  display: block;
  font-size: 1rem;
  margin-left: 1.25rem;
  color: #333;
}
.card-section div {
  margin-left: 1.25rem;
  margin-top: 0.625rem;
  font-weight: 700;
}

.card-section .menu-recommend-card {
  display: flex;
  flex-direction: column;
  padding: 0.625rem;
  margin: 0.313rem;
  width: calc(100% / 3);
  height: 40vh;
  border: solid #25ab9b 0.125rem;
  border-radius: 1.25rem;
  cursor: pointer;
}
.card-section .menu-recommend-card a {
  position: relative;
}
.card-section .menu-recommend-card img {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: 0;
  max-width: 100%;
  max-height: 75%;
}
.card-section .menu-search-card {
  display: flex;
  flex-direction: column;
  padding: 0.625rem;
  margin: 0.313rem;
  width: calc(100% / 3);
  height: 40vh;
  border: solid #25ab9b 0.125rem;
  border-radius: 1.25rem;
  cursor: pointer;
}
.card-section .menu-search-card a {
  position: relative;
}
.card-section .menu-search-card img {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: 0;
  max-width: 100%;
  max-height: 75%;
  object-fit: cover;
}
.card-section .menu-record-card {
  display: flex;
  flex-direction: column;
  padding: 0.625rem;
  margin: 0.313rem;
  width: calc(100% / 3);
  height: 40vh;
  border: solid #25ab9b 0.125rem;
  border-radius: 1.25rem;
  cursor: pointer;
}
.card-section .menu-record-card a {
  position: relative;
}
.card-section .menu-record-card img {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: 0;
  max-width: 100%;
  max-height: 75%;
}
</style>
