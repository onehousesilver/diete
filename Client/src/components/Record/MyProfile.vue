<template>
  <div>
    <div id="wrap">
      <div id="my-profile">
        <div class="my-summary-wrap">
          <div class="profile-wrap">
            <div class="profile-thumb-wrap">
              <div v-if="userGender == 0">
                <img
                  src="../../assets/Profile/male_profile.svg"
                  class="thumb-profile"
                  alt="프로필사진"
                />
              </div>
              <div v-else-if="userGender == 1">
                <img
                  src="../../assets/Profile/female_profile.svg"
                  class="thumb-profile"
                  alt="프로필사진"
                />
              </div>
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
                <!-- 변경가능 -->
                <span class="my-info-tit">키(cm)</span><br />
                <strong>{{ userHeight }}</strong>
              </li>
              <li class="my-info">
                <!-- 변경가능 -->
                <span class="my-info-tit">몸무게</span><br />
                <strong>{{ userWeight }} kg</strong>
              </li>
              <li class="my-info">
                <span class="my-info-tit">권장칼로리</span><br />
                <strong>{{ userKcal }} <span>kcal</span></strong>
              </li>
              <li class="my-info">
                <span class="my-info-tit"
                  >활동량
                  <span class="material-icons help" @mouseover="openMessage">
                    help_outline
                  </span></span
                ><br />

                <strong>{{ userActivity }}</strong>
              </li>
            </ul>
          </div>
        </div>
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
      userKcal: 2000,
      // 0 남자 1 여자
      userGender: 1,
      // 0 적음 1보통 2많음
      userActivity: "적음",
    };
  },
  methods: {
    goMyAnalysis() {
      this.$emit("goMyAnalysis");
    },
    openMessage() {
      this.$emit("openMessage");
    },
  },
};
</script>

<style>
#wrap {
  box-sizing: border-box;
  min-width: 320px;
  padding-top: 56px;
}
#my-profile {
  box-sizing: border-box;
}
li {
  list-style: none;
}
.my-summary-wrap {
  background: none;
  overflow: hidden;
  box-sizing: border-box;
  padding: 10px 10%;
}
.profile-wrap {
  float: left;
  width: 34%;
  padding-left: 137px;
  min-height: 120px;
  box-sizing: border-box;
  position: relative;
  padding-left: 100px;
  min-height: 84px;
}
.profile-thumb-wrap {
  width: 120px;
  height: 120px;
  box-sizing: border-box;
  position: absolute;
  top: 0;
  left: 0;
  width: 130px;
  height: 130px;
  overflow: hidden;
}
.thumb-profile {
  box-sizing: border-box;
  width: 100%;
  vertical-align: middle;
  border: 0;
  width: 100%;
}
.profile-info-wrap {
  box-sizing: border-box;
  color: #a1a4a8;
  font-size: 14px;
  padding: 24px 0 0;
  padding-left: 60px;
  font-size: 18px;
}
.profile-info-wrap:hover {
  text-decoration: none;
}
.profile-name {
  color: #3d4248;
  font-size: 24px;
  font-weight: bold;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  word-break: break-all;
  box-sizing: border-box;
}
.btn-profile-thumb {
  width: 103px;
  height: 28px;
  font-size: 12px;
  line-height: 26px;
  letter-spacing: -0.6px;
  box-sizing: border-box;
  display: block;
  margin: 6px 0 0;
  color: #b7b7b7;
  border: 1px solid #dfdfdf;
  text-align: center;
}

label {
  cursor: pointer;
}
.my-info-wrap {
  float: right;
  width: 65%;
  box-sizing: border-box;
}
.my-info-list {
  overflow: hidden;
  box-sizing: border-box;
}
.my-info {
  float: left;
  width: 19%;
  margin: 0;
  padding: 7px 0;
  background: #ffffff;
  border-right: 1px solid #eaeaea;
  text-align: center;
}

.help {
  font-size: 18px;
  vertical-align: top;
}

.help:hover {
  cursor: pointer;
}

.my-info-tit {
  height: auto;
  font-size: 14px;
  letter-spacing: -0.3px;
  display: block;
  color: #909397;
  box-sizing: border-box;
}
.my-info-txt {
  margin: 2px 0 0;
  font-size: 20px;
  letter-spacing: -0.5px;
  color: #2f3338;
}
.my-info:nth-child(2n) {
  margin: 0 1% 1% 0;
  width: 19%;
  padding: 7px 0;
  background: #ffffff;
  border-right: 1px solid #eaeaea;
  text-align: center;
}
.my-info:last-child {
  border: 0;
  margin: 0 1% 1% 0;
}
</style>
