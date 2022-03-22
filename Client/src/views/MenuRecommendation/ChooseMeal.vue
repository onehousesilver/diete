<template>
  <div>
    <BannerBar MainText="음식추천" SubText="" />
    <h1>추천받을 끼니를 선택해 주세요</h1>
    <div class="choose-container">
      <section id="bre" @click="chooseMeal">
        <h2>아침</h2>
        <img :src="require('@/assets/menu_rec/breakfast_img.png')" alt="">
        <button id="bre-btn" class="bttn-unite bttn-md bttn-success choose-btn" @click="test">선택</button>
      </section>
      <section id="lun" @click="chooseMeal">
        <h2>점심</h2>
        <img :src="require('@/assets/menu_rec/lunch_img.png')" alt="">
        <button id="lun-btn" class="bttn-unite bttn-md bttn-success choose-btn" @click="test">선택</button>
      </section>
      <section id="din" @click="chooseMeal">
        <h2>저녁</h2>
        <img :src="require('@/assets/menu_rec/dinner_img.png')" alt="">
        <button id="din-btn" class="bttn-unite bttn-md bttn-success choose-btn" @click="test">선택</button>
      </section>
    </div>
    <!-- <button class="bttn-unite bttn-md bttn-success next-btn">선택</button> -->
  </div>
</template>

<script>
import BannerBar from '@/components/Main/BannerBar.vue'
import $ from 'jquery'
export default {
  name: 'MenuView',
  components: {
    BannerBar
  },
  data() {
    return {
      selectedMeal: null,   // 선택한 끼니
    }
  },
  methods: {
    test() {
      console.log('zz')
    },
    chooseMeal(e) {
      if(this.selectedMeal){
        $(`#${this.selectedMeal}`).removeClass('select');
        $(`#${this.selectedMeal}-btn`).removeClass('select');
      }
      this.selectedMeal = e.target.id ? e.target.id : e.target.offsetParent.id;
      $(`#${this.selectedMeal}`).addClass('select');
      $(`#${this.selectedMeal}-btn`).addClass('select');
    }
  }
}
</script>

<style scoped>
.choose-btn {
  position: absolute;
  bottom: 2vh;
  left: 50%;
  transform: translateX(-50%);
  width: 15vw;
  height: 5vh;
  border-radius: 0.625rem;
  animation: none;
}
.bttn-unite.bttn-success:after
.bttn-unite.bttn-success:before {
  background: #25ab9b;
  color: #fff;
  
}
.choose-btn.select {
  background: #25ab9b;
  color: #fff;
}
h1 {
  text-align: center;
  font-size: 1.8vw;
  margin: 5vh 0;
}
.choose-container {
  position: relative;
  width: 90vw;
  display: flex;
  left: 50%;
  transform: translateX(-50%);
  gap: 3rem;
  justify-content: space-between;
}
.choose-container section {
  position: relative;
  width: 25vw;
  height: 45vh;
  border: solid #666 0.2rem;
  border-radius: 1.25rem;
  cursor: pointer;
  animation: ease 2s;
}
.choose-container section:hover {
  border: solid #25ab9b 0.2rem;
  box-shadow: 4px 4px 4px #ccc;
}
.choose-container section.select {
  border: solid #25ab9b 0.2rem;
  box-shadow: 4px 4px 4px #ccc;
}
.choose-container h2 {
  text-align: center;
  font-size: 1.5vw;
}
.choose-container section img {
  display: block;
  width: 18vw;
  height: 25vh;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}
/* .choose-container section:hover{
   -webkit-animation:vibrate .2s ease-in-out 0s infinite;
   -moz-animation:vibrate .2s ease-in-out 0s infinite;
   animation:vibrate .2s ease-in-out 0s infinite;
} */
@keyframes vibrate {
  0% { 
    -webkit-transform: rotate(1deg); 
  }
  50% {
    -webkit-transform: rotate(-1deg); 
  }
  100% {
    -webkit-transform: rotate(1deg); 
  }
}
</style>