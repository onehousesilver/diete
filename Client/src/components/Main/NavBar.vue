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
            <!-- @mouseover="isRecordMouseOver" -->
          <span
            @mouseover="iconToggle"
            @mouseleave="iconToggle"
            id="1"
            class="nav-food-rec material-icons"
          > restaurant 
            <!-- <span class="" v-show="isRecord"></span> -->
          </span>
        </router-link>
        <router-link :to="{ name: 'search', params: { onlySearch: true } }">
          <span 
            class="nav-food-search material-icons"
            @mouseover="iconToggle" 
            @mouseleave="iconToggle"
            id="2"
          > 
            search 
          </span>
        </router-link>
        <router-link :to="{ name: 'record' }">
          <span 
            @mouseover="iconToggle" 
            @mouseleave="iconToggle"
            id="3"
            class="nav-food-mypage material-icons"
          >
            portrait
          </span>
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
import $ from 'jquery';
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
    // hover 시에 아이콘 > 글자 토글
    iconToggle(e){
      // target id 값 기준으로 1,2,3일때
      switch(e.target.id){
        case "1":
          // mouseover 이벤트가 발생하면
          if(e.type=='mouseover'){
            // innerText 변경, material-icons 클래스 삭제
            $('.nav-food-rec').text("음식추천").removeClass('material-icons');
          }
          else{
            $('.nav-food-rec').text("restaurant").addClass('material-icons');
          }
          break
        case "2":
          if(e.type=='mouseover'){
            $('.nav-food-search').text("음식검색").removeClass('material-icons');
          }
          else{
            $('.nav-food-search').text("search").addClass('material-icons');
          }
          break
        case "3":
          if(e.type=='mouseover'){
            $('.nav-food-mypage').text("나의기록").removeClass('material-icons');
          }
          else{
            $('.nav-food-mypage').text("portrait").addClass('material-icons');
          }
          break
        default:
          break
      }
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
  font-size: 1vw;
  color: #333;
  vertical-align: -webkit-baseline-middle;
}
.nav-food-rec.material-icons,
.nav-food-search.material-icons,
.nav-food-mypage.material-icons {
  font-size: 1.5vw;
}
</style>
