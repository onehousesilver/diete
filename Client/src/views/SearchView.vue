<template>
  <div>
    <BannerBar
      MainText="음식검색"
      SubText="diète에서 다양한 음식을 검색해보세요"
    />
    <SearchBar @searchKeyword="onSearchKeyword" />
    <CategoryBar @changeCategory="changeCategory" />
    <div class="no-result" v-show="noResult">
      <img
        class="no-search-img"
        src="../assets/search/no_search_img.svg"
        alt=""
      />
      <div class="no-search-text">
        <span style="color: #25ab9b; font-weight: 700"
          >"{{ currentKeyword }}"</span
        >
        에 대한 검색결과가 없습니다.
      </div>
    </div>
    <img class="loading-img" src="../assets/spinner.gif" alt="loading spinner" v-show="!resultState&&loadingState">
    <SearchResult
      v-show="resultState"
      :receivedData="searchData"
      @showModal="showModal"
      @searchKeyword="onSearchKeyword"
      :onlySearch="onlySearch"
    />
    <MiniBasket v-show="!onlySearch" />
  </div>
</template>

<script>
import BannerBar from "@/components/Main/BannerBar.vue";
import SearchBar from "@/components/Search/SearchBar.vue";
import CategoryBar from "@/components/Search/CategoryBar.vue";
import SearchResult from "@/components/Search/SearchResult.vue";
import MiniBasket from "@/components/Basket/MiniBasket.vue";
import axios from "axios";

export default {
  name: "RecommendMeal",
  props: {
    keyword: String, // params로 prop 해서 온 데이터(검색 키워드)
    onlySearch: Boolean,
  },
  components: {
    BannerBar,
    SearchBar,
    CategoryBar,
    SearchResult,
    MiniBasket,
  },
  data() {
    return {
      searchResult: null, // 검색 결과(Array)
      noResult: false, // 검색결과가 없습니다 T/F
      category: "all", // 검색카테고리 (default=all)
      currentKeyword: "", // 검색키워드

      loadingState: false, // loading spinner On/Off
      resultState: false, // 검색결과 T/F
      searchData: [], // 검색결과 Data
      modalState: false, // Modal On/Off State
    };
  },
  methods: {
    onSearchKeyword(keyword) {
      this.currentKeyword = keyword;
      this.resultState=false;
      this.noResult=false;
      this.loadingState=true;
      axios({
        method: "get",
        url: `${process.env.VUE_APP_API_URL}/search/${this.category}/${keyword}/`,
      })
        .then((res) => {
          // 검색결과가 있을때 (Array의 크기가 0보다 클 때)는 검색결과를 emit, 없다면 noResult emit
          if (res.data.length) {
            this.resultState = true;
            this.searchData = res.data;
            this.noResult = false;
          } else {
            this.resultState = false;
            this.noResult = true;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // 검색결과가 없다면 검색결과가 없습니다 표시
    // 검색결과가 있다면 검색 결과 컴포넌트 표시
    showModal() {
      this.modalState = !this.modalState;
    },
    changeCategory(category) {
      this.category = category;
    },
  },
  mounted() {
    // router로 이동해서 params가 있다면 검색
    if (this.keyword) {
      this.currentKeyword = this.keyword;
      this.onSearchKeyword(this.keyword);
    } else {
      this.$swal.fire({
        icon: "question",
        title: "어떤 음식이 궁금하신가요?",
        text: "궁금한 음식을 검색해보세요",
      });
    }
  },
  watch: {
    category() {
      this.onSearchKeyword(this.currentKeyword);
    },
  },
};
</script>

<style>
.no-search-img {
  display: block;
  margin: 2vw auto;
  width: 14vw;
  height: 14vw;
}
.no-search-text {
  font-size: 2vw;
  text-align: center;
}
.loading-img {
  width: 30vw;
  position: relative;
  left: 50%;
  transform: translateX(-50%);
}
</style>
