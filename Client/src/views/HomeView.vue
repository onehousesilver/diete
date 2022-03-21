<template>
  <div class="home">
    <BannerPage />
    <MainDescription />
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
};
</script>

<style></style>
