import Vue from 'vue'
import Router from 'vue-router'
import HomeComponent from './views/home.vue';
import RegistrationComponent from './views/registration.vue';
import NotFound from './views/404.vue'
import LoginComponent from './views/login.vue'

Vue.use(Router)

const router = new Router({
    mode: 'history',
    routes: [
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
            path: '*',
            component: NotFound
        }
    ]
})

export default router