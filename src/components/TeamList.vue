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

    <v-container class="pt-0">
      <v-row style="background: #fff">
        <v-col v-for="c in teams" :key="c.id" cols="12" sm="6">
          <!-- <v-card class="pa-2 pb-5" outlined :disabled="c.kompetisi.isExpired"> -->
          <v-card class="pa-2 pb-5" outlined>
            <v-card-title class="display-1 mt-5">{{c.nama}}</v-card-title>
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
              <v-text-field class="pt-0" disabled v-model="c.nama"></v-text-field>

              <p class="black--text mb-1">Asal Institusi</p>
              <v-text-field class="pt-0" disabled v-model="c.asal"></v-text-field>

              <p class="black--text mb-1">Token Tim</p>
              <v-text-field
                :id="`CopyThis-`+c.id"
                v-model="c.token"
                readonly
                class="pt-0"
                append-icon="mdi-content-copy"
                @click:append="copyText(c.id, c.token)"
                :persistent-hint="true"
                hint="Berikan token diatas ke user lain untuk bergabung dengan tim ini."
              ></v-text-field>
              <!--<v-btn @click="copyText('' + c.invitation_token)">copy</v-btn>-->
            </v-card-subtitle>
            <v-card-subtitle>
              <h2 class="black--text mb-2">Pendamping Tim</h2>
              <p class="black--text mb-0 mt-4">Nama Pendamping</p>
              <v-text-field class="pt-0" disabled v-model="c.pembimbing.nama"></v-text-field>
            </v-card-subtitle>
            <v-card-subtitle>
              <h2 class="black--text mb-2">Anggota Tim</h2>
              <p class="mt-2">
                Dibawah ini daftar anggota dalam tim ini. Untuk menambahkan anggota berikan token diatas ke teman anda dan join melalui menu kompetisi.
                Anggota tim yang sudah bergabung tidak dapat diganti/dihapus.
              </p>
              <v-content class="px-0 black--text pb-0">
                <ol>
                  <li v-for="u in c.anggota" :key="u" class="mb-0">
                    <span v-if="c.ketua == u">
                      <b>{{u}} - Team Leader</b>
                    </span>
                    <span v-else>{{u}}</span>
                  </li>
                </ol>
              </v-content>
              <v-alert v-if="!c.task_permission" type="error" outlined prominent class="mt-4" dense>
                Anda tidak bisa mengerjakan tugas sebelum anggota tim lengkap.
                <b>Minimal {{c.kompetisi.team_min_member}} orang diperlukan untuk 1 tim dalam kompetisi ini.</b>
              </v-alert>
            </v-card-subtitle>
            <v-card-subtitle :hidden="!c.task_permission">
              <h2 class="black--text mb-1">Task Lomba</h2>
              <p
                class="mt-2"
              >Dibawah ini adalah task-task yang harus diselesaikan oleh tim untuk mengikuti kompetisi.</p>

              <v-stepper vertical v-model="c.current_task.order">
                <div v-for="task in c.tasks" :key="task.task.order">
                  <v-stepper-step
                    :step="task.task.order"
                    :complete="task.task.order < c.current_task.order"
                  >
                    <b>{{task.task.name}}</b>
                    <small
                      v-if="task.task.task_type !== 'pengumuman' && task.response.status !== 'selesai'"
                      class="mt-2"
                    >Task Deadline: {{moment(String(task.task.deadline)).format("DD MMMM YYYY hh:mm A")}}</small>

                    <small
                      class="mt-2"
                      v-if="task.response.length !== 0 && task.response.status === 'selesai'"
                    >
                      File berhasil diunggah pada
                      <b>{{moment(String(task.response.updated_at)).format("DD MMMM YYYY hh:mm A")}}</b>
                      <p class="mt-2 mb-0">
                        <a
                          :href="`/api/file/download/` + task.response.response +`/`"
                          class="body-link"
                          target="_blank"
                        >Unduh file</a>
                      </p>
                    </small>
                  </v-stepper-step>

                  <v-stepper-content
                    :step="task.task.order"
                    :complete="task.task.order < c.current_task.order"
                  >
                    <span v-if="task.task.order === c.current_task.order">
                      <div v-if="!moment().isAfter(moment(task.task.deadline))">
                        <UploaderWidget
                          :hidden="task.task.task_type !== 'file_uploader' && task.task.task_type !== 'payment_verification'"
                          :task="task.task"
                          :response="task.response"
                          :team="c"
                        />
                      </div>
                      <div v-else>
                        <b>{{task.task.name}}</b> sudah ditutup.
                      </div>
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

    <v-snackbar v-model="snackbar">Kode token tim berhasil di salin.</v-snackbar>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import moment from "moment";
import UploaderWidget from "./UploaderWidget.vue";
export default {
  data: () => ({
    snackbar: false
  }),
  computed: mapState({
    competitions: state => state.competition.competitions,
    teams: state => state.competition.teams
  }),
  components: {
    UploaderWidget
  },
  methods: {
    async copyText(id, invitation_token) {
      //async function copyToClipboard() {
      try {
        // 1) Copy text
        //console.log('copyinig');
        //await
        navigator.clipboard.writeText(invitation_token);

        this.snackbar = true;
        await setTimeout(() => (this.snackbar = false), 2000);
        // 2) Catch errors
      } catch (err) {
        //console.error('Failed to copy: ', err);
      }
      //}
    },
    moment
  }
};
</script>