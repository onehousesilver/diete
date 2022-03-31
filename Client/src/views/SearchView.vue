<template>
  <div>
    <BannerBar
      MainText="음식검색"
      SubText="diète에서 다양한 음식을 검색해보세요"
    />
    <SearchBar />
    <CategoryBar />
    <SearchList />
  </div>
</template>

<script>
import BannerBar from "../components/Main/BannerBar.vue";
import SearchList from "../components/Search/SearchList.vue";
import CategoryBar from "../components/Search/CategoryBar.vue";
import SearchBar from "../components/SearchBar.vue";
export default {
  components: {
    BannerBar,
    SearchBar,
    SearchList,
    CategoryBar,
  },
};
</script>

<style></style>
