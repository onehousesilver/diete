<template>
  <div class="signup-container">
    <div class="second-step">
      <div class="group">
        <input
          class="my-input"
          type="text"
          id="userHeight"
          placeholder="예시) 163.1"
          v-model="formData.height"
        />
        <label for="userHeight">키</label>
        <span class="cm">CM</span>
        <span class="highlight"></span>
        <span class="bar"></span>
        <div class="error-msg" v-if="formData.height" style="color: green">
          <span class="material-icons">check_circle</span>
          <span>확인 되었습니다.</span>
        </div>
        <div v-else class="error-msg" style="color: red">
          <span class="material-icons">cancel</span>
          <span>필수 항목입니다.</span>
        </div>
      </div>

      <div class="group">
        <input
          class="my-input"
          type="text"
          id="userWeight"
          placeholder="예시) 78.2"
          v-model="formData.weight"
        />
        <label for="userWeight">몸무게</label>
        <span class="kg">KG</span>
        <span class="highlight"></span>
        <span class="bar"></span>
        <div class="error-msg" v-if="formData.weight" style="color: green">
          <span class="material-icons">check_circle</span>
          <span>확인 되었습니다.</span>
        </div>
        <div v-else class="error-msg" style="color: red">
          <span class="material-icons">cancel</span>
          <span>필수 항목입니다.</span>
        </div>
      </div>

      <div class="gender-btn">
        <span class="gender-title">성별</span>
        <input
          type="radio"
          id="gender-m"
          name="gender"
          value="0"
          class="btn__man"
          v-model="formData.gender"
        />
        <label for="gender-m">남자</label>
        <input
          type="radio"
          id="gender-w"
          name="gender"
          value="1"
          class="btn__woman"
          v-model="formData.gender"
        />
        <label for="gender-w">여자</label>
        <div class="error-msg2" v-if="formData.gender" style="color: green">
          <span class="material-icons">check_circle</span>
          <span>확인 되었습니다.</span>
        </div>
        <div v-else class="error-msg2" style="color: red">
          <span class="material-icons">cancel</span>
          <span>필수 항목입니다.</span>
        </div>
      </div>
      <div class="activity-btn">
        <div>
          <span class="activity-title"
            >활동량
            <span class="material-icons help" @click="showImg"
              >help_outline</span
            ></span
          >
        </div>
        <!-- 활동량 설명 이미지 -->
        <div v-show="showImgflag">
          <div class="activitiy-description">
            <span>적음</span> <br />
            <p>
              앉아서 주로 생활하거나, 매일 가벼운 움직임만 하며 <br />
              활동량이 적은 경우
            </p>
            <span>보통</span> <br />
            <p>규칙적인 생활로 보통의 활동량을 가진 경우</p>
            <span>많음</span> <br />
            <p>육체노동 등 평소 신체 활동량이 많은 경우</p>
          </div>
        </div>
        <input
          type="radio"
          id="activity-s"
          name="activity"
          value="적음"
          class="btn__s"
          v-model="formData.activity"
        />
        <label for="activity-s">적음</label>
        <input
          type="radio"
          id="activity-m"
          name="activity"
          value="보통"
          class="btn__m"
          v-model="formData.activity"
        />
        <label for="activity-m">보통</label>
        <input
          type="radio"
          id="activity-l"
          name="activity"
          value="많음"
          class="btn__w"
          v-model="formData.activity"
        />
        <label for="activity-l">많음</label>
        <div class="error-msg2" v-if="formData.activity" style="color: green">
          <span class="material-icons">check_circle</span>
          <span>확인 되었습니다.</span>
        </div>
        <div v-else class="error-msg2" style="color: red">
          <span class="material-icons">cancel</span>
          <span>필수 항목입니다.</span>
        </div>
      </div>

      <button
        class="bttn-unite bttn-md bttn-success next-btn"
        @click="nextStep"
      >
        다음 단계
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "JoinSecondStep",
  data() {
    return {
      formData: {
        height: null,
        weight: null,
        activity: null,
        gender: null,
      },
      showImgflag: false,
    };
  },
  methods: {
    // 다음단계로 이동
    nextStep() {
      // 모든 정보를 입력 했을 때만 다음단계로 이동
      if (
        this.formData.height &&
        this.formData.weight &&
        this.formData.activity &&
        this.formData.gender
      ) {
        this.$emit("nextStep", this.formData);
      } else {
        this.$swal.fire({
          icon: "error",
          title: "필수항목을 입력해주세요.",
          text: "모든 항목은 필수입니다.",
        });
      }
    },
    showImg() {
      this.showImgflag = !this.showImgflag;
    },
  },
};
</script>

<style scoped>
.signup-container {
  position: relative;
  top: 3.75rem;
  width: 50rem;
  margin: 0 auto;
  /* border: 5px solid #25AB9B; */
  border-radius: 1.875rem;
  text-align: center;
}
/* Button */
.bttn-unite.bttn-success {
  border-radius: 0.625rem;
}
.bttn-unite.bttn-success:before {
  background: #25ab9b;
}
.bttn-unite.bttn-success:after {
  background: #25ab9b;
}
.check-btn {
  position: absolute;
  font-size: 1rem;
  width: 6rem;
  right: 0;
  bottom: 0.25rem;
  height: 75%;
}
.next-btn {
  margin-top: 10rem;
  position: absolute;
  width: calc(40vw - 2.2rem);
  left: 50%;
  transform: translatex(-50%);
  z-index: -1;
}
input[type="radio"] {
  display: none;
}
.gender-btn {
  position: relative;
  display: flex;
  width: 40vw;
  left: 50%;
  transform: translateX(-50%);
}
.gender-btn .btn__woman {
  width: 50%;
  top: 1rem;
  border-radius: 0 1rem 1rem 0;
}
.gender-btn .btn__man {
  /* position: absolute; */
  width: 50%;
  top: 1rem;
  border-radius: 1rem 0 0 1rem;
}
.gender-btn .gender-title {
  position: absolute;
  top: -1.875rem;
  font-size: 1.4rem;
  color: #25ab9b;
}
.gender-btn label,
.gender-btn label {
  margin-top: 1rem;
  font-size: 1.4rem;
  color: #25ab9b;
  cursor: pointer;
  border: 1px solid #25ab9b;
  width: 50%;
  top: 1rem;
  border-radius: 1rem;
  text-align: center;
}
input[type="radio"]:checked + label {
  background: #25ab9b;
  color: #fff;
}
.activity-btn {
  top: 3rem;
  position: relative;
  display: flex;
  width: 40vw;
  left: 50%;
  transform: translateX(-50%);
}
.activity-btn .btn__s {
  width: 50%;
  top: 1rem;
  border-radius: 0 1rem 1rem 0;
}
.activity-btn .btn__m {
  /* position: absolute; */
  width: 50%;
  top: 1rem;
  border-radius: 1rem 0 0 1rem;
}
.activity-btn .btn__l {
  /* position: absolute; */
  width: 50%;
  top: 1rem;
  border-radius: 1rem 0 0 1rem;
}
.activity-btn .activity-title {
  position: absolute;
  top: -1.875rem;
  font-size: 1.4rem;
  color: #25ab9b;
}
.material-icons.help {
  color: #25ab9b;
  position: absolute;
  top: 0.13vw;
}
.material-icons.help:hover {
  cursor: pointer;
}
.activitiy-description {
  position: absolute;
  text-align: left;
  width: 19vw;
  background-color: #fff;
  top: 0.5vw;
  border: 2px solid #25ab9b;
  border-radius: 10px;
  padding: 0.7vw;
  left: 3vw;
  z-index: 1;
}
.activitiy-description span {
  font-size: 1vw;
  font-weight: 700;
  color: #25ab9b;
}

.activitiy-description p {
  font-size: 0.8vw;
}
.activity-btn label,
.activity-btn label {
  margin-top: 1rem;
  font-size: 1.4rem;
  color: #25ab9b;
  cursor: pointer;
  border: 1px solid #25ab9b;
  width: 50%;
  top: 1rem;
  border-radius: 1rem;
  text-align: center;
}
input[type="radio"]:checked + label {
  background: #25ab9b;
  color: #fff;
}
.second-step {
  width: 100%;
  position: relative;
}
.group {
  position: relative;
  margin: 2.8125rem 0px;
  width: 40vw;
  left: 50%;
  transform: translateX(-50%);
}
.group .my-input {
  font-size: 1rem;
  padding: 1.2rem 1.875rem 0.625rem 0.3125rem;
  display: block;
  width: calc(40vw - 2.2rem);
  border: none;
  border-bottom: 1px solid #757575;
  color: #555;
}
.group .my-input:focus {
  outline: none;
}

.group label {
  color: #ccc;
  font-size: 1.125rem;
  position: absolute;
  pointer-events: none;
  left: 0.3125rem;
  top: 0.625rem;
  transition: 0.2s ease all;
  -moz-transition: 0.2s ease all;
  -webkit-transition: 0.2s ease all;
}
.error-msg {
  display: flex;
  align-items: center;
  position: absolute;
  right: 0;
}
.error-msg2 {
  display: flex;
  align-items: center;
  position: absolute;
  right: 0;
  bottom: -2rem;
}

.cm {
  position: absolute;
  right: 0;
  bottom: 0;
  font-size: 2rem;
}
.kg {
  position: absolute;
  right: 0;
  bottom: 0;
  font-size: 2rem;
}

/* active state */
.group .my-input:focus ~ label,
.my-input:valid ~ label {
  top: -1.875rem;
  font-size: 1.4rem;
  color: #25ab9b;
}
/* HIGHLIGHTER ================================== */
.highlight {
  position: absolute;
  height: 60%;
  width: 6.25rem;
  top: 25%;
  left: 0;
  pointer-events: none;
  opacity: 0.5;
}
/* BOTTOM BARS ================================= */
.bar {
  position: relative;
  display: block;
  width: 40vw;
}
.bar:before,
.bar:after {
  content: "";
  height: 0.125rem;
  width: 0;
  bottom: 0;
  position: absolute;
  background: #25ab9b;
  transition: 0.2s ease all;
  -moz-transition: 0.2s ease all;
  -webkit-transition: 0.2s ease all;
}
.bar:before {
  left: 50%;
}
.bar:after {
  right: 50%;
}

/* active state */
input:focus ~ .bar:before,
input:focus ~ .bar:after {
  width: 50%;
}
/* active state */
input:focus ~ .highlight {
  -webkit-animation: inputHighlighter 0.3s ease;
  -moz-animation: inputHighlighter 0.3s ease;
  animation: inputHighlighter 0.3s ease;
}

/* ANIMATIONS ================ */
@-webkit-keyframes inputHighlighter {
  from {
    background: #5264ae;
  }
  to {
    width: 0;
    background: transparent;
  }
}
@-moz-keyframes inputHighlighter {
  from {
    background: #5264ae;
  }
  to {
    width: 0;
    background: transparent;
  }
}
@keyframes inputHighlighter {
  from {
    background: #5264ae;
  }
  to {
    width: 0;
    background: transparent;
  }
}
</style>
