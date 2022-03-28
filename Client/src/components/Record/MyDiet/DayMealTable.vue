<template>
  <div>
    <div class="day-calendar">
      <span id="month-text"></span>
      <div class="day">
        <!-- 전날로 넘어가는 버튼 -->
        <span class="material-icons navigate"> navigate_before </span>
        <!-- 오늘 날짜 -->
        <span id="today">{{ todayStr }}</span>

        <!-- 다음날로 넘어가는 버튼 -->
        <span class="material-icons navigate"> navigate_next </span>
        <!-- 수정버튼 -->
        <span class="material-icons settings" @click="editMealTable">
          settings
        </span>
      </div>
      <div class="menu-card">
        <div class="morning">
          <div class="morning-text animate__animated animate__fadeInUp">
            아침
          </div>
          <!-- 만약 데이터가 있으면 보여주고, 없으면 찾으러가기 버튼 활성화-->
          <div class="meal-table-el animate__animated animate__zoomIn">
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
          <div
            class="lunch-text to-right-underline animate__animated animate__fadeInUp"
          >
            점심
          </div>
          <div class="meal-table-el animate__animated animate__zoomIn">
            <span>밥</span>
            <span>소고기무국</span>
            <span>김치</span><br />
            <!-- 권장칼로리와 비교해서 색으로 위험여부 보여주기 -->
            <span class="color-change">{{ sumFoodKcal }} kcal</span>
          </div>
        </div>
        <div class="dinner">
          <div
            class="dinner-text to-right-underline animate__animated animate__fadeInUp"
          >
            저녁
          </div>
          <div class="meal-table-el animate__animated animate__zoomIn">
            <span>밥</span>
            <span>소고기무국</span>
            <span>김치</span><br />
            <span class="color-change">{{ sumFoodKcal }} kcal</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import moment from "vue-moment";
export default {
  name: "DayMealTable",
  data() {
    return {
      userForm: {
        userId: "tori",
        userName: "채은",
        userHeight: 200,
        userWeight: 200,
        userKcal: 2000,
        // 0 남자 1 여자
        userGender: 1,
        // 0 적음 1보통 2많음
        userActivity: "적음",
      },
      editFlag: false,
      show: true,
      sumFoodKcal: 1000,
      today: new Date(),
      todayStr: "",
    };
  },
  props: {
    userKcal: Number,
  },
  methods: {
    goPocket() {
      this.$router.push({ name: "menu" });
    },
    test() {
      this.today = this.today.getDate();
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
  mounted() {
    this.todayStr = `${this.today.getMonth() + 1}월 ${this.today.getDate()}일`;
  },
};
</script>

<style scoped>
.day-calendar {
  width: 50rem;
  height: 100%;
  border-radius: 1.25rem;
}
.day {
  font-size: 1.5rem;
  text-align: center;
  margin-left: 1.875rem;
  font-weight: 700;
}

#month-text {
  font-size: 1.875rem;
  display: inline-block;
  text-align: center;
  margin-bottom: 1.25rem;
  margin-top: -1.25rem;
  position: relative;
  left: 45%;
  font-weight: 700;
}
.meal-table-el {
  width: calc(700px / 3);
  height: 300px;
  border: 0.188rem solid #25ab9b;
  margin: 0.313rem;
  border-radius: 1.25rem;
  position: relative;
  top: 1.25rem;
  text-align: center;
  font-size: 1.25rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  font-weight: 700;
}
.meal-table-el.clicked {
  animation-name: vibration;
  animation-duration: 0.5s;
  animation-iteration-count: infinite;
}
.meal-table-el.clicked:hover {
  cursor: pointer;
}
.color-change.red {
  color: red;
}
.color-change.blue {
  color: blue;
}
.menu-card {
  display: flex;
  justify-content: center;
  align-items: center;
  align-content: center;
}

.morning-text,
.lunch-text,
.dinner-text {
  font-size: 1.5rem;
  text-align: center;
  margin-top: 1.875rem;
  font-weight: 700;
}

.goToRecommend-btn {
  border-radius: 0.625rem;
  width: 6.25rem;
  font-size: 0.875rem;
  margin: 0 auto;
  position: relative;
  margin-top: 0.625rem;
}
.navigate {
  font-size: 2rems;
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
  font-size: 1.75rem;
  left: 17rem;
  bottom: 4.125rem;
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
