<template>
  <v-layout class="bg-img" pt-12>
    <!-- /* LOGOUT BUTTON */ -->
    <div class="logout-btn" @click="logoutActions">
      <a>Keluar</a>
    </div>

    <v-container class="mb-5 pb-5">
      <div class="row align-items-center">
        <div class="col-auto">
          <div class="header-box">
            <img class="circle-top" src="https://dashboard.ifest-uajy.com/assets/ifest5050.png"/>
          </div>
        </div>
        <div class="col pl-0">
          <h3 class="judul mb-0 font-weight-bold">Dashboard Panitia</h3>
          <h5 class="font-weight-bold mb-0">Informatics Festival (IFest) #9</h5>
        </div>
      </div>

      <v-container class="pt-0 mt-0">
        <div class="mt-5 pt-5">
          <div class="row">
            <div class="col-sm-4" v-if="loading">
              <d-card>
                <d-card-body>
                   <v-skeleton-loader
                      class="pb-5"
                      type="heading"
                    ></v-skeleton-loader>
                    <v-skeleton-loader
                        class="pb-5"
                        max-width="250"
                        type="text"
                    ></v-skeleton-loader>
                    <v-skeleton-loader
                        class="pb-3"
                        type="button"
                    ></v-skeleton-loader>
                </d-card-body>
              </d-card>
            </div>
            <div class="col-sm-4" v-for="(competition, k) in competitions" :key="k" v-else>
              <d-card>
                <d-card-body>
                  <d-badge class="mb-3 mr-1">Competition</d-badge>
                  <d-badge v-if="competition.isExpired" theme="danger" class="mb-3">Closed</d-badge>
                  <p class="font-weight-bold">{{competition.name}}</p>
                  <router-link :to="`/administrasi/competition/` + competition.slug_name + `/`">
                    <d-btn theme="light">Lihat Data &rarr;
                    </d-btn>
                  </router-link>
                </d-card-body>
              </d-card>
            </div>
          </div>
        </div>
      </v-container>
    </v-container>
  </v-layout>
</template>

<script>
import {mapActions, mapState} from "vuex";

export default {
  data: () => ({}),
  computed: {
    ...mapState({
      user: state => state.authsys.user,
      competitions: state => state.competition.competitions,
      loading: state => state.competition.isLoading
    })
  },
  beforeMount() {
    if (this.user.is_staff) {
      this.getCompetition();
    } else {
      this.$router.push({name: "dashboard"});
    }
  },
  methods: {
    ...mapActions({
      logoutActions: "authsys/logout",
      getCompetition: "competition/getCompetition",
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

.circle-top {
  margin: auto 10px;
  /* padding: 10px; */
  height: 50px;
  width: 50px;
  background: white;
  border-radius: 100%;
}

.judul {
  font-family: "Roboto", sans-serif;
  line-height: 1.1em;
  font-size: 30pt;
  color: #0f4c75;
  font-weight: 500;
}
</style>
