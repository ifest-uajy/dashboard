<template>
  <v-container>
    <v-layout justify-center>
      <v-card outlined max-width="500" width="500">
        <v-card-title>Reset Password</v-card-title>
        <v-card-subtitle>Informatics Festival #8</v-card-subtitle>

        <v-card-text v-if="hideBoxes">
          <v-form ref="form" @submit.prevent="resetPassword">
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
              <router-link to="/register">Belum punya akun?</router-link>
            </p>

            <v-btn
              large
              block
              color="primary"
              type="submit"
              :loading="loading"
              :disabled="!this.validPassword(this.password, this.confirmPassword)"
            >Register</v-btn>
          </v-form>
        </v-card-text>
        <v-card-text>
             <v-alert v-if="messages.message" type="success" outlined>{{ messages.message }}</v-alert>
              <v-layout v-if="messages.message" justify-center>
            <router-link to="/login/"><v-btn color="success" dark>Login ke dashboard</v-btn></router-link>
          </v-layout>
          <v-alert v-if="errors.message" type="error" outlined>{{ errors.message }}</v-alert>
          <v-layout v-if="errors.message" justify-center>
            <router-link to="/"><v-btn color="error" dark>Kembali ke halaman utama</v-btn></router-link>
          </v-layout>
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
        password: '',
        confirmPassword: '',
        passwordRules: [
        v => !!v || "Password is required"
    ]
    }),
      components: {
    Footer
  },
    computed: {
      hideBoxes() {
        if(this.errors.message || this.messages.message)
          return false;
        else return true;
      },
        ...mapState({
            messages: state => state.authsys.message,
            errors: state => state.authsys.errors,
            loading: state=> state.authsys.loading
        })
    },
    methods: {
      validPassword(password, current) {
        if(password === current && password && current)
          return true
      },
        ...mapActions({
            resetAction: 'authsys/checkTokenReset',
            setPassword: 'authsys/resetPassword',
            clear: 'authsys/clear'
        }),

        resetPassword() {
            this.setPassword({
                token: this.$route.params.token,
                new_password: this.password,
                router: this.$router
            })
        }
    },  
    beforeMount() {
      console.log(this.$route.params.token),
      this.resetAction({
        token: this.$route.params.token,
      })
    },
    beforeRouteLeave(to, from, next) {
       this.clear()
       next()
    }
}
</script>