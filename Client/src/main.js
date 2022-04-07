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

// SweetModal
import SweetModal from "sweet-modal-vue/src/plugin.js";
Vue.use(SweetModal);

// VueAwesomeSwiper
import VueAwesomeSwiper from 'vue-awesome-swiper';
Vue.use(VueAwesomeSwiper)

// animation
import "animate.css";
import "hover.css";

//vuetify
import vuetify from './plugins/vuetify'

//VueSweetalert2
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

Vue.use(VueSweetalert2);

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App)
}).$mount("#app");
