<template>
  <v-flex>
    <v-form @submit.prevent="sumbitFile">
      <v-flex>
        <v-flex>
          <vue-dropzone
          class="mb-5"
            ref="dropzone"
            id="dropzone"
            :hidden="response.status === 'selesai' || response.status === 'menunggu_verifikasi'"
            :options="dropOptions"
            @vdropzone-file-added="uploadFile"
            @vdropzone-success="uploadSuccess"
            @vdropzone-error="uploadError"
            @vdropzone-complete="uploadComplete"
          />
        </v-flex>
        <div v-if="response.length !== 0 && response.status !== 'ditolak'">
          File berhasil diunggah pada
          <b>{{moment(String(response.updated_at)).format("DD MMMM YYYY hh:mm A")}}</b>
          <br />
          <a :href="downloadUrl" class="body-link" target="_blank">Unduh file</a>
        </div>
        
        <div v-else><div v-html="task.deskripsi"></div></div> <br />

        <div v-if="response.length !== 0 && response.status === 'ditolak'">
          File terakhir berhasil diunggah pada 
          <b>{{moment(String(response.updated_at)).format("DD MMMM YYYY hh:mm A")}}</b>
          <br />
          <a :href="downloadUrl" class="body-link" target="_blank">Unduh file</a>
        </div>

        <v-alert
          v-if="response.length !== 0 && response.status === 'ditolak'"
          :value="true"
          class="mt-5"
          type="error"
          outlined
          prominent
        >File yang anda upload tidak sesuai dengan kriteria. Silahkan upload ulang atau hubungi pihak panitia untuk informasi lebih lanjut.</v-alert>
        <v-alert
          v-if="response.length !== 0 && response.status === 'menunggu_verifikasi'"
          :value="true"
          type="info"
          outlined
          prominent
        >
          Panitia akan memverifikasi file yang anda upload.
          <br />Mohon tunggu dalam waktu
          <b>1 x 24</b> jam.
        </v-alert>
        <v-alert v-if="dropzoneError" :value="true" type="error" outlined>{{ dropzoneError }}</v-alert>
      </v-flex>
    </v-form>
    <v-dialog v-model="dialog" persistent max-width="350">
      <v-card>
        <v-card-title class="headline">Pastikan file yang diupload sudah benar!</v-card-title>
        <v-card-text>File yang akan diupload adalah <b>{{file_name}}</b>. Kesempatan untuk mengunggah file hanya ada sekali.</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="handleUpload">Upload</v-btn>
          <v-btn color="red darken-1" text @click="handleBatal">Batal</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-snackbar
      v-model="uploadBatalSB"
    >
      Upload file dibatalkan
    </v-snackbar>
  </v-flex>
</template>

<script>
import vue2Dropzone from "vue2-dropzone";
import { mapState, mapActions } from 'vuex'
import Cookies from 'js-cookie'
import moment from "moment";
import "vue2-dropzone/dist/vue2Dropzone.min.css";
export default {
  props: ["task", "response", "team"],
  components: {
    vueDropzone: vue2Dropzone
  },
  data: () => ({
    dialog: false,
    file_name: "",
    uploadBatalSB: false,
    loading: false,
      dropOptions: {
        url: "/api/file/upload/",
        maxFiles: 1,
        maxFilesize: 10, // MB,
        autoProcessQueue: false,
        addRemoveLinks: true,
        dictDefaultMessage: "<i class='fa fa-cloud-upload'></i> Upload File",
        acceptedFiles: '.zip',
      },
      dropzoneError: null
  }),
  methods: {
    moment,
    ...mapActions({
    addTaskResponse: 'competition/postTaskResponse',
    getTeams: "competition/getTeams",
  }),
  handleUpload: function() {
    this.dialog = false
    this.$refs.dropzone.processQueue()
    this.file_name = ""
  },
  handleBatal: async function() {
    this.dialog = false
    this.$refs.dropzone.removeAllFiles(true)
    this.file_name = ""
    this.uploadBatalSB = true
     await setTimeout(() => (this.uploadBatalSB = false), 2000);
  },
    uploadFile: function (file) { 
      this.dialog = true
      this.file_name = file.name;
      this.dropzoneError = null
    },
    uploadSuccess: function (file, response) {
      this.addTaskResponse({
        team_id: this.team.id,
        task_id: this.task.id,
        response: response.message,
      }),
      this.loading = true;
      this.getTeams();
      this.loading = false;
    },
    uploadError: function (file, message, xhr) {
      this.dropzoneError = message
    },
    uploadComplete: function (file) {
      this.$refs.dropzone.removeAllFiles(true)
      this.file_name = ""
    }
  },
  computed: {
    downloadUrl: function () {
      if(this.response.length == 0) return false
      return "/api/file/download/" + this.response.response + '/'
    },
  },
  mounted: function () {
    this.$refs.dropzone.setOption(
      'headers',
      {
        'X-CSRFToken': Cookies.get('csrftoken')
      }
    )
  }
};
</script>

<style>
@import url("https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css");
</style>