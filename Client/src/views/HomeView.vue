<template>
  <div class="home">
    <BannerPage />
    <MainDescription />
    <div id="to-top">
      <div class="material-icons" @click="toTop">arrow_upward</div>
    </div>
  </div>
</template>

<script>
import BannerPage from "@/components/Main/BannerPage.vue";
import MainDescription from "@/components/Main/LandingPage.vue";

export default {
  name: "HomeView",
  components: {
    BannerPage,
    MainDescription,
  },
  methods: {
    toTop() {
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    },
  },
};
</script>

<style scoped>
#to-top {
  width: 50px;
  height: 50px;
  background-color: #25ab9b;
  color: #fff;
  border: 2px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  bottom: 30px;
  right: 30px;
}
</style>
