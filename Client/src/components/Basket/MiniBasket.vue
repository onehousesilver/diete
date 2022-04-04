<template>
  <div>
    <div class="mini-basket-form" @click="test">
      <span class="material-icons basket-btn">shopping_cart</span>
    </div>
    <div class="basket-list">
      <div class="basket-title">오늘의 {{ mealTime }} 메뉴</div>
      <div class="food-list-area">
        <div v-for="(food, idx) in menus" :key="idx">
          <div class="basket-food">
            <div class="basket-food-name">
              {{ food.foodName }}
            </div>
            <div class="basket-kcal">
              <div class="basket-food-kcal">
                {{ food.foodKcal }}kcal
                <span
                  class="material-icons cancel-btn"
                  @click="deleteMenu(idx)"
                >
                  close
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="test">
        <div class="basket-totalkcal">
          <div>{{ totalKcal }}kcal</div>
        </div>
        <button
          class="bttn-unite bttn-md bttn-success done-btn"
          @click="goToBasketPage"
        >
          장바구니로 이동
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import $ from "jquery";
import { mapActions } from "vuex";
export default {
  data() {
    return {
      totalKcal: 0, // 합산칼로리
      basketState: false, // 장바구니 On/Off
    };
  },
  methods: {
    ...mapActions(["menusUpdate"]),
    // 메뉴 삭제
    deleteMenu(idx) {
      // 현 컴포넌트의 배열에서 idx위치에 있는 값 삭제
      this.menus.splice(idx, 1);
      // 전역변수에 있는 배열 업데이트
      this.menusUpdate(this.menus);
    },
    goToBasketPage() {
      this.$swal
        .fire({
          title: "장바구니로 이동하시겠습니까?",
          text: "맛있는 한끼를 만드셨나요?",
          icon: "question",
          showCancelButton: true,
          confirmButtonColor: "#25ab9b",
          cancelButtonColor: "#ff484a",
          confirmButtonText: "네",
          cancelButtonText: "아니요",
        })
        .then((result) => {
          if (result.isConfirmed) {
            this.$swal.fire(
              "장바구니로 이동합니다",
              "장바구니에서 식단을 저장해주세요!",
              "success"
            );
            this.$router.push({ name: "basket" });
          }
        });
    },
    test() {
      if (this.basketState) {
        $(".basket-list").removeClass("selected");
      } else {
        $(".basket-list").addClass("selected");
      }
      this.basketState = !this.basketState;
      console.log(this.mealTime);
    },
  },
  computed: {
    // 장바구니 목록
    menus() {
      return this.$store.state.menus;
    },
    // 선택한 끼니
    mealTime() {
      switch (this.$store.state.mealTime) {
        case 0:
          return "아침";
        case 1:
          return "점심";
        case 2:
          return "저녁";
        default:
          return 0;
      }
    },
  },
  mounted() {
    if (this.menus) {
      this.menus.forEach((menu) => {
        this.totalKcal += parseFloat(menu.foodKcal);
      });
    }
  },
  watch: {
    // 메뉴의 총 칼로리 합산
    menus() {
      this.totalKcal = 0;
      if (this.menus) {
        this.menus.forEach((menu) => {
          this.totalKcal += parseFloat(menu.foodKcal);
        });
      }
    },
  },
};
</script>

<style scoped>
.mini-basket-form {
  position: fixed;
  width: 5vw;
  height: 5vw;
  right: 0;
  font-size: 3vw;
  top: 45%;
  background-color: #25ab9b;
  border-radius: 50% 0 0 50%;
  cursor: pointer;
}
.food-list-area {
  height: 15vw;
  overflow-y: auto;
  overflow-x: hidden;
}
.basket-btn {
  color: #fff;
  position: fixed;
  right: 0;
  font-size: 2vw;
  top: 45%;
  cursor: pointer;
  margin-top: 1.5vw;
  margin-right: 1vw;
}

.basket-list {
  border: 3px solid #25ab9b;
  border-radius: 10px;
  width: 3vw;
  height: 3vw;
  position: fixed;
  right: 0;
  top: 50%;
  background: #fff;
  color: #fff;
  opacity: 0;
  transition-property: right, opacity, top, width, height, z-index, color; /* 어떤 css 프로퍼티를 transition할지 지정 */
  transition-duration: 1s;
  z-index: -1;
}
.basket-list.selected {
  right: 4.5vw;
  width: 15vw;
  top: 20vw;
  opacity: 1;
  height: 50vh;
  z-index: 1;
  color: #111;
  padding: 1vw;
}
.basket-list .basket-title {
  font-size: 1.2vw;
  text-align: center;
  font-weight: 700;
  margin-bottom: 1vw;
}

.basket-list .basket-food {
  display: grid;
  grid-template-columns: 10fr 3fr;
  width: 13vw;
  padding-bottom: 1vh;
  text-align: center;
  align-items: center;
}
.basket-list .basket-food .basket-food-name {
  font-size: 1vw;
  top: 1vw;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.basket-list .basket-food .basket-food-kcal {
  font-size: 0.8vw;
  align-items: center;
}
.basket-list .cancel-btn {
  cursor: pointer;
  color: #25ab9b;
}
.basket-list .basket-totalkcal {
  text-align: center;
  font-size: 1.5vw;
  position: absolute;
  bottom: 5vh;
  left: 50%;
  transform: translateX(-50%);
}
.basket-list .done-btn {
  position: absolute;
  width: 10vw;
  border-radius: 0.4vw;
  font-size: 1vw;

  bottom: 1vh;
  left: 50%;
  transform: translateX(-50%);
}
.basket-food .basket-kcal {
  padding-right: 1vw;
  width: 7vw;
}
@keyframes basketani {
  0% {
    /* transform: ; */
  }
  /* 25% {
    transform: translateX(-100px);
  }
  50% {
    transform: translateX(200px);
  } */
  100% {
    opacity: 0;
  }
}
@keyframes box-ani {
  from {
    transform: translate(0, 0);
  }
  to {
    transform: translate(100px, 100px);
  }
}
</style>
