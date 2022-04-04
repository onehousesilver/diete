<template>
  <div id="body">
    <!-- 비회원일 때 랜딩 페이지 -->
    <div id="logout" v-if="!isLogin">
      <div id="to-top">
        <div class="material-icons arrow" @click="toTop">arrow_upward</div>
      </div>
      <!-- top -->
      <section class="top-section">
        <div class="inner">
          <div class="text-group">
            <div class="title">
              <span class="di" style="color: #2bc0af">di</span>
              <span class="e" style="color: #25ab9b">è</span>
              <span class="te" style="color: #219285">te </span>
              <b>시작하기</b>
            </div>
            <div class="description">
              <b class="text-highlight">빅데이터</b>를 이용하여
              <br />
              <b>음식 추천 서비스</b>와 <b>맞춤형 식단관리 서비스</b>를
              제공합니다.
              <br />
              또한, <b>건강한 식습관을 지향</b>하고 <br />
              <b>사용자가 선호하는 음식을 추천</b>해드립니다.
            </div>
          </div>
          <img src="../../assets/main_logout/main_landing.gif" alt="" />
          <div class="scroll-container">
            <div class="scroll-bar"></div>
            <div class="scroll-bar"></div>
            <div class="scroll-bar"></div>
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
          <img
            class="bottom-bg"
            src="../../assets/main_logout/walk.gif"
            alt=""
          />
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
      </section>
    </div>
    <!-- 회원일 때 랜딩 페이지 -->
    <div id="login" v-else>
      <div class="main-section-login">
        <div class="main-title">건강한 하루의 시작</div>
        <div class="main-sub-title">
          {{ userInfo.data.name }}님, 오늘 하루도 건강하게 시작해보세요!
        </div>
        <div class="card-section">
          <div class="menu-recommend-card">
            <router-link :to="{ name: 'ChooseMeal' }">
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
  data() {
    return {
      userName: null,
    };
  },
  methods: {
    startScrollEvent() {
      scroll();
    },
    goToJoin() {
      this.$router.push({ name: "join" });
    },
    toTop() {
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    },
  },
  mounted() {
    this.startScrollEvent();
    this.userName = this.userInfo.data.name;
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
    userInfo() {
      return this.$store.getters.getUserInfo;
    },
  },
};
</script>

<style scoped>
#to-top {
  width: 3vw;
  height: 3vw;
  background-color: #25ab9b;
  color: #fff;
  border: 0.1vw solid #fff;
  border-radius: 0.4vw;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  bottom: 1.5vw;
  right: 1.5vw;
}

#to-top .arrow {
  font-size: 1.5vw;
}
.text-highlight {
  background: linear-gradient(to top, #b7fef6 50%, transparent 50%);
}
/* Logout 랜딩 페이지 */

.top-section {
  background-color: #fdfefe;
  height: 38vw;
  color: #333;
}

.top-section .inner {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 50vw;
  height: 30vw;
  margin: 0 auto;
}

.top-section .text-group .title {
  position: relative;
  font-size: 3vw;
  font-weight: 700;
  bottom: 2vw;
}
.top-section .inner img {
  display: block;
  position: absolute;
  width: 35vw;
  right: -16vw;
}
.top-section .text-group .description {
  position: relative;
  font-size: 1.5vw;
  top: 1vw;
  z-index: 1;
}

/* middle */
.middle-section .inner {
  position: relative;
  height: 40vh;
  width: 60vw;
  margin: 0 auto;
}
.middle-section .inner .recommend_page {
  display: block;
  position: absolute;
  width: 23vw;
  left: 3vw;
}

.middle-section .text-group {
  position: absolute;
  top: 3vw;
  left: 30vw;
  width: 30vw;
  height: 8vw;
}
.middle-section .text-group .title {
  width: 17vw;
  height: 5vw;
}

.middle-section .text-group .description {
  display: block;
  width: 31vw;
  height: 3.5vw;
  margin-left: 0.5vw;
}

/* middle-sction2 */
.middle-section2 {
  background-image: url("../../assets/main_logout/main_bg.png");
  height: 100%;
}
.middle-section2 .inner {
  position: relative;
  height: 40vh;
  width: 60vw;
  margin: 0 auto;
  top: 4vw;
}
.middle-section2 .inner .my_page {
  display: block;
  position: absolute;
  width: 23vw;
  right: -1vw;
}

.middle-section2 .text-group {
  position: absolute;
  top: 2vw;
  left: 4vw;
}

.middle-section2 .text-group .title {
  width: 14vw;
  height: 5vw;
}

.middle-section2 .text-group .description {
  display: block;
  width: 31vw;
  height: 3.5vw;
  margin-left: 0.3vw;
}

/* bottom */

.bottom-section .inner {
  position: relative;
  height: 40vh;
  width: 45vw;
  margin: 0 auto;
  top: 2vw;
}
.bottom-section .inner .bottom-bg {
  display: block;
  position: absolute;
  width: 42vw;
  right: -8vw;
}
.bottom-section .text-group {
  width: 26vw;
  display: flex;
  justify-content: flex-end;
  flex-wrap: wrap;
  position: relative;
  left: -9vw;
}

.bottom-section .text-group .title {
  margin-bottom: -2vw;
  position: relative;
  left: 1vw;
  width: 17vw;
  height: 15vw;
}

.bottom-section .text-group .text {
  position: relative;
  width: 32vw;
  height: 16vw;
}
.bottom-section .start-btn {
  margin-top: 1vw;
  margin-right: 1vw;
  margin-bottom: 1vw;
  width: 10vw;
  height: 2vw;
  font-size: 1vw;
  border-radius: 0.3vw;
  height: 2.5vw;
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
  margin: 0 5vw;
}
a {
  width: 100%;
  height: 100%;
}
.main-section-login .main-title {
  font-size: 2vw;
  font-weight: 700;
  margin-top: 1.5vw;
  margin-left: 0.5vw;
}
.main-section-login .main-sub-title {
  font-size: 1.3vw;
  margin-left: 0.5vw;
}

.card-section {
  display: flex;
  font-size: 1.8vw;
  justify-items: center;
  margin-top: 1vw;
  color: #333;
}
.card-section span {
  display: block;
  font-size: 1vw;
  margin-left: 1.2vw;
  color: #333;
}
.card-section div {
  margin-left: 1.1vw;
  margin-top: 0.3vw;
  font-weight: 700;
}

.card-section .menu-recommend-card,
.card-section .menu-search-card,
.card-section .menu-record-card {
  display: flex;
  flex-direction: column;
  padding: 0.5vw;
  margin: 0.3vw;
  width: 33vw;
  height: 23vw;
  border: solid #25ab9b 0.2vw;
  border-radius: 1vw;
  cursor: pointer;
}
.card-section .menu-recommend-card a,
.card-section .menu-search-card a,
.card-section .menu-record-card a {
  position: relative;
}

.card-section .menu-search-card img,
.card-section .menu-record-card img,
.card-section .menu-recommend-card img {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: 0;
  max-width: 100%;
  max-height: 75%;
  object-fit: cover;
}

.scroll-bar {
  position: absolute;
  width: 3vw;
  height: 8px;
  left: 50%;
  bottom: 5rem;
  opacity: 0;
  transform: scale3d(0.5, 0.5, 0.5);
  animation: move 3s ease-out infinite;
}

.scroll-bar:first-child {
  animation: move 3s ease-out 1s infinite;
}

.scroll-bar:nth-child(2) {
  animation: move 3s ease-out 2s infinite;
}

.scroll-bar:before,
.scroll-bar:after {
  content: "";
  position: absolute;
  top: 0;
  height: 100%;
  width: 50%;
  background: #aaa;
}

.scroll-bar:before {
  left: 0;
  transform: skew(0deg, 30deg);
}

.scroll-bar:after {
  right: 0;
  width: 50%;
  transform: skew(0deg, -30deg);
}

@keyframes move {
  25% {
    opacity: 1;
  }
  33% {
    opacity: 1;
    transform: translateY(2rem);
  }
  67% {
    opacity: 1;
    transform: translateY(3rem);
  }
  100% {
    opacity: 0;
    transform: translateY(4rem) scale3d(0.5, 0.5, 0.5);
  }
}
</style>
