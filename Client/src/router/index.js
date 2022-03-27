import Vue from "vue";
import VueRouter from "vue-router";
import store from '../store'
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("@/views/HomeView.vue"),
  },
  {
    path: "/join",
    name: "join",
    component: () => import("@/views/JoinView.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () => import("@/views/LoginView.vue"),
  },
  {
    path: "/menu/choose",
    name: "ChooseMeal",
    component: () => import("@/views/MenuRecommendation/ChooseMeal.vue"),
    meta: {requiresAuth: true}
  },
  {
    path: "/menu/recommendation",
    name: "RecommendMeal",
    component: () => import("@/views/MenuRecommendation/RecommendMeal.vue"),
    meta: {requiresAuth: true}
  },
  {
    path: "/search",
    name: "search",
    component: () => import("@/views/SearchView.vue"),
    meta: {requiresAuth: true}
  },
  {
    path: "/basket",
    name: "basket",
    component: () => import("@/views/BasketView.vue"),
    meta: {requiresAuth: true}
  },
  {
    path: "/record",
    name: "record",
    component: () => import("@/views/RecordView.vue"),
    meta: {requiresAuth: true}
  },
  {
    path: "/404",
    name: "404",
    component: () => import("../views/NotFound.vue")
  },
  {
    path: "*",
    redirect: "/404"
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {

  const isLogin = store.getters.isLogin
  
 // requiresAuth 체크 
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // 비회원 접근 차단
    if(!isLogin) {
      alert('로그인이 필요합니다')
      next('/login')
    }
  }
  // requiresAuth가 false일 때 (권한이 필요 없는 페이지)
    next()
})

export default router;
