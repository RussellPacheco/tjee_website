import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from "../views/Login"
import Admin from "../views/Admin"
import NewMessage from "../views/Line/NewMessage"
import ViewMessages from "../views/Line/ViewMessages"
import SendMessage from "../views/Line/SendMessage"
import EditMessage from "../views/Line/EditMessage"
import Permissions from "../views/Bot/Permissions"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/admin',
    name: 'Admin',
    component: Admin
  },
  {
    path: '/line/new-message',
    name: 'NewMessage',
    component: NewMessage
  },
  {
    path: '/line/view-messages',
    name: 'ViewMessages',
    component: ViewMessages
  },
  {
    path:'/line/send-message',
    name: 'SendMessage',
    component: SendMessage
  },
  {
    path:'/line/edit-message',
    name: 'EditMessage',
    component: EditMessage
  },
  {
    path: '/bot/permissions',
    name: 'Permissions',
    component: Permissions
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
