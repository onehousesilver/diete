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
                  ><input type="number" v-model="userForm.userHeight"
                /></strong>
              </li>
              <li class="my-info">
                <!-- 몸무게, 수정가능(숫자만 가능) -->
                <span class="my-info-tit">몸무게</span><br />
                <strong v-if="!edit">{{ userForm.userWeight }} kg</strong>
                <strong v-else
                  ><input type="number" v-model="userForm.userWeight"
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
                  ><select v-model="userForm.userActivity">
                    <option disabled>활동량을 선택해주세요</option>
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
import axios from "axios";
import { mapActions } from "vuex";

export default {
  name: "MyProfile",
  data() {
    return {
      userForm: {
        userId: null,
        userName: null,
        userHeight: null,
        userWeight: null,
        userKcal: null,
        userGender: null,
        userActivity: null,
      },
      edit: false,
      showImgflag: false,
    };
  },
  methods: {
    ...mapActions(["updateUserInfo"]),
    setToken: function () {
      const token = localStorage.getItem("userToken");
      const config = {
        Authorization: `JWT ${token}`,
      };
      return config;
    },
    goMyAnalysis() {
      this.$emit("goMyAnalysis");
    },
    openMessage() {
      this.$emit("openMessage");
    },
    // 프로필 편집 버튼
    editProfile() {
      this.edit = !this.edit;
      this.$emit("editMode");
      if (!this.edit) {
        axios({
          method: "put",
          url: `${process.env.VUE_APP_API_URL}/user/update/`,
          data: {
            height: this.userForm.userHeight,
            weight: this.userForm.userWeight,
            activity: this.userForm.userActivity,
          },
          headers: this.setToken(),
        })
          .then((res) => {
            // kcal state 변경
            this.updateUserInfo(res.data);
            // 컴포넌트내의 data 변경
            this.userForm.userKcal = res.data.kcal;
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
    // 활동량에 대한 정보 보여주기
    showImg() {
      this.showImgflag = !this.showImgflag;
    },
  },
  computed: {
    userInfo() {
      return this.$store.getters.getUserInfo;
    },
  },
  mounted() {
    this.userForm.userId = this.userInfo.data.username;
    this.userForm.userName = this.userInfo.data.name;
    this.userForm.userHeight = this.userInfo.data.height;
    this.userForm.userWeight = this.userInfo.data.weight;
    this.userForm.userKcal = this.userInfo.data.kcal;
    this.userForm.userGender = this.userInfo.data.gender;
    this.userForm.userActivity = this.userInfo.data.activity;
  },
};
</script>

<style scoped>
input {
  outline: none;
  font-family: "MinSans-Regular";
}
#wrap {
  box-sizing: border-box;
  min-width: 20rem;
  padding-top: 3.5rem;
}
#my-profile {
  box-sizing: border-box;
}
li {
  list-style: none;
}
.my-summary-wrap {
  background: none;
  box-sizing: border-box;
  padding: 0.625rem 10%;
  height: 7vw;
}
.profile-wrap {
  float: left;
  width: 15vw;
  box-sizing: border-box;
  position: relative;
  padding-left: 4vw;
}
.profile-thumb-wrap {
  box-sizing: border-box;
  position: absolute;
  top: 0;
  left: 0;
  width: 6.4vw;
  height: 6.4vw;
}
.thumb-profile {
  box-sizing: border-box;
  vertical-align: middle;
  border: 0;
  width: 100%;
}
.profile-info-wrap {
  box-sizing: border-box;
  color: #a1a4a8;
  padding-top: 1.1vw;
  padding-left: 3.1vw;
  font-size: 1.1vw;
}
.profile-info-wrap:hover {
  text-decoration: none;
}
.profile-name {
  color: #3d4248;
  font-size: 1.1vw;
  font-weight: bold;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  word-break: break-all;
  box-sizing: border-box;
}

label {
  cursor: pointer;
}
.my-info-wrap {
  float: right;
  width: 52vw;
  box-sizing: border-box;
}
.my-info-list {
  box-sizing: border-box;
}
.my-info {
  float: left;
  width: 10vw;
  margin: 0;
  padding: 0.37vw 0;
  background: #ffffff;
  border-right: 0.063rem solid #eaeaea;
  text-align: center;
}

.help {
  font-size: 0.95vw;
  vertical-align: top;
}
.user-activity-img {
  position: absolute;
  box-shadow: 2px 2px 10px rgb(173 173 173);
  border-radius: 0.5vw;
  background-color: #fff;
  left: 81.5vw;
  top: 8.8vw;
  z-index: 4;
}

.help:hover {
  cursor: pointer;
}

.my-info-tit {
  height: auto;
  font-size: 0.7vw;
  display: block;
  color: #909397;
  box-sizing: border-box;
}

.my-info:nth-child(2n) {
  margin: 0 1% 1% 0;
  width: 10vw;
  padding: 0.438rem 0;
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
  top: 0.5vw;
  font-size: 0.8vw;
}
input {
  border: solid 2px #25ab9b;
  width: 7vw;
  height: 1vw;
  border-radius: 0.313rem;
  text-align: center;
}
select {
  border: solid 2px #25ab9b;
  width: 7.5vw;
  height: 1.2vw;
  font-size: 0.75vw;
  text-align: center;
  border-radius: 0.313rem;
}
</style>
