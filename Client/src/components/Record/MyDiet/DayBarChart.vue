<template>
  <div class="day-chart">
    <div id="chart">
      <ApexChart
        ref="daybarchart"
        type="bar"
        :options="chartOptions"
        :series="series"
      ></ApexChart>
    </div>
  </div>
</template>

<script>
export default {
  name: "DayBarChart",
  props: {
    dayData:Array,
  },
  data() {
    return {
      series: [
        {
          name: "열량(kcal)",
          data: [],
        },
        {
          name: "탄수화물(g)",
          data: [],
        },
        {
          name: "단백질(g)",
          data: [],
        },
        {
          name: "지방(g)",
          data: [],
        },
        {
          name: "총 당류(g)",
          data: [],
        },
        {
          name: "총 포화지방산(g)",
          data: [],
        },
      ],
      chartOptions: {
        chart: {
          type: "bar",
          width: "10vw",
          stacked: true,
        },
        plotOptions: {
          bar: {
            horizontal: true,
          },
        },
        stroke: {
          width: 1,
          colors: ["#fff"],
        },
        // title: {
        //   text: "DAY",
        // },
        xaxis: {
          categories: ["아침", "점심", "저녁"],
          labels: {
            formatter: function (val) {
              return val
            },
          },
        },
        yaxis: {
          title: {
            text: undefined,
          },
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return val
            },
          },
        },
        fill: {
          opacity: 1,
        },
        legend: {
          position: "top",
          horizontalAlign: "left",
          offsetX: 40,
        },
      },
      morningData: [{menus: '식단이 없어요!'}],
      lunchData: [{menus: '식단이 없어요!'}],
      dinnerData: [{menus: '식단이 없어요!'}],
    };
  },
  watch: {
    dayData(){
      this.series[0].data = []
      this.series[1].data = []
      this.series[2].data = []
      this.series[3].data = []
      this.series[4].data = []
      this.series[5].data = []
      const morningData = this.dayData.find(menu => menu.mealTime == '0')
      const lunchData = this.dayData.find(menu => menu.mealTime == '1')
      const dinnerData = this.dayData.find(menu => menu.mealTime == '2')
      if (morningData){
        this.series[0].data.push(morningData.total_kcal)
        this.series[1].data.push(morningData.total_carbo)
        this.series[2].data.push(morningData.total_protein)
        this.series[3].data.push(morningData.total_fat)
        this.series[4].data.push(morningData.total_sugar)
        this.series[5].data.push(morningData.total_fatty)
      }
      else {
        this.series[0].data.push(0)
        this.series[1].data.push(0)
        this.series[2].data.push(0)
        this.series[3].data.push(0)
        this.series[4].data.push(0)
        this.series[5].data.push(0)
      }
      if (lunchData){
        this.series[0].data.push(lunchData.total_kcal)
        this.series[1].data.push(lunchData.total_carbo)
        this.series[2].data.push(lunchData.total_protein)
        this.series[3].data.push(lunchData.total_fat)
        this.series[4].data.push(lunchData.total_sugar)
        this.series[5].data.push(lunchData.total_fatty)
      }
      else {
        this.series[0].data.push(0)
        this.series[1].data.push(0)
        this.series[2].data.push(0)
        this.series[3].data.push(0)
        this.series[4].data.push(0)
        this.series[5].data.push(0)
      }
      if (dinnerData){
        this.series[0].data.push(dinnerData.total_kcal)
        this.series[1].data.push(dinnerData.total_carbo)
        this.series[2].data.push(dinnerData.total_protein)
        this.series[3].data.push(dinnerData.total_fat)
        this.series[4].data.push(dinnerData.total_sugar)
        this.series[5].data.push(dinnerData.total_fatty)
      }
      else {
        this.series[0].data.push(0)
        this.series[1].data.push(0)
        this.series[2].data.push(0)
        this.series[3].data.push(0)
        this.series[4].data.push(0)
        this.series[5].data.push(0)
      }
      this.$refs.daybarchart.chart.update();
    },
  }
};
</script>

<style scoped>
#chart {
  width: 40vw;
  align-self: center;
  text-align: -webkit-center;
}
.day-chart {
  display: flex;
  height: 24vw;
  position: relative;
  right: 3vw;
}
</style>
