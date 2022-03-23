<template>
  <div>
    <div class="week-calendar">
      <!-- 수정버튼 -->
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
          <div class="text">월</div>
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
          <div class="text">화</div>
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
          <div class="text">수</div>
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
          <div class="text">목</div>
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
          <div class="text">금</div>
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
          <div class="text">토</div>
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
          <div class="text">일</div>
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
  },
};
</script>

<style scoped>
.week-calendar {
  width: 800px;
  height: 100%;
  border-radius: 20px;
  text-align: center;
}
.meal-table-el {
  width: calc(600px / 7);
  height: 120px;
  border: 2px solid #25ab9b;
  margin: 5px;
  border-radius: 20px;
  position: relative;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
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
}
.meal-time {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 280px;
  font-size: 20px;
  font-weight: 700;
  margin: 0 12px;
}
.text {
  font-size: 20px;
  font-weight: 700;
}
.material-icons {
  font-size: 28px;
  vertical-align: bottom;
  color: #333;
  position: relative;
  left: 350px;
  bottom: 20px;
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
  font-size: 14px;
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
