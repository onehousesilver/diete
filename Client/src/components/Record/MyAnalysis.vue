<template>
  <div>
    <div class="charts">
      <AnalysisBarChart />
      <AnlysisDonutsChart />
    </div>
    <div class="text-box">
      <h1>탄수화물 섭취량이 많습니다!</h1>
      <h2>단백질위주로 식사하세요!</h2>
    </div>
  </div>
</template>

<script>
import AnalysisBarChart from "./MyAnalysis/AnalysisBarChart.vue";
import AnlysisDonutsChart from "./MyAnalysis/AnlysisDonutsChart.vue";
export default {
  name: "MyAnalysis",
  components: {
    AnlysisDonutsChart,
    AnalysisBarChart,
  },
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
