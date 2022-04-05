<template>
  <div>
    <BannerBar
      MainText="음식추천"
      SubText="diète에서 맛있는 음식을 추천받아보세요"
    />
    <SearchBar />
    <MiniBasket />
    <div v-if="loadingState" class="loading-container">
      <img class="loading-img" src="../../assets/spinner.gif" alt="loading spinner">
      <span class="loading-text">{{userInfo.data.name}}님의 선호도를 분석 중입니다.</span>
    </div>
    <RecFoodList
      v-else 
      v-for="(data,key) in recommendedData"
      :key="key"
      :receivedData="data"
      :dataKey="key"
      @showModal="showModal"
    />
  </div>
</template>

<script>
import BannerBar from "@/components/Main/BannerBar.vue";
import axios from 'axios';
import SearchBar from "@/components/Search/SearchBar.vue";
import MiniBasket from '@/components/Basket/MiniBasket.vue'
import RecFoodList from "@/components/Recommend/RecFoodList.vue";
export default {
  name: 'RecommendMeal',
  components: {
    BannerBar,
    SearchBar,
    MiniBasket,
    RecFoodList,
  },
  data() {
    return {
      recommendedData: null,  // 추천된음식 데이터
      modalState: false,
      loadingState: true,
      test: 'test'
    }
  },
  methods: {
    // 추천식단 API 호출
    getRecommendedMeal(){
      axios({
        method: "get",
        url: `${process.env.VUE_APP_API_URL}/menu/recommendation/${this.userInfo.username}/`,
        headers: {
          Authorization: `JWT ${this.token}`
        }
      })
        .then(res => {
          this.recommendedData = res.data
          console.log(res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    showModal() {
      this.modalState = !this.modalState;
    }
  },
  computed:{
    userInfo() { return this.$store.getters.getUserInfo },
    token() { return this.$store.getters.getUserToken }
  },
  mounted() {
    this.getRecommendedMeal()
    setTimeout(() => {
      this.loadingState=false;
    }, 5000);
  }
};
</script>

<style lang="scss">
.loading-container {
  position: relative;
  width: 100vw;
  height: 50vh;
}
.loading-img{
  width: 1000px;
  position: absolute;
  left:50%;
  transform: translateX(-50%);
}
.loading-text{
  font-size: 3vw;
  position: absolute;
  top:0;
  left: 50%;
  transform: translateX(-50%);
}

</style>