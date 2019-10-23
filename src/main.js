// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Buefy from 'buefy'
import VueAxios from 'vue-axios'
import axios from 'axios'
import router from './router'
import 'buefy/dist/buefy.css'

Vue.config.productionTip = false

Vue.use(VueAxios, axios)
Vue.use(Buefy)

/* eslint-disable no-new */
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')