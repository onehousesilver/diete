<template>
  <div>
    <h1>페이지를 찾을 수 없습니다. <br /> 잠시 후 최초 페이지로 이동합니다.</h1>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
  methods: {
    // 5초 후 랜딩페이지로 이동
    goToHomeAfterFiveSec(){
      setTimeout(() => {
        this.$router.push({ name: 'home' })
      }, 5000)
    }
  },
  mounted() {
    this.goToHomeAfterFiveSec()
  },
}
</script>

<style scoped>
h1 {
  text-align: center;
  top: 30vh;
  position: relative;
}

</style>