<template>
  <div>
    <BannerBar MainText="음식검색" SubText="diète에서 다양한 음식을 검색해보세요"/>
    <SearchBar 
      @searchKeyword="onSearchKeyword"
    />
    <CategoryBar
      @changeCategory="changeCategory"
    />
    <div class="no-result" v-show="noResult">
      검색결과가 없습니다.
    </div>
    <!-- <RecFoodList /> -->
    <SearchResult 
      v-show="resultState"
      :receivedData="searchData"
      @showModal="showModal"
    />
    <SearchResultItem :modalState="modalState" :foodData="foodData" />
    <MiniBasket />
  </div>
</template>

<script>
import BannerBar from "@/components/Main/BannerBar.vue";
import SearchBar from "@/components/Search/SearchBar.vue";
import CategoryBar from '@/components/Search/CategoryBar.vue'
import SearchResult from "@/components/Search/SearchResult.vue";
import SearchResultItem from "@/components/Search/SearchResultItem.vue";
import MiniBasket from "@/components/Basket/MiniBasket.vue";
import axios from 'axios';

export default {
  name: "RecommendMeal",
  props: {
    keyword: String, // params로 prop 해서 온 데이터(검색 키워드)
  },
  components: {
    BannerBar,
    SearchBar,
    CategoryBar,
    SearchResult,
    SearchResultItem,
    MiniBasket,
  },
  data() {
    return {
      searchResult: null,   // 검색 결과(Array)
      noResult: false,    // 검색결과가 없습니다 T/F
      category: 'all',    // 검색카테고리 (default=all)
      currentKeyword: '',

      resultState: false, // 검색결과 T/F
      searchData : [],  // 검색결과 Data
      modalState: false,   // Modal On/Off State
      foodData: {
        foodName: '',
        foodKcal: 0,
        servingSize: 0,
        image: '',
        carbohydrate: 0,
        protein: 0,
        fat: 0,
        sugar: 0,
        fattyAcid: 0,
      },
    }
  },
  methods: {
    onSearchKeyword(keyword){
      this.currentKeyword = keyword
      axios({
        method: 'get',
        url: `${process.env.VUE_APP_API_URL}/search/${this.category}/${keyword}/`
      })
        .then(res => {
          // 검색결과가 있을때 (Array의 크기가 0보다 클 때)는 검색결과를 emit, 없다면 noResult emit
          if(res.data.length){
            this.resultState = true;
            this.searchData = res.data;
            this.noResult = false;
          }
          else {
            this.resultState = false;
            this.noResult = true;
          }
        })
        .catch(err => { console.log(err) })
    },
    // 검색결과가 없다면 검색결과가 없습니다 표시
    // 검색결과가 있다면 검색 결과 컴포넌트 표시
    showModal(food){
      this.foodData = food
      this.modalState = !this.modalState
    },
    changeCategory(category){
      this.category = category
    }
  },
  mounted(){
    // router로 이동해서 params가 있다면 검색
    if(this.keyword){
      this.currentKeyword = this.keyword
      this.onSearchKeyword(this.keyword)
    }
  },
  watch: {
    category() {
      this.onSearchKeyword(this.currentKeyword)
    }
  }
};
</script>

<style>
.no-result {
  font-size: 3vw;
  position: relative;
  width: 100%;
  line-height: 30vh;
  height: 30vh;
  text-align: center;
  z-index: 3;
}
</style>
