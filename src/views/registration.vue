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
          >Registrasi</v-card-title
        >
        <v-card-subtitle class="subtitle_card_cloverleaf"
          >Informatics Festival (IFest) #9</v-card-subtitle
        >
        <v-card-text v-if="!messages.message" class="mb-7">
          <v-form ref="form" @submit.prevent="register">
            <v-text-field
              v-model="full_name"
              label="Nama Lengkap"
              hint="Isi dengan mengunakan singkatan sedikit mungkin."
              :error="errors.full_name"
              :error-messages="errors.full_name"
              :rules="nameRequired"
            ></v-text-field>
            <v-text-field
              v-model="email"
              label="Email Aktif"
              type="email"
              hint="Gunakan alamat email aktif untuk kepentingan konfirmasi pendaftaran akun."
              required
              :rules="emailRules"
              :error="errors.email"
              :error-messages="errors.email"
            ></v-text-field>
            <v-text-field
              v-model="password"
              label="Password"
              type="password"
              autocomplete="current-password"
              required
              :rules="passwordRules"
            ></v-text-field>
            <v-text-field
              v-model="confirmPassword"
              label="Confirm Password"
              type="password"
              class="mb-3"
              required
              :rules="[
                v => !!v || 'Confirm Password cannot be empty',
                v => v === password || 'Password does not match'
              ]"
            ></v-text-field>

            <p class="font-weight-medium">
              <router-link to="/login" class="link_clover"
                >Sudah punya akun?</router-link
              >
            </p>
            <!-- <p class="font-weight-medium">
              <router-link to="/login" class="link_clover">Sudah punya akun?</router-link>
            </p> -->

            <v-btn
              large
              block
              color="primary"
              type="submit"
              :loading="loading"
              :disabled="!isComplete"
              >Daftar</v-btn
            >
          </v-form>
        </v-card-text>
        <v-card-text class="mt-5" v-if="messages.message">
          <v-alert type="success" class="mb-8" outlined prominent>{{
            messages.message
          }}</v-alert>
          <v-layout justify-center class="mb-5">
            <router-link to="/login">
              <v-btn color="success" dark>Login ke dashboard</v-btn>
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
    password: "",
    confirmPassword: "",
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+\..+/.test(v) || "E-mail must be valid"
    ],
    passwordRules: [v => !!v || "Password is required"],
    nameRequired: [v => !!v || "Nama diperlukan"]
  }),
  computed: {
    isComplete() {
      return (
        this.full_name &&
        this.email &&
        this.password &&
        this.confirmPassword &&
        this.password === this.confirmPassword
      );
    },
    ...mapState({
      errors: state => state.authsys.errors,
      messages: state => state.authsys.message,
      loading: state => state.authsys.loading
    })
  },
  methods: {
    ...mapActions({
      registerAction: "authsys/register",
      clear: "authsys/clear"
    }),
    register() {
      this.registerAction({
        full_name: this.full_name,
        password: this.password,
        email: this.email
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