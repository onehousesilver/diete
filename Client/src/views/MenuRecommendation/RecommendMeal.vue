<template>
  <div>
    <BannerBar
      MainText="음식추천"
      SubText="diète에서 맛있는 음식을 추천받아보세요"
    />
    <SearchBar />
    <MiniBasket />
    <div v-if="loadingState" class="loading-container">
      <img
        class="loading-img"
        src="../../assets/main_logout/main_landing.gif"
        alt="loading spinner"
      />
      <span class="loading-text">{{ loadingText }}</span>
    </div>
    <RecFoodList
      v-else
      v-for="(data, key) in recommendedData"
      :key="key"
      :receivedData="data"
      :dataKey="key"
      @showModal="showModal"
    />
  </div>
</template>

<script>
import BannerBar from "@/components/Main/BannerBar.vue";
import axios from "axios";
import SearchBar from "@/components/Search/SearchBar.vue";
import MiniBasket from "@/components/Basket/MiniBasket.vue";
import RecFoodList from "@/components/Recommend/RecFoodList.vue";
export default {
  name: "RecommendMeal",
  components: {
    BannerBar,
    SearchBar,
    MiniBasket,
    RecFoodList,
  },
  data() {
    return {
      recommendedData: null, // 추천된음식 데이터
      modalState: false,
      loadingState: true,
      test: "test",
      loadingText: ``,
    };
  },
  methods: {
    // 추천식단 API 호출
    getRecommendedMeal() {
      axios({
        method: "get",
        url: `${process.env.VUE_APP_API_URL}/menu/recommendation/${this.userInfo.username}/`,
        headers: {
          Authorization: `JWT ${this.token}`,
        },
      })
        .then((res) => {
          this.recommendedData = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    showModal() {
      this.modalState = !this.modalState;
    },
  },
  computed: {
    userInfo() {
      return this.$store.getters.getUserInfo;
    },
    token() {
      return this.$store.getters.getUserToken;
    },
  },
  mounted() {
    this.getRecommendedMeal();
    this.loadingText = `${this.userInfo.data.name}님에게 추천할 음식을 요리하고있어요`;
    let loading = setInterval(() => {
      this.loadingText += ".";
    }, 1300);
    setTimeout(() => {
      this.loadingState = false;
      clearTimeout(loading);
      this.$swal.fire({
        title: "장바구니를 이용해보세요!",
        text: "장바구니에 담아 실시간 칼로리를 확인해보세요",
        imageUrl: require("../../assets/alert_basket.gif"),
        imageWidth: 800,
        imageHeight: 400,
        width: 850,
        imageAlt: "basket gif",
      });
    }, 3800);
  },
  // alert 추가
};
</script>

<style lang="scss">
.loading-container {
  position: relative;
  width: 100vw;
  height: 50vh;
}
.loading-img {
  width: 40vw;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}
.loading-text {
  font-size: 2vw;
  position: absolute;
  font-weight: 700;
  top: 2vw;
  left: 50%;
  transform: translateX(-50%);
}
/* .swal2-popup {
  width: 35vw;
} */
</style>
