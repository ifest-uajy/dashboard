import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./plugins/shards";
import '@/plugins/vuesax'
import vuetify from "@/plugins/vuetify";
import VueLetterAvatar from "vue-letter-avatar";
import VueAnalytics from "vue-analytics";

Vue.use(VueAnalytics, {
  id: "UA-154113787-4",
  router
});

Vue.config.productionTip = false;
Vue.use(VueLetterAvatar);

new Vue({
  router,
  store,
  vuetify,
  render: function(h) {
    return h(App);
  }
}).$mount("#app");
