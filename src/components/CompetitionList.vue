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
          <p
            class="black--text text--darken-2 mb-1"
          >Tunggu info selanjutnya di media sosial kami untuk kompetisi yang akan berlangsung.</p>
        </v-alert>
      </v-content>
    </v-container>

    <v-container class="pt-0">
      <v-row style="background: #fff">
        <v-col v-for="c in competitions" :key="c.id" cols="12" sm="4">
          <v-card class="pa-2 pb-5" outlined :disabled="c.isExpired">
            <v-card-title class="mb-3">
              <span class="wordBreak">{{c.name}}</span>
            </v-card-title>

            <v-card-subtitle class="pb-0">
              <p>{{c.description}}</p>

              <v-chip class="mr-2 mb-3" outlined color="black">
                <v-avatar left>
                  <v-icon>mdi-calendar</v-icon>
                </v-avatar>
                {{moment(String(c.closed_date)).format("DD MMMM YYYY")}}
              </v-chip>

              <v-chip color="black accent-3 mb-3" outlined>
                <span v-if="c.team_min_member !== c.team_max_member">
                  <v-avatar left>
                    <v-icon>mdi-account-group</v-icon>
                  </v-avatar>
                  {{c.team_min_member}} - {{c.team_max_member}} orang
                </span>
                <span v-if="c.team_min_member === c.team_max_member">
                  <span v-if="c.team_min_member === 1">
                    <v-avatar left>
                      <v-icon>mdi-account</v-icon>
                    </v-avatar>Individual
                  </span>
                  <span v-if="c.team_min_member !== 1">
                    <v-avatar left>
                      <v-icon>mdi-account</v-icon>
                    </v-avatar>
                    {{c.team_min_member}} orang
                  </span>
                </span>
              </v-chip>

              <v-chip color="black mb-3" outlined>
                <span v-if="c.biaya_pendaftaran !== 0">
                  <v-avatar left>
                    <v-icon>mdi-cash</v-icon>
                  </v-avatar>
                  Rp. {{formatPrice(c.biaya_pendaftaran)}}
                </span>
                <span v-if="c.biaya_pendaftaran === 0">
                  <v-avatar left>
                    <v-icon>mdi-cash</v-icon>
                  </v-avatar>Gratis
                </span>
              </v-chip>
            </v-card-subtitle>

            <v-card-actions>
              <v-btn v-if="c.isExpired" color="grey" text>Daftar</v-btn>
              <v-btn
                class="ml-2"
                v-if="!c.isExpired"
                outlined
                :to="`competition/`+c.slug_name"
                color="black"
              >Daftar</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="12" sm="4">
          <v-card class="pa-2 pb-5" outlined>
            <v-card-title>Punya invitation token?</v-card-title>

            <v-card-text v-if="messages.message">
              <v-alert type="success" outlined>{{ messages.message }}</v-alert>
              <v-layout v-if="messages.message" justify-center>
                <router-link to="/dashboard/teams">
                  <v-btn color="success" dark>Lihat Tim</v-btn>
                </router-link>
              </v-layout>
            </v-card-text>

            <v-form v-if="!messages.message" ref="form" @submit.prevent="joinTeamHandler">
              <v-container>
                <v-text-field v-model="token" outlined label="Token" required :rules="tokenRules"></v-text-field>
                <v-btn
                  large
                  block
                  color="primary"
                  type="submit"
                  :error="errors.token"
                  :error-messages="errors.token"
                  :disabled="!isTokenFilled"
                >Gabung</v-btn>
              </v-container>
            </v-form>

            <v-card-text>
              Gunakan invitation token yang diberikan oleh ketua tim untuk bergabung dalam satu tim.
            </v-card-text>

            <v-card-text v-if="errors.message" class="pb-0 mb-0">
              <v-alert class="mb-0" type="error" outlined>{{ errors.message }}</v-alert>
            </v-card-text>

          </v-card>
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
      loading: state => state.competition.loading,
    })
  },
  methods: {
    moment,
    formatPrice(value) {
      let val = (value / 1).toFixed(2).replace(".", ",");
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
      this.$refs.form.reset()
    }
  },
  beforeRouteLeave(to, from, next) {
    this.clear();
    next();
  }
};
</script>

<style scoped>
.wordBreak{
  word-break: normal !important;
}
</style>