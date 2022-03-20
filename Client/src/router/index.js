import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import JoinView from "../views/JoinView.vue";
import LoginView from "../views/LoginView.vue";
import MenuView from "../views/MenuView.vue";
import RecordView from "../views/RecordView.vue";
import SearchView from "../views/SearchView.vue";
import PocketView from "../views/PocketView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/join",
    name: "join",
    component: JoinView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/menu",
    name: "menu",
    component: MenuView,
  },
  {
    path: "/search",
    name: "search",
    component: SearchView,
  },
  {
    path: "/pocket",
    name: "pocket",
    component: PocketView,
  },
  {
    path: "/record",
    name: "record",
    component: RecordView,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
