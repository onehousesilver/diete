<template>
  <div>
    <div class="day-calendar">
      <div class="day">
        <!-- 전날로 넘어가는 버튼 -->
        <span class="material-icons navigate" @click="goYesterDay">
          navigate_before
        </span>
        <!-- 오늘 날짜 -->
        {{ $moment().format("M월 DD일") }}
        <!-- 다음날로 넘어가는 버튼 -->
        <span class="material-icons navigate" @click="goTomorrow">
          navigate_next
        </span>
        <!-- 수정버튼 -->
        <span class="material-icons settings" @click="editMealTable">
          settings
        </span>
      </div>
      <div class="card">
        <div class="morning">
          <div class="morning-text to-right-underline">아침</div>
          <!-- 만약 데이터가 있으면 보여주고, 없으면 찾으러가기 버튼 활성화-->
          <div class="meal-table-el">
            <span> 식단이 없어요!</span>
            <button
              class="bttn-unite bttn-md bttn-success goToRecommend-btn"
              @click="goPocket"
            >
              내 식단 찾기
            </button>
          </div>
        </div>
        <div class="lunch">
          <div class="lunch-text to-right-underline">점심</div>
          <div class="meal-table-el">
            <span>밥</span>
            <span>소고기무국</span>
            <span>김치</span><br />
            <!-- 권장칼로리와 비교해서 색으로 위험여부 보여주기 -->
            <span style="color: tomato">1500kcal</span>
          </div>
        </div>
        <div class="dinner">
          <div class="dinner-text to-right-underline">저녁</div>
          <div class="meal-table-el">
            <span>밥</span>
            <span>소고기무국</span>
            <span>김치</span><br />
            <span style="color: royalblue">1500kcal</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DayMealTable",
  data() {
    return {
      editFlag: false,
    };
  },
  methods: {
    goYesterDay() {},
    goPocket() {
      this.$router.push({ name: "menu" });
    },
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
.day-calendar {
  width: 800px;
  height: 100%;
  /* border: 2px solid #25ab9b; */
  border-radius: 20px;
}
.day {
  font-size: 24px;
  text-align: center;
  margin-top: 20px;
  margin-left: 30px;
  font-weight: 700;
}
.meal-table-el {
  width: calc(700px / 3);
  height: 300px;
  border: 3px solid #25ab9b;
  margin: 5px;
  border-radius: 20px;
  position: relative;
  top: 20px;
  text-align: center;
  font-size: 20px;
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

.morning-text,
.lunch-text,
.dinner-text {
  font-size: 24px;
  text-align: center;
  margin-top: 30px;
  font-weight: 700;
}

.goToRecommend-btn {
  border-radius: 10px;
  width: 100px;
  font-size: 14px;
  margin: 0 auto;
  position: relative;
  margin-top: 10px;
}
.navigate {
  font-size: 32px;
  vertical-align: bottom;
  color: #333;
}
.material-icons:hover {
  cursor: pointer;
  color: #25ab9b;
  transform: scale(1.2);
  transition: transform 0.1s;
  background-color: rgb(221, 221, 221);
  border-radius: 50%;
}

.settings {
  position: relative;
  font-size: 28px;
  left: 240px;
  color: #333;
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
