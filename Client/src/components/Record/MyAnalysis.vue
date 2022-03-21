<template>
  <div>
    <div class="charts">
      <BarChart />
      <DonutsChart />
    </div>
    <div class="text-box">
      <h1>탄수화물 섭취량이 많습니다!</h1>
      <h2>단백질위주로 식사하세요!</h2>
    </div>
  </div>
</template>

<script>
import BarChart from "./BarChart.vue";
import DonutsChart from "./DonutsChart.vue";
export default {
  components: { DonutsChart, BarChart },
  name: "MyAnalysis",
  data() {
    return {};
  },
};
</script>

<style scoped>
.charts {
  display: flex;
  justify-content: center;
}
.text-box {
  text-align: center;
}
</style>
