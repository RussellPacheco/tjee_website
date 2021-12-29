import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    adminLogin: false,
    messages: [
      {
        id: 1, 
        created_by: "Russell", 
        message: "This is a sample message. It will likely be a long message. I need to check and make sure that it gets clipped properly.",
        created_at: "One week ago",
        last_sent: "Yesterday",
        last_modified: "Today"
      },
      {
        id: 2, 
        created_by: "Russell2", 
        message: "This is another sample message. It will likely be a long message. I need to check and make sure that it gets clipped properly.",
        created_at: "Two weeks ago",
        last_sent: "Yesterday",
        last_modified: "The other day"
      }
    ],
    editMessage: {
      id: 0,
      created_by: "Default",
      message: "Default message",
      created_at: "Default Time",
      last_sent: "Default Time",
      last_modified: "Default Time"
    }
  },
  mutations: {
    setAdminLoginToTrue(state) {
      state.adminLogin = true
    },
    setEditMessage(state, payload) {
      state.editMessage = payload
    }
  },
  actions: {
  },
  modules: {
  }
})
