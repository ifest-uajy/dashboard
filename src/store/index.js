import Vue from 'vue'
import Vuex from 'vuex'

// Website modules import
import authsys from '../models/authsys'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    authsys
  }
})
