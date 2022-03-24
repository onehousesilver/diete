<template>
  <div class="signup-container">
    <input type="text" v-model="likeMenu">
    <button 
      class="bttn-unite bttn-success next-btn"
      @click="completedForm"
    >
      회원가입완료
    </button>
  </div>
</template>

<script>
export default {
  name: 'JoinSecondStep',
  data() {
    return {
      likeMenu: 1,
    }
  },
  methods: {
    completedForm() {
      this.$emit('completedForm', this.likeMenu)
    }
  }
}
</script>

<style>

</style>