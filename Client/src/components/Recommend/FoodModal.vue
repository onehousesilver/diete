<template>
  <div>
    <sweet-modal id="main-modal" ref="modals">
      <div class="modal">
        <section class="food-modal-header">
          <div class="food-modal-header-left">
            <img
              :src="`data:image/png;base64,${foodData.image}`"
              alt="음식 사진"
              class="modal-img"
            />
            <div class="food-modal-text">
              <div class="food-modal-name">{{ foodData.foodName }}</div>
              <div class="food-modal-kcal">{{ foodData.foodKcal }}kcal</div>
              <div class="food-modal-g">
                1회제공량: {{ foodData.servingSize }}g
              </div>
            </div>
          </div>
          <div id="my-chart">
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
            <div class="food-modal-bottom-text">다른 사용자들은 이런 음식도 먹었어요</div>

            <swiper ref="mySwiper" :options="swiperOptions" class="my-swiper">
              <swiper-slide
                v-for="(subFood, idx) in subMenu"
                :key="idx"
                class="submenu"
                :id="`${idx}`"
              >
                <img
                  :src="`data:image/png;base64,${subFood.img}`"
                  alt="음식예시사진"
                  class="modal-bottom-img"
                  @click="mainMenuUpdate(subFood)"
                />
                <div 
                  class="modal-bottom-img-text"
                  @click="mainMenuUpdate(subFood)"
                >
                  {{ subFood.foodName }}
                </div>
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
              @click="putInBasket"
              v-show="!onlySearch"
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
import axios from 'axios';
import { mapActions } from "vuex";
export default {
  name: "SearchResultItem",
  props: {
    modalState: Boolean,
    foodData: Object,
    onlySearch: Boolean,
  },
  data() {
    return {
      subMenu: null,    // 추가메뉴
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
      // Apexchart,
      series: [
        {
          name: "함량",
          data: [
            0, 0, 0, 0, 0,
          ],
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
          offsetX: -10,
          style: {
            fontSize: "12px",
            colors: ["#fff"],
          },
        },
        xaxis: {
          categories: ["탄수화물", "단백질", "지방", "당류", "총 포화지방산"],
          title: {
            text: "g (gram)",
          },
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return `${val} g`;
            },
          },
        },
      },
      selectFlag: false,
      newData: null,
    };
  },
  methods: {
    ...mapActions(["myMenuUpdate"]),
    showModal() {
      this.$refs.modals.open("main-modal");
    },
    dataUpdate() {
      this.series[0].data = [
        { x: "탄수화물", y: this.foodData.carbohydrate },
        { x: "단백질", y: this.foodData.protein },
        { x: "지방", y: this.foodData.fat },
        { x: "총 당류", y: this.foodData.sugar },
        { x: "포화지방산", y: this.foodData.fattyAcid },
      ];
    },
    subMenuUpdate() {
      axios({
        method: 'get',
        url: `${process.env.VUE_APP_API_URL}/menu/submenu/${this.foodData.id}/`
      })
        .then(res => {
          this.subMenu = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 아쉽지만
    mainMenuUpdate(subMenu){
      console.log(subMenu)
      axios({
        method: 'get',
        url: `${process.env.VUE_APP_API_URL}/menu/${subMenu.foodId}/`
      })
        .then(res => {
          this.$emit('dataUpdate', res.data)
          console.log(res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 장바구니담기
    putInBasket(){
      // 선택한 음식이 이미 장바구니에 존재할 때
      if (this.$store.state.menus.length){
        let alreadyIncludeState = this.$store.state.menus.every(food => food.id == this.foodData.id)
        if (alreadyIncludeState){
          this.$swal.fire({
            icon: "error",
            title: "이미 장바구니에 들어있어요.",
          });
        }
        else {
          this.myMenuUpdate(this.foodData);
          this.$swal.fire({
            icon: "success",
            title: "장바구니에 추가되었습니다."
          });
        }
      }
      else{
        this.myMenuUpdate(this.foodData);
        this.$swal.fire({
          icon: "success",
          title: "장바구니에 추가되었습니다."
        });
      }
      this.$refs.modals.close("main-modal");
    }
  },
  watch: {
    modalState() {
      this.showModal();
    },
    foodData() {
      this.dataUpdate();
      this.subMenuUpdate();
    },
  },
};
</script>

<style>
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
  color:#eee;
  cursor:pointer;
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
