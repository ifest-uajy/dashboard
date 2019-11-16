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
          <v-card class="pa-2 pb-5" outlined :disabled="c.kompetisi.isExpired">
            <v-card-title>{{c.nama}}</v-card-title>
            <v-card-subtitle class="pb-0">
              <p>
                by
                <span class>{{c.ketua}}</span>
              </p>
            </v-card-subtitle>
            <v-card-subtitle>
              <h2 class="black--text mb-2">Informasi Tim</h2>

              <h3>{{c.kompetisi.name}}</h3>

              <p class="black--text mb-1 mt-4">Nama Tim</p>
              <v-text-field readonly v-model="c.nama" outlined></v-text-field>

              <p class="black--text mb-1">Asal Institusi</p>
              <v-text-field readonly v-model="c.asal" outlined></v-text-field>

              <p class="black--text mb-1">Token Tim</p>
              <v-text-field
                :id="`CopyThis-`+c.id"
                v-model="c.token"
                readonly
                append-icon="mdi-content-copy"
                @click:append="copyText(c.id, c.token)"
                outlined
                :persistent-hint="true"
                hint="Berikan token diatas ke user lain untuk bergabung dengan tim ini."
              ></v-text-field>
              <!--<v-btn @click="copyText('' + c.invitation_token)">copy</v-btn>-->
            </v-card-subtitle>
            <v-card-subtitle>
              <h2 class="black--text mb-2">Anggota Tim</h2>
              <v-content class="px-0" v-for="u in c.anggota" :key="u">
                <p class="mb-0">
                  {{u}}
                  <span v-if="c.ketua == u">(Ketua Tim)</span>
                </p>
              </v-content>
            </v-card-subtitle>
            <v-card-subtitle>
              <h2 class="black--text mb-1">Task Lomba</h2>
              <p
                class="mt-2"
              >Dibawah ini adalah task-task yang harus diselesaikan oleh tim untuk mengikuti kompetisi.</p>

              <v-stepper vertical>
                <div v-for="task in c.tasks" :key="task.task.order">
                  <v-stepper-step
                    :step="task.task.order"
                    :complete="task.task.order < c.current_task.order"
                  >
                    {{task.task.name}}
                    <small
                      v-if="task.task.task_type === 'upload file'"
                      class="mt-2"
                    >Task Deadline: {{moment(String(task.task.deadline)).format("DD MMMM YYYY HH:MM")}}</small>
                  </v-stepper-step>

                  <v-stepper-content
                    :step="task.task.order"
                    :complete="task.task.order < c.current_task.order"
                  >
                    <span v-if="task.task.order === c.current_task.order">
                      <UploaderWidget :task="task.task" :response="task.response" />
                    </span>
                  </v-stepper-content>
                </div>
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
import UploaderWidget from "./UploaderWidget.vue";
export default {
  computed: mapState({
    competitions: state => state.competition.competitions,
    teams: state => state.competition.teams,
  }),
  components: {
    UploaderWidget
  },
  methods: {
    copyText(id, invitation_token) {
      //async function copyToClipboard() {
      try {
        // 1) Copy text
        //console.log('copyinig');
        //await
        navigator.clipboard.writeText(invitation_token);

        console.log(this.$refs["CopyThis-" + id]);
        // 2) Catch errors
      } catch (err) {
        //console.error('Failed to copy: ', err);
      }
      //}
    },
    moment,
  },
};
</script>