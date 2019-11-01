<template>
  <v-container>
    <v-layout justify-center>
      <v-card outlined max-width="500" width="500">
        <v-card-title>Registrasi Peserta</v-card-title>
        <v-card-subtitle>Informatics Festival #8</v-card-subtitle>

        <v-card-text v-if="!messages.message">
          <v-form ref="form" @submit.prevent="register">
            <v-text-field v-model="full_name" label="Name" outlined               :error="errors.full_name"
              :error-messages="errors.full_name"></v-text-field>
            <v-text-field
              v-model="email"
              label="Email"
              type="email"
              required
              :rules="emailRules"
              outlined
              :error="errors.email"
              :error-messages="errors.email"
            ></v-text-field>
            <v-text-field
              v-model="password"
              label="Password"
              type="password"
              autocomplete="current-password"
              required
              outlined
              :rules="passwordRules"
            ></v-text-field>
            <v-text-field
              v-model="confirmPassword"
              label="Confirm Password"
              type="password"
              required
              :rules="[(v) => !!v || 'Confirm Password cannot be empty', (v) => v === password || 'Password does not match']"
              outlined
            ></v-text-field>

            <p class="font-weight-medium">
              <router-link to="/reset-password">Lupa password?</router-link>
            </p>
            <p class="font-weight-medium">
              <router-link to="/login">Sudah punya akun?</router-link>
            </p>

            <v-btn
              large
              block
              color="primary"
              type="submit"
              :loading="loading"
              :disabled="!isComplete"
            >Register</v-btn>
          </v-form>
        </v-card-text>
        <v-card-text>
          <v-alert v-if="messages.message" type="success" outlined>{{ messages.message }}</v-alert>
          <v-layout v-if="messages.message" justify-center>
            <router-link to="/login"><v-btn color="success" dark>Login ke dashboard</v-btn></router-link>
          </v-layout>
        </v-card-text>
      </v-card>
    </v-layout>
    <Footer />
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import Footer from "../components/Footer";

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
    passwordRules: [
        v => !!v || "Password is required"
    ]
  }),
  components: {
    Footer
  },
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