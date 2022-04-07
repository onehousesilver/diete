<template>
  <div>
    <toggle-button
      class="toggle-btn"
      :value="true"
      :labels="{ checked: 'Day', unchecked: 'Week' }"
      :color="{ checked: '#00a488', unchecked: '#77be8e' }"
      :width="85"
      :height="28"
      :font-size="16"
      @change="onChangeToggle"
    />
    <div class="body">
      <DayBarChart 
        v-show="current" 
        @goToDay="goToDay" 
        :dayData="dateAnalysis"
      />
      <WeekBarChart 
        v-show="!current" @goToWeek="goToWeek" 
        :weekData="weekAnalysis"
        :startDay="monday"
      />
      <WeekMealTable 
        v-show="!current"
        @goToWeek="goToWeek"
        :weekData="weekData"
        :startDay="monday"
      />
      <DayMealTable 
        v-show="current" 
        @goToWeek="goToWeek"
        :targetDate="targetDate"
        @dateChange="getMonday"
        :dayData="dateData"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import DayBarChart from "./MyDiet/DayBarChart.vue";
import DayMealTable from "./MyDiet/DayMealTable.vue";
import WeekBarChart from "./MyDiet/WeekBarChart.vue";
import WeekMealTable from "./MyDiet/WeekMealTable.vue";
export default {
  name: "MyDiet",
  components: {
    DayBarChart,
    WeekBarChart,
    WeekMealTable,
    DayMealTable,
  },
  data() {
    return {
      current: true,
      today: new Date(+new Date() + 3240 * 10000).toISOString().substring(0,10),  // 오늘날짜
      startDay: null, // search 기준일 YYYYMMDD
      monday: null,   // search 기준일 YYYY-MM-DD
      targetDate: new Date(+new Date() + 3240 * 10000).toISOString().substring(0,10), // 
      dateData: [[{menus:[{foodName:'asd'}]}]], // 일간식단
      weekData: null, // 주간식단
      dateAnalysis: null,
      weekAnalysis: null,
    };
  },
  methods: {
    onChangeToggle() {
      if (this.current == true) {
        this.goToWeek();
      } else {
        this.goToDay();
      }
    },

    goToWeek() {
      this.current = false;
    },
    goToDay() {
      this.getWeekDiet()
      this.current = true;
    },
    getMonday(updateDate) {
      // 오늘날짜 string(YYYY-mm-dd)
      // let today = new Date(+new Date() + 3240 * 10000).toISOString().substring(0,10);
      this.targetDate = updateDate
      // 오늘날짜 date형식
      let date = new Date(updateDate);
      // 월요일구하기
      let day = date.getDay();
      let diff = date.getDate() - day + (day == 0 ? -6 : 1);

      // YYYYMMDD형식으로 parsing
      let monday = new Date(date.setDate(diff)).toISOString().substring(0,10)
      this.monday = monday
      this.startDay = monday.replaceAll('-', '')
    },
    getWeekDiet(){
      axios({
        method:'get',
        url: `${process.env.VUE_APP_API_URL}/record/menu/${this.userInfo.username}/${this.startDay}/`
      })
        .then(res => {
          // 주간식단 update
          this.weekData = res.data
          // console.log(this.weekData)
          // 일간식단 update
          this.getDateDiet()
          // 주간그래프 update
          this.getWeekAnalysis()
        })
        .catch(err => {
          console.log(err)
        })
    },
    getDateDiet(){
      this.dateData = this.weekData.filter(menu => {
        return menu.dateTime == this.targetDate
      })
    },
    getWeekAnalysis(){
      axios({
        method: 'get',
        url: `${process.env.VUE_APP_API_URL}/record/nutrients/${this.userInfo.username}/${this.startDay}/`
      })
        .then(res => {
          this.weekAnalysis = res.data
          this.dateAnalysis = this.weekAnalysis.filter(data => {
            return data.dateTime == this.targetDate
          })
          // console.log(res.data)
        })
        .catch(err => {
          console.log(err)
          this.weekAnalysis = []
          this.dateAnalysis = []
        })
    },
  },
  mounted: async function() {
    await this.getMonday(this.targetDate)
    await this.getWeekDiet()
  },
  computed: {
    userInfo() { return this.$store.getters.getUserInfo }
  },
  watch: {
    // 기준일 변경시마다 주간, 일간 데이터 update
    targetDate: async function(){
      await this.getMonday(this.targetDate)
      await this.getWeekDiet()
    },
  }
};
</script>

<style>
.toggle-btn {
  left: 8.5vw;
  bottom: 1.5vw;
}
.body {
  display: flex;
  height: 24vw;
  justify-content: center;
}

.apexcharts-reset-icon {
  display: none;
}
/* @media screen and (max-width: 1770px){

} */
</style>
