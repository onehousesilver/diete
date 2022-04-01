<template>
  <div id="rec-food-list">
    <div class="search-text">
      <span style="color: #219285">"{{ keyword }}"</span> 검색 결과
    </div>
    <div v-show="!isTrue" class="food-wrap">
      <div v-for="idx in foodList.length" :key="idx" class="food-list">
        <div
          v-for="(food, idx) in foodList"
          :key="idx"
          class="food-list-el"
          :id="`${idx}`"
          @click="showModal"
        >
          <img
            src="../../assets/menu_rec/food_example_img.jpg"
            alt="음식예시사진"
          />
          <div class="food-description">
            <!-- API에서 받아온 음식 이름 -->
            <div class="food-name">{{ food.foodName }}</div>
            <!-- API에서 받아온 음식 kcal -->
            <div class="food-kcal">{{ food.foodKcal }} kcal</div>
          </div>
        </div>
      </div>
      <SearchModal :test="myState" :foodData="foodList[`${tempidx}`]" />
    </div>
    <div v-show="isTrue">
      <img
        class="no-search-img"
        src="../../assets/search/no_search_img.svg"
        alt=""
      />
      <div class="no-search-text">검색 결과가 없습니다.</div>
    </div>
  </div>
</template>

<script>
import SearchModal from "./searchModal.vue";
export default {
  components: { SearchModal },
  name: "SearchList",
  props: {
    search: String,
  },
  data() {
    return {
      foodList: [
        { foodName: "소고기무국", foodKcal: 1000 },
        { foodName: "보쌈", foodKcal: 3000 },
        { foodName: "족발", foodKcal: 2000 },
      ],
      sumFoodKcal: 1500,
      current: true,
      myState: false,
      tempidx: 0,
      userName: "한채은",
      keyword: "소고기무국",
      isTrue: false,
    };
  },
  methods: {
    showAnimation() {
      const foodListEl = document.querySelectorAll(".food-list-el");
      for (let j = 0; j < foodListEl.length; j++) {
        foodListEl[j].className += " animate__animated animate__zoomIn";
      }
    },
    goToPocket() {
      this.$router.push({ name: "pocket" }).catch(() => {});
    },
    showModal(e) {
      this.myState = !this.myState;
      console.log(e);
      this.tempidx = e.target.offsetParent.id;
      // console.log(this.$refs.modal0);
      // this.$refs.modal.open("main-modal");
      // this.$refs.modal.open("main-modal1");
      // console.log(this.$refs.modal);
      // this.current = !this.current;
    },
  },

  // computed: {
  //   userInfo() {
  //     return this.$store.getters.getUserInfo;
  //   },
  // },

  mounted() {
    this.showAnimation();
  },
};
</script>

<style scoped>
img {
  display: block;
  margin: 0.4vw 0.8vw;
  border-radius: 10px;
  width: 11vw;
  height: 14vh;
}
#rec-food-list {
  width: 73vw;
  margin: 0 auto;
}
.search-text {
  font-size: 1vw;
  font-weight: 700;
  position: relative;
  bottom: 1.3vw;
}

.food-wrap {
  position: relative;
  display: flex;
  justify-content: center;
}

.food-wrap .food-list .food-list-el {
  background-color: #fff;
  border: solid 3px #25ab9b;
  width: 24vw;
  height: 16vh;
  margin: 0.4vw;
  border-radius: 10px;
  display: flex;
}

.food-list .food-list-el .food-description {
  text-align: center;
  width: 100%;
  align-self: center;
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

.no-search-img {
  width: 13.7vw;
  height: 27vh;
  margin: 0 auto;
}

.no-search-text {
  text-align: center;
  font-size: 1.6vw;
  margin-top: 1.6vw;
  font-weight: 700;
}
</style>
