<template>
  <div id="my-profile">
    <div class="my-summary-wrap">
      <div class="profile-wrap">
        <div class="profile-thumb-wrap">
          <img src="" alt="" />
        </div>

        <div class="profile-info-wrap">
          안녕하세요.
          <div class="profile-name cut-txt">{{ userName }} 님</div>
          <label for="uplodad" class="btn-profile-thumb">프로필 편집</label>
        </div>
      </div>

      <div class="my-info-wrap">
        <ul class="my-info-list">
          <li class="my-info">
            <span class="my-info-tit">아이디</span><br />
            <strong class="my-info-txt">{{ userId }}</strong>
          </li>
          <li class="my-info">
            <span class="my-info-tit">키</span><br />
            <strong>{{ userHeight }}</strong>
          </li>
          <li class="my-info">
            <span class="my-info-tit">몸무게</span><br />
            <strong>{{ userWeight }}</strong>
          </li>
          <li class="my-info">
            <span class="my-info-tit">권장칼로리</span><br />
            <strong>{{ userKcal }}</strong>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MyProfile",
  data() {
    return {
      userId: "tori",
      userName: "채은",
      userHeight: 200,
      userWeight: 200,
      userKcal: 200,
    };
  },
  methods: {
    nextStep() {
      this.$emit("nextStep", this.formData);
    },
  },
};
</script>

<style>
#my-profile {
  box-sizing: border-box;
}
li {
  list-style: none;
}
.my-summary-warp {
  padding: 50px 10%;
  background: none;
  overflow: hidden;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  -webkit-text-size-adjust: none;
  vertical-align: baseline;
}
.profile-wrap {
  position: relative;
  float: left;
  width: 34%;
  padding-left: 137px;
  min-height: 120px;
}
.profile-info-wrap {
  padding: 14px 0 0;
  font-size: 18px;
  color: #a1a4a8;
}
.profile-info-wrap:hover {
  text-decoration: none;
}
.profile-name {
  font-size: 24px;
}
.btn-profile-thumb {
  width: 103px;
  height: 28px;
  font-size: 12px;
  line-height: 26px;
  letter-spacing: -0.6px;
}
.btn-profile-thumb {
  display: block;
  width: 103px;
  height: 24px;
  margin: 6px 0 0;
  color: #b7b7b7;
  font-size: 12px;
  border: 1px solid #dfdfdf;
  text-align: center;
  line-height: 22px;
}
label {
  cursor: pointer;
}
.my-info-wrap {
  float: right;
  width: 65%;
  margin: 30px 0 0;
}
.my-info-list {
  overflow: hidden;
}
.my-info {
  float: left;
  width: 24%;
  margin: 0;
  padding: 7px 0;
  background: #ffffff;
  border-right: 1px solid #eaeaea;
  text-align: center;
}
.my-info-tit {
  height: auto;
  font-size: 14px;
  letter-spacing: -0.3px;
  color: #909397;
}
.my-info-txt {
  margin: 2px 0 0;
  font-size: 22px;
  letter-spacing: -0.5px;
  color: #2f3338;
}
.my-info:nth-child(2n) {
  margin: 0 1% 1% 0;
}
.my-info:last-child {
  border: 0;
}
</style>
