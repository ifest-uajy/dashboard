import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeComponent from '../views/home.vue'
import LoginComponent from '../views/Login.vue'
import NotFoundComponent from '../views/404.vue'
import RegistrationComponent from '../views/registration.vue'
import DashboardComponent from '../views/dashboard.vue'

import { reqLogin, reqAnonymous } from '../control/userhandle'

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
    name: 'login',
    path: '/login',
    component: LoginComponent,
    meta: {
      title: 'Login Peserta - Informatics Festival #8',
      metaTags: [
        {
          name: 'description',
          content: 'Deskripsi ifest 8 tolong segera di lengkapi ya'
        },
        {
          property: 'og:description',
          content: 'Deskripsi ifest 8 tolong segera di lengkapi ya'
        }
      ]
    },
    beforeEnter: reqAnonymous
  },
  {
    path: '/register',
    component: RegistrationComponent,
    meta: {
      title: 'Registrasi Peserta - Informatics Festival #8',
      metaTags: [
        {
          name: 'description',
          content: 'Deskripsi ifest 8 tolong segera di lengkapi ya'
        },
        {
          property: 'og:description',
          content: 'Deskripsi ifest 8 tolong segera di lengkapi ya'
        }
      ]
    }
  },
  {
    name: 'dashboard',
    path: '/dashboard',
    component: DashboardComponent,
    beforeEnter: reqLogin,
    meta: {
      title: 'Dashboard Peserta - Informatics Festival #8',
      metaTags: [
        {
          name: 'description',
          content: 'Deskripsi ifest 8 tolong segera di lengkapi ya'
        },
        {
          property: 'og:description',
          content: 'Deskripsi ifest 8 tolong segera di lengkapi ya'
        }
      ]
    }
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


