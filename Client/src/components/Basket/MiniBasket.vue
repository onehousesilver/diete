<template>
  <div>
    <span class="material-icons basket-btn" @click="test">add</span>
    <section class="basket-list">

    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {

    }
  },
  methods: {
    test( ) {
      console.log(this.basket)
    }
  },
  computed: {
    basket() { return this.$store.state.myBasket}
  }
}
</script>

<style>
.basket-btn {
  background: #25ab9b;
  color: #fff;
  position: fixed;
  right: 0;
  font-size: 3vw;
  top: 50%;
  cursor: pointer;
}
</style>