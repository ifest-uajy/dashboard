<template>
  <v-flex>
    <v-form @submit.prevent="sumbitFile">
      <v-flex>
        <v-flex>
          <vue-dropzone
          class="mb-5"
            ref="dropzone"
            id="dropzone"
            :hidden="response.status === 'selesai'"
            :options="dropOptions"
            @vdropzone-file-added="uploadFile"
            @vdropzone-success="uploadSuccess"
            @vdropzone-error="uploadError"
            @vdropzone-complete="uploadComplete"
          />
        </v-flex>
        <div v-if="response.length !== 0">
          File berhasil diunggah:
          <b>{{moment(String(response.updated_at)).format("DD MMMM YYYY hh:mm A")}}</b>
          <br />
          <a :href="downloadUrl" class="body-link" target="_blank">Unduh file</a>
        </div>
        
        <div v-else>Belum ada file diunggah.<br/></div>
        <div class="mt-3" v-if="response.length !== 0 && response.status === 'menunggu_verifikasi'" v-html="task.deskripsi"></div>

        <br />
        <v-alert
          v-if="response.length !== 0 && response.status === 'ditolak'"
          :value="true"
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
    loading: false,
      dropOptions: {
        url: "/api/file/upload/",
        maxFiles: 1,
        maxFilesize: 10, // MB
        addRemoveLinks: true,
        dictDefaultMessage: "<i class='fa fa-cloud-upload'></i> Upload File"
      },
      dropzoneError: null
  }),
  methods: {
    moment,
    ...mapActions({
    addTaskResponse: 'competition/postTaskResponse',
    getTeams: "competition/getTeams",
  }),
    uploadFile: function () {
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