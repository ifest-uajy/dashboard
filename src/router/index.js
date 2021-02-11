import Vue from "vue";
import VueRouter from "vue-router";
import HomeComponent from "../views/Home.vue";

import LoginComponent from "../views/Login.vue";
import NotFoundComponent from "../views/404.vue";
import KontakKamiView from "../views/KontakKamiView";
import RegistrationComponent from "../views/registration.vue";
import ResendActivation from "../views/ResendActivation.vue"
/*

  TODO:
  Make sure imported modules below changed to use lazy load
  eg: const Home = () => import(/* webpackChunkName: "home" `*`/ './Home.vue');
  docs: https://dzone.com/articles/3-code-splitting-patterns-for-vuejs-and-webpack

*/

import ConfirmComponent from "../views/Confirm.vue";
import ResetPasswordComponent from "../views/ResetPassword.vue";
import ResetPasswordHandlerComponent from "../views/resetPasswordHandler.vue";
import changePasswordComponent from "../views/changePassword.vue";

import DashboardComponent from "../views/DashboardView.vue";
import PemberitahuanComponent from "../components/Pemberitahuan.vue";
import ProfileComponent from "../components/ProfileView";
import CompetitionListComponent from "../components/CompetitionList";
import CompetitionRegisterComponent from "../components/CompetitionRegister";
import TeamListView from "../components/TeamList";
import SekretView from "../views/sekret.vue";
import PanitiaView from "../views/DashboardPanitia.vue";

import { reqLogin, reqAnonymous } from "../control/userhandle";
import HelpDesk from "@/views/HelpDesk";

Vue.use(VueRouter);

const routes = [
  {
    path: "/index.html",
    redirect: "/"
  },
  {
    path: "/",
    title: "Informatics Festival (IFest) #9",
    component: HomeComponent,
    meta: {
      title: "Dashboard - Informatics Festival (IFest) #9"
    }
  },
  {
    name: "kontak-kami",
    path: "/contact",
    meta: {
      title: "Kontak Kami - Informatics Festival (IFest) #9"
    },
    component: KontakKamiView
  },
  {
    name: "sekret-view",
    path: "/administrasi",
    component: PanitiaView,
    meta: {
      title: "Administrasi Data - Informatics Festival (IFest) #9"
    },
    beforeEnter: reqLogin
  },
  {
    path: "/administrasi/competition/:slug",
    component: SekretView,
    meta: {
      title: "Administrasi Data - Informatics Festival (IFest) #9"
    },
    beforeEnter: reqLogin
  },
  {
    name: "login",
    path: "/login",
    component: LoginComponent,
    meta: {
      title: "Masuk - Informatics Festival (IFest) #9",
      hideFooter: true
    },
    beforeEnter: reqAnonymous
  },
  {
    name: "register",
    path: "/register",
    component: RegistrationComponent,
    beforeEnter: reqAnonymous,
    meta: {
      title: "Pendaftaran - Informatics Festival (IFest) #9",
      hideFooter: true
    }
  },
  {
    path: "/resend",
    component: ResendActivation,
    beforeEnter: reqAnonymous,
    meta: {
      title: "Kirim Ulang Email Aktivasi - Informatics Festival (IFest) #9"
    }
  },
  {
    path: "/dashboard",
    component: DashboardComponent,
    beforeEnter: reqLogin,
    children: [
      {
        path: "",
        name: "dashboard",
        component: PemberitahuanComponent,
        meta: {
          title: "Pengumuman - Informatics Festival (IFest) #9"
        }
      },
      {
        path: "competition",
        name: "kompetisi",
        component: CompetitionListComponent,
        meta: {
          title: "Kompetisi - Informatics Festival (IFest) #9"
        }
      },
      {
        path: "profile",
        name: "profil",
        component: ProfileComponent,
        meta: {
          title: "Profil - Informatics Festival (IFest) #9"
        }
      },
      {
        path: "teams",
        name: "teams",
        component: TeamListView,
        meta: {
          title: "Tim - Informatics Festival (IFest) #9"
        }
      },
      {
        path: "competition/:slug",
        name: "register_competition",
        component: CompetitionRegisterComponent,
        meta: {
          title: "Daftar Kompetisi - Informatics Festival (IFest) #9"
        }
      },
      {
        path: "profile/changepassword",
        name: "changepassword",
        component: changePasswordComponent,
        meta: {
          title: "Ganti Password - Informatics Festival (IFest) #9"
        }
      },
      {
        path: "helpdesk",
        name: "Help Desk",
        component: HelpDesk,
        meta: {
          title: "Help Desk - Informatics Festival (IFesst) #9"
        }
      }
    ]
  },
  {
    path: "/confirm/:token",
    component: ConfirmComponent,
    beforeEnter: reqAnonymous,
    meta: {
      title: "Konfirmasi Email - Informatics Festival (IFest) #9"
    }
  },
  {
    path: "/reset-password/:token",
    component: ResetPasswordHandlerComponent,
    beforeEnter: reqAnonymous,
    meta: {
      title: "Reset Password - Informatics Festival (IFest) #9"
    }
  },
  {
    path: "/reset-password",
    component: ResetPasswordComponent,
    beforeEnter: reqAnonymous,
    meta: {
      title: "Reset Password - Informatics Festival (IFest) #9"
    }
  },
  {
    path: "*",
    component: NotFoundComponent,
    meta: {
      title: "Halaman Tidak Ditemukan - Informatics Festival (IFest) #9"
    }
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title;
  }
  next();
});

export default router;
