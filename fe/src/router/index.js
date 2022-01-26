import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from "../views/User/Login"
import Admin from "../views/Admin"
import NewMessage from "../views/Line/NewMessage"
import ViewMessages from "../views/Line/ViewMessages"
import SendMessage from "../views/Line/SendMessage"
import EditMessage from "../views/Line/EditMessage"
import Permissions from "../views/Bot/Permissions"
import NewMember from "../views/Member/NewMember"
import ViewMembers from "../views/Member/ViewMembers"
import EditMember from "../views/Member/EditMember"
import ViewPendingMembers from "../views/Member/ViewPendingMembers"
import Settings from "../views/User/Settings"
import NotFound from "../views/NotFound"
import store from "../store"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/admin',
    name: 'Admin',
    component: Admin,
    beforeEnter: (to, from, next) => {
      if (!store.getters.isAuthenticated) {
        next('/login')
      } else {
        next()
      }
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/user/settings',
    name: 'Settings',
    component: Settings,
    beforeEnter: (to, from, next) => {
      if (!store.getters.isAuthenticated) {
        next('/login')
      } else {
        next()
      }
    }
  },
  {
    path: '/line/new-message',
    name: 'NewMessage',
    component: NewMessage,
    beforeEnter: (to, from, next) => {
      if (!store.getters.isAuthenticated) {
        next('/login')
      } else {
        next()
      }
    }
  },
  {
    path: '/line/view-messages',
    name: 'ViewMessages',
    component: ViewMessages,
    beforeEnter: (to, from, next) => {
      if (!store.getters.isAuthenticated) {
        next('/login')
      } else {
        next()
      }
    }
  },
  {
    path:'/line/send-message',
    name: 'SendMessage',
    component: SendMessage,
    beforeEnter: (to, from, next) => {
      if (!store.getters.isAuthenticated) {
        next('/login')
      } else {
        next()
      }
    }
  },
  {
    path:'/line/edit-message',
    name: 'EditMessage',
    component: EditMessage,
    beforeEnter: (to, from, next) => {
      if (!store.getters.isAuthenticated) {
        next('/login')
      } else {
        next()
      }
    }
  },
  {
    path: '/bot/permissions',
    name: 'Permissions',
    component: Permissions,
    beforeEnter: (to, from, next) => {
      if (!store.getters.isAuthenticated) {
        next('/login')
      } else {
        next()
      }
    }
  },
  {
    path: '/member/new-member',
    name: 'NewMember',
    component: NewMember,
    beforeEnter: (to, from, next) => {
      if (!store.getters.isAuthenticated) {
        next('/login')
      } else {
        next()
      }
    }
  },
  {
    path: '/member/view-member',
    name: 'ViewMembers',
    component: ViewMembers,
    beforeEnter: (to, from, next) => {
      if (!store.getters.isAuthenticated) {
        next('/login')
      } else {
        next()
      }
    }
  },
  {
    path:'/member/edit-member',
    name: 'EditMember',
    component: EditMember,
    beforeEnter: (to, from, next) => {
      if (!store.getters.isAuthenticated) {
        next('/login')
      } else {
        next()
      }
    }
  },
  {
    path:'/member/pending-members',
    name: 'ViewPendingMembers',
    component: ViewPendingMembers,
    beforeEnter: (to, from, next) => {
      if (!store.getters.isAuthenticated) {
        next('/login')
      } else {
        next()
      }
    }
  },
  {
    path: '*',
    name: 'NotFound',
    component: NotFound,
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
