<template>
  <div class="week-calendar">
    <!-- 수정버튼 -->

    <span class="today-week"> 3월 첫째주</span>
    <span class="material-icons settings" @click="editMealTable">
      settings
    </span>
    <div class="card">
      <div class="meal-time">
        <div>아침</div>
        <div>점심</div>
        <div>저녁</div>
      </div>
      <div class="monday">
        <div class="text animate__animated animate__tada">월</div>
        <div class="meal-table-el">
          <span>밥</span>
          <span>카레</span>
          <span>배추김치</span>
        </div>
        <div class="meal-table-el">
          <span>밥</span>
          <span>돈까스</span>
          <span>샐러드</span>
          <span>각종소스</span>
          <span>콜라</span>
        </div>
        <div class="meal-table-el">
          <span
            >식단이 <br />
            없어요!</span
          >
        </div>
      </div>
      <div class="tuesday">
        <div class="text animate__animated animate__tada">화</div>
        <div class="meal-table-el">
          <span
            >식단이 <br />
            없어요!</span
          >
        </div>
        <div class="meal-table-el">식단 1개</div>
        <div class="meal-table-el">식단 1개</div>
      </div>
      <div class="wednesday">
        <div class="text animate__animated animate__tada">수</div>
        <div class="meal-table-el">
          <span
            >식단이 <br />
            없어요!</span
          >
        </div>
        <div class="meal-table-el">식단 1개</div>
        <div class="meal-table-el">식단 1개</div>
      </div>
      <div class="thursday">
        <div class="text animate__animated animate__tada">목</div>
        <div class="meal-table-el">
          <span
            >식단이 <br />
            없어요!</span
          >
        </div>
        <div class="meal-table-el">식단 1개</div>
        <div class="meal-table-el">식단 1개</div>
      </div>
      <div class="friday">
        <div class="text animate__animated animate__tada">금</div>
        <div class="meal-table-el">
          <span
            >식단이 <br />
            없어요!</span
          >
        </div>
        <div class="meal-table-el">식단 1개</div>
        <div class="meal-table-el">식단 1개</div>
      </div>
      <div class="saturday">
        <div class="text animate__animated animate__tada">토</div>
        <div class="meal-table-el">
          <span
            >식단이 <br />
            없어요!</span
          >
        </div>
        <div class="meal-table-el">식단 1개</div>
        <div class="meal-table-el">식단 1개</div>
      </div>
      <div class="sunday">
        <div class="text animate__animated animate__tada">일</div>
        <div class="meal-table-el">
          <span>식빵</span>
          <span>버터</span>
          <span>크림스프</span>
          <span>딸기잼</span>
          <span>우유</span>
        </div>
        <div class="meal-table-el">식단 1개</div>
        <div class="meal-table-el">식단 1개</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "WeekMealTable",
  data() {
    return {
      editFlag: false,
    };
  },
  methods: {
    // 수정버튼 클릭시 모든 요소 진동 효과
    editMealTable() {
      const editMeal = document.querySelectorAll(".meal-table-el");
      if (this.editFlag == true) {
        this.editFlag = false;
        for (let i = 0; i < editMeal.length; i++) {
          editMeal[i].classList.remove("clicked");
        }
      } else {
        this.editFlag = true;
        for (let i = 0; i < editMeal.length; i++) {
          editMeal[i].classList.add("clicked");
        }
      }
    },
    animationTada() {
      const mealTableEl = document.querySelectorAll(".meal-table-el");
      for (let j = 0; j < mealTableEl.length; j++) {
        mealTableEl[j].className += " animate__animated animate__jello";
      }
    },
  },
  mounted() {
    this.animationTada();
  },
};
</script>

<style scoped>
.week-calendar {
  width: 50rem;
  height: 100%;
  border-radius: 1.25rem;
  text-align: center;
}
.meal-table-el {
  width: calc(600px / 7);
  height: 7.5rem;
  border: 0.125rem solid #25ab9b;
  margin: 0.313rem;
  border-radius: 1.25rem;
  position: relative;
  text-align: center;
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  position: relative;
  top: 2.063rem;
}

.meal-table-el.clicked {
  animation-name: vibration;
  animation-duration: 0.5s;
  animation-iteration-count: infinite;
}

.meal-table-el.clicked:hover {
  cursor: pointer;
}
.card {
  display: flex;
  justify-content: center;
  align-items: center;
  align-content: center;
  position: relative;
  top: -0.625rem;
}
.meal-time {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 17.5rem;
  font-size: 1.125rem;
  font-weight: 700;
  margin: 0 0.75rem;
  position: relative;
  top: 2.75rem;
}
.text {
  font-size: 1.125rem;
  font-weight: 700;
  position: relative;
  top: 1.875rem;
}
.material-icons {
  font-size: 1.75rem;
  vertical-align: bottom;
  color: #333;
  position: relative;
  left: 19.375rem;
  bottom: 1.5rem;
}
.material-icons:hover {
  cursor: pointer;
  color: #25ab9b;
  transform: scale(1.2);
  transition: transform 0.1s;
  background-color: rgb(221, 221, 221);
  border-radius: 50%;
}
span {
  font-size: 0.875rem;
}
.today-week {
  font-size: 1.375rem;
  position: relative;
  right: 33%;
  font-weight: 700;
}

@keyframes vibration {
  0% {
    -webkit-transform: rotate(-5deg);
  }
  50% {
    -webkit-transform: rotate(5deg);
  }
  100% {
    -webkit-transform: rotate(-5deg);
  }
}
</style>
