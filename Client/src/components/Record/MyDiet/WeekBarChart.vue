<template>
  <div class="week-chart">
    <div id="chart">
      <ApexChart
        ref="weekbarchart"
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
    weekData: Array,
    startDay: String,
  },
  data() {
    return {
      monday: new Date('2022-04-06'),
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
              return val;
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
              return val;
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
  watch: {
    weekData() {
      this.series[0].data = []
      this.series[1].data = []
      this.series[2].data = []
      this.series[3].data = []
      this.series[4].data = []
      this.series[5].data = []

      let weekAnalyData = [];
      weekAnalyData.push(this.weekData.filter(meal => { return meal.dateTime==`${this.monday}`}))
      weekAnalyData.push(this.weekData.filter(meal => { return meal.dateTime==`${this.tueday}`}))
      weekAnalyData.push(this.weekData.filter(meal => { return meal.dateTime==`${this.wedday}`}))
      weekAnalyData.push(this.weekData.filter(meal => { return meal.dateTime==`${this.thuday}`}))
      weekAnalyData.push(this.weekData.filter(meal => { return meal.dateTime==`${this.friday}`}))
      weekAnalyData.push(this.weekData.filter(meal => { return meal.dateTime==`${this.satday}`}))
      weekAnalyData.push(this.weekData.filter(meal => { return meal.dateTime==`${this.sunday}`}))
      for (let i = 0; i < 7; i++) {
        let total_kcal = 0
        let total_carbo = 0
        let total_protein = 0
        let total_fat = 0
        let total_sugar = 0
        let total_fatty = 0
        if(weekAnalyData[i].length > 0){
          weekAnalyData[i].forEach(data => {
            total_carbo += data.total_carbo
            total_kcal += data.total_kcal
            total_carbo += data.total_carbo
            total_protein += data.total_protein
            total_fat += data.total_fat
            total_sugar += data.total_sugar
            total_fatty += data.total_fatty
          })
        }
        this.series[0].data.push(total_kcal)
        this.series[1].data.push(total_carbo)
        this.series[2].data.push(total_protein)
        this.series[3].data.push(total_fat)
        this.series[4].data.push(total_sugar)
        this.series[5].data.push(total_fatty)
      }
      
      this.$refs.weekbarchart.chart.update();
      // let monData = this.weekData.filter(meal => { return meal.dateTime==`${this.monday}`})
      // let tueData = this.weekData.filter(meal => { return meal.dateTime==`${this.tueday}`})
      // let wedData = this.weekData.filter(meal => { return meal.dateTime==`${this.wedday}`})
      // let thuData = this.weekData.filter(meal => { return meal.dateTime==`${this.thuday}`})
      // let friData = this.weekData.filter(meal => { return meal.dateTime==`${this.friday}`})
      // let satData = this.weekData.filter(meal => { return meal.dateTime==`${this.satday}`})
      // let sunData = this.weekData.filter(meal => { return meal.dateTime==`${this.sunday}`})
      // monData.push(mon ? mon : {});
      // tueData.push(tue ? tue : {});
      // wedData.push(wed ? wed : {});
      // thuData.push(thu ? thu : {});
      // friData.push(fri ? fri : {});
      // satData.push(sat ? sat : {});
      // sunData.push(sun ? sun : {});
      // for (let i = 0; i < 3; i++) {
      //   if (monData[i].length > 0){
      //     this.series[0].data.push(monData[i].total_kcal)
      //     this.series[1].data.push(monData[i].total_carbo)
      //     this.series[2].data.push(monData[i].total_protein)
      //     this.series[3].data.push(monData[i].total_fat)
      //     this.series[4].data.push(monData[i].total_sugar)
      //     this.series[5].data.push(monData[i].total_fatty)
      //   }
        
      // }
      // console.log(tueData)
      // if (monData.length >0){
      //   this.series[0].data.push(monData.`${i}`)
      //   this.series[1].data.push(monData.`${i}`)
      //   this.series[2].data.push(monData.`${i}`)
      //   this.series[3].data.push(monData.`${i}`)
      //   this.series[4].data.push(monData.`${i}`)
      //   this.series[5].data.push(monData.`${i}`)
      // }
      // const morningData = this.dayData.filter(menu => menu.dateTime == '0')
      // const lunchData = this.dayData.filter(menu => menu.dateTime == '1')
      // const dinnerData = this.dayData.filter(menu => menu.dateTime == '2')
      // this.series[0].data.push(morningData.total_kcal)
      // this.series[1].data.push(morningData.total_carbo)
      // this.series[2].data.push(morningData.total_protein)
      // this.series[3].data.push(morningData.total_fat)
      // this.series[4].data.push(morningData.total_sugar)
      // this.series[5].data.push(morningData.total_fatty)
      // this.series[0].data.push(lunchData.total_kcal)
      // this.series[1].data.push(lunchData.total_carbo)
      // this.series[2].data.push(lunchData.total_protein)
      // this.series[3].data.push(lunchData.total_fat)
      // this.series[4].data.push(lunchData.total_sugar)
      // this.series[5].data.push(lunchData.total_fatty)
      // this.series[0].data.push(dinnerData.total_kcal)
      // this.series[1].data.push(dinnerData.total_carbo)
      // this.series[2].data.push(dinnerData.total_protein)
      // this.series[3].data.push(dinnerData.total_fat)
      // this.series[4].data.push(dinnerData.total_sugar)
      // this.series[5].data.push(dinnerData.total_fatty)
    },
    
    startDay() {
      this.monday = new Date(this.startDay)
      this.tueday = new Date(this.monday.setDate(this.monday.getDate()+1)).toISOString().substring(0,10)
      this.wedday = new Date(this.monday.setDate(this.monday.getDate()+1)).toISOString().substring(0,10)
      this.thuday = new Date(this.monday.setDate(this.monday.getDate()+1)).toISOString().substring(0,10)
      this.friday = new Date(this.monday.setDate(this.monday.getDate()+1)).toISOString().substring(0,10)
      this.satday = new Date(this.monday.setDate(this.monday.getDate()+1)).toISOString().substring(0,10)
      this.sunday = new Date(this.monday.setDate(this.monday.getDate()+1)).toISOString().substring(0,10)
      this.monday = new Date(this.startDay).toISOString().substring(0,10)
    },
  }
};
</script>

<style scoped>
#chart {
  width: 40vw;
}
.week-chart {
  display: flex;
  align-self: center;
  text-align: -webkit-center;
  right: 0.5vw;
  position: relative;
}
</style>
