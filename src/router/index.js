import Vue from 'vue'
import Router from 'vue-router'
import LoginComponent from "../views/login.vue"
import DashboardComponent from "../views/dashboard.vue"
import RegistrationComponent from "../views/registration.vue"

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: {
        name: "login"
      }
    },
    {
      path: "/registration",
      name: "registration",
      component: RegistrationComponent
    },
    {
      path: "/login",
      name: "login",
      component: LoginComponent
    },
    {
      path: "/dashboard",
      name: "dashboard",
      component: DashboardComponent
    }
  ]
})