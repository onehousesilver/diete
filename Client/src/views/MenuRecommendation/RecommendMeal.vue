<template>
  <div>
    <BannerBar
      MainText="음식추천"
      SubText="맛있는 음식을 추천해드립니다."
    />
    <SearchBar />
    <button @click="test">asfddasfasdf</button>
    <!-- <CategoryBar/>
    <SearchList /> -->
  </div>
</template>

<script>
import BannerBar from "@/components/Main/BannerBar.vue";
import axios from 'axios';
import SearchBar from "@/components/Search/SearchBar.vue";
// import SearchList from "@/components/Search/SearchList.vue";
// import CategoryBar from "@/components/Search/CategoryBar.vue";
export default {
  name: 'RecommendMeal',
  components: {
    BannerBar,
    SearchBar,
    // SearchList,
    // CategoryBar,
  },
  data() {
    return {
      recommendedData: null,  // 추천된음식 데이터
    }
  },
  methods: {
    test(){
      axios({
        method: "get",
        url: `${process.env.VUE_APP_API_URL}/menu/recommendation/${this.userInfo.username}/`,
        headers: {
          Authorization: `JWT ${this.token}`
        }
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  computed:{
    userInfo() { return this.$store.getters.getUserInfo },
    token() { return this.$store.getters.getUserToken }
  }
};
</script>

<style>
</style>