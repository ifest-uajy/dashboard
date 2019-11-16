<template>
  <v-flex>
    <v-form @submit.prevent="sumbitFile">
      <v-flex>
        <v-flex class="mb-5">
          <vue-dropzone
            ref="dropzone"
            id="dropzone"
            v-if="response.status !== 'selesai'"
            :options="dropOptions"
          />
        </v-flex>
        <div v-if="response.length !== 0">
          File berhasil diunggah:
          <b>{{moment(String(response.updated_at)).format("DD MMMM YYYY HH:MM")}}</b> (UTC+7)
          <br />
          <a :href="downloadUrl" class="body-link" target="_blank">Unduh file</a>
        </div>
        <div v-else>Belum ada file diunggah.</div>

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
        <v-alert v-if="dropzoneError" :value="true" type="error" outline>{{ dropzoneError }}</v-alert>
      </v-flex>
    </v-form>
  </v-flex>
</template>

<script>
import vue2Dropzone from "vue2-dropzone";
import moment from "moment";
import "vue2-dropzone/dist/vue2Dropzone.min.css";
export default {
  props: ["task", "response"],
  components: {
    vueDropzone: vue2Dropzone
  },
  data: function() {
    return {
      dropOptions: {
        url: "https://httpbin.org/post",
        maxFiles: 1,
        maxFilesize: 10,
        addRemoveLinks: true,
        dictDefaultMessage: "<i class='fa fa-cloud-upload'></i> Upload File"
      },
      dropzoneError: null
    };
  },
  methods: {
    moment
  }
};
</script>

<style>
@import url("https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css");
</style>