<template>
  <div>
    <div class="banner">
      <div class="banner-head">
        <div v-if="!MainText" class="default-text">
          <div class="my-text">diète</div>
          <div class="banner-sub-head">
            <!-- <span>diète에서 맞춤형 음식을 추천받아보세요</span> -->
          </div>
        </div>
        <div v-else class="present-text">
          {{ MainText }}
          <div class="banner-sub-head">
            <span>{{ SubText }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TextScramble from "@/js/bannerani.js";
export default {
  props: {
    MainText: String,
    SubText: String,
    isHome: Boolean,
  },
  methods: {
    textAnimation() {
      const phrases = [
        "diète",
        "식단",
        "饮食",
        "Diät",
        "dieta",
        "しょくじ",
        "diet",
      ];

      const el = document.querySelector(".my-text");
      const fx = new TextScramble(el);

      let counter = 0;
      const next = () => {
        fx.setText(phrases[counter]).then(() => {
          setTimeout(next, 3000);
        });
        counter = (counter + 1) % phrases.length;
      };
      next();
    },
  },
  mounted() {
    if (this.isHome) {
      this.textAnimation();
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
};
</script>

<style>
.banner {
  height: 20vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-image: url("../../assets/banner.png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
.banner .banner-head {
  text-align: center;
  font-size: 3vw;
  font-weight: 700;
}

.banner .banner-sub-head {
  font-size: 1.2vw;
  color: #333;
}
</style>
