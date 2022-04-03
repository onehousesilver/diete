<template>
  <div class="search-bar">
    <h2>찾는 음식이 있으신가요 ?</h2>
    <input type="text" v-model="keyword" @keyup.enter="searchKeyword">
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
      keyword: null,    // 검색 키워드
    }
  },
  methods: {
    searchKeyword() {
      // 현재 search 페이지일때는 emit으로 검색
      if(this.$route.path=='/search'){
        this.$emit('searchKeyword', this.keyword)
      }
      // search 페이지가 아니라면 params에 담아서 검색
      else{
        this.$router.push({ name: 'search', params: { keyword: this.keyword }})
      }
    },
  }
}
</script>

<style scoped>

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
  background: #fff;
  position: absolute;
  right: 8vw;
  height: 5vh;
  width: 20vw;
  border-radius: 1rem;
  border: none;
  font-size: 1vw;
  outline: none;
  font-family: 'MinSans-Regular';
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