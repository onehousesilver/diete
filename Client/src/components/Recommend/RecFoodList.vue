<template>
  <div id="rec-food-list">
    <div v-if="userName" class="rec-text">
      {{ userName }}님을 위한 음식 추천
    </div>
    <div class="food-wrap">
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
      <FoodModal :test="myState" :foodData="foodList[`${tempidx}`]" />
      <div class="mini-pocket animate__animated animate__fadeInRight">
        <div>
          <!-- 내 칼로리보다 10%이상 높을 경우빨간색 
          낮을경우 파란색, +- 10%까지는 봐주기 -->
          <!-- 전체 더한 kcal -->
          <div class="mini-pocket-kcal">{{ sumFoodKcal }} kcal</div>
          <button
            class="bttn-unite bttn-md bttn-success done-btn"
            @click="goToPocket"
          >
            선택완료
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import FoodModal from "./FoodModal.vue";
export default {
  components: { FoodModal },
  name: "RecFoodList",
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
  margin: 10px 20px;
  border-radius: 10px;
}
#rec-food-list {
  width: 73vw;
  margin: 0 auto;
}
.rec-text {
  font-size: 1vw;
  font-weight: 700;
  position: relative;
  bottom: 1.3vw;
  left: 10px;
}

.food-wrap {
  position: relative;
  display: flex;
  justify-content: center;
}

.food-wrap .food-list .food-list-el {
  background-color: #fff;
  border: solid 3px #25ab9b;
  width: 20vw;
  height: 16vh;
  margin: 10px;
  border-radius: 10px;
  display: flex;
}

.food-list .food-list-el .food-description {
  text-align: center;
  width: 100%;
  align-self: center;
}

.food-list .food-list-el .food-description .food-name {
  font-size: 30px;
  font-weight: 700;
}

.food-list .food-list-el .food-description .food-kcal {
  font-size: 20px;
  display: block;
}

.food-list .food-list-el:hover {
  cursor: pointer;
}

.mini-pocket {
  width: 10vw;
  border: solid 3px #25ab9b;
  border-radius: 10px;
  margin: 10px;
  display: flex;
  flex-direction: column;
  overflow: auto;
}
.mini-pocket .mini-pocket-kcal {
  font-size: 20px;
  text-align: center;
  display: block;
  margin: 20px;
}
.mini-pocket .done-btn {
  width: 7vw;
  height: 3.5vh;
  font-size: 0.8vw;
  position: relative;
  display: block;
  border-radius: 10px;
  margin: 0.8vw auto;
}
</style>
