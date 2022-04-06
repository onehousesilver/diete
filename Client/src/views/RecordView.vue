<template>
  <div>
    <MyProfile @editMode="editMode" />
    <div class="btn-container">
      <button class="bttn-unite bttn-md bttn-success my-diet" @click="goMyDiet">
        나의식단
      </button>
      <button
        class="bttn-unite bttn-md bttn-success my-analysis"
        @click="goMyAnalysis"
      >
        식단분석
      </button>
    </div>
    <MyDiet v-if="current" @goMyAnalysis="goMyAnalysis" />
    <MyAnalysis v-else @goMyDiet="goMyDiet" />
    <div class="edit-cover" v-show="editState"></div>
  </div>
</template>

<script>
import MyProfile from "../components/Record/MyProfile.vue";
import MyAnalysis from "../components/Record/MyAnalysis.vue";
import MyDiet from "@/components/Record/MyDiet.vue";
export default {
  components: {
    MyProfile,
    MyAnalysis,
    MyDiet,
  },
  data() {
    return {
      current: true,
      editState: false,
      alertState: false,
    };
  },
  methods: {
    goMyDiet() {
      this.current = true;
    },
    goMyAnalysis() {
      this.current = false;
      if (this.alertState == false) {
        this.$swal.fire({
          title: "나의 식단을 분석해보세요!",
          text: "나의 식단을 한국보건산업진흥원에서 제공하는 영양소와 비교해보세요!",
          imageUrl: require("../assets/alert_mypage_analysis.gif"),
          imageWidth: 800,
          imageHeight: 400,
          width: 850,
          imageAlt: "basket gif",
        });
        this.alertState = true;
      }
    },
    // 프로필 수정모드 On/Off
    editMode() {
      this.editState = !this.editState;
    },
  },
  mounted() {
    this.$swal.fire({
      title: "나의 식단을 확인하고 수정해보세요!",
      text: "일별, 주별로 식단을 확인하고 그래프를 클릭해서 원하는 영양정보만 확인해보세요!",
      imageUrl: require("../assets/alert_mypage_check.gif"),
      imageWidth: 800,
      imageHeight: 400,
      width: 850,
      imageAlt: "basket gif",
    });
  },
};
</script>

<style>
.btn-container {
  margin: 2.5vw auto;
  display: block;
  width: 30vw;
  text-align: center;
}

.btn-container .my-diet,
.btn-container .my-analysis {
  border-radius: 0;
  width: 10vw;
  height: 2.5vw;
  margin-right: 0.1vw;
  font-size: 1vw;
}
.edit-cover {
  opacity: 0.7;
  z-index: 3;
  width: 100%;
  height: 70vh;
  position: fixed;
  top: 14vw;
  background: #fff;
}
</style>
