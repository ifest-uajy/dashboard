<template>
  <v-layout mt-12>
    <!-- /* LOGOUT BUTTON */ -->
    <div @click="logoutActions" class="logout-btn">
      <a>Logout</a>
    </div>

    <v-container>
      <v-container>
        <h2 class="display-1">Dashboard</h2>
        <h1 class="title">
          Selamat datang,
          <span class="font-weight-bold">{{user.full_name}}</span>!
        </h1>
      </v-container>

      <v-tabs grow :show-arrows="true">
        <v-tab to="/dashboard">
          <div class="pr-5">
            <v-badge class="mt-2">
              <template v-if="anouncementsCount !== 0" v-slot:badge>{{anouncementsCount}}</template>
              Pengumuman
            </v-badge>
          </div>
        </v-tab>
        <v-tab to="/dashboard/competition">
          <div class="pr-5">
            <v-badge class="mt-2">
              <template v-if="competitionsCount !== 0" v-slot:badge>{{competitionsCount}}</template>
              Kompetisi
            </v-badge>
          </div>
        </v-tab>
        <v-tab to="/dashboard/teams">
          <div class="pr-5">
            <v-badge class="mt-2">
              <template v-if="teamsCount !== 0" v-slot:badge>{{teamsCount}}</template>
              Teams
            </v-badge>
          </div>
        </v-tab>
        <v-tab to="/dashboard/profile">
          <div class="pr-5">
            <v-badge class="mt-2" color="red">
              <template v-if="user.isProfileComplete !== true" v-slot:badge>!</template>
              Profil
            </v-badge>
          </div>
        </v-tab>
      </v-tabs>

      <router-view class="mt-8"></router-view>
    </v-container>
  </v-layout>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  data: () => ({}),
  beforeMount() {
    if (this.user.is_staff) {
      this.$router.push({ name: "sekret-view" });
    } else {
      console.log("Damn")
      this.getAnouncement();
      this.getCompetition();
      this.getTeams();
    }
    
  },
  computed: {
    ...mapState({
      user: state => state.authsys.user,
      competitionsCount: state => state.competition.competitionsCount,
      anouncementsCount: state => state.pemberitahuan.announcementsCount,
      teamsCount: state => state.competition.teamsCount
    })
  },

  methods: {
    ...mapActions({
      logoutActions: "authsys/logout",
      getCompetition: "competition/getCompetition",
      getAnouncement: "pemberitahuan/getPemberitahuan",
      getTeams: "competition/getTeams",
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