import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    // 현재 장바구니 정보
    myMenu: {

    },
    // 로그인 여부
    isLogin: false,
    // JWT.payload
    userToken: null,
  },
  getters: {

  },
  mutations: {
    // 장바구니 갱신
    SET_MENU: function(state, menus) {
      state.myMenu = menus;
    },
    // 로그인
    SET_LOGIN: function(state, token) {
      // * Token decoding 필요
      state.userToken = token;

      state.isLogin = true;
      localStorage.setItem('userToken', token);
    },
    // 로그아웃
    SET_LOGOUT: function(state) {
      // user state 초기화
      state.userToken = null;
      state.isLogin = false;
      // 로컬스토리지에 저장된 토큰 제거
      localStorage.removeItem('userToken');
      // 페이지 새로고침
      location.reload();
    },
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
  },
  modules: {
  }
})
