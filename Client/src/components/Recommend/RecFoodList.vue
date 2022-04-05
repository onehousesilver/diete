<template>
  <div class="rec-food-list">
    <div class="rec-text">{{ description }}</div>
    <div class="food-wrap">
      <div class="food-list">
        <button class="material-icons prev-btn" @click="prevPage">
          arrow_back
        </button>
        <div
          class="food-list-el"
          v-for="(food, idx) in receivedData.data.slice(startIdx, endIdx)"
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
            <!-- API에서 받아온 음식 kcal -->
            <div class="food-name">{{ food.foodName }}</div>
            <div class="food-kcal">{{ food.foodKcal }} kcal</div>
          </div>
        </div>
        <button class="material-icons next-btn" @click="nextPage">
          arrow_forward
        </button>
      </div>
    </div>
    <FoodModal :modalState="modalState" :foodData="foodData" />
  </div>
</template>

<script>
import FoodModal from "@/components/Recommend/FoodModal.vue";
import axios from "axios";
export default {
  name: "SearchResult",
  props: {
    receivedData: Object,
    onlySearch: Boolean,
    dataKey: String,
  },
  components: {
    FoodModal,
  },
  data() {
    return {
      foodIdx: 0,
      startIdx: 0,
      endIdx: 3,
      modalState: false, // Modal On/Off State
      foodData: {}, // 모달에 전달해줄 Data
      description: "",
    };
  },
  methods: {
    nextPage() {
      if (this.startIdx < this.receivedData.data.length - 3) {
        this.startIdx += 3;
        this.endIdx += 3;
      }
    },
    prevPage() {
      if (this.startIdx > 0) {
        this.startIdx -= 3;
        this.endIdx -= 3;
      }
    },
    showModal(food) {
      this.modalState = !this.modalState;
      this.foodData = food;
    },
    // 음식정보 상세조회
    getFoodDetail() {
      axios({
        method: "get",
        url: `${process.env.VUE_APP_API_URL}/menu/`,
      })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    //
    textInit() {
      Math.random();
      switch (this.dataKey) {
        case "all":
          this.description = `${this.userInfo.data.name}님이 가장 좋아하실 만한 음식이에요.`;
          break;
        case "oily":
          this.description = `포만감 한 가득, 먹어도 먹어도 배고픈 당신을 위해 준비했어요.`;
          break;
        case "meat":
          this.description = `단백질 가득 고기, 든든하고 풍성한 한끼를 만들어 보세요`;
          break;
        case "seafood":
          this.description = `영양만점 해산물, 내일 아침에는 고소한 생선 구이 어떠세요?`;
          this.description = `바다 향이 가득한 해조류, 영양 풍부하고 맛 좋은 해조류로 차리는 한 상`;
          break;
        case "vegetable":
          this.description = `건강한 자연 식물식, 가공 식품을 최소화한 식단`;
          break;
        case "spicy":
          this.description = `날씨가 추워지면 생각나는, 얼큰한 음식`;
          this.description = `얼큰하게 즐기는 매운 음식, 스트레스를 풀어보세요`;
          break;
        default:
          break;
      }
    },
  },

  computed: {
    userInfo() {
      return this.$store.getters.getUserInfo;
    },
  },
  watch: {
    // 탭을 변경하거나 다른키워드로 검색했을 때 다시 첫 인덱스부터
    receivedData() {
      this.startIdx = 0;
      this.endIdx = 3;
      this.textInit();
    },
  },
  mounted() {
    this.textInit();
  },
};
</script>

<style>
.rec-food-list {
  width: 73vw;
  height: 8vw;
  margin-top: 1vw;
  margin-bottom: 5vw;
  margin-left: 13vw;
}
.rec-text {
  font-size: 1.3vw;
  font-weight: 700;
  padding-top: 20px;
  padding-bottom: 10px;
  width: 50vw;
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
  left: 0.5vw;
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
.modal-bottom-img {
  width: 300px;
}
.prev-btn,
.next-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font-size: 2vw;
  color: #25ab9b;

  background-color: rgb(221, 221, 221);
  border-radius: 50%;
}
.prev-btn:hover,
.next-btn:hover {
  transform: translateY(-50%) scale(1.2);
  transition: transform 0.1s;
}
.prev-btn {
  left: -3vw;
}
.next-btn {
  right: -3vw;
}
.sweet-modal {
  max-width: 60vw;
  overflow-x: hidden;
}

.food-modal-text {
  font-weight: 700;
  align-self: center;
}
.food-modal-name {
  font-size: 1.6vw;
}
.food-modal-kcal {
  font-size: 1.4vw;
}
.food-modal-g {
  font-size: 1.2vw;
}

.modal-img {
  width: 12vw;
  height: 23vh;
  border-radius: 10px;
}
.modal-bottom-img {
  width: 10vw;
  height: 10vw;
  border-radius: 10px;
}
#my-chart {
  width: 30vw;
}

.pocket-btn {
  width: 10vw;
  height: 2vw;
  font-size: 1vw;
  display: block;
  border-radius: 0.5vw;
  left: 84%;
  top: 1vw;
}

.food-modal-header {
  display: flex;
  justify-content: space-evenly;
}
.food-set {
  width: 31vw;
  display: flex;
  justify-content: space-around;
  align-self: center;
}
.food-modal-text {
  font-weight: 700;
  align-self: center;
}

#chart {
  width: 25vw;
}
.food-modal-bottom {
  padding: 0.78vw;
  position: relative;
  top: 1.2vw;
  width: 100%;
}
.food-modal-bottom .swiper-wrapper {
  display: flex;
  justify-content: center;
  height: 15.42vh;
}

.food-modal-bottom-text {
  font-size: 1vw;
  font-weight: 700;
  text-align: left;
  position: relative;
  left: 2.1vw;
  margin-bottom: 10px;
}
.modal-bottom-img {
  width: 7.8vw;
  height: 15.42vh;
  margin: 10px;
  border-radius: 10px;
}
.modal-bottom-img:hover {
  cursor: pointer;
}
.sub-food-name {
  font-size: 0.9vw;
}

.recswiper {
  width: 50vw;
}
.swiper-prev,
.swiper-next {
  width: 1.6vw;
  height: 3.23vh;
  outline: none;
  border: 3px solid #ffffff;
  background-color: rgb(0, 0, 0);
  border-radius: 50%;
  color: #ffffff;
  position: absolute;
  top: 0;
  bottom: 0;
  margin: auto;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: 0.4s;
}

.swiper-next {
  right: 2.1vw;
}
.swiper-prev:hover,
.swiper-next:hover {
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
}
.swiper-container {
  overflow: visible;
}
.swiper-slide {
  opacity: 0.4;
  transition: opacity 0.3s;
}
.swiper-slide-active,
.swiper-slide-active + .swiper-slide,
.swiper-slide-active + .swiper-slide + .swiper-slide,
.swiper-slide-active + .swiper-slide + .swiper-slide + .swiper-slide {
  opacity: 1;
}
.modal-bottom-img:hover {
  filter: brightness(40%);
}
.submenu {
  position: relative;
}
.modal-bottom-img-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  opacity: 0;
  z-index: -1;
  color: #eee;
  cursor: pointer;
}
.modal-bottom-img:hover + .modal-bottom-img-text {
  opacity: 1;
  z-index: 1;
  cursor: pointer;
}
.read-more {
  position: absolute;
  top: 8vh;
  margin-left: 4.3vw;
  z-index: 1;
  color: #fff;
  font-size: 0.7vw;
}
</style>
