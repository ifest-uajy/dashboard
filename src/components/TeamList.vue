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
    <v-container v-if="Object.keys(teams).length === 0">
      <v-content>
        <v-alert prominent outlined>
          <p class="font-weight-bold mb-0">Wah, sepertinya kamu belum mendaftar kompetisi apapun.</p>
          <p
            class="black--text text--darken-2 mb-1"
          >Untuk dapat mulai berkompetisi lengkapi profil kamu di tab profil dan daftarkan tim kamu di tab kompetisi.</p>
        </v-alert>
      </v-content>
    </v-container>

    <v-container class="grey lighten-5 pt-0">
      <v-row style="background: #fff">
        <v-col v-for="c in teams" :key="c.id" cols="12" sm="4">
          <v-card class="pa-2 pb-5" outlined :disabled="c.isExpired">
            <v-card-title>{{c.name}}</v-card-title>
            <v-card-subtitle class="pb-0">
              <p>
                by
                <span class>{{c.team_leader_name}}</span>
              </p>
            </v-card-subtitle>
            <v-card-subtitle>
              <p class="black--text mb-2">Team Invitation Token</p>
                  <v-text-field :id="`CopyThis-`+c.id"
              v-model="c.invitation_token"
              readonly
              append-icon="mdi-content-copy"
              @click:append="copyText(c.id, c.invitation_token)"
              outlined
              :persistent-hint="true"
              hint="Berikan token diatas ke user lain untuk bergabung dengan tim ini."
              ></v-text-field>
              <!--<v-btn @click="copyText('' + c.invitation_token)">copy</v-btn>-->
  
            </v-card-subtitle>
            <v-card-subtitle class="pb-0 pt-0">
              <p class="mb-0 pb-0 black--text bold">{{c.institution}}</p>
              <p class="mb-0 pb-0">{{c.track.name}}</p>
            </v-card-subtitle>
            <v-card-subtitle>
              <p class="black--text mb-1">Anggota Tim</p>
                <v-content class="px-0" v-for="u in c.team_members" :key="u.id">
                    <p class="mb-0">{{u.user}}
                      <span v-if="c.team_leader_name == u.user">(Ketua Tim)</span>
                    </p>
                </v-content>
            </v-card-subtitle>
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
    competitions: state => state.competition.competitions,
    teams: state => state.competition.teams
  }),
  methods: {
    copyText (id, invitation_token) {
      //async function copyToClipboard() {
        try {
          // 1) Copy text
          //console.log('copyinig');
          //await 
          navigator.clipboard.writeText(invitation_token);
          
      console.log(this.$refs['CopyThis-' + id])
          // 2) Catch errors
        } catch (err) {
          //console.error('Failed to copy: ', err);
        }
      //}

    }
  }
};
</script>