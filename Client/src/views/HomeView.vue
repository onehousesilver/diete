<template>
  <div class="home">
    <BannerPage />
    <MainDescription/>
  </div>
</template>

<script>
import BannerPage from "@/components/Main/BannerPage.vue";
import MainDescription from '@/components/Main/MainDescription.vue';

export default {
  name: "HomeView",
  components: {
    BannerPage,
    MainDescription,
  },
};
</script>

<style scoped></style>
