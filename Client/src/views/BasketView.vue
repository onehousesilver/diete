<template>
  <div>
    <BannerBar MainText="오늘의 한끼" SubText="SubText"/>
    <div class="basket-container">
      <FoodList />
    </div>
  </div>
</template>

<script>
import BannerBar from '@/components/Main/BannerBar.vue'
import FoodList from '@/components/Basket/FoodList.vue'
export default {
  name: 'BasketView',
  components: {
    BannerBar,
    FoodList
  }
}
</script>

<style scoped>
.basket-container {
  width: calc(100vw - 12.5rem);
  height: 70vh;
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  background: #ccc;
}
</style>