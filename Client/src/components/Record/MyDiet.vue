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
      <DayBarChart v-if="current == true" @goToDay="goToDay" />
      <WeekBarChart v-else-if="current == false" @goToWeek="goToWeek" />
      <WeekMealTable v-if="current == false" @goToWeek="goToWeek" />
      <DayMealTable v-else-if="current == true" @goToWeek="goToWeek" />
    </div>
  </div>
</template>

<script>
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
  },
};
</script>

<style>
.toggle-btn {
  left: 8%;
  bottom: 40px;
}
.body {
  display: flex;
  justify-content: space-evenly;
}
</style>
