<template>
  <div class="signup-container">
    <input type="text" v-model="likeMenu">
    <button 
      class="bttn-unite bttn-md bttn-success next-btn"
      @click="completedForm"
    >
      다음 단계
    </button>
  </div>
</template>

<script>
export default {
  name: 'JoinSecondStep',
  data() {
    return {
      likeMenu: null,
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