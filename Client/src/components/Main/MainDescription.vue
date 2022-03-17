<template>
  <div>
    <div id="logout" v-if="!isLogin">
      <div class="main-section-logout"><div>로그아웃</div></div>
    </div>
    <div id="login" v-else>
      <div class="main-section-login">
        <div class="main-title">건강한 하루의 시작</div>
        <div class="main-sub-title">오늘 하루도 건강하게 시작해보세요!</div>
        <div class="card-section">
          <div class="menu-recommend-card">
            <router-link :to="{ name: 'menu' }">
              <div>음식추천</div>
              <span>나에게 꼭 맞는 식단을 추천해드립니다.</span>
              <!-- <img src="../../assets/recommend-card.svg" alt=""/> -->
            </router-link>
          </div>

          <div class="menu-search-card">
            <router-link :to="{ name: 'search' }">
              <div>음식검색</div>
              <span>어떤 음식이든 검색해보세요!</span>
              <!-- <img src="../../assets/search-card.svg" alt="" /> -->
            </router-link>
          </div>

          <div class="menu-record-card">
            <router-link :to="{ name: 'record' }">
              <div>나의기록</div>
              <span>내 기록을 남겨보세요.</span>
              <!-- <img src="../../assets/record-card.svg" alt=""/> -->
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MainDescription",
  data: function () {
    return {
      isLogin: true,
    };
  },
};
</script>

<style scoped>
/* @media screen and (max-width: 1350px) {
  .main-section-login .main-title,
  .main-section-login .main-sub-title {
    display: flex;
    justify-content: center;
  }
  .card-section {
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .card-section .menu-recommend-card {
    height: 400px;
  }
} */

#login {
  margin: 0 100px;
}
a {
  width: 100%;
  height: 100%;
}
.main-section-login .main-title {
  font-size: 30px;
  font-weight: 700;
  margin-top: 30px;
}
.main-section-login .main-sub-title {
  font-size: 20px;
  margin-bottom: 20px;
}

.card-section {
  display: flex;
  font-size: 30px;
  justify-items: center;
}
.card-section span {
  display: block;
  font-size: 14px;
  margin-left: 20px;
}
.card-section div {
  margin-left: 20px;
  margin-top: 10px;
  font-weight: 700;
}

/* .card-section .menu-recommend-card,
.card-section .menu-search-card,
.card-section .menu-record-card {
  display: flex;
  flex-direction: column;
  padding: 10px;
  margin: 5px;
  width: calc(100% / 3);
  border: solid #25ab9b 2px;
  border-radius: 20px;
  cursor: pointer;
} */

.card-section .menu-recommend-card {
  display: flex;
  flex-direction: column;
  padding: 10px;
  margin: 5px;
  width: calc(100% / 3);
  border: solid #25ab9b 2px;
  border-radius: 20px;
  cursor: pointer;
  background-size: 75%;
  background-position-x: 100%;
  background-position-y: 80%;
  background-repeat: no-repeat;
  background-image: url("../../assets/recommend-card.svg");
}
.card-section .menu-search-card {
  display: flex;
  flex-direction: column;
  padding: 10px;
  margin: 5px;
  width: calc(100% / 3);
  height: 400px;
  border: solid #25ab9b 2px;
  border-radius: 20px;
  cursor: pointer;
  background-size: 60%;
  background-position-x: 100%;
  background-position-y: 80%;
  background-repeat: no-repeat;
  background-image: url("../../assets/search-card.svg");
}
.card-section .menu-record-card {
  display: flex;
  flex-direction: column;
  padding: 10px;
  margin: 5px;
  width: calc(100% / 3);
  height: 400px;
  border: solid #25ab9b 2px;
  border-radius: 20px;
  cursor: pointer;
  background-size: 60%;
  background-position-x: 100%;
  background-position-y: 80%;
  background-repeat: no-repeat;
  background-image: url("../../assets/record-card.svg");
}

/* .card-section .menu-recommend-card img {
  display: block;
  margin: 20px auto;
  width: 100%;
}

.card-section .menu-search-card img {
  display: inline-block;
  margin-top: 30px;
  width: 100%;
}

.card-section .menu-record-card img {
  display: inline-block;
  width: 100%;
} */
</style>
