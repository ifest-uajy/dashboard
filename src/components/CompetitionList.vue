<template>
  <v-container class="px-0 mx-0">
    <!--   <v-container class="mb-0 pb-0">
     <v-badge class="mb-5">
        <template
          v-if="Object.keys(competitions).length !== 0"
          v-slot:badge
        >{{Object.keys(competitions).length}}</template>
        <h3 class="subtitle pb-0 mb-0">Kompetisi</h3>
      </v-badge>
    </v-container>
    -->
    <v-container v-if="Object.keys(competitions).length === 0">
      <v-content>
        <v-alert prominent outlined>
          <p class="font-weight-bold mb-0">Be ready!</p>
          <p class="black--text text--darken-2 mb-1">
            Tunggu info selanjutnya di media sosial kami untuk kompetisi yang
            akan berlangsung.
          </p>
        </v-alert>
      </v-content>
    </v-container>

    <v-container class="pt-0">
      <v-row style="background: #fff">
        <v-col v-for="c in competitions" :key="c.id" cols="12" sm="4">
          <d-card :disabled="c.isExpired || c.is_closed">
            <d-card-body :title="c.name">
              <d-badge class="mr-2" pill theme="primary">
                <span v-if="c.team_min_member !== c.team_max_member">
                  Tim: <strong>{{ c.team_min_member }}</strong> - <strong>{{ c.team_max_member }}</strong> orang
                </span>
                <span v-if="c.team_min_member === c.team_max_member">
                  <span v-if="c.team_min_member === 1">
                    Individual
                  </span>
                  <span v-if="c.team_min_member !== 1">
                    Tim: <strong>{{ c.team_min_member }}</strong> orang
                  </span>
                </span>
              </d-badge>
              <d-badge pill theme="light">
                Biaya:
                <strong>
                <span v-if="c.biaya_pendaftaran !== 0">
                  Rp. {{ formatPrice(c.biaya_pendaftaran) }}
                </span>
                <span v-if="c.biaya_pendaftaran === 0">
                  Gratis
                </span>
                  </strong>
              </d-badge>
              <p class="mt-3">{{ c.description }}</p>
              <p class="red--text darken-4">
                📢 Daftar sebelum
                <span class="font-weight-bold">
                  {{ moment(String(c.closed_date)).format("DD MMMM YYYY") }}
                </span>
              </p>
              <span v-if="c.isExpired || c.is_closed">
                <d-btn block-level disabled theme="danger">
                Pendaftaran Ditutup
              </d-btn>
              </span>
              <span v-else>
                <router-link :to="`competition/` + c.slug_name">
                <d-btn block-level theme="success">Daftar &rarr;</d-btn>
              </router-link>
              </span>
            </d-card-body>
          </d-card>
        </v-col>
      </v-row>
    </v-container>

    <!--<v-container>
      <div >
        <v-card class="mb-5" outlined>
          
        </v-card>
      </div>
    </v-container>-->
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import moment from "moment";
export default {
  data: () => ({
    token: "",
    tokenRules: [v => !!v || "Token diperlukan"]
  }),
  computed: {
    isTokenFilled() {
      return this.token;
    },
    ...mapState({
      competitions: state => state.competition.competitions,
      errors: state => state.competition.errors,
      messages: state => state.competition.messages,
      loading: state => state.competition.loading
    })
  },
  methods: {
    moment,
    formatPrice(value) {
      let val = (value / 1).toFixed(0).replace(".", ",");
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    },
    ...mapActions({
      joinTeam: "competition/joinTeam",
      clear: "competition/clear"
    }),
    joinTeamHandler(e) {
      this.joinTeam({
        token: this.token
      });
      this.$refs.form.reset();
    }
  },
  beforeRouteLeave(to, from, next) {
    this.clear();
    next();
  }
};
</script>

<style scoped>
.wordBreak {
  word-break: normal !important;
}
</style>
