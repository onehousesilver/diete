<template>
  <div class="rec-food-list">
    <div class="rec-text">검색결과</div>
    <div class="food-wrap">
      <div class="food-list">
        <button class="material-icons prev-btn" @click="prevPage">arrow_back</button>
        <div 
          class="food-list-el"
          v-for="(food, idx) in receivedData.slice(startIdx,endIdx)"
          :key="idx"
          :id="`${idx}`"
          @click="showModal(food)"
        >
          <img
            :src="`data:image/png;base64,${food.image}`"
            alt="음식 사진"
            class="food-image"
          />
          <div class="food-description" :id="`${idx}`">
            <!-- API에서 받아온 음식 이름 -->
            <div class="food-name">{{ food.foodName }}</div>
            <!-- API에서 받아온 음식 kcal -->
            <div class="food-kcal">{{ food.foodKcal }} kcal</div>
          </div>
        </div>
        <button class="material-icons next-btn" @click="nextPage">arrow_forward</button>
      </div>
    </div>
    <SearchResultItem :modalState="modalState" :foodData="foodData" />
  </div>
</template>

<script>
import SearchResultItem from "@/components/Search/SearchResultItem.vue";
import axios from 'axios';
export default {
  name: "SearchResult",
  props: {
    receivedData: Array,
  },
  components: {
    SearchResultItem,
  },
  data() {
    return {
      startIdx: 0,
      endIdx: 9,
      sumFoodKcal: 1500,    // 끼니 합산 칼로리
      modalState: false,   // Modal On/Off State
      foodIdx: 0,
      foodData: {},     // 모달에 전달해줄 Data
    };
  },
  methods: {
    nextPage(){
      if (this.startIdx < this.receivedData.length-9){
        this.startIdx += 9;
        this.endIdx += 9;
      }
    },
    prevPage(){
      if (this.startIdx > 8){
        this.startIdx -= 9;
        this.endIdx -= 9;
      }
    },
    showAnimation() {
      const foodListEl = document.querySelectorAll(".food-list-el");
      for (let j = 0; j < foodListEl.length; j++) {
        foodListEl[j].className += " animate__animated animate__zoomIn";
      }
    },
    goToPocket() {
      this.$router.push({ name: "pocket" }).catch(() => {});
    },
    showModal(food) {
      this.modalState = !this.modalState
      this.foodData = food
      // this.$emit('showModal', food)
    },
    // 음식정보 상세조회
    getFoodDetail(){
      axios({
        method:'get',
        url: `${process.env.VUE_APP_API_URL}/menu/`
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
  },

  computed: {
    userInfo() { return this.$store.getters.getUserInfo; },
  },
  watch: {
    // 탭을 변경하거나 다른키워드로 검색했을 때 다시 첫 인덱스부터
    receivedData() {
      this.startIdx = 0;
      this.endIdx = 9;
      window.scrollTo({top: 500, behavior: 'smooth'})
    }
  },
  mounted() {
    this.showAnimation();
  },
};
</script>

<style scoped>
.rec-food-list {
  width: 73vw;
  margin-bottom: 5vw;
  margin-left: 13vw;
}
.rec-text {
  font-size: 1.5vw;
  font-weight: 700;
  padding-top: 20px;
  padding-bottom: 10px;
  width: 10vw;
  position: relative;
  left: 0;
}

.food-wrap {
  position: relative;
  display: flex;
}

.food-wrap .food-list {
  display: flex;
  /* width: 100%; */
  flex-wrap: wrap;
  justify-content: space-around;
  gap: 10px;
}
.food-wrap .food-list .food-list-el {
  background-color: #fff;
  border: solid 3px #25ab9b;
  width: calc(70vw / 3);
  height: 16vh;
  border-radius: 10px;
  display: flex;
  align-items: center;
  position: relative;
}

.food-wrap .food-list .food-list-el .food-image {
  display: block;
  position: absolute;
  left: .5vw;
  border-radius: 10px;
  object-fit: cover;
  width: 8vw;
  height: 14vh;
}
.food-list .food-list-el .food-description {
  position: absolute;
  right: 2vw;
  text-align: center;
  width: 10vw;
}

.food-list .food-list-el .food-description .food-name {
  font-size: 1.5vw;
  font-weight: 700;
}

.food-list .food-list-el .food-description .food-kcal {
  font-size: 1vw;
  display: block;
}

.food-list .food-list-el:hover {
  cursor: pointer;
}

.prev-btn,
.next-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font-size: 3vw;
}
.prev-btn {
  left: -3vw;
}
.next-btn{
  right: -3vw;
}
</style>
