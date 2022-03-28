<template>
  <div>
    <BannerBar MainText="음식추천" SubText="맛있는 음식을 추천해드립니다." />
    <SearchBar />
    <RecFoodList />
  </div>
</template>

<script>
import BannerBar from "@/components/Main/BannerBar.vue";
import SearchBar from "@/components/SearchBar.vue";
import RecFoodList from "@/components/Recommend/RecFoodList.vue";

export default {
  name: "RecommendMeal",
  components: {
    BannerBar,
    SearchBar,
    RecFoodList,
  },
  data() {},
  methods: {},
};
</script>

<style></style>
