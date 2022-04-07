<template>
  <div class="analysisBarChart">
    <div id="analysischart">
      <ApexChart
        ref="analysisChart"
        type="line"
        :options="chartOptions"
        :series="series"
      ></ApexChart>
    </div>
  </div>
</template>

<script>
export default {
  name: "BarChart",
  props: {
    recordData: Array,
    chartState: Boolean,
  },
  data() {
    return {
      series: [
        {
          name: "총 열량(kcal)",
          type: "column",
          data: [],
          // data: [23, 42, 35, 27, 43, 22, 17],
        },
        {
          name: "총 당류(g)",
          type: "line",
          data: [],
          // data: [23, 42, 35, 27, 43, 22, 17],
        },
        {
          name: "탄수화물(g)",
          type: "line",
          data: [],
          // data: [23, 42, 35, 27, 43, 22, 17],
        },
        {
          name: "단백질(g)",
          type: "line",
          data: [],
          // data: [23, 42, 35, 27, 43, 22, 17],
        },
        {
          name: "지방(g)",
          type: "line",
          data: [],
          // data: [23, 42, 35, 27, 43, 22, 17],
        },
        {
          name: "총 포화지방산(g)",
          type: "line",
          data: [],
          // data: [23, 42, 35, 27, 43, 22, 17],
        },
      ],
      chartOptions: {
        chart: {
          height: 350,
          type: "line",
        },
        stroke: {
          curve: 'straight',
          width: [3, 3, 3, 3, 3, 3]
        },
        title: {
          text: "일별 전체 영양소 조회",
        },
        dataLabels: {
          enabled: true,
          enabledOnSeries: [0],
        },
        labels: [],
        xaxis: {
          type: "datetime",
        },
        yaxis: [
          {
            title: {
              text: "",
            },
          },
          {
            opposite: true,
            title: {
              text: "",
            },
          },
        ],
      },
    };
  },
  methods: {
    setInit() {
      this.recordData.forEach((day) => {
        this.chartOptions.labels.push(day.dateTime);
        this.series[0].data.push(day.total_kcal ? day.total_kcal : "0");
        this.series[1].data.push(day.total_sugar ? day.total_sugar : "0");
        this.series[2].data.push(day.total_carbo ? day.total_carbo : "0");
        this.series[3].data.push(day.total_protein ? day.total_protein : "0");
        this.series[4].data.push(day.total_fat ? day.total_fat : "0");
        this.series[5].data.push(day.total_fatty ? day.total_fatty : "0");
        // console.log(this.chartOptions.labels)
      });
      this.$refs.analysisChart.chart.update();
    },
  },
  watch: {
    recordData() {
      this.setInit();
    },
  },
  mounted() {
    // console.log(this.$refs.myChart);
    // console.log('mounted')
  },
};
</script>

<style>
#analysischart {
  width: 40vw;
}
.analysisBarChart {
  width: 50vw;
}

</style>
