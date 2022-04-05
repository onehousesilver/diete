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
      <DayBarChart v-if="current" @goToDay="goToDay" />
      <WeekBarChart v-else @goToWeek="goToWeek" />
      <WeekMealTable v-if="!current" @goToWeek="goToWeek" />
      <DayMealTable v-else @goToWeek="goToWeek" />
    </div>
    <button @click="getDiet">asdf</button>
  </div>
</template>

<script>
import axios from 'axios';
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
      this.current = true;
    },
    getDiet(){
      axios({
        method:'get',
        url: `${process.env.VUE_APP_API_URL}/record/menu/qwer1234/20220407/`
        // url: `${process.env.VUE_APP_API_URL}/record/qwer1234/`
      })
        .then(res => {
          console.log(res)
        })
    }
  },
};
</script>

<style>
.toggle-btn {
  left: 84vw;
}
.body {
  display: flex;
  justify-content: center;
}

.apexcharts-reset-icon {
  display: none;
}
/* @media screen and (max-width: 1770px){
  
} */
</style>
