<template>
  <v-container>
    <v-layout justify-center>
      <v-card outlined max-width="500" width="500">
        <v-card-title>Hubungi Kami</v-card-title>
        <v-card-subtitle>Informatics Festival (IFest) #8</v-card-subtitle>

        <v-card-text v-if="!messages.message">
          <v-form ref="form" @submit.prevent="register">
            <v-text-field
              v-model="full_name"
              label="Nama Lengkap"
              outlined
              :error="errors.full_name"
              :error-messages="errors.nama_pengirim"
              :rules="rulesNama"
            ></v-text-field>
            <v-text-field
              v-model="email"
              label="Email"
              type="email"
              required
              :rules="emailRules"
              outlined
              :error="errors.email"
              :error-messages="errors.email_pengirim"
            ></v-text-field>
            <v-textarea v-model="pesan" :error-messages="errors.pesan" outlined :rules="rulesPesan"></v-textarea>
            <v-btn
              large
              block
              label="Pesan"
              color="primary"
              type="submit"
              :loading="loading"
              :disabled="!isComplete"
            >Kirim</v-btn>
          </v-form>
          <br />Silahkan kirimkan pertanyaan, kritik atau saran kepada pihak panitia melalui form resmi diatas.
          Panitia akan berusaha secepat mungkin untuk membalas pesan anda.
        </v-card-text>
        <v-card-text>
          <v-alert v-if="messages.message" type="success" outlined>{{ messages.message }}</v-alert>
          <v-layout v-if="messages.message" justify-center>
            <router-link to="/">
              <v-btn color="success" dark>Kembali ke Dashboard</v-btn>
            </router-link>
          </v-layout>
        </v-card-text>
      </v-card>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  data: () => ({
    btnDisabled: true,
    full_name: "",
    email: "",
    pesan: "",
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+\..+/.test(v) || "E-mail must be valid"
    ],
    rulesNama: [v => !!v || "Nama Lengkap harus diisi."],
    rulesPesan: [v => !!v || "Pesan harus diisi."]
  }),
  computed: {
    isComplete() {
      return this.full_name && this.email && this.pesan;
    },
    ...mapState({
      errors: state => state.msgHandle.errors,
      messages: state => state.msgHandle.messages,
      loading: state => state.msgHandle.loading
    })
  },
  methods: {
    ...mapActions({
      sendPesan: "msgHandle/send",
      clear: "msgHandle/clear"
    }),

    register() {
      this.sendPesan({
        nama_pengirim: this.full_name,
        pesan: this.pesan,
        email_pengirim: this.email
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
.title-section {
  margin-bottom: 50px;
}
.registrationSection {
  margin: 10vh auto;
  min-height: 100vh;
  max-height: 100vh;
}
</style>