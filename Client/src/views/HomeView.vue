<template>
  <div class="home">
    <BannerBar />
    <MainDescription />
  </div>
</template>

<script>
import BannerBar from "@/components/Main/BannerBar.vue";
import MainDescription from "@/components/Main/LandingPage.vue";

export default {
  name: "HomeView",
  components: {
    BannerBar,
    MainDescription,
  },
};
</script>

<style></style>
