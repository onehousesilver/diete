<template>
  <div>
    <div class="charts">
      <AnalysisBarChart 
        :recordData="recordData"
      />
      <AnalysisDonutsChart 
        :avgAnalysis="avgAnalysis"
      />
    </div>
    <div class="text-box">
      <!-- <h1>탄수화물 섭취량이 많습니다!</h1>
      <h2>단백질위주로 식사하세요!</h2> -->
    </div>
  </div>
</template>

<script>
import AnalysisBarChart from "./MyAnalysis/AnalysisBarChart.vue";
import AnalysisDonutsChart from "./MyAnalysis/AnalysisDonutsChart.vue";
import axios from 'axios';
export default {
  name: "MyAnalysis",
  components: {
    AnalysisDonutsChart,
    AnalysisBarChart,
  },
  data() {
    return {
      recordData: null,
      avgAnalysis: null,
      startDay: null,
      targetDate: new Date(+new Date() + 3240 * 10000).toISOString().substring(0,10), // 
    };
  },
  methods:{
    getRecordData(){
      axios({
        method:'get',
        url: `${process.env.VUE_APP_API_URL}/record/${this.userInfo.username}/`
      })
        .then(res => {
          this.recordData = res.data;
          this.recordData.sort((a, b) => {
            // 날짜 오름차순으로 정렬
            return new Date(a.dateTime) - new Date(b.dateTime)
          })
        })
    },
    
    getWeekAvg(){
      axios({
        method: 'get',
        url: `${process.env.VUE_APP_API_URL}/record/${this.userInfo.username}/${this.startDay}/`
      })
        .then(res => {
          this.avgAnalysis = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    getMonday() {
      // 오늘날짜 string(YYYY-mm-dd)
      // let today = new Date(+new Date() + 3240 * 10000).toISOString().substring(0,10);

      // 오늘날짜 date형식
      let date = new Date(this.targetDate);
      // 월요일구하기
      let day = date.getDay();
      let diff = date.getDate() - day + (day == 0 ? -6 : 1);

      // YYYYMMDD형식으로 parsing
      let monday = new Date(date.setDate(diff)).toISOString().substring(0,10)
      this.startDay = monday.replaceAll('-', '')
    },
  },
  mounted: async function() {
    this.getRecordData()
    await this.getMonday(this.targetDate)
    await this.getWeekAvg()
  },
  computed: {
    userInfo() { return this.$store.getters.getUserInfo }
  }
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
