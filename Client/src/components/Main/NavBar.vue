<template>
  <div class="nav">
    <div class="logo" @click="goToHome">
      <span class="di" style="color: #2bc0af">di</span>
      <span class="e" style="color: #25ab9b">è</span>
      <span class="te" style="color: #219285">te</span>
    </div>
    <div class="menu">
      <div class="login-join" v-if="!isLogin">
        <button
          class="bttn-unite bttn-md bttn-success login-btn"
          @click="goToLogin"
        >
          로그인
        </button>
        <router-link :to="{ name: 'join' }">
          <button class="bttn-unite bttn-md bttn-success join-btn">
            회원가입
          </button></router-link
        >
      </div>
      <div class="menu-items" v-else>
        <router-link :to="{ name: 'ChooseMeal' }">
          <div
            @mouseover="isRecordMouseOver"
            @mouseleave="isRecordshowMouseLeave"
          >
            <span class="material-icons" v-show="!isRecord"> restaurant </span>
            <span class="nav-food-rec" v-show="isRecord"></span>
          </div>
        </router-link>
        <router-link :to="{ name: 'search', params: { onlySearch: true } }">
          <div @mouseover="isSearchMouseOver" @mouseleave="isSearchMouseLeave">
            <span class="material-icons" v-show="!isSearch"> search </span>
            <span class="nav-food-search" v-show="isSearch"></span>
          </div>
        </router-link>
        <router-link :to="{ name: 'record' }">
          <div @mouseover="isMyPageMouseOver" @mouseleave="isMyPageMouseLeave">
            <span class="material-icons" v-show="!isMyPage"> portrait</span>
            <span class="nav-food-mypage" v-show="isMyPage"></span>
          </div>
        </router-link>
        <button
          class="bttn-unite bttn-md bttn-success logout-btn"
          @click="goToLogout"
        >
          로그아웃
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "NavBar",
  data() {
    return {
      isRecord: false,
      isSearch: false,
      isMyPage: false,
    };
  },
  methods: {
    ...mapActions(["removeUserToken"]),
    goToHome() {
      this.$router.push({ name: "home" }).catch(() => {});
    },
    goToLogin() {
      this.$router.push({ name: "login" }).catch(() => {});
    },
    goToLogout() {
      this.$router.push({ name: "home" }).catch(() => {});
      this.removeUserToken();
    },
    isRecordMouseOver() {
      this.isRecord = true;
      const recordText = document.querySelector(".nav-food-rec");
      recordText.textContent = "음식추천";
    },
    isRecordshowMouseLeave() {
      this.isRecord = false;
    },
    isSearchMouseOver() {
      this.isSearch = true;
      const searchText = document.querySelector(".nav-food-search");
      searchText.textContent = "음식검색";
    },
    isSearchMouseLeave() {
      this.isSearch = false;
    },
    isMyPageMouseOver() {
      this.isMyPage = true;
      const myText = document.querySelector(".nav-food-mypage");
      myText.textContent = "나의기록";
    },
    isMyPageMouseLeave() {
      this.isMyPage = false;
    },
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
};
</script>

<style>
a {
  text-decoration: none;
  color: black;
}

.nav {
  position: sticky;
  top: 0;
  z-index: 2;
  opacity: 0.8;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 8vh;
  margin: 0 auto;
  background-color: #fff;
}
.nav .logo {
  display: inline-block;
  font-weight: 700;
  font-size: 2vw;
  margin-left: 4vw;
}
.nav .logo:hover {
  cursor: pointer;
}
.nav .menu {
  margin-right: 5vw;
}
.nav .menu .login-join .login-btn {
  border-radius: 0.4vw;
  font-size: 0.8vw;
  width: 5vw;
  height: 100%;
  margin-right: 1vw;
}
.nav .menu .login-join .join-btn {
  border-radius: 0.4vw;
  margin-right: 2vw;
  font-size: 0.8vw;
  height: 100%;
  width: 5vw;
}
.bttn-unite.bttn-success:after,
.bttn-unite.bttn-success:before {
  background: #25ab9b;
}
.nav .menu .menu-items {
  font-weight: 700;
  display: flex;
  align-items: center;
}

.nav .menu .menu-items a {
  font-size: 0.8vw;
  margin-right: 2vw;
}

.nav .menu .menu-items .logout-btn {
  font-size: 0.8vw;
  width: 5vw;
  height: 100%;
  border-radius: 0.4vw;
}
.material-icons {
  font-size: 1.5vw;
  color: #333;
  vertical-align: -webkit-baseline-middle;
}

.nav-food-rec,
.nav-food-search,
.nav-food-mypage {
  font-size: 0.9vw;
  color: #333;
  vertical-align: -webkit-baseline-middle;
}
</style>
