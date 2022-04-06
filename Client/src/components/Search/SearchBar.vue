<template>
  <div class="search-bar">
    <h2>{{ userName }}님, 찾는 음식이 있으신가요?</h2>
    <input type="text" v-model="keyword" @keyup.enter="searchKeyword" />
    <button class="material-icons search-btn" @click="searchKeyword">
      search
    </button>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  data() {
    return {
      keyword: null, // 검색 키워드
      userName: null,
    };
  },
  methods: {
    searchKeyword() {
      // 현재 search 페이지일때는 emit으로 검색
      if (this.$route.path == "/search") {
        this.$emit("searchKeyword", this.keyword);
      }
      // search 페이지가 아니라면 params에 담아서 검색
      else {
        this.$router.push({
          name: "search",
          params: { keyword: this.keyword },
        });
      }
    },
  },
  computed: {
    userInfo() {
      return this.$store.getters.getUserInfo;
    },
  },
  mounted() {
    this.userName = this.userInfo.data.name;
  },
};
</script>

<style scoped>
.search-bar {
  background: #25ab9b;
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
  left: 13vw;
  color: #fff;
}
.search-bar form {
  position: absolute;
  right: 8vw;
}
.search-bar input {
  background: #fff;
  position: absolute;
  right: 13vw;
  height: 5vh;
  width: 22vw;
  border-radius: 0.7vw;
  border: none;
  font-size: 1vw;
  outline: none;
  padding-left: 1vw;
  font-family: "MinSans-Regular";
}
.search-bar input:focus {
  animation: input-focus 0.3s ease-in-out;
  animation-fill-mode: forwards;
}
.search-bar input:not(:focus) {
  animation: input-blur 0.3s ease-out;
}
.search-bar .search-btn {
  position: absolute;
  right: 13.5vw;
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
}
@keyframes input-focus {
  from {
    width: 22vw;
  }
  to {
    width: 30vw;
  }
}
@keyframes input-blur {
  from {
    width: 30vw;
  }
  to {
    width: 22vw;
  }
}
</style>
