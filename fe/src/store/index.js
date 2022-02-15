import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import { isValidJwt, EventBus } from '@/utils'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    
////////////
//
// Members
//
////////////

    unregistedMembers: [{
      id: 0,
      name: "Default",
      status: "Default",
      joined: 1,
      city: "Default city",
      country: "Default country",
      localized_country_name: "localized_country_name", 
      lat: "",
      lon: "",
      photo: {
        id: 303069491, 
        highres_link: 'highres_link', 
        photo_link: 'photo_link',
        thumb_link: 'thumbnail_link',
        type: 'member', 
        base_url: 'base_url'
      },
      group_profile: "",
      is_pro_admin: ""
    }],
    members: [{
      id: 1,
      firstname: "Russell",
      lastname: "Pacheco",
      gender: "Male",
      country: "USA",
      native_lang: "English",
      lang_focus: "Japanese",
      line_id: "line_id",
      meetup_name: "Russell Pacheco",
      created_at: "Yesterday"
    }, {
      id: 2,
      firstname: "Jarett",
      lastname: "Leno",
      gender: "Male",
      country: "USA",
      native_lang: "English",
      lang_focus: "Japanese",
      line_id: "line_id",
      meetup_name: "jarettleno",
      created_at: "before"
    }],
    editMember: {
      id: 0,
      firstname: "DEFAULT",
      lastname: "DEFAULT",
      gender: "Male",
      country: "DEFAULT",
      native_lang: "DEFAULT",
      lang_focus: "DEFAULT",
      line_id: "DEFAULT",
      meetup_name: "DEFAULT",
      created_at: "DEFAULT"
    },
////////////
//
// Admin
//
////////////

    adminLogin: false,
    admins: [{
      id: 0,
      member_id: "Default_member_id",
      username: "Default_username",
      firstname: "Default_firstname"
    }],
    currentAdmin: {
      id: 1,
      member_id: "kj2jnd2kj32kjdsdsd",
      username: "default_username",
      password: "default_password",
      created_at: "yesterday",
      last_modified: "yesterday"
      
    },
////////////
//
// Line
//
////////////

    messages: [
      {
        id: 1, 
        created_by: "254aa-3453v2-a-23",
        created_by_name: "Russell", 
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
      num_id: 0,
      created_by: "Default",
      message: "Default message",
      created_at: "Default Time",
      last_sent: "Default Time",
      last_modified: "Default Time"
    },
////////////
//
// Bot
//
////////////

    botPermissions: [
      {
        permission_name: "default_name",
        permission_value: false
      }
    ],

////////////
//
// Meetup
//
////////////

    pendingMember: {
      id:0,
      name:"Default Name",
      app_date:"Default app. date",
      link: "Default link",
      answers: {
        answer_one: "one",
        answer_two: "two",
        answer_three: "three"
      }
    },
    pendingMembers: [{
      id:0,
      name:"Default Name",
      app_date:"Default app. date",
      link: "Default link",
    }],

////////////
//
// Other
//
////////////

    statusMessage: null,
    jwt: "",
    
  },
  getters: {
    isAuthenticated(state) {
      return isValidJwt(state.jwt)
    }

  },

  mutations: {

////////////
//
// Members
//
////////////

    setUnregisteredMembers(state, payload) {
      state.unregisteredMembers = payload.unregisteredMembers
      state.unregisteredMembers.push({name: "MEMBER DOESN'T EXIST"})
    },
    setMembers(state, payload) {
      state.members = payload
    },
    setEditMember(state, payload) {
      state.editMember = payload
    },

////////////
//
// Admin
//
////////////

    setAdminLoginToTrue(state) {
      state.adminLogin = true
    },
    setAdmins(state, payload) {
      state.admins = payload
    },
    setCurrentAdmin(state, payload) {
      state.currentAdmin = payload
    },

////////////
//
// Line
//
////////////

    setMessages(state, payload) {
      state.messages = payload
    },    
    setEditMessage(state, payload) {
      state.editMessage = payload
    },

////////////
//
// Bot
//
////////////

    setBotPermissions(state, payload) {
      state.botPermissions = payload
    },

////////////
//
// Meetup
//
////////////

    setPendingMembers(state, payload) {
      state.pendingMembers = payload
    },

////////////
//
// Other
//
////////////

    setStatusMessage(state, payload) {
      state.statusMessage = payload
    },
    setJwtToken(state, payload) {
      localStorage.token = payload.jwt.token
      state.jwt = payload.jwt
    },
  },
  actions: {
////////////
//
// Members
//
////////////
    
    async saveNewMember({ commit, dispatch }, payload) {
      try {
        const auth = { headers: { Authorization: this.state.jwt } }
        const res = await axios.post("/api/members/create/", payload, auth)
          if (res.data.status != 0) {
            throw res.data.status
          }
        dispatch("getMembers")

        const unregistedMembers = await axios.get("/api/meetup/current-members", auth)
        commit("setUnregisteredMembers", unregistedMembers.data)
      
      } catch (err) {
        console.error(err)
        EventBus.$emit("failedMemberCreation", err)
      }
    },

    async getMembers({ commit }) {
      try {
        const auth = { headers: { Authorization: this.state.jwt } }
        const res = await axios.get("/api/members/", auth)
        if (res.data.status == 0) {
          commit("setMembers", res.data.members)          
        }
      } catch (err) {
        console.error(err)
      }
    },

    async updateMember({ dispatch }, payload) {
      try {
        const auth = { headers: { Authorization: this.state.jwt } }
        const res = await axios.post("/api/members/update/", payload, auth)
        if (res.data.status == 0) {
          dispatch("getMembers")
        } else {
          throw "Member not found!"
        }        
      } catch (err) {
        console.log(err)        
      }
    },

////////////
//
// Admin
//
////////////
    async login({ commit, dispatch }, payload) {
      try {
        const res = await axios.post("/api/admins/login/", payload)

        if (res.data.status == -1) {
          throw res.data.status
        }
        commit("setJwtToken", {jwt: res.data.token})
        commit("setCurrentAdmin", res.data)
        commit("setAdminLoginToTrue")
        dispatch("getData")
      } catch (err) {
        EventBus.$emit('failedAuthentication', err)
      }
    },

    async getAdmins({ commit }) {
      try {
        const auth = { headers: { Authorization: this.state.jwt } }
        const res = await axios.get("/api/admins", auth)

        if (res.data.status != 0) {
          throw res.data.status
        }

        commit("setAdmins", res.data.admins)
      } catch(err) {
        console.error(err)
      }

    },

    async getData({ commit, dispatch }) {
      try {

        const auth = { headers: { Authorization: this.state.jwt } }

        const unregistedMembers = await axios.get("/api/meetup/current-members", auth)
        commit("setUnregisteredMembers", unregistedMembers.data)

        const registeredMembers = await axios.get("/api/members", auth)
        commit("setMembers", registeredMembers.data.members)

        const lineMessages = await axios.get("/api/line/messages", auth)
        commit("setMessages", lineMessages.data.messages)

        const botPermissions = await axios.get("/api/line/bot", auth)
        commit("setBotPermissions", botPermissions.data.permissions)

        const admins = await axios.get("/api/admins", auth)
        commit("setAdmins", admins.data.admins)

        dispatch("getPendingMembers")
        dispatch("updatePendingMembers")

      } catch (err) {
        console.error(err)
      }
    },

    async saveNewPassword(context, payload) {
      try {
        context
        const auth = { headers: { Authorization: this.state.jwt } }
        const res = await axios.post("/api/admins/password", payload, auth)

        if (res.data.status != 0) {
          EventBus.$emit("failedPassword", 1)

        }

      } catch (err) {
        console.error(err)
      }
    },

    async createNewAdmin({ commit, dispatch }, payload) {
      try {
        commit
        const auth = { headers: { Authorization: this.state.jwt } }
        const res = await axios.post("/api/admins/create/", payload, auth)
        if (res.data.status == 0) {
          dispatch("getAdmins")
        } else {
          throw "Create New Admin Failed!"

        }
      } catch (err) {
        console.error(err)
      }
    },

////////////
//
// Line
//
////////////

    async saveLineMessage({ commit }, payload) {
      try {
        const auth = { headers: { Authorization: this.state.jwt } }
        await axios.post("/api/line/messages/create/", payload, auth)
        const lineMessages = await axios.get("/api/line/messages", auth)
        commit("setMessages", lineMessages.data.messages)
      } catch (err) {
        console.error(err)
      }
    },

    async getSavedMessages({ commit }) {
      try {
        const auth = { headers: { Authorization: this.state.jwt } }
        const res = await axios.get("/api/line/messages", auth)
        commit ("setMessages", res.data)
      } catch (err) {
        console.error(err)
      }
    },

    async saveEditedMessage({ commit }, payload) {
      try {
        const auth = { headers: { Authorization: this.state.jwt } }
        const res = await axios.post(`/api/line/messages/message/${payload.id}`, payload, auth)
        commit("setMessages", res.data.messages)        

      } catch (err) {
        console.error(err)
      }
    },

////////////
//
// Bot
//
////////////

    async getBotPermissions({commit}) {
      try {
        const auth = { headers: { Authorization: this.state.jwt } }
        const res = await axios.get("/api/line/bot", auth)
        commit("setBotPermissions", res.data.permissions)
      } catch (err) {
        console.error(err)
      }
    },

    async updateBotPermissions({dispatch}, payload) {
      try {
        const auth = { headers: { Authorization: this.state.jwt } }
        const res = await axios.post('/api/line/bot', payload, auth)
        await dispatch("getBotPermissions", res.data.permissions)
      } catch (err) {
        console.error(err)
      }
    },

////////////
//
// Meetup
//
////////////
    async getPendingMembers({ commit }) {
      try {
        const auth = { headers: { Authorization: this.state.jwt } }
        const res = await axios.get("/api/meetup/new-members/", auth)
        if (res.data.status == 0) {
          commit("setPendingMembers", res.data.pending_members)
        }
      } catch (err) {
        console.error(err)
      }
    },
    async updatePendingMembers() {
      try {
        const auth = { headers: { Authorization: this.state.jwt } }
        await axios.get("/api/meetup/new-members/update/", auth)

      } catch (err) {
        console.error(err)
      }
    },
    async approvePendingMember({ commit }, payload) {
      try {
        const auth = { headers: { Authorization: this.state.jwt } }
        const res = await axios.post("/api/meetup/new-members/approve/", payload, auth)
        if (res.data.status == 0) {
          commit("setPendingMembers", res.data.pending_members)
        }

      } catch (err) {
        console.error(err)
      }
    },
    async denyPendingMember({ commit }, payload) {
      try {
        const auth = { headers: { Authorization: this.state.jwt } }
        const res = await axios.post("/api/meetup/new-members/deny/", payload, auth)
        if (res.data.status == 0) {
          commit("setPendingMembers", res.data.pending_members)
        }

      } catch (err) {
        console.error(err)
      }
    },
  },
  modules: {
  }
})
