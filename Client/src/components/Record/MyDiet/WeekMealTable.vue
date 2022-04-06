<template>
  <div class="week-calendar">
    <!-- 수정버튼 -->
    <!-- <select name="week-select" class="week-select" v-model="targetWeek">
      <option class="week-item" value="twolast">지지난주</option>
      <option class="week-item" value="last">지난주</option>
      <option class="week-item" value="current">이번주</option>
    </select> -->
    <div class="my-card">
      <div class="meal-time">
        <div>아침</div>
        <div>점심</div>
        <div>저녁</div>
      </div>
      <div class="monday">
        <div class="text animate__animated animate__tada">월</div>
        <div 
          v-for="(meal, idx) in monData"
          :key="idx"
          class="meal-table-el animate__animated animate__jello"
        >
          <div class="meal-table-item">
            <div
              v-for="(food, index) in meal.menus"
              :key="index"
            >
                {{ food.foodName }}
            </div>
          </div>
        </div> 
      </div>
      <div class="tuesday">
        <div class="text animate__animated animate__tada">화</div>
        <div 
          v-for="(meal, idx) in tueData"
          :key="idx"
          class="meal-table-el animate__animated animate__jello"
        >
          <div class="meal-table-item">
            <div
              v-for="(food, index) in meal.menus"
              :key="index"
            >
                {{ food.foodName }}
            </div>
          </div>
        </div> 
      </div>
      <div class="wednesday">
        <div class="text animate__animated animate__tada">수</div>
        <div 
          v-for="(meal, idx) in wedData"
          :key="idx"
          class="meal-table-el animate__animated animate__jello"
        >
          <div class="meal-table-item">
            <div
              v-for="(food, index) in meal.menus"
              :key="index"
            >
                {{ food.foodName }}
            </div>
          </div>
        </div> 
      </div>
      <div class="thursday">
        <div class="text animate__animated animate__tada">목</div>
        <div 
          v-for="(meal, idx) in thuData"
          :key="idx"
          class="meal-table-el animate__animated animate__jello"
        >
          <div class="meal-table-item">
            <div
              v-for="(food, index) in meal.menus"
              :key="index"
            >
                {{ food.foodName }}
            </div>
          </div>
        </div> 
      </div>
      <div class="friday">
        <div class="text animate__animated animate__tada">금</div>
        <div 
          v-for="(meal, idx) in friData"
          :key="idx"
          class="meal-table-el animate__animated animate__jello"
        >
          <div class="meal-table-item">
            <div
              v-for="(food, index) in meal.menus"
              :key="index"
            >
                {{ food.foodName }}
            </div>
          </div>
        </div> 
      </div>
      <div class="saturday">
        <div class="text animate__animated animate__tada">토</div>
        <div 
          v-for="(meal, idx) in satData"
          :key="idx"
          class="meal-table-el animate__animated animate__jello"
        >
          <div class="meal-table-item">
            <div
              v-for="(food, index) in meal.menus"
              :key="index"
            >
                {{ food.foodName }}
            </div>
          </div>
        </div> 
      </div>
      <div class="sunday">
        <div class="text animate__animated animate__tada">일</div>
        <div 
          v-for="(meal, idx) in sunData"
          :key="idx"
          class="meal-table-el animate__animated animate__jello"
        >
          <div class="meal-table-item">
            <div
              v-for="(food, index) in meal.menus"
              :key="index"
            >
                {{ food.foodName }}
            </div>
          </div>
        </div> 
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "WeekMealTable",
  props: {
    weekData: Array,
    startDay: String,
  },
  data() {
    return {
      editFlag: false,
      monday: new Date('2022-04-06'),
      targetWeek: 'current',
      defaultData: [{mealTime: 0,menus: [{foodName:'작성된 식단이 없어요!'}]},{mealTime: 1,menus: [{foodName:'작성된 식단이 없어요!'}]},{mealTime: 2,menus: [{foodName:'작성된 식단이 없어요!'}]}],
      monData: [],
      tueData: [],
      wedData: [],
      thuData: [],
      friData: [],
      satData: [],
      sunData: [],
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
  watch: {
    weekData() {
      this.monData = [];
      this.tueData = [];
      this.wedData = [];
      this.thuData = [];
      this.friData = [];
      this.satData = [];
      this.sunData = [];
      for (let i = 0; i < 3; i++) {
        this.monData.push(this.weekData.find(meal =>  { return (meal.mealTime==`${i}`)&&(meal.dateTime==`${this.monday}`)})? this.weekData.find(meal =>  { return((meal.mealTime==`${i}`)&&(meal.dateTime==`${this.monday}`))}) : {mealTime: `${i}`,menus: [{foodName:'빈 식단'}]})
        this.tueData.push(this.weekData.find(meal =>  { return (meal.mealTime==`${i}`)&&(meal.dateTime==`${this.tueday}`)})? this.weekData.find(meal =>  { return((meal.mealTime==`${i}`)&&(meal.dateTime==`${this.tueday}`))}) : {mealTime: `${i}`,menus: [{foodName:'빈 식단'}]})
        this.wedData.push(this.weekData.find(meal =>  { return (meal.mealTime==`${i}`)&&(meal.dateTime==`${this.wedday}`)})? this.weekData.find(meal =>  { return((meal.mealTime==`${i}`)&&(meal.dateTime==`${this.wedday}`))}) : {mealTime: `${i}`,menus: [{foodName:'빈 식단'}]})
        this.thuData.push(this.weekData.find(meal =>  { return (meal.mealTime==`${i}`)&&(meal.dateTime==`${this.thuday}`)})? this.weekData.find(meal =>  { return((meal.mealTime==`${i}`)&&(meal.dateTime==`${this.thuday}`))}) : {mealTime: `${i}`,menus: [{foodName:'빈 식단'}]})
        this.friData.push(this.weekData.find(meal =>  { return (meal.mealTime==`${i}`)&&(meal.dateTime==`${this.friday}`)})? this.weekData.find(meal =>  { return((meal.mealTime==`${i}`)&&(meal.dateTime==`${this.friday}`))}) : {mealTime: `${i}`,menus: [{foodName:'빈 식단'}]})
        this.satData.push(this.weekData.find(meal =>  { return (meal.mealTime==`${i}`)&&(meal.dateTime==`${this.satday}`)})? this.weekData.find(meal =>  { return((meal.mealTime==`${i}`)&&(meal.dateTime==`${this.satday}`))}) : {mealTime: `${i}`,menus: [{foodName:'빈 식단'}]})
        this.sunData.push(this.weekData.find(meal =>  { return (meal.mealTime==`${i}`)&&(meal.dateTime==`${this.sunday}`)})? this.weekData.find(meal =>  { return((meal.mealTime==`${i}`)&&(meal.dateTime==`${this.sunday}`))}) : {mealTime: `${i}`,menus: [{foodName:'빈 식단'}]})
      }
    },
    startDay() {
      this.monday = new Date(this.startDay)
      this.tueday = new Date(this.monday.setDate(this.monday.getDate()+1)).toISOString().substring(0,10)
      this.wedday = new Date(this.monday.setDate(this.monday.getDate()+1)).toISOString().substring(0,10)
      this.thuday = new Date(this.monday.setDate(this.monday.getDate()+1)).toISOString().substring(0,10)
      this.friday = new Date(this.monday.setDate(this.monday.getDate()+1)).toISOString().substring(0,10)
      this.satday = new Date(this.monday.setDate(this.monday.getDate()+1)).toISOString().substring(0,10)
      this.sunday = new Date(this.monday.setDate(this.monday.getDate()+1)).toISOString().substring(0,10)
      this.monday = new Date(this.startDay).toISOString().substring(0,10)
    },
  }
};
</script>

<style scoped>
.week-calendar {
  width: 45vw;
  height: 100%;
  border-radius: 1vw;
}
.meal-table-el {
  width: calc(40vw / 7);
  height: 7.5vw;
  border: 0.125rem solid #25ab9b;
  margin: 0.2vw;
  border-radius: 1vw;
  position: relative;
  text-align: center;
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  top: 1.5vw;
  font-size: 0.7vw;
}
.meal-table-item {
  width: 4vw;
  margin: 0.5vw;
  overflow-y: auto;
}
.meal-table-item div {
  display: block;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.meal-table-item::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Opera*/
}
.week-select {
  width: 6vw;
  height: 1.5vw;
  text-align: center;
  border: #25ab9b 2px solid;
  border-radius: 0.5vw;
  position: relative;
  font-size: 0.9vw;
  left: 40vw;
  top: -4.4vw;
}

.meal-table-el.clicked {
  animation-name: vibration;
  animation-duration: 0.5s;
  animation-iteration-count: infinite;
}

.meal-table-el.clicked:hover {
  cursor: pointer;
}
.my-card {
  display: flex;
  justify-content: center;
  align-items: center;
  align-content: center;
  position: relative;
  top: -0.3vw;
  right: 2vw;
  width: 50vw;
  height: 18vw;
}
.meal-time {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 13.8vw;
  font-size: 1vw;
  font-weight: 700;
  margin: 0 1vw;
  position: relative;
  top: 2vw;
}
.meal-time div {
  width: 2vw;
}
.text {
  font-size: 1vw;
  font-weight: 700;
  position: relative;
  top: 1vw;
  text-align: center;
}
.settings {
  position: relative;
  font-size: 1.4vw;
  left: 45vw;
  top: -4vw;
}
.settings:hover {
  cursor: pointer;
  color: #25ab9b;
  transform: scale(1.2);
  transition: transform 0.1s;
  background-color: rgb(221, 221, 221);
  border-radius: 50%;
}

.today-week {
  font-weight: 700;
  font-size: 1vw;
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
