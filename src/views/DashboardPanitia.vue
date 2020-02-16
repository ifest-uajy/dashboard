<template>
  <v-layout pt-12 class="bg-img">
    <!-- /* LOGOUT BUTTON */ -->
    <div @click="logoutActions" class="logout-btn">
      <a>Keluar</a>
    </div>

    <v-container>
      <div class="header-box">
        <img
          class="circle-top"
          src="https://dashboard.ifest-uajy.com/assets/atma_jaya5050.png"
        />
        <img
          class="circle-top"
          src="https://dashboard.ifest-uajy.com/assets/himaforka5050.png"
        />
        <img
          class="circle-top"
          src="https://dashboard.ifest-uajy.com/assets/ifest5050.png"
        />
      </div>
      <v-container>
        <h2 class="judul">Dashboard Panitia</h2>
        <h1 class="title sub-judul mb-0">
          Selamat datang,
          <span class="font-weight-bold">{{ user.full_name }}</span
          >!
        </h1>
      </v-container>

      <v-container class="pt-0 mt-0">
        <h1 class="title">Rekap Data Peserta Lomba</h1>
        <p>
          Menu ini adalah menu untuk menyajikan data peserta dalam tim yang
          sudah mendaftar dalam masing-masing kompetisi.
        </p>

        <div v-if="loading">
          <v-row style="background: #fff">
            <v-col key="0" cols="12" sm="4">
              <v-card class="pa-2 pb-5" outlined>
                <v-skeleton-loader
                  class="mt-5 ml-5 pb-5"
                  type="heading"
                ></v-skeleton-loader>
                <v-skeleton-loader
                  type="text"
                  class="ml-5 pb-5"
                  max-width="250"
                ></v-skeleton-loader>
                <v-skeleton-loader
                  type="button"
                  class="ml-5 pb-3"
                ></v-skeleton-loader>
              </v-card>
            </v-col>
          </v-row>
        </div>
        <div v-else>
          <v-row>
            <v-col v-for="c in competitions" :key="c.id" cols="12" sm="4">
              <v-card class="pa-2 pb-5" outlined>
                <v-card-title class="mb-0">
                  <span class="wordBreak">{{ c.name }}</span>
                </v-card-title>

                <v-card-subtitle class="pb-0 pt-1 pb-3">
                  Jumlah Pendaftar :
                  <strong>Undefined</strong> Tim
                </v-card-subtitle>

                <v-card-actions>
                  <v-btn
                    class="ml-2 mt-0"
                    outlined
                    :to="`/administrasi/competition/` + c.slug_name + `/`"
                    color="black"
                    >Lihat Data</v-btn
                  >
                </v-card-actions>
              </v-card>
            </v-col>
          </v-row>
        </div>
      </v-container>
    </v-container>
  </v-layout>
</template>

<script>
import { mapState, mapActions } from "vuex";

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
      this.$router.push({ name: "dashboard" });
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

.subtitle-inner {
  font-size: 9pt;
  margin: 0;
  font-weight: bold;
  color: rgb(0, 11, 32);
}

.subtitle-outer {
  margin: 0;
  padding: 0;
  margin-bottom: 10px;
}

.title-inner {
  margin: 0;
  padding: 0;
  margin-bottom: 10px;
  font-size: 14pt;
  font-weight: bold;
  margin-top: 25px;
}

.outer-link {
  text-decoration: none !important;
  font-size: 16pt;
  margin-top: 10px;
}

.wordBreak {
  word-break: normal !important;
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

.sub-judul {
  font-family: "Roboto", sans-serif;
  line-height: 1.1em;
  font-size: 24pt;
  font-weight: 500;
  margin-bottom: 20px;
}

.bg-img {
  width: 100%;
  background: url("https://ifest-uajy.com/assets/email/bg_top2.jpg") no-repeat;
}
</style>
