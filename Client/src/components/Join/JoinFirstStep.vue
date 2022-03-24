<template>
  <div class="signup-container">
    <div class="first-step">
        <div class="group">
          <input 
            class="my-input" 
            type="text" 
            id="userID" 
            placeholder="영문, 숫자를 각 1자 이상 포함해 8자 이상 16자 미만으로 입력해주세요"
            v-model="formData.userId"
          >
          <label for="userID">아이디</label>
          <span class="highlight"></span>
          <span class="bar"></span>
          <button class="bttn-unite bttn-success check-btn" @click="userDuplicateCheck">중복체크</button>
          <div v-show="idInputFlag">
            <div class="error-msg" v-if="duplicateCheckFlag==1" style="color:green">
              <span class="material-icons">check_circle</span>
              <span>아이디 중복체크가 통과되었습니다.</span>
            </div>
            <div class="error-msg" v-else-if="duplicateCheckFlag==0" style="color:red">
              <span class="material-icons">cancel</span>
              <span>이미 존재하는 아이디 입니다.</span>
            </div>
            <div class="error-msg" v-else style="color:red">
              <span class="material-icons">cancel</span>
              <span>유효하지 않은 아이디 입니다.</span>
            </div>
          </div>
        </div>
          
        <div class="group">
          <input 
            class="my-input"  
            type="password" 
            id="userPW" 
            placeholder="영문, 숫자, 특수문자를 각 1자 이상 포함해 8자 이상 16자 미만으로 입력해주세요"
            v-model="formData.userPw"
            @input="passwordValidation"
          >
          <label for="userPW">비밀번호</label>
          <span class="highlight"></span>
          <span class="bar"></span>
          <div v-show="pwInputFlag">
            <div class="error-msg" v-if="passwordValidateFlag" style="color:green">
              <span class="material-icons">check_circle</span>
              <span>비밀번호가 유효합니다.</span>
            </div>
            <div class="error-msg" v-else style="color:red">
              <span class="material-icons">cancel</span>
              <span>비밀번호가 유효하지 않습니다.</span>
            </div>
          </div>
        </div>

        <div class="group">
          <input 
            class="my-input"  
            type="password" 
            id="userPWConf" 
            placeholder="비밀번호를 확인합니다"
            v-model="formData.userPwConf"
            @input="passwordConfirm"
          >
          <label for="userPWConf">비밀번호 확인</label>
          <span class="highlight"></span>
          <span class="bar"></span>
          <div v-show="passwordValidateFlag">
            <div class="error-msg" v-if="passwordCheckFlag" style="color:green">
              <span class="material-icons">check_circle</span>
              <span>비밀번호가 일치합니다.</span>
            </div>
            <div class="error-msg" v-else style="color:red">
              <span class="material-icons">cancel</span>
              <span>비밀번호가 다릅니다.</span>
            </div>
          </div>
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
          <div v-show="nameInputFlag">
            <div class="error-msg" v-if="formData.userName" style="color:green">
              <span class="material-icons">check_circle</span>
              <span>확인 되었습니다.</span>
            </div>
            <div class="error-msg" v-else style="color:red">
              <span class="material-icons">cancel</span>
              <span>필수 항목입니다.</span>
            </div>
          </div>
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
          <div v-show="birthInputFlag">
            <div class="error-msg" v-if="formData.userBirth" style="color:green">
              <span class="material-icons">check_circle</span>
              <span>확인 되었습니다.</span>
            </div>
            <div class="error-msg" v-else style="color:red">
              <span class="material-icons">cancel</span>
              <span>필수 항목입니다.</span>
            </div>
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
import axios from 'axios'
import { BASE_API_URL } from '@/config/config.js'
export default {
  name: 'JoinFirstStep',
  data() {
    return {
      // 유저 데이터
      formData: {
        userId: null,
        userPw: null,
        userPwConf: null,
        userName: null,
        userBirth: null
      },
      // 에러메시지 출력을 위한 flag
      idInputFlag: false,
      pwInputFlag: false,
      nameInputFlag: false,
      birthInputFlag: false,

      // form 유효성 검사 확인 flag
      duplicateCheckFlag: 2,
      passwordValidateFlag: false,
      passwordCheckFlag: false,
      
    }
  },
  methods: {
    // 다음단계로 이동
    nextStep() {
      // 모든 입력사항 체크 완료
      if (this.duplicateCheckFlag===1 && this.passwordValidateFlag && this.passwordCheckFlag && !this.userName && !this.userBirth){
        // 부모 컴포넌트에 emit
        this.$emit('nextStep', this.formData);
      }
      // 미입력된 폼이 있을 때 에러메시지 v-show
      else {
        this.idInputFlag = true;
        this.pwInputFlag = true;
        this.nameInputFlag = true;
        this.birthInputFlag = true;
      }
    },

    // ID 중복체크
    userDuplicateCheck() {
      // 중복체크 버튼 클릭 시 에러메시지 출력
      this.idInputFlag = true
      if(this.formData.userId){
        // JS 정규표현식. ID가 영문자, 숫자가 모두 포함된 8~15자 여야 유효
        const idRule = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,15}$/;
        // const idRule = /^[A-Za-z\d]{8,15}$/;
        // 유효하지 않은 ID일때 에러메시지 상태변경
        if (!idRule.test(this.formData.userId)){
          this.duplicateCheckFlag = 2
        }
        // 유효한 ID일때 서버에 중복체크 요청
        else {
        axios({
          method: 'get',
          url: `${BASE_API_URL}/user/id/${this.formData.userId}/`
        })
          .then((res) => {
            // 중복되지 않은 아이디 일때 유효성 검사 통과
            this.duplicateCheckFlag = res.data.isUnique ? 1 : 0
            console.log(res)
          })
          .catch(() => {})
        }
      }
    },

    // PW 유효성검사
    passwordValidation() {
      this.pwInputFlag = true
      // JS 정규표현식. PW가 영문자, 숫자, 특수문자가 모두 포함되고 8~15자 여야 유효
      const pwRule = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,15}$/;
      // 유효한 PW일때 유효성검사 통과
      this.passwordValidateFlag = pwRule.test(this.formData.userPw) ? true : false
    },
    
    // PWConf 유효성검사
    passwordConfirm(){
      // PW가 유효한 경우에
      if (this.passwordValidateFlag){
        // PW, PW확인이 일치할 경우 유효성검사 통과
        this.passwordCheckFlag = (this.formData.userPw == this.formData.userPwConf)
      }
    },
    
  }
}
</script>

<style scoped>
  /* Button */
  .bttn-unite.bttn-success{
    border-radius: 0.625rem;
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
  .error-msg {
    display: flex;
    align-items: center;
    position: absolute;
    right: 0;
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
    width: 18.75rem;
    margin-bottom: 1.875rem;
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