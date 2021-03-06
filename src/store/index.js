import Vue from "vue";
import Vuex from "vuex";

// Website modules import
import authsys from "../models/authsys";
import pemberitahuan from "../models/pemberitahuan";
import competition from "../models/competition";
import msgHandle from "../models/msgHandle";
import sekret from "../models/sekretariat";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    authsys,
    pemberitahuan,
    competition,
    msgHandle,
    sekret
  }
});
