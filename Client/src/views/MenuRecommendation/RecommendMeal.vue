<template>
  <div>
    <BannerBar MainText="음식추천" SubText="음식추천SubText" />
    <SearchBar />
  </div>
</template>

<script>
import BannerBar from '@/components/Main/BannerBar.vue'
import SearchBar from '@/components/SearchBar.vue'

export default {
  name: 'RecommendMeal',
  components: {
    BannerBar,
    SearchBar,
  },
  methods: {

  }
}
</script>

<style>

</style>