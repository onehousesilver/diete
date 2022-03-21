import Vue from "vue";
import VueRouter from "vue-router";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("../views/HomeView.vue"),
  },
  {
    path: "/join",
    name: "join",
    component: () => import("../views/JoinView.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/LoginView.vue"),
  },
  {
    path: "/menu",
    name: "menu",
    component: () => import("../views/MenuRecommendation/ChooseMeal.vue"),
  },
  {
    path: "/search",
    name: "search",
    component: () => import("../views/SearchView.vue"),
  },
  {
    path: "/pocket",
    name: "pocket",
    component: () => import("../views/PocketView.vue"),
  },
  {
    path: "/record",
    name: "record",
    component: () => import("../views/RecordView.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
