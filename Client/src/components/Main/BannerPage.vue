<template>
  <div>
    <div class="banner">
      <div class="banner-head">
        <span class="di" style="color: #2bc0af">di</span>
        <span class="e" style="color: #25ab9b">è</span>
        <span class="te" style="color: #219285">te</span>
      </div>
      <div class="banner-sub-head">
        <span>개인별 맞춤형 식단과 음식을 추천해드립니다.</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.banner {
  height: 250px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-image: url("../../assets/bannerimg.png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
.banner .banner-head {
  font-size: 60px;
  font-weight: 700;
}

.banner .banner-sub-head {
  font-size: 18px;
  color: #333;
}
</style>
