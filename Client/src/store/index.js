import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import jwt_decode from 'jwt-decode'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    // 현재 장바구니 정보
    myMenu: {

    },

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
    }
  },
  mutations: {
    // 장바구니 갱신
    SET_MENU: function(state, menus) {
      state.myMenu = menus;
    },
    // 로그인
    SET_LOGIN: function(state, token) {
      let decoded_token = jwt_decode(token)
      // * Token decoding 필요
      state.userToken = token;
      state.userInfo = decoded_token;
      state.isLogin = true;
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
    myMenuUpdate: function({ commit }, menus) {
      // 전달받은 장바구니 메뉴 목록을 commit
      commit("SET_MENU", menus);
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
    }
  },
  modules: {
  }
})
