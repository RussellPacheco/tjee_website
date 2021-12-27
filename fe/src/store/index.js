import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    adminLogin: false,
  },
  mutations: {
    setAdminLoginToTrue(state) {
      state.adminLogin = true
    }
  },
  actions: {
  },
  modules: {
  }
})
