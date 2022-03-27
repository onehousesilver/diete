<template>
  <div>
    <!-- Banner -->
    <BannerBar MainText="음식추천" SubText="SubText" />
    <h1>추천받을 끼니를 선택해 주세요</h1>
    <div class="choose-container">
      <section id="breakfast" @click="chooseMeal">
        <h2>아침</h2>
        <img :src="require('@/assets/menu_rec/breakfast_img.png')" alt="예시이미지-아침">
        <button id="breakfast-btn" class="bttn-unite bttn-md bttn-success btn-group" @click="chooseMeal">선택</button>
      </section>
      <section id="lunch" @click="chooseMeal">
        <h2>점심</h2>
        <img :src="require('@/assets/menu_rec/lunch_img.png')" alt="예시이미지-점심">
        <button id="lunch-btn" class="bttn-unite bttn-md bttn-success btn-group" @click="chooseMeal">선택</button>
      </section>
      <section id="dinner" @click="chooseMeal">
        <h2>저녁</h2>
        <img :src="require('@/assets/menu_rec/dinner_img.png')" alt="예시이미지-저녁">
        <button id="dinner-btn" class="bttn-unite bttn-md bttn-success btn-group" @click="chooseMeal">선택</button>
      </section>
    </div>
    <button 
      class="bttn-unite bttn-md bttn-success btn-group"
      @click="nextStep"
    >
      추천받기
    </button>
  </div>
</template>

<script>
import BannerBar from '@/components/Main/BannerBar.vue'
import $ from 'jquery'

export default {
  name: 'ChooseMeal',
  components: {
    BannerBar
  },
  data() {
    return {
      selectedMeal: null,   // 선택한 끼니
    }
  },
  methods: {
    // 끼니 선택 메서드. 선택된 섹션의 style을 변경하고, 변수에 바인딩
    chooseMeal(e) {
      // 이미 선택된 섹션이 있을 때 
      if(this.selectedMeal)
      {
        // 기존에 선택된 섹션 선택 해제(클래스 제거)
        $(`#${this.selectedMeal}`).removeClass('select');
        $(`#${this.selectedMeal}-btn`).removeClass('select');
      }
      // 부모요소에 id가 지정되어 있다면(버튼을 클릭했을 때) 부모요소의 id, 없다면(버튼 이외의 섹션을 클릭했을 때) 자기 자신의 id 저장 
      this.selectedMeal = e.target.offsetParent.id ? e.target.offsetParent.id : e.target.id;
      // 섹션 선택(클래스 추가)
      $(`#${this.selectedMeal}`).addClass('select');
      $(`#${this.selectedMeal}-btn`).addClass('select');
    },
    nextStep() {
      this.$router.push({ path: '/menu/recommendation' })
    }
  }
}
</script>

<style scoped>
.btn-group  {
  position: absolute;
  bottom: 2vh;
  left: 50%;
  transform: translateX(-50%);
  width: 15vw;
  height: 5vh;
  border-radius: 0.625rem;
  animation: none;
}
.bttn-unite.bttn-success:before{
  background: #25AB9B;
}
.bttn-unite.bttn-success:after{
  background: #25AB9B;
}
.btn-group.select {
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