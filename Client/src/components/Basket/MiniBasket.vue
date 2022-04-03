<template>
  <div>
    <span class="material-icons basket-btn" @click="test">add</span>
    <div class="basket-list">
      <h2>장바구니</h2>
      <h3>오늘의 {{ mealTime }} 메뉴</h3>
      <div
        v-for="(food,idx) in menus"
        :key="idx"  
      >
        <div class="basket-food">
          <div class="basket-food-name">
            {{ food.foodName }}
          </div>
          <div class="basket-food-kcal">
            {{ food.foodKcal }}kcal
          </div>
          <div class="material-icons cancel-btn" @click="deleteMenu(idx)">close</div>
        </div>
      </div>
      <div class="basket-totalkcal">
        {{ totalKcal }}kcal
      </div>
      <button class="bttn-unite bttn-md bttn-success done-btn" @click="goToBasketPage">장바구니로 이동</button>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
import { mapActions } from 'vuex'
export default {
  data() {
    return {
      totalKcal: 0, // 합산칼로리
      basketState: false, // 장바구니 On/Off
    }
  },
  methods: {
    ...mapActions([
      'menusUpdate'
    ]),
    // 메뉴 삭제
    deleteMenu(idx) {
      // 현 컴포넌트의 배열에서 idx위치에 있는 값 삭제
      this.menus.splice(idx, 1)
      // 전역변수에 있는 배열 업데이트
      this.menusUpdate(this.menus)
    },
    goToBasketPage(){
      this.$router.push({ name: 'basket' })
    },
    test() {
      if(this.basketState){
        $('.basket-list').removeClass('selected');
      }
      else{
        $('.basket-list').addClass('selected');
      }
      this.basketState = !this.basketState
    }
  },
  computed: {
    // 장바구니 목록
    menus() { return this.$store.state.menus },
    // 선택한 끼니
    mealTime() { 
      switch(this.$store.state.mealTime){
        case 0:
          return "아침"
        case 1:
          return "점심"
        case 2:
          return "저녁"
        default:
          return 0
      }
    },
  },
  mounted() {
    // 메뉴의 총 칼로리 합산
    if (this.menus){
      this.menus.forEach(menu => {
        this.totalKcal += parseFloat(menu.foodKcal)
      });
    }
  }
}
</script>

<style scoped>
.basket-btn {
  background: #25ab9b;
  color: #fff;
  position: fixed;
  right: 0;
  font-size: 3vw;
  top: 50%;
  cursor: pointer;
}
.basket-list {
  border: 3px solid #25ab9b;
  border-radius: 10px;
  width: 15vw;
  height: 50vh;
  position: fixed;
  right: -15vw;
  top: 20vw;
  background: #fff;
  opacity: 0;
  transition-property: right, opacity ; /* 어떤 css 프로퍼티를 transition할지 지정 */
  transition-duration: 1s, 1s;
}
.basket-list.selected {
  right: 5vw;
  opacity: 1;
}
.basket-list h2 {
  font-size: 1.2vw;
  text-align: center;
}
.basket-list h3 {
  font-size: 1vw;
  text-align: center;
}

.basket-list .basket-food {
  display: grid;
  grid-template-columns: 8fr 3fr 1fr;
  width: 14vw;
  margin-left: .5vw;
  padding-bottom: 1vh;
}
.basket-list .basket-food .basket-food-name{
  font-size: 1vw;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.basket-list .basket-food .basket-food-kcal{
  font-size: .8vw;
  align-items: center;
}
.basket-list .cancel-btn{
  cursor: pointer;
  color: #25ab9b;
}
.basket-list .basket-totalkcal{
  text-align: center;
  font-size: 1.5vw;
  position: absolute;
  bottom: 5vh;
  left: 50%;
  transform: translateX(-50%);
}
.basket-list .done-btn {
  position: absolute;
  bottom: 1vh;
  left: 50%;
  transform: translateX(-50%);
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
@keyframes box-ani { from { transform: translate(0, 0); } to { transform: translate(100px, 100px); } }

</style>