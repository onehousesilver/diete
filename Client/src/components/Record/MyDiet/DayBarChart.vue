<template>
  <div>
    <div class="week-chart">
      <div id="chart">
        <ApexChart
          type="bar"
          height="500"
          width="800"
          :options="chartOptions"
          :series="series"
        ></ApexChart>
      </div>
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
          height: 400,
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
        //   text: "WEEK",
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

<style>
.week-chart {
  display: flex;
  /* justify-content: center; */
  left: 12.5rem;
}
</style>
