<template>
  <div>
    <sweet-modal id="main-modal" ref="modal">
      <div class="modal">
        <section class="food-modal-header">
          <div class="food-set">
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

        <section class="food-modal-bottom">
          <div class="inner">
            <div class="food-modal-bottom-text">이런 음식은 어때요?</div>

            <swiper ref="mySwiper" :options="swiperOptions" class="my-swiper">
              <swiper-slide>
                <div class="read-more" v-show="isRead">자세히보기</div>
                <img
                  src="../../assets/menu_rec/food_example_img.jpg"
                  alt="음식예시사진"
                  class="modal-bottom-img"
                />
                <div class="sub-food-name">소고기무국</div>
              </swiper-slide>
              <swiper-slide>
                <img
                  src="../../assets/menu_rec/food_example_img.jpg"
                  alt="음식예시사진"
                  class="modal-bottom-img"
                />
                <div class="sub-food-name">소고기무국</div>
              </swiper-slide>
              <swiper-slide>
                <img
                  src="../../assets/menu_rec/food_example_img.jpg"
                  alt="음식예시사진"
                  class="modal-bottom-img"
                />
                <div class="sub-food-name">소고기무국</div>
              </swiper-slide>
              <swiper-slide>
                <img
                  src="../../assets/menu_rec/food_example_img.jpg"
                  alt="음식예시사진"
                  class="modal-bottom-img"
                />
                <div class="sub-food-name">소고기무국</div>
              </swiper-slide>
              <swiper-slide>
                <img
                  src="../../assets/menu_rec/food_example_img2.png"
                  alt="음식예시사진"
                  class="modal-bottom-img"
                />
                <div class="sub-food-name">보쌈</div>
              </swiper-slide>
            </swiper>
            <div class="swiper-prev">
              <span class="material-icons">arrow_back</span>
            </div>
            <div class="swiper-next">
              <span class="material-icons">arrow_forward</span>
            </div>
          </div>
        </section>
      </div>
    </sweet-modal>
  </div>
</template>

<script>
export default {
  name: "searchModal",
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
        isRead: true,
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
    readMore() {
      const readMoreItem = document.querySelector("read-more");
      console.log(readMoreItem);
    },
  },
  watch: {
    test() {
      console.log(this.test);
      this.showModal();
    },
  },
  mounted() {
    // this.showSwiper();
  },
};
</script>

<style>
.sweet-modal {
  max-width: 60vw;
  overflow-x: hidden;
}
.modal-img {
  width: 11.7vw;
  height: 23.1vh;
  border-radius: 10px;
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

.food-modal-name {
  font-size: 1.8vw;
  margin-bottom: 0.78vw;
}
.food-modal-kcal {
  font-size: 1.4vw;
  margin-bottom: 0.78vw;
}
.food-modal-g {
  font-size: 1.2vw;
}

#chart {
  width: 19.53vw;
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

.my-swiper {
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
.read-more {
  position: absolute;
  top: 8vh;
  margin-left: 4.3vw;
  z-index: 1;
  color: #fff;
  font-size: 0.7vw;
}
@media screen and (max-width: 1440px) {
  .food-modal-header {
    display: block;
  }
  #chart {
    position: relative;
    left: 3.87vw;
    width: 43vw;
  }
  .food-set {
    width: 100%;
    display: flex;
    justify-content: space-evenly;
  }
  .modal-img {
    width: 20vw;
    height: 20.1vh;
    border-radius: 10px;
  }
  .food-modal-bottom-text {
    font-size: 1.5vw;
    font-weight: 700;
    text-align: left;
    position: relative;
    left: 2.1vw;
    margin-bottom: 10px;
  }
  .modal-bottom-img {
    width: 10.8vw;
    height: 15.42vh;
    border-radius: 10px;
  }
  .sub-food-name {
    font-size: 1.3vw;
    margin-left: 1vw;
  }
}
</style>
