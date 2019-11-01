<template>
  <v-container>
    <v-layout justify-center>
      <v-card outlined max-width="500" width="500">
        <v-card-title>Reset Password</v-card-title>
        <v-card-subtitle>Informatics Festival #8</v-card-subtitle>

        <v-card-text v-if="!messages.message">
          <v-form ref="form" @submit.prevent="resetPassword">
            <v-text-field
              v-model="email"
              label="Email"
              type="email"
              required
              autocomplete="username"
              :rules="emailRules"
              outlined
              v-on:focus="this.clear"
            ></v-text-field>
            <p class="font-weight-medium">
              <router-link to="/register">Belum punya akun?</router-link>
            </p>

            <v-btn
              large
              block
              color="primary"
              type="submit"
              :loading="loading"
              :disabled="!this.validEmail(this.email)"
            >Register</v-btn>
          </v-form>
        </v-card-text>
        <v-card-text>
             <v-alert v-if="messages.message" type="success" outlined>{{ messages.message }}</v-alert>
              <v-layout v-if="messages.message" justify-center>
            <router-link to="/"><v-btn color="success" dark>Kembali ke halaman utama</v-btn></router-link>
          </v-layout>
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
        emailRules: [
            v => !!v || "E-mail is required",
            v => /.+@.+\..+/.test(v) || "E-mail must be valid"
        ],
    }),
      components: {
    Footer
  },
    computed: {
        ...mapState({
            messages: state => state.authsys.message,
            errors: state => state.authsys.errors,
            loading: state=> state.authsys.loading
        })
    },
    methods: {
        validEmail: function (email) {
      var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
        ...mapActions({
            resetAction: 'authsys/reset',
            clear: 'authsys/clear'
        }),

        resetPassword() {
            this.resetAction({
                email: this.email,
                password: this.password,
                router: this.$router
            })
        }
    },
    beforeRouteLeave(to, from, next) {
       this.clear()
       next()
    }
}
</script>