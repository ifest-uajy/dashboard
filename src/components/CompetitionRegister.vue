<template>
  <v-container>
    <v-card outlined max-width="600" width="600" class="card_cloverleaf mb-5 mt-10 px-5 mr-auto ml-auto">
        <v-card-title class="title_card_cloverleaf pt-10">Registrasi Tim</v-card-title>
        <v-card-subtitle class="subtitle_card_cloverleaf">Informatics Festival#8</v-card-subtitle>

      <v-card-text v-if="messages.message">
        <v-alert type="success" outlined>{{ messages.message }}</v-alert>
        <v-layout v-if="messages.message" justify-center>
          <router-link to="/dashboard/teams">
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
          <v-text-field 
            v-model="name" 
            label="Nama Tim" 
            required 
            :error-messages="nameErrors"
            :counter="25"
            @input="$v.name.$touch()"
            @blur="$v.name.$touch()"
          ></v-text-field>
          <v-text-field
            v-model="namaInstitusi"
            label="Asal Institusi"
            required
            :error-messages="instituteErrors"
            @input="$v.namaInstitusi.$touch()"
            @blur="$v.namaInstitusi.$touch()"
            hint="Isilah dengan nama asal universitas atau sekolah tim."
          ></v-text-field>
          <v-textarea
            v-model="alamatInstitusi"
            label="Alamat Asal Institusi"
            required
            :error-messages="addressErrors"
            @input="$v.alamatInstitusi.$touch()"
            @blur="$v.alamatInstitusi.$touch()"
            hint="Isilah dengan alamat asal universitas atau sekolah tim."
          ></v-textarea>

          <v-container class="px-0 grey--text text--darken-4 title">Informasi Pendamping Tim</v-container>

          <v-text-field 
            v-model="namaPendamping"
            label="Nama Pendamping Tim" 
            required 
            :error-messages="pendampingNameErrors"
            @input="$v.namaPendamping.$touch()"
            @blur="$v.namaPendamping.$touch()"
            hint="Isilah dengan nama lengkap guru atau dosen pendamping tim."
          ></v-text-field>
          <v-text-field
            v-model="teleponPendamping"
            prefix="+62"
            @keypress="isNumber($event)"
            label="Nomor Telepon"
            counter="15"
             type="number"
            :error-messages="teleponPendampingErrors"
            @input="$v.teleponPendamping.$touch()"
            @blur="$v.teleponPendamping.$touch()"
          ></v-text-field>

          <p class="mr-1 ml-1 mt-5">
            <span style="font-weight: bold;">
              Ketentuan Perlombaan
            </span>
            <br/>
            Dengan membuat tim saya bersedia untuk menaati segala peraturan yang telah dipublikasikan dalam laman resmi tiap kompetisi perlombaan.
        </p>
        

          <center class="mt-8 mb-5">
            <v-btn
            large
            color="primary"
            type="submit"
            :loading="loading"
            :disabled='!isComplete'
          >Register</v-btn>

          <router-link to="/dashboard/competition">
            <v-btn large class="ml-5" dark>Batal</v-btn>
          </router-link>
          </center>
        </v-container>
      </v-form>

    </v-card>
  </v-container>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, maxLength, numeric, minLength} from 'vuelidate/lib/validators'
import { mapState, mapActions } from "vuex";
import moment from "moment";
export default {
  mixins: [validationMixin],
  validations: {
      name: { required, maxLength: maxLength(25), minLength: minLength(3)},
      namaInstitusi: { required, maxLength: maxLength(100)},
      alamatInstitusi : {required},
      namaPendamping: {required},
      teleponPendamping: {required, minLength: minLength(7), maxLength: maxLength(15)}
    },
  data: () => ({
    name: "",
    namaInstitusi: "",
    alamatInstitusi: "",
    namaPendamping: "",
    teleponPendamping: ""
  }),
  computed: {
    ...mapState({
    competitions: state => state.competition.competitions,
    loading: state => state.competition.isLoading,
    errors: state => state.competition.errors,
    messages: state => state.competition.messages
  }),
  instituteErrors () {
        const errors = []
        if (!this.$v.namaInstitusi.$dirty) return errors
        !this.$v.namaInstitusi.maxLength && errors.push('This field must be at most 100 characters long')
        !this.$v.namaInstitusi.required && errors.push('Asal institusi diperlukan untuk pendaftaran tim.')
        return errors
  },
  nameErrors() {
    const errors = []
    if (!this.$v.name.$dirty) return errors
        !this.$v.name.maxLength && errors.push('Name must be at most 25 characters long')
        !this.$v.name.minLength && errors.push('Nama tim harus paling tidak terdiri dari 3 karakter.')
        !this.$v.name.required && errors.push('Name is required.')
        return errors
  },
  addressErrors () {
        const errors = []
        if (!this.$v.alamatInstitusi.$dirty) return errors
        !this.$v.alamatInstitusi.required && errors.push('Alamat asal institusi diperlukan untuk pendaftaran tim.')
        return errors
  },
  pendampingNameErrors () {
    const errors = []
        if (!this.$v.namaPendamping.$dirty) return errors
        !this.$v.namaPendamping.required && errors.push('Nama pendamping tim tidak boleh kosong.')
        return errors
  },
  teleponPendampingErrors () {
    const errors = []
    if(!this.$v.teleponPendamping.$dirty) return errors
    !this.$v.teleponPendamping.required && errors.push('Nomor telepon pendamping tim tidak boleh kosong.')
    !this.$v.teleponPendamping.maxLength && errors.push('Nomor telepon pendamping must be at most 15 characters long')
        !this.$v.teleponPendamping.minLength && errors.push('Nomor telepon pendamping tim harus paling tidak terdiri dari 7 karakter.')
        return errors
  },
   isComplete () {
    return this.name && this.alamatInstitusi && this.namaInstitusi && this.teleponPendamping && this.namaPendamping
    && this.teleponPendamping.length >= 7 && this.name.length >=3
    
  }
  },
  methods: {
    removeNameError() {
      this.clear();
    },
    isNumber: function(evt) {
      evt = (evt) ? evt : window.event;
      var charCode = (evt.which) ? evt.which : evt.keyCode;
      if ((charCode > 31 && (charCode < 48 || charCode > 57)) && charCode !== 46) {
        evt.preventDefault();;
      } else {
        return true;
      }
    },
    moment,
    ...mapActions({
      registerCompetition: "competition/register",
      clear: "competition/clear"
    }),
    register() {
      this.registerCompetition({
        slug_name: this.$route.params.slug,
        name: this.name,
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

<style scoped>
.card_cloverleaf {
  box-shadow: 0 10px 20px 0 rgba(53,64,90,.2);
  outline: none;
  border: none !important;
  border-radius: 8px !important;
}

.title_card_cloverleaf {
  font-size: 20pt;
  margin-top: 10px;
}

.subtitle_card_cloverleaf {
  font-size: 15pt;
}
</style>