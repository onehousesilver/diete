import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;

// apexcharts
import VueApexCharts from "vue-apexcharts";
Vue.component("ApexChart", VueApexCharts);
Vue.use(VueApexCharts);

// togglebtn
import ToggleButton from "vue-js-toggle-button";
Vue.use(ToggleButton);

// vueMoment
import vueMoment from "vue-moment";
import moment from "moment";

moment.locale("ko");
Vue.use(vueMoment, { moment });

//modal
import SweetModal from "sweet-modal-vue/src/plugin.js";
Vue.use(SweetModal);

// animate
import "animate.css";

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
