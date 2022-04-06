<template>
  <div class="day-chart">
    <div id="chart">
      <ApexChart
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
  data() {
    return {
      series: [
        {
          name: "탄수화물",
          data: [851, 564, 700],
        },
        {
          name: "지방",
          data: [400, 300, 300],
        },
        {
          name: "단백질",
          data: [700, 614, 400],
        },
        {
          name: "총당류",
          data: [60, 100, 112],
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
              return val + "Kcal";
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
              return val + "Kcal";
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
    };
  },
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
