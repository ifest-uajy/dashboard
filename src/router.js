import Vue from 'vue'
import Router from 'vue-router'
import HomeComponent from './views/home.vue';
import RegistrationComponent from './views/registration.vue';

Vue.use(Router)

const router = new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: HomeComponent
        },
        {
            path: '/register',
            component: RegistrationComponent
        }
    ]
})

export default router