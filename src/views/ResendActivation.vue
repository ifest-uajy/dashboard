<template>
  <v-container>
    <v-layout justify-center>
      <v-card
        outlined
        max-width="500"
        width="500"
        class="card_cloverleaf mb-5 mt-10 px-5"
      >
        <v-card-title class="title_card_cloverleaf mt-7"
          >Kirim Ulang Email Aktivasi</v-card-title
        >
        <v-card-subtitle class="subtitle_card_cloverleaf"
          >Informatics Festival (IFest) #9</v-card-subtitle
        >

        <v-card-text v-if="!messages.message && !errors.message" class="mb-6">
          <v-form ref="form" @submit.prevent="kirimEmail">
            <v-text-field
              v-model="email"
              label="Email"
              type="email"
              class="mb-3"
              required
              autocomplete="username"
              :rules="emailRules"
              v-on:focus="this.clear"
            ></v-text-field>
            <p class="font-weight-medium">
              <router-link to="/register" class="link_clover"
                >Belum punya akun?</router-link
              >
            </p>

            <v-btn
              large
              block
              color="primary"
              type="submit"
              :loading="loading"
              :disabled="!this.validEmail(this.email)"
              >Kirim</v-btn
            >
          </v-form>
        </v-card-text>
        <v-card-text class="mt-5" v-if="messages.message">
          <v-alert type="success" class="mb-8" outlined prominent>{{
            messages.message
          }}</v-alert>
          <v-layout justify-center class="mb-5">
            <router-link to="/">
              <v-btn color="success" dark>Kembali ke Halaman Utama</v-btn>
            </router-link>
          </v-layout>
        </v-card-text>
        <v-card-text class="mt-5" v-if="errors.message">
          <v-alert type="error" class="mb-8" outlined prominent>{{
            errors.message
          }}</v-alert>
          <v-layout justify-center class="mb-5">
            <router-link to="/">
              <v-btn color="error" dark>Kembali ke Halaman Utama</v-btn>
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
    email: "",
    emailRules: [
      v => !!v || "Email diperlukan untuk melanjutkan.",
      v => /.+@.+\..+/.test(v) || "Email tidak valid."
    ]
  }),
  computed: {
    ...mapState({
      messages: state => state.authsys.message,
      errors: state => state.authsys.errors,
      loading: state => state.authsys.loading
    })
  },
  methods: {
    validEmail: function(email) {
      var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
    ...mapActions({
      resendAction: "authsys/resend",
      clear: "authsys/clear"
    }),

    kirimEmail() {
      this.resendAction({
        email: this.email,
        router: this.$router
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
  box-shadow: 0 10px 20px 0 rgba(53, 64, 90, 0.2);
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
