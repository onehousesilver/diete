<template>
  <div>
    <MyProfile 
      @editMode="editMode"
    />
    <div class="btn-container">
      <button
        class="bttn-unite bttn-md bttn-success my-diet"
        @click="goMyDiet"
      >
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
    };
  },
  methods: {
    goMyDiet() {
      this.current = true;
    },
    goMyAnalysis() {
      this.current = false;
    },
    // 프로필 수정모드 On/Off
    editMode() {
      this.editState = !this.editState
    },
  },
};
</script>

<style>
.btn-container {
  margin: 30px auto;
  display: block;
  width: 30vw;
  text-align: center;
}

.btn-container .my-diet {
  border-radius: 0;
  width: 10vw;
  margin-right: 2px;
}
.btn-container .my-analysis {
  border-radius: 0;
  width: 10vw;
}
.edit-cover {
  opacity: 0.7;
  z-index: 3;
  width: 100%;
  height: 70vh;
  position: fixed;
  top: 30vh;
  background: #fff;
}
</style>
