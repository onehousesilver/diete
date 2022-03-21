<template>
  <div>
    <div class="banner">
      <div class="banner-head">
        <div v-if="!MainText" class="default-text">
          <span class="di" style="color: #2bc0af">di</span>
          <span class="e" style="color: #25ab9b">è</span>
          <span class="te" style="color: #219285">te</span>
          <div class="banner-sub-head">
            <span>개인별 맞춤형 식단과 음식을 추천해드립니다.</span>
          </div>
        </div>
        <div v-else class="present-text">
          {{ MainText }}
          <div class="banner-sub-head">
            <span>{{ SubText }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    MainText: String,
    SubText: String,
  },
};
</script>

<style>
.banner {
  height: 20vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-image: url("../../assets/banner.png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
.banner .banner-head {
  text-align: center;
  font-size: 3vw;
  font-weight: 700;
}

.banner .banner-sub-head {
  font-size: 1.2vw;
  color: #333;
}
</style>
