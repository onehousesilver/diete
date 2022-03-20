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
              <img src="../../assets/recommend-card.svg" alt=""/>
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
              <img src="../../assets/record-card.svg" alt=""/>
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

#login {
  margin: 0 100px;
}
a {
  width: 100%;
  height: 100%;
}
.main-section-login .main-title {
  font-size: 3rem;
  font-weight: 700;
  margin-top: 1.875rem;
}
.main-section-login .main-sub-title {
  font-size: 1.5rem;
}

.card-section {
  display: flex;
  font-size: 2rem;
  justify-items: center;
  margin-top: 1.875rem;
}
.card-section span {
  display: block;
  font-size: 1rem;
  margin-left: 20px;
}
.card-section div {
  margin-left: 20px;
  margin-top: 10px;
  font-weight: 700;
}

.card-section .menu-recommend-card {
  display: flex;
  flex-direction: column;
  padding: 10px;
  margin: 5px;
  width: calc(100% / 3);
  height: 40vh;
  border: solid #25ab9b 2px;
  border-radius: 20px;
  cursor: pointer;
}
.card-section .menu-recommend-card a{
  position: relative;
}
.card-section .menu-recommend-card img{
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
  padding: 10px;
  margin: 5px;
  width: calc(100% / 3);
  height: 40vh;
  border: solid #25ab9b 2px;
  border-radius: 20px;
  cursor: pointer;
}
.card-section .menu-search-card a{
  position: relative;
}
.card-section .menu-search-card img{
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
  padding: 10px;
  margin: 5px;
  width: calc(100% / 3);
  height: 40vh;
  border: solid #25ab9b 2px;
  border-radius: 20px;
  cursor: pointer;
}
.card-section .menu-record-card a{
  position: relative;
}
.card-section .menu-record-card img{
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: 0;
  max-width: 100%;
  max-height: 75%;
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
