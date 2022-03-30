<template>
  <div class="signup-container">
    <div class="top">
      <div class="text">어떤 식단을 선호하세요?</div>
    </div>

    <div class="card-choice">
      <!-- 채소위주 식단 -->
      <section id="vegetable" class="hvr-glow" @click="clickEvent">
        <div class="main-text">
          <span class="card-main-text" style="color: #25ab2e">채소위주</span>의
          식단을 선호합니다.
        </div>
        <div class="sub-text">
          이런분들에게 추천해요! <br />
          고기를 자주 먹지 않고, <br />
          <span class="card-sub-text">야채 위주의 식단</span>을 선호하는
          편입니다.<br />
        </div>
        <img class="carrot-img" src="../../assets/join/veg_img.jpg" alt="" />
      </section>

      <!-- 고기위주 식단 -->
      <section id="meat" class="hvr-glow" @click="clickEvent">
        <div class="main-text">
          <span class="card-main-text" style="color: #7f4b3a">고기위주</span>의
          식단을 선호합니다.
        </div>
        <div class="sub-text">
          이런분들에게 추천해요!<br />
          고기를 자주 먹고, <br />
          <span class="card-sub-text">고기 위주의 식단</span>을 선호하는
          편입니다.
          <br />
        </div>
        <img class="meat-img" src="../../assets/join/meat_img.jpg" alt="" />
      </section>

      <!-- 일반식단 -->
      <section id="general" class="hvr-glow" @click="clickEvent">
        <div class="main-text">
          <span class="card-main-text" style="color: #4978a3">일반식단</span>을
          선호합니다.
        </div>
        <div class="sub-text">
          이런분들에게 추천해요!<br />
          고기, 야채 상관없이 <br />
          <span class="card-sub-text">일반 식단</span>을 선호하는 편입니다.
          <br />
        </div>
        <img class="general-img" src="../../assets/join/general_img.png" alt="" />
      </section>
    </div>

    <button class="bttn-unite bttn-success next-btn" @click="completedForm">
      회원가입완료
    </button>
  </div>
</template>

<script>
// jquery import
import $ from "jquery";
export default {
  name: "JoinSecondStep",
  data() {
    return {
      likeMenu: 1,
      clickCard: null, // 선택한 식단
    };
  },
  methods: {
    completedForm() {
      this.$emit("completedForm", this.likeMenu);
    },
    // 선택한 상태에서 다른 거 눌렀을 때 해제
    clickEvent(e) {
      // 이미 선택된 섹션이 있을 때
      if (this.clickCard) {
        // 기존에 선택된 섹션 선택 해제(클래스 제거)
        $(`#${this.clickCard}`).removeClass("clicked");
      }
      // 부모요소에 id가 지정되어 있다면(버튼을 클릭했을 때) 부모요소의 id, 없다면(버튼 이외의 섹션을 클릭했을 때) 자기 자신의 id 저장
      this.clickCard = e.target.offsetParent.id
        ? e.target.offsetParent.id
        : e.target.id;
      // 섹션 선택(클래스 추가)
      $(`#${this.clickCard}`).addClass("clicked");
    },
  },
};
</script>
<style scoped>
img {
  display: block;
}
.top .text {
  text-align: center;
  font-size: 2.6vw;
  font-weight: 700;
}
.card-choice {
  display: flex;
  justify-content: center;
  text-align: center;
  top: 3vh;
  position: relative;
  height: 65vh;
}
.card-choice #vegetable,
.card-choice #meat,
.card-choice #general {
  width: 26vw;
  height: 63vh;
  border: 3px solid #25ab9b;
  margin: 10px;
  border-radius: 20px;
}
.card-choice #vegetable:hover,
.card-choice #meat:hover,
.card-choice #general:hover {
  cursor: pointer;
}
.card-choice section.clicked {
  animation: pulse;
  animation-duration: 1.5s;
  animation-iteration-count: infinite;
}
.card-choice .main-text {
  font-size: 1.3vw;
  font-weight: 700;
  position: relative;
  top: 1vw;
}
.main-text .card-main-text {
  font-size: 40px;
}
.card-choice .sub-text {
  font-size: 1.15vw;
  font-weight: 700;
  position: relative;
  top: 1.56vw;
  line-height: 1.6;
}
.sub-text .card-sub-text {
  font-size: 1.56vw;
  background: linear-gradient(to top, #e6f7be 50%, transparent 50%);
}
.next-btn {
  display: block;
  margin: 0 auto;
  border-radius: 5px;
  width: 20vw;
  height: 6vh;
  font-size: 1.3vw;
  top: 4.17vw;
}
.meat-img {
  margin: 0 auto;
  width: 21vw;
}
.carrot-img {
  top: 2.6vw;
  position: relative;
  margin: 0 auto;
  width: 16.7vw;
}
.general-img {
  margin: 0 auto;
  top: 4.1vw;
  position: relative;
  width: 13.02vw;
}
.animate__animated.animate__pulse {
  animation-iteration-count: infinite;
}
</style>
