<template>
  <div>
    <div class="charts">
      <AnalysisBarChart 
        :recordData="recordData"
        :chartState="chartState"
      />
      <AnlysisDonutsChart />
    </div>
    <div class="text-box">
      <!-- <h1>탄수화물 섭취량이 많습니다!</h1>
      <h2>단백질위주로 식사하세요!</h2> -->
    </div>
  </div>
</template>

<script>
import AnalysisBarChart from "./MyAnalysis/AnalysisBarChart.vue";
import AnlysisDonutsChart from "./MyAnalysis/AnlysisDonutsChart.vue";
import axios from 'axios';
export default {
  name: "MyAnalysis",
  components: {
    AnlysisDonutsChart,
    AnalysisBarChart,
  },
  data() {
    return {
      recordData: null,
      chartState: false,
    };
  },
  methods:{
    getRecordData(){
      axios({
        method:'get',
        url: `${process.env.VUE_APP_API_URL}/record/${this.userInfo.username}/`
      })
        .then(res => {
          console.log(res)
          this.recordData = res.data;
          this.chartState = !this.chartState;
        })
    }
  },
  mounted() {
    this.getRecordData()
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
