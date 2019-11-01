<template>
  <v-container>
    <v-layout justify-center>
      <v-card outlined max-width="500" width="500">
        <v-card-title>Registrasi Peserta</v-card-title>
        <v-card-subtitle>Informatics Festival #8</v-card-subtitle>

        <v-card-text>
          <v-form ref="form" @submit.prevent="login">
            <v-text-field
              v-model="email"
              label="Email"
              type="email"
              required
              :rules="emailRules"
              outlined
            ></v-text-field>
            <v-text-field
              v-model="password"
              label="Password"
              type="password"
              autocomplete="current-password"
              required
              outlined
            ></v-text-field>

            <p class="font-weight-medium">
              <router-link to="/reset-password">Lupa password?</router-link>
            </p>
            <p class="font-weight-medium">
              <router-link to="/register">Belum punya akun?</router-link>
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
          <v-alert v-if="errors.message" type="error" outlined>{{ errors.message }}</v-alert>
        </v-card-text>
      </v-card>
    </v-layout>
    <Footer />
  </v-container>
</template>
<script>
import { mapState, mapActions } from 'vuex'
import Footer from "../components/Footer";

export default {
    data: () => ({
        email: '',
        password: '',
        emailRules: [
            v => !!v || "E-mail is required",
            v => /.+@.+\..+/.test(v) || "E-mail must be valid"
        ]
    }),
      components: {
    Footer
  },
    computed: {
            isComplete() {
      return (
        this.email &&
        this.password
      );
    },
        ...mapState({
            errors: state => state.authsys.errors,
            loading: state=> state.authsys.loading
        })
    },
    methods: {
        ...mapActions({
            loginAction: 'authsys/login',
            clear: 'authsys/clear'
        }),

        login() {
            this.loginAction({
                email: this.email,
                password: this.password,
                router: this.$router
            })
        }
    },
    //beforeRouteLeave(to, from, next) {
       // this.clear()
       // next()
    //}
}
</script>