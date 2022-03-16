<template>
  <div class="signup-container">
    <div class="first-step">
      <h1>회원가입</h1>
        <div class="group">
          <input class="my-input" type="text" id="userID" placeholder="6~16자 이내">
          <label for="userID">ID</label>
          <span class="highlight"></span>
          <span class="bar"></span>
        </div>
          
        <div class="group">
          <input class="my-input"  type="password" id="userPW" placeholder="영문 숫자를 포함한 8~16자 이내">
          <label for="userPW">PASSWORD</label>
          <span class="highlight"></span>
          <span class="bar"></span>
        </div>
        <div class="group">      
          <input class="my-input"  type="password" id="userPWConf" placeholder="비밀번호를 확인합니다">
          <label for="userPWConf">PASSWORD CHECK</label>
          <span class="highlight"></span>
          <span class="bar"></span>
        </div>
        <div class="group">
          <input class="my-input" type="text" id="userID" placeholder="이름을 입력해주세요">
          <label for="userID">이름</label>
          <span class="highlight"></span>
          <span class="bar"></span>
        </div>
        <div class="group">
          <input class="my-input" type="date" id="userID" placeholder="6~16자 이내">
          <label for="userID">생년월일</label>
          <span class="highlight"></span>
          <span class="bar"></span>
        </div>
        <button class="bttn-unite bttn-md bttn-success next-btn">NEXT</button>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
  .bttn-unite.bttn-success{
    border-radius: 10px;
    width: 300px;
    margin-bottom: 30px;
  }
  .bttn-unite.bttn-success:before{
    background: #25AB9B;
  }
  .bttn-unite.bttn-success:after{
    background: #25AB9B;
  }
  .signup-container {
    position: relative;
    top: 60px;
    width: 800px;
    margin: 0 auto;
    border: 5px solid #25AB9B;
    border-radius: 30px;
  }
  .first-step {
    width: 100%;
    position: relative;
  }
  .signup-container h1 {
    width: 500px;
    top: 0;
    position: relative;
    text-align: center;
    left: 50%;
    transform: translateX(-50%);
    font-size: 30px;
  }
  .group { 
    position:relative; 
    margin-bottom:45px; 
    width: 300px;
    left: 50%;
    transform: translateX(-50%);
  }
  .group .my-input {
    font-size:12px;
    padding: 10px;
    display:block;
    width:280px;
    border:none;
    border-bottom:1px solid #757575;
  }
  .group .my-input:focus 		{ outline:none; }

  .group label 				 {
    color:#999; 
    font-size:18px;
    position:absolute;
    pointer-events:none;
    left:5px;
    top:10px;
    transition:0.2s ease all; 
    -moz-transition:0.2s ease all; 
    -webkit-transition:0.2s ease all;
  }
  .next-btn {
    position: relative;
  }
  .first-step .check-btn {
    position: relative;
    right: -150px;
    width: 200px;
    font-size: 18px;
  }

  /* active state */
  .first-step .group .my-input:focus ~ label, .my-input:valid ~ label 		{
    top:-20px;
    font-size:16px;
    color:#5264AE;
  }
  /* HIGHLIGHTER ================================== */
  .highlight {
    position:absolute;
    height:60%; 
    width:100px; 
    top:25%; 
    left:0;
    pointer-events:none;
    opacity:0.5;
  }
  /* BOTTOM BARS ================================= */
  .bar 	{ position:relative; display:block; width:300px; }
  .bar:before, .bar:after 	{
    content:'';
    height:2px; 
    width:0;
    bottom:1px; 
    position:absolute;
    background:#5264AE; 
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