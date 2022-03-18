<template>
  <div class="signup-container">
    <div class="first-step">
        <div class="group">
          <input 
            class="my-input" 
            type="text" 
            id="userID" 
            placeholder="6~16자 이내"
            v-model="formData.userId"
          >
          <label for="userID">아이디</label>
          <span class="highlight"></span>
          <span class="bar"></span>
        </div>
          
        <div class="group">
          <input 
            class="my-input"  
            type="password" 
            id="userPW" 
            placeholder="영문 숫자를 포함한 8~16자 이내"
            v-model="formData.userPw"
          >
          <label for="userPW">비밀번호</label>
          <span class="highlight"></span>
          <span class="bar"></span>
        </div>
        <div class="group">
          <input 
            class="my-input"  
            type="password" 
            id="userPWConf" 
            placeholder="비밀번호를 확인합니다"
            v-model="formData.userPwConf"
          >
          <label for="userPWConf">비밀번호 확인</label>
          <span class="highlight"></span>
          <span class="bar"></span>
        </div>
        <div class="group">
          <input 
            class="my-input" 
            type="text" 
            id="userName" 
            placeholder="이름을 입력해주세요"
            v-model="formData.userName"
          >
          <label for="userName">이름</label>
          <span class="highlight"></span>
          <span class="bar"></span>
        </div>
        <div class="group">
          <input 
            class="my-input" 
            type="date" 
            id="userBirth" 
            placeholder="6~16자 이내"
            v-model="formData.userBirth"
          >
          <label for="userBirth">생년월일</label>
          <span class="highlight"></span>
          <span class="bar"></span>
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
  name: 'JoinFirstStep',
  data() {
    return {
      formData: {
        userId: null,
        userPw: null,
        userPwConf: null,
        userName: null,
        userBirth: null
      },
    }
  },
  methods: {
    nextStep() {
      this.$emit('nextStep', this.formData);
    }
  }
}
</script>

<style scoped>
  /* Button */
  .bttn-unite.bttn-success{
    border-radius: 0.625rem;
    width: 18.75rem;
    margin-bottom: 1.875rem;
  }
  .bttn-unite.bttn-success:before{
    background: #25AB9B;
  }
  .bttn-unite.bttn-success:after{
    background: #25AB9B;
  }
  
  .signup-container {
    position: relative;
    top: 3.75rem;
    width: 50rem;
    margin: 0 auto;
    /* border: 5px solid #25AB9B; */
    border-radius: 1.875rem;
    text-align: center;
  }
  .first-step {
    width: 100%;
    position: relative;
  }
  .group { 
    position:relative; 
    margin: 2.8125rem 0px;
    width: 40vw;
    left: 50%;
    transform: translateX(-50%);
  }
  .group .my-input {
    font-size: 1rem;
    padding: 1.2rem 1.875rem 0.625rem 0.3125rem;
    display:block;
    width:calc(40vw - 2.2rem);
    border:none;
    border-bottom:1px solid #757575;
    color: #555;
  }
  .group .my-input:focus 		{ outline:none; }

  .group label {
    color:#ccc;
    font-size: 1.125rem;
    position:absolute;
    pointer-events:none;
    left: 0.3125rem;
    top: 0.625rem;
    transition:0.2s ease all; 
    -moz-transition:0.2s ease all; 
    -webkit-transition:0.2s ease all;
  }
  .next-btn {
    position: relative;
    width: 100%;
  }

  /* active state */
  .first-step .group .my-input:focus ~ label, .my-input:valid ~ label 		{
    top: -1.875rem;
    font-size: 1.4rem;
    color:#25AB9B;
  }
  /* HIGHLIGHTER ================================== */
  .highlight {
    position:absolute;
    height:60%; 
    width: 6.25rem; 
    top: 25%; 
    left: 0;
    pointer-events:none;
    opacity:0.5;
  }
  /* BOTTOM BARS ================================= */
  .bar 	{ position:relative; display:block; width:40vw; }
  .bar:before, .bar:after 	{
    content:'';
    height: 0.125rem; 
    width:0;
    bottom: 0; 
    position:absolute;
    background:#25AB9B; 
    transition:0.2s ease all; 
    -moz-transition:0.2s ease all; 
    -webkit-transition:0.2s ease all;
  }
  .bar:before {
    left:50%;
  }
  .bar:after {
    right:50%; 
  }

  /* active state */
  input:focus ~ .bar:before, input:focus ~ .bar:after {
    width:50%;
  }
  /* active state */
  input:focus ~ .highlight {
    -webkit-animation:inputHighlighter 0.3s ease;
    -moz-animation:inputHighlighter 0.3s ease;
    animation:inputHighlighter 0.3s ease;
  }

  /* ANIMATIONS ================ */
  @-webkit-keyframes inputHighlighter {
    from { background:#5264AE; }
    to 	{ width:0; background:transparent; }
  }
  @-moz-keyframes inputHighlighter {
    from { background:#5264AE; }
    to 	{ width:0; background:transparent; }
  }
  @keyframes inputHighlighter {
    from { background:#5264AE; }
    to 	{ width:0; background:transparent; }
  }
</style>