<template>
  <div>
    <div >
      <ApexChart
        ref="radialchart"
        type="radialBar"
        width="500"
        height="400"
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
          show:true
        },
        chart: {
          width: 380,
          type: "pie",
        },
        labels: ["총 열량", "탄수화물", "단백질", "지방", "총 당류", "총 포화지방산"],
        total: {
          show: true,
          label: 'Total'
        },
        value: {
          show: true,
          fontSize: '14px',
          formatter: function (val) {
            return val + '%'
          }
        },
      },
    };
  },
  computed: {
    userInfo() { return this.$store.state.userInfo }
  },
  watch: {
    avgAnalysis(){
      this.series.push(Math.ceil(parseFloat(this.avgAnalysis.aver_kcal) / parseFloat(this.userInfo.data.kcal) / 3 * 100))    // 열량
      this.series.push(Math.ceil(parseFloat(this.avgAnalysis.aver_carbo) / 90 * 100))    // 탄수화물
      this.series.push(Math.ceil(parseFloat(this.avgAnalysis.aver_protein) / parseFloat(this.userInfo.data.weight) / 3 * 100))    // 단백질
      this.series.push(Math.ceil(parseFloat(this.avgAnalysis.aver_fat) / 17 * 100))    // 지방
      this.series.push(Math.ceil(parseFloat(this.avgAnalysis.aver_sugar) / 10 * 100))    // 총 당류
      this.series.push(Math.ceil(parseFloat(this.avgAnalysis.aver_fatty) / 5 * 100))    // 총 포화지방산
      // this.series.push(parseFloat(this.avgAnalysis.aver_kcal) / parseFloat(this.userInfo.data.kcal / 3))    // 열량
      // this.series.push(parseFloat(this.avgAnalysis.aver_carbo) / 90)    // 탄수화물
      // this.series.push(parseFloat(this.avgAnalysis.aver_protein) / parseFloat(this.userInfo.data.weight) / 3)    // 단백질
      // this.series.push(parseFloat(this.avgAnalysis.aver_fat) / 17)    // 지방
      // this.series.push(parseFloat(this.avgAnalysis.aver_sugar) / 10)    // 총 당류
      // this.series.push(parseFloat(this.avgAnalysis.aver_fatty) / 5)    // 총 포화지방산
      this.$refs.radialchart.chart.update();
    }
  }
};
</script>

<style scoped></style>
