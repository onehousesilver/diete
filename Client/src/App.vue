<template>
  <div id="app">
    <!-- nav바 -->
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
          <router-link :to="{ name: 'menu' }">
            <div>음식추천</div>
          </router-link>
          <router-link :to="{ name: 'search' }"
            ><div>영양정보</div>
          </router-link>
          <router-link :to="{ name: 'pocket' }"
            ><div>오늘한끼</div>
          </router-link>
          <router-link :to="{ name: 'record' }"
            ><div>나의기록</div>
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
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
  data: function () {
    return {
      isLogin: false,
    };
  },
  methods: {
    goToHome() {
      this.$router.push({ name: "home" }).catch(() => {});
    },
    goToLogin() {
      this.$router.push({ name: "login" });
      this.isLogin = true;
    },
    goToLogout() {
      this.$router.push({ name: "home" });
      this.isLogin = false;
    },
  },
};
</script>

<style>
@font-face {
  font-family: "MinSans-Regular";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2201-2@1.0/MinSans-Regular.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
#app {
  font-family: "Roboto", "MinSans-Regular";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
a {
  text-decoration: none;
  color: black;
}

.nav {
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
  font-size: 30px;
  margin-left: 100px;
}
.nav .logo:hover {
  cursor: pointer;
}
.nav .menu {
  margin-right: 100px;
}
.nav .menu .login-join .login-btn {
  border-radius: 10px;
  font-size: 14px;
  width: 100px;
  margin-right: 20px;
}
.nav .menu .login-join .join-btn {
  border-radius: 10px;
  margin-right: 45px;
  font-size: 14px;
  width: 100px;
}

.nav .menu .menu-items {
  display: flex;
  align-items: center;
}

.nav .menu .menu-items a {
  margin-right: 45px;
}

.nav .menu .menu-items .logout-btn {
  font-size: 14px;
  width: 100px;
  border-radius: 10px;
}
</style>
