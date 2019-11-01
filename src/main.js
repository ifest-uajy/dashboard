import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
//import Buefy from 'buefy'
//import 'buefy/dist/buefy.css'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

//Vue.use(Buefy)
//Vue.use(Vuetify)

new Vue({
  router,
  store,
  vuetify,
  render: function (h) { return h(App) }
}).$mount('#app')
