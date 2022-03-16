<template>
  <div id="app">
    <div class="nav">
      <div class="logo" @click="$router.push({ name: 'home' }).catch(() => {})">
        <span class="di" style="color: #2bc0af">di</span>
        <span class="e" style="color: #25ab9b">è</span>
        <span class="te" style="color: #219285">te</span>
      </div>
      <div class="menu">
        <button
          class="bttn-unite bttn-md bttn-success login-btn"
          @click="$router.push({ name: 'login' })"
        >
          로그인
        </button>
        <button
          class="bttn-unite bttn-md bttn-success join-btn"
          @click="$router.push({ name: 'join' })"
        >
          회원가입
        </button>
      </div>
    </div>
    <router-view />
  </div>
</template>

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

.nav {
  align-items: center;
  display: flex;
  justify-content: space-between;
  height: 80px;
  margin: 0 auto;
  background-color: #f4f4f4;
}
.nav .logo {
  display: inline-block;
  font-weight: 700;
  font-size: 30px;
  margin-left: 45px;
}
.nav .logo:hover {
  cursor: pointer;
}

.nav .menu .login-btn {
  border-radius: 10px;
  font-size: 14px;
  width: 100px;
  margin-right: 20px;
}
.nav .menu .join-btn {
  border-radius: 10px;
  margin-right: 45px;
  font-size: 14px;
  width: 100px;
}
</style>
