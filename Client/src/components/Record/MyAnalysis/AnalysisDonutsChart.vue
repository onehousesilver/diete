<template>
  <div class="raial-chart">
    <div class="chart-text">
      <span style="color: #25ab9b; font-weight: 700"
        >한국보건산업진흥원에서</span
      >
      제공하는 <br />
      일주일 영양소 권장량 대비
      <span style="color: #25ab9b; font-weight: 700">{{
        userInfo.data.name
      }}</span
      >님이 섭취한
      <span style="color: #25ab9b; font-weight: 700">일주일 평균 영양소입니다.</span>
      <br />
      <span style="font-size: 0.9vw; color: #333"
        >차트 게이지에 맞게 섭취하시는걸 권장합니다.</span
      >
      <span style="font-size: 0.7vw; color: #333"
        >(차트에 마우스를 올려보세요!)</span
      >
    </div>
    <div id="radialchart">
      <ApexChart
        ref="radialchart"
        type="radialBar"
        :options="chartOptions"
        :series="series"
      ></ApexChart>
    </div>
  </div>
</template>

<script>
export default {
  name: "DonutsChart",
  props: {
    avgAnalysis: Object,
  },
  data() {
    return {
      // 탄수화물 권장량 : 250g
      // 단백질 하루권장 : 몸무게 * 1 g (평균적)
      // 지방 권장량 : 51g
      // 당 권장량: 30g
      // 포화지방산 하루권장:15g
      // recAmountCarbo: 250, // 탄수화물 하루권장량,
      // recAmountCarbo: null, // 탄수화물 하루권장량,
      // recAmountCarbo: null, // 탄수화물 하루권장량,
      // recAmountCarbo: null, // 탄수화물 하루권장량,
      // recAmountCarbo: null, // 탄수화물 하루권장량,
      series: [],

      chartOptions: {
        name: {
          show: true,
        },
        chart: {
          width: 380,
          type: "pie",
        },
        labels: [
          "총 열량",
          "탄수화물",
          "단백질",
          "지방",
          "총 당류",
          "총 포화지방산",
        ],
        total: {
          show: true,
          label: "Total",
        },
        value: {
          show: true,
          fontSize: "14px",
          formatter: function (val) {
            return val + "%";
          },
        },
      },
    };
  },
  computed: {
    userInfo() {
      return this.$store.state.userInfo;
    },
  },
  watch: {
    avgAnalysis() {
      this.series.push(
        Math.ceil(
          (parseFloat(this.avgAnalysis.aver_kcal) /
            parseFloat(this.userInfo.data.kcal) *
            3) *
            100
        )
      ); // 열량
      this.series.push(
        Math.ceil((parseFloat(this.avgAnalysis.aver_carbo) / 90) * 100)
      ); // 탄수화물
      this.series.push(
        Math.ceil(
          (parseFloat(this.avgAnalysis.aver_protein) /
            parseFloat(this.userInfo.data.weight) *
            3) *
            100
        )
      ); // 단백질
      this.series.push(
        Math.ceil((parseFloat(this.avgAnalysis.aver_fat) / 17) * 100)
      ); // 지방
      this.series.push(
        Math.ceil((parseFloat(this.avgAnalysis.aver_sugar) / 10) * 100)
      ); // 총 당류
      this.series.push(
        Math.ceil((parseFloat(this.avgAnalysis.aver_fatty) / 5) * 100)
      ); // 총 포화지방산
      // this.series.push(parseFloat(this.avgAnalysis.aver_kcal) / parseFloat(this.userInfo.data.kcal / 3))    // 열량
      // this.series.push(parseFloat(this.avgAnalysis.aver_carbo) / 90)    // 탄수화물
      // this.series.push(parseFloat(this.avgAnalysis.aver_protein) / parseFloat(this.userInfo.data.weight) / 3)    // 단백질
      // this.series.push(parseFloat(this.avgAnalysis.aver_fat) / 17)    // 지방
      // this.series.push(parseFloat(this.avgAnalysis.aver_sugar) / 10)    // 총 당류
      // this.series.push(parseFloat(this.avgAnalysis.aver_fatty) / 5)    // 총 포화지방산
      this.$refs.radialchart.chart.update();
    },
  },
};
</script>

<style scoped>
#radialchart {
  width: 30vw;
}
.raial-chart {
  width: 30vw;
}
.chart-text {
  font-size: 1vw;
}
</style>
