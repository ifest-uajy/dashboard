import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeComponent from '../views/home.vue'
import LoginComponent from '../views/Login.vue'
import NotFoundComponent from '../views/404.vue'
import RegistrationComponent from '../views/registration.vue'
import DashboardComponent from '../views/dashboard.vue'

import { reqLogin } from '../control/userhandle'

Vue.use(VueRouter)

const routes = [
  {
    path: "/index.html",
    redirect: "/" 
  },
  {
    path: '/',
    component: HomeComponent
  },
  {
    path: '/login',
    component: LoginComponent
  },
  {
    path: '/register',
    component: RegistrationComponent
  },
  {
    name: 'dashboard',
    path: '/dashboard',
    component: DashboardComponent,
    beforeEnter: reqLogin
  },
  {
    path: '*',
    component: NotFoundComponent
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})

export default router


