<template>
  <div>
    <BannerBar
      MainText="로그인"
      SubText="diète의 다양한 기능을 사용해 보세요."
    />
    <div class="login-container">
      <div class="group">
        <input class="my-input" type="text" id="userId" v-model="userId" />
        <label for="userID">아이디</label>
        <span class="highlight"></span>
        <span class="bar"></span>
      </div>

      <div class="group">
        <input
          class="my-input"
          type="password"
          id="userPW"
          v-model="userPW"
          @keyup.enter="userLogin"
        />
        <label for="userPW">비밀번호</label>
        <span class="highlight"></span>
        <span class="bar"></span>
      </div>

      <button
        class="bttn-unite bttn-md bttn-success login-btn"
        @click="userLogin"
      >
        로그인
      </button>
      <div class="additional-btn">
        <span>비밀번호 찾기 | </span>
        <span>아이디 찾기 | </span>
        <span @click="goToJoin"> 회원가입 </span>
      </div>
    </div>
  </div>
</template>

<script>
import BannerBar from "@/components/Main/BannerBar.vue";
import axios from "axios";
import { mapActions } from "vuex";

export default {
  name: "LoginView",
  components: {
    BannerBar,
  },
  data() {
    return {
      userId: null,
      userPW: null,
    };
  },
  methods: {
    ...mapActions(["getUserToken"]),
    userLogin() {
      axios({
        method: "post",
        url: `${process.env.VUE_APP_API_URL}/user/api-token-auth/`,
        data: {
          username: this.userId,
          password: this.userPW,
        },
      })
        .then((res) => {
          this.getUserToken(res.data.token);
          this.$router.push({ name: "home" });
        })
        .catch(() => {
          this.$swal.fire({
            icon: "error",
            title: "로그인 할 수 없어요!",
            text: "아이디 또는 비밀번호를 확인해주세요.",
          });
          // console.log(err)
        })        
        .catch((err) => {
          console.log(err);
        });
    },
    goToJoin() {
      this.$router.push({ name: "join" }).catch(() => {});
    },
  },
};
</script>

<style scoped>
.bttn-unite.bttn-success {
  border-radius: 0.625rem;
  margin-bottom: 1.875rem;
}
.bttn-unite.bttn-success:before {
  background: #25ab9b;
}
.bttn-unite.bttn-success:after {
  background: #25ab9b;
}
.login-container {
  position: relative;
  top: 8rem;
  width: 50rem;
  margin: 0 auto;
  border-radius: 1.875rem;
  text-align: center;
}
.group {
  position: relative;
  margin-bottom: 2.8125rem;
  width: 30vw;
  left: 50%;
  transform: translateX(-50%);
}
.group .my-input {
  font-size: 1rem;
  padding: 1.2rem 1rem 0.625rem 0.3125rem;
  display: block;
  width: calc(30vw - 1.3125rem);
  border: none;
  border-bottom: 1px solid #757575;
}
.group .my-input:focus {
  outline: none;
}

.group label {
  color: #999;
  font-size: 1.125rem;
  position: absolute;
  pointer-events: none;
  left: 0.3125rem;
  top: 0.625rem;
  transition: 0.2s ease all;
  -moz-transition: 0.2s ease all;
  -webkit-transition: 0.2s ease all;
}
.login-btn {
  position: relative;
  width: 30vw;
  height: 3rem;
  text-align: center;
}
.additional-btn {
  font-size: 1.2rem;
  cursor: pointer;
}

/* active state */
.group .my-input:focus ~ label,
.my-input:valid ~ label {
  top: -1.25rem;
  font-size: 1.4rem;
  color: #25ab9b;
}
/* HIGHLIGHTER ================================== */
.highlight {
  position: absolute;
  height: 60%;
  width: 6.25rem;
  top: 25%;
  left: 0;
  pointer-events: none;
  opacity: 0.5;
}
/* BOTTOM BARS ================================= */
.bar {
  position: relative;
  display: block;
  width: 30vw;
}
.bar:before,
.bar:after {
  content: "";
  height: 0.125rem;
  width: 0;
  bottom: 0;
  position: absolute;
  background: #25ab9b;
  transition: 0.2s ease all;
  -moz-transition: 0.2s ease all;
  -webkit-transition: 0.2s ease all;
}
.bar:before {
  left: 50%;
}
.bar:after {
  right: 50%;
}

/* active state */
input:focus ~ .bar:before,
input:focus ~ .bar:after {
  width: 50%;
}
/* active state */
input:focus ~ .highlight {
  -webkit-animation: inputHighlighter 0.3s ease;
  -moz-animation: inputHighlighter 0.3s ease;
  animation: inputHighlighter 0.3s ease;
}

/* ANIMATIONS ================ */
@-webkit-keyframes inputHighlighter {
  from {
    background: #5264ae;
  }
  to {
    width: 0;
    background: transparent;
  }
}
@-moz-keyframes inputHighlighter {
  from {
    background: #5264ae;
  }
  to {
    width: 0;
    background: transparent;
  }
}
@keyframes inputHighlighter {
  from {
    background: #5264ae;
  }
  to {
    width: 0;
    background: transparent;
  }
}
</style>
