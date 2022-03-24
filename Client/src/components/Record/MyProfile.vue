<template>
  <div>
    <div id="wrap">
      <div id="my-profile">
        <div class="my-summary-wrap">
          <!-- 프로필 사진, 유저 성별에 따라 프로필 사진 변경 -->
          <div class="profile-wrap">
            <div class="profile-thumb-wrap">
              <div v-if="userForm.userGender == 0">
                <img
                  src="../../assets/profile/male_profile.svg"
                  class="thumb-profile"
                  alt="프로필사진"
                />
              </div>
              <div v-else>
                <img
                  src="../../assets/profile/female_profile.svg"
                  class="thumb-profile"
                  alt="프로필사진"
                />
              </div>
            </div>
            {{ userInfo }}
            <div class="profile-info-wrap">
              안녕하세요.
              <!-- 유저 이름 -->
              <div class="profile-name cut-txt">{{ userForm.userName }} 님</div>
              <!-- 프로필 편집 버튼 -->
              <button
                class="bttn-unite bttn-md bttn-success edit-btn"
                v-show="!edit"
                @click="editProfile"
              >
                프로필 편집
              </button>
              <!-- 프로필 수정 완료 버튼 -->
              <button
                class="bttn-unite bttn-md bttn-success edit-done-btn"
                v-show="edit"
                @click="editProfile"
              >
                편집완료
              </button>
            </div>
          </div>

          <!-- 유저 입력정보 -->
          <div class="my-info-wrap">
            <ul class="my-info-list">
              <li class="my-info">
                <!-- 아이디, 수정불가 -->
                <span class="my-info-tit">아이디</span><br />
                <strong class="my-info-txt">{{ userForm.userId }}</strong>
              </li>
              <li class="my-info">
                <!-- 키, 수정가능(숫자만 가능) -->
                <span class="my-info-tit">키</span><br />
                <strong v-if="!edit">{{ userForm.userHeight }} cm</strong>
                <strong v-else
                  ><input
                    type="number"
                    value="value"
                    min="0"
                    step="10"
                    required
                /></strong>
              </li>
              <li class="my-info">
                <!-- 몸무게, 수정가능(숫자만 가능) -->
                <span class="my-info-tit">몸무게</span><br />
                <strong v-if="!edit">{{ userForm.userWeight }} kg</strong>
                <strong v-else
                  ><input
                    type="number"
                    value="value"
                    min="0"
                    step="10"
                    required
                /></strong>
              </li>
              <li class="my-info">
                <!-- 권장칼로리, 수정불가 -->
                <span class="my-info-tit">권장칼로리</span><br />
                <strong>{{ userForm.userKcal }} <span>kcal</span></strong>
              </li>
              <li class="my-info">
                <!-- 활동량, 수정가능(옵션선택) -->
                <span class="my-info-tit"
                  >활동량
                  <div class="material-icons help" @click="showImg">
                    help_outline
                  </div>
                  <!-- 활동량 설명 이미지 -->
                  <img
                    v-show="showImgflag"
                    class="user-activity-img"
                    src="../../assets/profile/user_activity_box.png"
                    alt="" /></span
                ><br />
                <!-- 활동량 수정 선택창 -->
                <strong v-if="!edit">{{ userForm.userActivity }}</strong>
                <strong v-else
                  ><select name="" id="">
                    <option value="" disabled>활동량을 선택해주세요</option>
                    <option value="적음">적음</option>
                    <option value="보통">보통</option>
                    <option value="많음">많음</option>
                  </select></strong
                >
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
      userForm: {
        userId: "tori",
        userName: "채은",
        userHeight: 200,
        userWeight: 200,
        userKcal: 2000,
        // 0 남자 1 여자
        userGender: 1,
        // 0 적음 1보통 2많음
        userActivity: "적음",
      },
      edit: false,
      showImgflag: false,
    };
  },
  methods: {
    goMyAnalysis() {
      this.$emit("goMyAnalysis");
    },
    openMessage() {
      this.$emit("openMessage");
    },
    // 프로필 편집 버튼
    editProfile() {
      this.edit = !this.edit;
    },
    // 활동량에 대한 정보 보여주기
    showImg() {
      this.showImgflag = !this.showImgflag;
    },
  },
  computed: {
    userInfo() { return this.$store.getters.getUserInfo}
  }
};
</script>

<style scoped>
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
  width: 120px;
  height: 120px;
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
.user-activity-img {
  position: absolute;
  box-shadow: 2px 2px 10px rgb(173, 173, 173);
  border-radius: 10px;
  top: 238px;
  right: 58px;
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

.edit-btn {
  border-radius: 0;
}

.edit-done-btn {
  border-radius: 0;
}
.bttn-unite.bttn-md {
  font-size: 14px;
}
input {
  border: solid 2px #25ab9b;
  width: 150px;
  height: 20px;
  border-radius: 5px;
  text-align: center;
}
select {
  border: solid 2px #25ab9b;
  width: 150px;
  height: 25px;
  font-size: 14px;
  text-align: center;
  border-radius: 5px;
}
</style>
