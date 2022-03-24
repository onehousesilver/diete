import Vue from "vue";
import VueRouter from "vue-router";
import store from '../store'
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
    path: "/menu/choose",
    name: "ChooseMeal",
    component: () => import("../views/MenuRecommendation/ChooseMeal.vue"),
  },
  {
    path: "/menu/recommendation",
    name: "RecommendMeal",
    component: () => import("../views/MenuRecommendation/RecommendMeal.vue"),
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

router.beforeEach((to, from, next) => {

  const isLogin = store.getters['isLogin']
  
 // requiresAuth 체크
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if(to.name === 'NewsFeed' && !isLogin) {
      next('/login')
    }
    else if(to.name !== 'login' && to.name !== 'join') {
      if(!isLogin) {
        alert('로그인이 필요합니다')
        next('/login')
      }
    }
    else{
      next('/login')
    }
  }
  // requiresAuth가 false일 때 (권한이 필요 없는 페이지)
  next()
})

export default router;
