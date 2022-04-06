<template>
  <div>
    <ul class="category">
      <li
        id="all"
        class="category-item category-item--current animate__animated animate__fadeInUp"
      >
        <div class="category-link" @click="clickEvent">전체</div>
      </li>
      <li id="meat" class="category-item animate__animated animate__fadeInUp">
        <div class="category-link" @click="clickEvent">고기</div>
      </li>
      <li
        id="vegetable"
        class="category-item animate__animated animate__fadeInUp"
      >
        <div class="category-link" @click="clickEvent">채소</div>
      </li>
      <li id="fish" class="category-item animate__animated animate__fadeInUp">
        <div class="category-link" @click="clickEvent">생선</div>
      </li>
      <li id="drink" class="category-item animate__animated animate__fadeInUp">
        <div class="category-link" @click="clickEvent">음료</div>
      </li>
      <li id="bread" class="category-item animate__animated animate__fadeInUp">
        <div class="category-link" @click="clickEvent">밥/빵/면</div>
      </li>
      <li id="etc" class="category-item animate__animated animate__fadeInUp">
        <div class="category-link" @click="clickEvent">기타</div>
      </li>
    </ul>
  </div>
</template>

<script>
import $ from "jquery";
export default {
  name: "CategoryBar",
  data() {
    return {
      // 먼저 선택되어있는 class
      clickCategory: "all",
    };
  },

  methods: {
    clickEvent(e) {
      // 기존의 선택되어 있는 class
      if (this.clickCategory) {
        // 클래스 제거
        $(`#${this.clickCategory}`).removeClass("category-item--current");
      }
      // 부모요소에 id가 지정되어 있다면(버튼을 클릭했을 때) 부모요소의 id, 없다면(버튼 이외의 섹션을 클릭했을 때) 자기 자신의 id 저장
      this.clickCategory = e.target.offsetParent.id
        ? e.target.offsetParent.id
        : e.target.id;
      // 클래스 추가
      $(`#${this.clickCategory}`).addClass("category-item--current");
      this.$emit('changeCategory', this.clickCategory)
    },
  },
};
</script>

<style scoped>
.category {
  display: flex;
  margin: 2vw auto 0vw;
  width: 73vw;
  cursor: pointer;
}
ul {
  list-style: none;
}

.category-item--current {
  z-index: 1;
}
.category-item--current .category-link {
  border-color: #25ab9b;
  box-shadow: inset 0 0 0 1px #25ab9b;
  color: #25ab9b;
  font-weight: 700;
}

.category-item {
  width: 100%;
}

.category-item:first-child .category-link {
  margin-left: 0;
  width: 100%;
}

.category-link {
  align-items: center;
  border: 1px solid #e6e6e6;
  box-sizing: border-box;
  color: #999;
  display: flex;
  font-size: 1vw;
  height: 6.24vh;
  justify-content: center;
  margin-left: -1px;
  text-align: center;
  transition: color 0.35s ease, box-shadow 0.35s ease;
  width: calc(100% + 1px);
}
.category-link:hover {
  color: #25ab9b;
}
</style>
