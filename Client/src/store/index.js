import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import jwt_decode from 'jwt-decode'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    // 현재 장바구니 정보
    myBasket: {
      
    },
    mealTime: 0,  // 끼니 (0, 1, 2)
    menus: [],    // 끼니별 식단

    // 로그인 여부
    isLogin: false,
    // JWT
    userToken: null,
    // JWT.payload
    userInfo: null,
  },
  getters: {
    isLogin(state) {
      return state.isLogin;
    },
    getUserInfo(state) {
      return state.userInfo;
    },
    getUserToken(state) {
      return state.userToken;
    },
    getMyBasket(state) {
      return state.myBasket;
    }
  },
  mutations: {
    // 장바구니 갱신
    SET_MENU: function(state, menu) {
      if (!state.menus[0]){
        state.menus[0] = menu
      }
      else {
        state.menus.push(menu)
      }
    },
    // 장바구니 끼니 선택
    SET_BASKET_MEAL: function(state, mealTime){
      state.myBasket.mealTime = mealTime
    },
    SET_MENUS_UPDATE: function(state, menus){
      state.menus = menus
    },
    // 로그인
    SET_LOGIN: function(state, token) {
      let decoded_token = jwt_decode(token)
      state.userToken = token;
      state.userInfo = decoded_token;
      state.isLogin = true;
      // 장바구니 초기화
      state.menus = [];
      state.mealTime = 0;
      localStorage.setItem('userToken', token);
    },
    // 로그아웃
    SET_LOGOUT: function(state) {
      // user state 초기화
      state.userToken = null;
      state.isLogin = false;
      state.userInfo = null;
      // 로컬스토리지에 저장된 토큰 제거
      localStorage.removeItem('userToken');
    },
    // 권장칼로리 변경
    SET_KCAL: function(state, data) {
      state.userInfo.data.kcal = data.kcal;
      state.userInfo.data.height = data.height;
      state.userInfo.data.weight = data.weight;
      state.userInfo.data.activity = data.activity;
    }
  },
  actions: {
    myMenuUpdate: function({ commit }, menu) {
      // 전달받은 장바구니 메뉴 목록을 commit
      commit("SET_MENU", menu);
    },
    getUserToken: function({ commit }, token){
      // 전달받은 토큰을 commit
      commit("SET_LOGIN", token);
    },
    removeUserToken: function({ commit }){
      commit("SET_LOGOUT")
    },
    updateUserInfo: function({ commit }, data){
      commit("SET_KCAL", data)
    },
    mealTimeUpdate: function({ commit }, mealTime) {
      commit("SET_BASKET_MEAL", mealTime)
    },
    menusUpdate: function({ commit }, menus){
      // 변경된 메뉴 전체업데이트
      commit("SET_MENUS_UPDATE", menus)
    }
  },
  modules: {
  }
})
