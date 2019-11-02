<template>
  <v-container class="px-0 mx-0">
    <v-container class="mb-0 pb-0">
      <v-badge class="mb-5">
        <template
          v-if="Object.keys(competitions).length !== 0"
          v-slot:badge
        >{{Object.keys(competitions).length}}</template>
        <h3 class="subtitle pb-0 mb-0">Kompetisi</h3>
      </v-badge>
    </v-container>

    <v-container class="grey lighten-5 pt-0">
      <v-row>
        <v-col v-for="c in competitions" :key="c.id" cols="12" sm="4">
          <v-card class="pa-2" outlined height="100%" :disabled="c.isExpired">
            <v-card-title class="mb-4">{{c.name}}</v-card-title>

            <v-card-subtitle>
              <p>{{c.description}}</p>

              <p class="subtitle-2 text--primary mb-0">
                <v-icon>mdi-calendar</v-icon>
                {{moment(String(c.closed_date)).format("DD MMMM YYYY")}}
              </p>
            </v-card-subtitle>

            <v-card-actions>
              <v-btn color="purple" text>Daftar</v-btn>
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
import { mapState, mapActions } from "vuex";
import moment from "moment";
export default {
  computed: mapState({
    competitions: state => state.competition.competitions
  }),
  methods: {
    ...mapActions({
      getCompetition: "competition/getCompetition"
    }),
    moment
  },
  beforeMount() {
    this.getCompetition();
  }
};
</script>