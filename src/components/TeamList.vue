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
          >Untuk dapat mulai berkompetisi lengkapi profil kamu di tab profil dan daftarkan tim kamu di tab kompetisi atau gunakan kode undangan dari ketua tim kamu di form dibawah ini.</p>
        </v-alert>
      </v-content>
    </v-container>

    <v-container class="grey lighten-5 pt-0">
      <v-row style="background: #fff">
        <v-col v-for="c in teams" :key="c.id" cols="12" sm="6">
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
            <v-card-subtitle>
              Task Kompetisi
              
              <br/>
              Tugas tim sekarang adalah {{c.current_task.name}} dengan batas submission pada 
              {{moment(String(c.current_task.deadline)).format("DD MMMM YYYY HH:MM")}}


            </v-card-subtitle>

            <v-card-subtitle>

<v-stepper v-for="task in c.task_list" :key="task.order" vertical>
    <v-stepper-step :step="task.order" :complete="c.current_task.order > task.order">
      {{task.name}}
      <small v-if="task.task_type === 'upload file'" class="mt-2">Task Deadline: {{moment(String(task.deadline)).format("DD MMMM YYYY HH:MM")}}</small>
      
          
      
      

    </v-stepper-step>

<v-stepper-content :step="task.order" v-if="c.current_task.order === task.order">

      <v-card color="grey lighten-1" class="mb-12" height="200px">

      <span v-if="c.current_task.order === task.order">

        SHOW THIS TO UP PROPO

      </span>
      <span v-if="c.current_task.order > task.order">

        Task ini sudah selese

      </span>
      </v-card>
    </v-stepper-content>

  </v-stepper>


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

    },
    moment,
  }
};
</script>