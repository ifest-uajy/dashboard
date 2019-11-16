<template>
  <v-container>
    <v-card class="mx-auto" outlined max-width="650">
      <v-card-title class="ml-3 mr-3 mt-5">Registrasi Tim</v-card-title>
      <v-card-subtitle class="ml-3 mr-3">Informatics Festival (IFest) #8</v-card-subtitle>

      <v-card-text v-if="messages.message">
        <v-alert type="success" outlined>{{ messages.message }}</v-alert>
        <v-layout v-if="messages.message" justify-center>
          <router-link to="/dashboard/competition">
            <v-btn color="success" dark>Lihat Tim</v-btn>
          </router-link>
        </v-layout>
      </v-card-text>

      <v-card-text v-if="errors.message" class="pb-0 mb-0">
        <v-alert class="mb-0" type="error" outlined>{{ errors.message }}</v-alert>
      </v-card-text>

      <v-form v-if="!messages.message" ref="form" @submit.prevent="register" class="mr-3 ml-3">
        <v-container>
          <v-container class="px-0 grey--text text--darken-4 title">Informasi Tim</v-container>
          <v-text-field v-model="namaTim" outlined label="Nama Tim" required></v-text-field>
          <v-text-field v-model="namaInstitusi" outlined label="Institusi Asal" required></v-text-field>
          <v-textarea v-model="alamatInstitusi" outlined label="Alamat Institusi" required></v-textarea>
          <v-container class="px-0 grey--text text--darken-4 title">Informasi Pendamping Tim</v-container>
          <v-text-field v-model="namaPendamping" outlined label="Nama Pendamping" required></v-text-field>
          <v-text-field
            v-model="teleponPendamping"
            outlined
            prefix="+62"
            label="Nomor Telepon"
            :persistent-hint="true"
            hint="Diutamakan untuk mengisi nomor telepon yang terhubung dengan WhatsApp."
          ></v-text-field>

          <p class="mr-1 ml-1 mt-5">
            <span style="font-weight: bold;">
              Ketentuan Perlombaan
            </span>
            <br/>
            Dengan membuat tim dalam kompetisi ini saya bersedia untuk ....
        </p>
        

          <center class="mt-8 mb-5">
            <v-btn
            large
            color="primary"
            type="submit"
            :loading="loading"
            :disabled="loading"
          >Register</v-btn>

          <router-link to="/dashboard/competition">
            <v-btn large class="ml-5" dark>Kembali</v-btn>
          </router-link>
          </center>
        </v-container>
      </v-form>

    </v-card>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import moment from "moment";
export default {
  data: () => ({
    namaTim: "",
    namaInstitusi: "",
    alamatInstitusi: "",
    namaPendamping: "",
    teleponPendamping: ""
  }),
  computed: mapState({
    competitions: state => state.competition.competitions,
    loading: state => state.competition.isLoading,
    errors: state => state.competition.errors,
    messages: state => state.competition.messages
  }),
  methods: {
    moment,
    ...mapActions({
      registerCompetition: "competition/register",
      clear: "competition/clear"
    }),
    register() {
      this.registerCompetition({
        slug_name: this.$route.params.slug,
        name: this.namaTim,
        team_institution: this.namaInstitusi,
        alamat_institution: this.alamatInstitusi,
        nama_pembimbing: this.namaPendamping,
        no_telp_pembimbing: this.teleponPendamping
      });
    }
  },
  beforeRouteLeave(to, from, next) {
    this.clear();
    next();
  }
};
</script>