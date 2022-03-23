<template>
  <div class="search-bar">
    <h2>찾는 음식이 있으신가요 ?</h2>
    <input type="text" v-model="keyword">
    <button 
      class="material-icons search-btn"
      @click="searchKeyword"
    >search</button>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      keyword: null,
    }
  },
  methods: {
    searchKeyword() {
      this.$emit('searchKeyword', this.keyword)
    }
  }
}
</script>

<style>
.search-bar {
  background: #25AB9B;
  width: 100%;
  height: 10vh;
  display: flex;
  position: relative;
  align-items: center;
}
.search-bar h2 {
  margin: 0;
  font-size: 1.5vw;
  position: absolute;
  left: 20vw;
  color: #fff;
}
.search-bar form {
  position: absolute;
  right: 8vw;
}
.search-bar input {
  position: absolute;
  right: 8vw;
  height: 5vh;
  width: 20vw;
  border-radius: 1rem;
  border: none;
  font-size: 1vw;
  outline: none;
}
.search-bar input:focus {
  animation: input-focus .3s ease-in-out;
  animation-fill-mode: forwards;
}
.search-bar input:not(:focus) {
  animation: input-blur .3s ease-out;
}
.search-bar .search-btn {
  position: absolute;
  right: 8vw;
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
}
@keyframes input-focus {
  from {
    width: 20vw;
  }
  to {
    width: 40vw;
  }
}
@keyframes input-blur {
  from {
    width: 40vw;
  }
  to {
    width: 20vw;
  }
}
</style>