<template>
  <div>
    <!-- Banner -->
    <BannerBar
      MainText="음식추천"
      SubText="diète에서 맛있는 음식을 추천받아보세요"
    />
    <h1>언제 드실 음식이신가요?</h1>
    <div class="choose-container">
      <section id="breakfast" @click="chooseMeal">
        <h2>아침</h2>
        <img
          :src="require('@/assets/menu_rec/breakfast_img.svg')"
          alt="예시이미지-아침"
          class="breakfast-img"
        />
        <button
          id="bre-btn"
          class="bttn-unite bttn-md bttn-success btn-group"
          @click="chooseMeal"
        >
          선택
        </button>
      </section>
      <section id="lunch" @click="chooseMeal">
        <h2>점심</h2>
        <img
          :src="require('@/assets/menu_rec/lunch_img.svg')"
          alt="예시이미지-점심"
          class="lunch-img"
        />
        <button
          id="lun-btn"
          class="bttn-unite bttn-md bttn-success btn-group"
          @click="chooseMeal"
        >
          선택
        </button>
      </section>
      <section id="dinner" @click="chooseMeal">
        <h2>저녁</h2>
        <img
          :src="require('@/assets/menu_rec/dinner_img.svg')"
          alt="예시이미지-저녁"
          class="dinner-img"
        />
        <button
          id="din-btn"
          class="bttn-unite bttn-md bttn-success btn-group"
          @click="chooseMeal"
        >
          선택
        </button>
      </section>
    </div>
    <button class="bttn-unite bttn-md bttn-success btn-group" @click="nextStep">
      추천받기
    </button>
  </div>
</template>

<script>
import BannerBar from "@/components/Main/BannerBar.vue";
import $ from "jquery";
import { mapActions } from "vuex";

export default {
  name: "ChooseMeal",
  components: {
    BannerBar,
  },
  data() {
    return {
      selectedMeal: null, // 선택한 끼니
      today: new Date(),
    };
  },
  methods: {
    ...mapActions(["mealTimeUpdate", "menusUpdate", "targetDateUpdate"]),
    // 끼니 선택 메서드. 선택된 섹션의 style을 변경하고, 변수에 바인딩
    chooseMeal(e) {
      // 이미 선택된 섹션이 있을 때
      if (this.selectedMeal) {
        // 기존에 선택된 섹션 선택 해제(클래스 제거)
        $(`#${this.selectedMeal}`).removeClass("select");
        $(`#${this.selectedMeal}-btn`).removeClass("select");
      }
      // 부모요소에 id가 지정되어 있다면(버튼을 클릭했을 때) 부모요소의 id, 없다면(버튼 이외의 섹션을 클릭했을 때) 자기 자신의 id 저장
      this.selectedMeal = e.target.offsetParent.id
        ? e.target.offsetParent.id
        : e.target.id;
      // 섹션 선택(클래스 추가)
      $(`#${this.selectedMeal}`).addClass("select");
      $(`#${this.selectedMeal}-btn`).addClass("select");
    },
    nextStep() {
      if (this.selectedMeal != null) {
        if(this.selectedMeal == 'breakfast'){
          this.mealTimeUpdate(0)
        }
        else if(this.selectedMeal == 'lunch'){
          this.mealTimeUpdate(1)
        }
        else {
          this.mealTimeUpdate(2)
        }
        this.menusUpdate([])
        this.targetDateUpdate(`${this.today.getFullYear()}-${this.today.getMonth() + 1}-${this.today.getDate()}`)
        this.$router.push({ path: "/menu/recommendation" });
      } else {
        this.$swal.fire({
          icon: "error",
          title: "끼니를 선택해주세요!",
          text: "언제 드실 음식이신가요?",
        });
      }
    },
  },
};
</script>

<style scoped>
.btn-group {
  position: absolute;
  bottom: 2vh;
  left: 50%;
  transform: translateX(-50%);
  width: 15vw;
  height: 5vh;
  border-radius: 0.625rem;
  animation: none;
  font-size: 1vw;
}
.bttn-unite.bttn-success:before {
  background: #25ab9b;
}
.bttn-unite.bttn-success:after {
  background: #25ab9b;
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
  margin-top: 3vh;
  text-align: center;
  font-size: 1.5vw;
}
.breakfast-img,
.lunch-img {
  display: block;
  width: 18vw;
  height: 30vh;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}
.dinner-img {
  display: block;
  width: 12vw;
  height: 30vh;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}
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
