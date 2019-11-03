<template>
  <v-container class="px-0 mx-0" >
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

    <v-container class="grey lighten-5 pt-0">
      <v-row style="background: #fff">
        <v-col v-for="c in competitions" :key="c.id" cols="12" sm="4">
          <v-card class="pa-2" outlined height="100%" :disabled="c.isExpired">
            <v-card-title class="mb-4">{{c.name}}</v-card-title>

            <v-card-subtitle class="pb-0">
              <p>{{c.description}}</p>

              <v-chip class="mr-2 mb-3" outlined color="blue">
                <v-avatar left>
                  <v-icon>mdi-calendar</v-icon>
                </v-avatar>
                {{moment(String(c.closed_date)).format("DD MMMM YYYY")}}
              </v-chip>

              <v-chip color="pink accent-3 mb-3" outlined>
                <span v-if="c.team_min_member !== c.team_max_member">
                  <v-avatar left>
                    <v-icon>mdi-account-group</v-icon>
                  </v-avatar>
                  {{c.team_min_member}} - {{c.team_max_member}} orang
                </span>
                <span v-if="c.team_min_member === c.team_max_member">
                  <v-avatar left>
                    <v-icon>mdi-account</v-icon>
                  </v-avatar>Individual
                </span>
              </v-chip>
            </v-card-subtitle>

            <v-card-actions>
              <v-btn v-if="!c.isExpired" color="green" text>Daftar</v-btn>
              <v-btn v-if="c.isExpired" color="grey" text>Ditutup</v-btn>
            </v-card-actions>
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
import { mapState } from "vuex";
import moment from "moment";
export default {
  computed: mapState({
    competitions: state => state.competition.competitions
  }),
  methods: {
    moment
  }
};
</script>