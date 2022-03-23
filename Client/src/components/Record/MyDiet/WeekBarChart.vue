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
          data: [300, 400, 700, 614, 851, 564, 700],
        },
        {
          name: "지방",
          data: [300, 851, 614, 564, 400, 300, 300],
        },
        {
          name: "단백질",
          data: [851, 300, 564, 300, 700, 614, 400],
        },
        {
          name: "총당류",
          data: [60, 100, 112, 88, 66, 99, 44],
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
          categories: ["월", "화", "수", "목", "금", "토", "일"],
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
  left: 200px;
}
</style>
