<template>
  <v-container>
    <v-layout justify-center>
      <v-card outlined max-width="500" width="500" class="card_cloverleaf mb-5 mt-10 px-5">
        <v-card-title class="title_card_cloverleaf mt-7">Kontak Kami</v-card-title>
        <v-card-subtitle class="subtitle_card_cloverleaf">Informatics Festival (IFest) #8</v-card-subtitle>

        <v-card-text v-if="!messages.message" class="mb-5">
          <v-form ref="form" @submit.prevent="register">
            <v-text-field
              v-model="full_name"
              label="Nama Lengkap"
              
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
              
              :error="errors.email"
              :error-messages="errors.email_pengirim"
            ></v-text-field>
            <v-textarea 
              label="Pesan"
            v-model="pesan" :error-messages="errors.pesan" :rules="rulesPesan" class="mb-3"></v-textarea>
            <v-btn
              large
              block
              color="primary"
              type="submit"
              :loading="loading"
              :disabled="!isComplete"
              
            >Kirim</v-btn>
          </v-form>
          <br />Silahkan kirimkan pertanyaan, kritik atau saran kepada pihak panitia melalui form resmi diatas.
          Panitia akan berusaha secepat mungkin untuk membalas pesan anda.
        </v-card-text>
        <v-card-text class="mt-5" v-if="messages.message">
          <v-alert type="success" class="mb-8" outlined prominent>{{ messages.message }}</v-alert>
          <v-layout justify-center class="mb-5">
            <router-link to="/">
              <v-btn color="success" dark>Kembali ke Halaman Utama</v-btn>
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

.link_clover {
  text-decoration: unset !important;
}

.link_clover:hover {
  color: cornflowerblue;
}
</style>