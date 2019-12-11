import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeComponent from '../views/Home.vue'
import LoginComponent from '../views/Login.vue'
import NotFoundComponent from '../views/404.vue'
import RegistrationComponent from '../views/registration.vue'
import DashboardComponent from '../views/DashboardView.vue'
import ConfirmComponent from '../views/Confirm.vue'
import ResetPasswordComponent from '../views/ResetPassword.vue'
import ResetPasswordHandlerComponent from '../views/resetPasswordHandler.vue'
import KontakKamiView from '../views/KontakKamiView'
import changePasswordComponent from '../views/changePassword.vue'

import PemberitahuanComponent from "../components/Pemberitahuan.vue";
import ProfileComponent from "../components/ProfileView";
import CompetitionListComponent from "../components/CompetitionList";
import CompetitionRegisterComponent from "../components/CompetitionRegister";
import TeamListView from "../components/TeamList";
import SekretView from "../views/sekret.vue"
import PanitiaView from "../views/DashboardPanitia.vue"

import { reqLogin, reqAnonymous } from '../control/userhandle'

Vue.use(VueRouter)

const routes = [
  {
    path: "/index.html",
    redirect: "/"
  },
  {
    path: '/',
    title: 'Informatics Festival (IFest) #8',
    component: HomeComponent
  },
  {
    name: 'kontak-kami',
    path: '/contact',
    component: KontakKamiView
  },
  {
    name: 'sekret-view',
    path: '/administrasi',
    component: PanitiaView,
    meta: {
      title: 'Administrasi Data - Informatics Festival (IFest) #8'
    },
    beforeEnter: reqLogin,
  },
  {
    path: '/administrasi/competition/:slug',
    component: SekretView,
    meta: {
      title: 'Administrasi Data - Informatics Festival (IFest) #8'
    },
    beforeEnter: reqLogin,
  },
  {
    name: 'login',
    path: '/login',
    component: LoginComponent,
    meta: {
      title: 'Login - Informatics Festival (IFest) #8',
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
    beforeEnter: reqAnonymous,
    meta: {
      title: 'Registrasi - Informatics Festival (IFest) #8',
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
    path: '/dashboard',
    component: DashboardComponent,
    beforeEnter: reqLogin,
    meta: {
      title: 'Dashboard - Informatics Festival (IFest) #8'
    },
    children: [
      {
        path: '',
        name: 'dashboard',
        component: PemberitahuanComponent
      },
      {
        path: 'competition',
        name: 'kompetisi',
        component: CompetitionListComponent,
      },
      {
        path: 'profile',
        name: 'profil',
        component: ProfileComponent,
      },
      {
        path: 'teams',
        name: 'teams',
        component: TeamListView
      },
      {
        path: 'competition/:slug',
        name: 'register_competition',
        component: CompetitionRegisterComponent
      },
      {
        path: "profile/changepassword",
        name: "changepassword",
        component: changePasswordComponent
      }
    ]
  },
  {
    path: '/confirm/:token',
    component: ConfirmComponent,
    beforeEnter: reqAnonymous
  },
  {
    path: '/reset-password/:token',
    component: ResetPasswordHandlerComponent,
    beforeEnter: reqAnonymous
  },
  {
    path: '/reset-password',
    component: ResetPasswordComponent,
    beforeEnter: reqAnonymous
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


