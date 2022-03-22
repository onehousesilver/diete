<template>
  <div>
    <BannerBar MainText="음추" SubText="음추받아보세연" />
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