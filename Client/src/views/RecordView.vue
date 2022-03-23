<template>
  <div>
    <MyProfile />
    <div>
      <div class="btns">
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
    </div>
    <MyDiet v-if="current == true" @goMyAnalysis="goMyAnalysis" />
    <MyAnalysis v-else-if="current == false" @goMyDiet="goMyDiet" />
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
    };
  },
  methods: {
    goMyDiet() {
      this.current = true;
    },
    goMyAnalysis() {
      this.current = false;
    },
  },
};
</script>

<style>
.btns {
  margin: 30px auto;
  display: block;
  width: 30vw;
  text-align: center;
}

.btns .my-diet {
  border-radius: 0;
  width: 10vw;
  margin-right: 2px;
}
.btns .my-analysis {
  border-radius: 0;
  width: 10vw;
}
</style>
