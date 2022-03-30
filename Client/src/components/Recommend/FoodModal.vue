<template>
  <div>
    <sweet-modal id="main-modal" ref="modal">
      <div class="modal">
        <section class="food-modal-header">
          <img
            src="../../assets/menu_rec/food_example_img.jpg"
            alt="음식예시사진"
            class="modal-img"
          />
          <div class="food-modal-text">
            <div class="food-modal-name">{{ foodData.foodName }}</div>
            <div class="food-modal-kcal">{{ foodData.foodKcal }}kcal</div>
            <div class="food-modal-g">1회제공량: 400g</div>
          </div>
          <div id="chart">
            <ApexChart
              type="bar"
              height="300"
              :options="chartOptions"
              :series="series"
            ></ApexChart>
          </div>
        </section>

        <section class="food-modal-bottom" @click="selectFood">
          <div class="inner">
            <div class="food-modal-bottom-text">이런 음식은 어때요?</div>

            <swiper ref="mySwiper" :options="swiperOptions" class="my-swiper">
              <swiper-slide>
                <img
                  src="../../assets/menu_rec/food_example_img.jpg"
                  alt="음식예시사진"
                  class="modal-bottom-img"
                />
              </swiper-slide>
              <swiper-slide>
                <img
                  src="../../assets/menu_rec/food_example_img.jpg"
                  alt="음식예시사진"
                  class="modal-bottom-img"
                />
              </swiper-slide>
              <swiper-slide>
                <img
                  src="../../assets/menu_rec/food_example_img.jpg"
                  alt="음식예시사진"
                  class="modal-bottom-img"
                />
              </swiper-slide>
              <swiper-slide>
                <img
                  src="../../assets/menu_rec/food_example_img.jpg"
                  alt="음식예시사진"
                  class="modal-bottom-img"
                />
              </swiper-slide>
              <swiper-slide>
                <img
                  src="../../assets/menu_rec/food_example_img2.png"
                  alt="음식예시사진"
                  class="modal-bottom-img"
                />
              </swiper-slide>
            </swiper>
            <div class="swiper-prev">
              <span class="material-icons">arrow_back</span>
            </div>
            <div class="swiper-next">
              <span class="material-icons">arrow_forward</span>
            </div>
            <button
              class="bttn-unite bttn-md bttn-success pocket-btn"
              @click="goToPocket"
            >
              장바구니에 담기
            </button>
          </div>
        </section>
      </div>
    </sweet-modal>
  </div>
</template>

<script>
// import swiper from "../../js/swiper";
export default {
  name: "FoodModal",
  props: {
    test: Boolean,
    foodData: Object,
  },
  data() {
    return {
      // swiper
      swiperOptions: {
        loop: true,
        observer: true,
        observeParents: true,
        slidesPerView: 4,
        spaceBetween: 30,
        setWrapperSize: true,
        navigation: {
          prevEl: ".swiper-prev",
          nextEl: ".swiper-next",
        },
      },
      // Aepxchart,
      series: [
        {
          data: [400, 430, 448, 470, 540, 580],
        },
      ],
      chartOptions: {
        chart: {
          type: "bar",
          height: 350,
          width: 400,
        },
        plotOptions: {
          bar: {
            borderRadius: 4,
            horizontal: true,
            dataLabels: {
              position: "top",
            },
          },
        },
        dataLabels: {
          enabled: true,
          offsetX: -6,
          style: {
            fontSize: "12px",
            colors: ["#fff"],
          },
        },
        xaxis: {
          categories: [
            "탄수화물",
            "단백질",
            "지방",
            "당류",
            "총 포화지방산",
            "콜레스테롤",
          ],
        },
      },
      selectFlag: false,
    };
  },
  methods: {
    showModal() {
      this.$refs.modal.open("main-modal");
    },
    goToPocket() {
      this.$refs.modal.close("main-modal");
    },
    selectFood() {
      const subRecommendFood = document.querySelectorAll(".modal-bottom-img");
      if (this.selectFlag == true) {
        this.selectFlag = false;
        for (let i = 0; i < subRecommendFood.length; i++) {
          subRecommendFood[i].classList.remove("clicked");
        }
      } else {
        this.selectFlag = true;
        for (let i = 0; i < subRecommendFood.length; i++) {
          subRecommendFood[i].classList.add("clicked");
        }
      }
    },
  },
  watch: {
    test() {
      console.log(this.test);
      this.showModal();
    },
  },
  mounted() {
    this.showSwiper();
  },
};
</script>

<style>
.modal-img {
  width: 300px;
  border-radius: 10px;
}
.food-modal-bottom {
  padding: 20px;
  position: relative;
  top: 30px;
  width: 100%;
}
.food-modal-bottom .swiper-wrapper {
  display: flex;
  justify-content: center;
}
.food-modal-header {
  display: flex;
  justify-content: space-around;
}

.food-modal-text {
  font-weight: 700;
  align-self: center;
}

.food-modal-name {
  font-size: 30px;
  margin-bottom: 20px;
}
.food-modal-kcal {
  font-size: 20px;
  margin-bottom: 20px;
}

#chart {
  width: 500px;
}

.food-modal-bottom-text {
  font-size: 25px;
  font-weight: 700;
  text-align: left;
  position: relative;
  left: 10px;
  margin-bottom: 10px;
}
.modal-bottom-img {
  width: 200px;
  height: 200px;
  margin: 10px;
  border-radius: 10px;
}
.modal-bottom-img:hover {
  cursor: pointer;
}

.pocket-btn {
  width: 170px;
  height: 50px;
  font-size: 18px;
  position: relative;
  display: block;
  border-radius: 7px;
  left: 84%;
  top: 20px;
}
.sweet-modal {
  max-width: 60vw;
  overflow-x: hidden;
}

.my-swiper {
  width: 50vw;
}
.swiper-prev,
.swiper-next {
  width: 42px;
  height: 42px;
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
  right: 55px;
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

/* 클래스 리스트 추가해서 수정 */
.modal-bottom-img.clicked {
  border: solid black 5px;
}
</style>
