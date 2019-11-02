<template>
  <v-layout mt-12>
    <!-- /* LOGOUT BUTTON */ -->
    <div @click="logoutActions" class="logout-btn">
      <a>Logout</a>
    </div>
    <v-container>
      <v-container>
        <h2 class="display-1">Dashboard IFest #8</h2>
        <h1 class="title">
          Selamat datang,
          <span class="font-weight-bold">{{user.full_name}}</span>!
        </h1>
      </v-container>

      <Pemberitahuan />

      <CompetitionList />

      <v-container>
        <h3 class="subtitle">Profil</h3>
        
      </v-container>

      <ProfileView />

    </v-container>
    
  </v-layout>
</template>

<script>
import { mapState, mapActions } from "vuex";

import Pemberitahuan from "../components/Pemberitahuan.vue";
import ProfileView from "../components/ProfileView";
import CompetitionList from "../components/CompetitionList"

export default {
  data: () => ({}),
  components: {
    Pemberitahuan,
    ProfileView,
    CompetitionList
  },
  computed: mapState({
    user: state => state.authsys.user
  }),
  methods: {
    ...mapActions({
      logoutActions: "authsys/logout",
      clear: "authsys/clear"
    })
  }
};
</script>

<style scoped>
.logout-btn {
  position: fixed;
  top: 50px;
  right: 0px;
  padding: 0px;
  margin: 0px;
  cursor: pointer;
  width: 40px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
  height: 100px;
  background: #13355b;
  color: #adadad;
  z-index: 15;
  border-radius: 8px 0px 0px 8px;
}
.logout-btn a {
  margin: auto 10px;
  margin-top: 25px;
  writing-mode: tb-rl;
  color: rgb(119, 170, 241);
  text-decoration: none;
}
.logout-btn a:visited {
  text-decoration: none;
}
.logout-btn:hover {
  background: rgb(13, 34, 65);
}
</style>