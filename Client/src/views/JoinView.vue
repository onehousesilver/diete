<template>
  <div>
    <BannerBar 
      MainText="회원가입" 
      SubText="diète가 추천하는 다양한 식단을 받아보세요" 
    />
    <JoinFirstStep 
      v-if="currentStep===0"
      @nextStep="toSecondStep"
    />
    <JoinSecondStep
      v-else-if="currentStep===1"
      @nextStep="toFinalStep"
    />
    <JoinFinalStep
      v-else-if="currentStep===2"
      @completedForm="sendFormData"
    />
  </div>
</template>

<script>
import BannerBar from '@/components/Main/BannerBar.vue'
import JoinFirstStep from '@/components/Join/JoinFirstStep.vue'
import JoinSecondStep from '@/components/Join/JoinSecondStep.vue'
import JoinFinalStep from '@/components/Join/JoinFinalStep.vue'
import axios from 'axios'

export default {
  name: 'JoinView',
  components: {
    BannerBar,
    JoinFirstStep,
    JoinSecondStep,
    JoinFinalStep
  },
  data() {
    return {
      currentStep: 0, // 현재 단계
      // 회원가입 유저 데이터
      userData: {
        username: null, // ID
        password: null, // PW
        name: null, // 이름
        birthDate: null, // 생년월일
        height: null, // 키
        weight: null, // 몸무게
        activity: null, // 활동량(0: 적음, 1: 보통, 2: 많음)
        gender: null, // 성별(0:남자, 1:여자)
        preference: 1, // 선호식단 > 추후수정
      }
    }
  },
  methods: {
    // step 2로 이동
    toSecondStep(formData) {
      this.currentStep = 1;
      this.userData.username = formData.userId
      this.userData.password = formData.userPw
      this.userData.name = formData.userName
      this.userData.birthDate = formData.userBirth
    },
    // step final로 이동
    toFinalStep(formData){
      this.currentStep = 2;
      this.userData.height = formData.height
      this.userData.weight = formData.weight
      this.userData.activity = formData.activity
      this.userData.gender = parseInt(formData.gender)
      
    },
    // 회원가입 완료 (api요청)
    sendFormData(emitData) {
      this.userData.preference = emitData // 추후에 추가
      axios({
        method: 'post',
        url: `${process.env.VUE_APP_API_URL}/user/join/`,
        data: this.userData
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
      this.$router.push({ name: 'login' }).catch(() => {})
    }
  }

}
</script>

<style scoped>

</style>