<template>
  <div id="body">
    <!-- 비회원일 때 랜딩 페이지 -->

    <div id="logout" v-if="isLogin">
      <!-- top -->
      <section class="top-section">
        <div class="top-title">
          <div class="title">
            <span class="di" style="color: #2bc0af">di</span>
            <span class="e" style="color: #25ab9b">è</span>
            <span class="te" style="color: #219285">te </span>
            <b>시작하기</b>
          </div>
          <div class="text">
            <section>
              <b class="text-highlight">빅데이터</b>를 이용하여
              <br />
              <b>음식 추천 서비스</b>와 <b>맞춤형 식단관리 서비스</b>를
              제공합니다.
              <br />
              또한, <b>건강한 식습관을 지향</b>하고 <br />
              <b>사용자가 선호하는 음식을 추천</b>해드립니다.
            </section>
          </div>
        </div>
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
                class="title back-to-position to-right delay-0"
              />
              <img
                src="../../assets/main_logout/bottom_description.png"
                alt=""
                class="text back-to-position to-right delay-1"
              />

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
import scroll from "../../js/scroll.js";

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
      scroll();
    },
    goToJoin() {
      this.$router.push({ name: "join" });
    },
  },
  mounted() {
    this.test();
  },
};
</script>

<style scoped>
.text-highlight {
  background: linear-gradient(to top, #b7fef6 50%, transparent 50%);
}
/* Logout 랜딩 페이지 */

.top-section {
  height: 80vh;
  background-image: url("../../assets/main_logout/person.gif");
  background-size: 60rem;
  background-repeat: no-repeat;
  background-position: right;
  color: #333;
  background-color: #f7fcff;
}
.top-section .top-title {
  height: 31.25rem;
  text-align: left;
  margin-left: 21.875rem;
}
.top-section .top-title .title {
  padding-top: 10.625rem;
  font-size: 4.375rem;
  font-weight: 700;
}
.top-section .top-title .text {
  margin-top: 1.25rem;
  font-size: 2.188rem;
}

.middle-section .inner {
  position: relative;
  height: 40vh;
}
.middle-section .inner .recommend_page {
  display: block;
  width: 37.5rem;
  margin-left: 18.75rem;
}

.middle-section .text-group {
  position: absolute;
  top: 6.25rem;
  right: 12.5rem;
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
  height: 40vh;
}
.middle-section2 .inner .my_page {
  width: 600px;
  display: block;
  text-align: left;
  margin-top: 6.25rem;
  margin-left: auto;
  margin-right: 15.625rem;
}

.middle-section2 .text-group {
  position: absolute;
  top: 6.25rem;
  left: 31.25rem;
}

.middle-section2 .text-group .description {
  display: block;
}

/* bottom */
.bottom-section {
  background-image: url("../../assets/main_logout/main_bg2.png");
  background-attachment: fixed;
  background-color: #eaf7ee;
  background-position: right;
  background-repeat: no-repeat;
  background-position-x: 56.25rem;
  background-size: 87.5rem;
}
.bottom-section .inner {
  padding: 6.25rem 0;
}
.bottom-section .text-group {
  width: 22.625rem;
  display: flex;
  justify-content: flex-end;
  flex-wrap: wrap;
  margin-left: 35.625rem;
}

.bottom-section .text-group .title {
  margin-bottom: -50px;
}
.bottom-section .start-btn {
  margin-top: 1.25rem;
  margin-right: 1.875rem;
  width: 18.75rem;
  height: 3.125rem;
  border-radius: 10px;
}
/*BACK TO POSITION*/
.back-to-position {
  opacity: 0;
  transition: 1s;
}
.back-to-position.to-right {
  transform: translateX(-150px);
}
.back-to-position.to-left {
  transform: translateX(150px);
}
.show .back-to-position {
  opacity: 1;
  transform: translateX(0);
}
.show .back-to-position.delay-0 {
  transition-delay: 0s;
}
.show .back-to-position.delay-1 {
  transition-delay: 0.3s;
}
.show .back-to-position.delay-2 {
  transition-delay: 0.6s;
}
.show .back-to-position.delay-3 {
  transition-delay: 0.9s;
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
