<template>
  <div>
    <BannerBar 
      MainText="회원가입" 
      SubText="diète가 추천하는 다양한 식단을 받아보세요" 
    />
    <JoinFirstStep 
      v-if="currentStep===0"
      @nextStep="nextStep"
    />
    <JoinSecondStep
      v-else-if="currentStep===1"
      @completedForm="sendFormData"
    />
  </div>
</template>

<script>
import BannerBar from '@/components/Main/BannerBar.vue'
import JoinFirstStep from '@/components/Join/JoinFirstStep.vue'
import JoinSecondStep from '../../../Client/src/components/Join/JoinSecondStep.vue'

export default {
  name: 'JoinView',
  components: {
    BannerBar,
    JoinFirstStep,
    JoinSecondStep
  },
  data() {
    return {
      currentStep: 0, // 
    }
  },
  methods: {
    // step 2로 이동
    nextStep(formData) {
      this.currentStep ++;
      console.log(formData)
    },
    // 회원가입 완료 (api요청)
    sendFormData(emitData) {
      console.log(emitData)
      this.$router.push({ name: 'login' }).catch(() => {})
    }
  }

}
</script>

<style scoped>

</style>