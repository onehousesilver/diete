<template>
  <div class="analysisBarChart">
    <div id="chart">
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
          width: [0, 4],
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
      dumpData1: [],
      dumpData2: [],
      dumpData3: [],
      dumpData4: [],
      dumpData5: [],
      dumpData6: [],
    };
  },
  methods: {
    test() {},
    setInit() {
      this.recordData.forEach((day) => {
        this.chartOptions.labels.push(day.dateTime);
        this.series[0].data.push(day.total_kcal);
        this.series[1].data.push(day.total_sugar);
        this.series[2].data.push(day.total_carbo);
        this.series[3].data.push(day.total_protein);
        this.series[4].data.push(day.total_fat);
        this.series[5].data.push(day.total_fatty);
        this.$refs.analysisChart.chart.update();
        // console.log(this.chartOptions.labels)
      });
    },
  },
  watch: {
    recordData() {
      // this.setInit();
    },
    chartState() {
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
#chart {
  width: 40vw;
}
.analysisBarChart {
  width: 50vw;
}

</style>
