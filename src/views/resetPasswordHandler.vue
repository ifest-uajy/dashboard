<template>
  <v-container>
    <v-layout justify-center>
      <v-card outlined max-width="500" width="500" class="card_cloverleaf mb-5 mt-10 px-5">
        <v-card-title class="title_card_cloverleaf mt-7">Reset Password</v-card-title>
        <v-card-subtitle class="subtitle_card_cloverleaf">Informatics Festival (IFest) #8</v-card-subtitle>


        <v-card-text v-if="hideBoxes" class="mb-6">
          <v-form ref="form" @submit.prevent="resetPassword">
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
              required
              class="mb-5"
              :rules="[(v) => !!v || 'Confirm Password cannot be empty', (v) => v === password || 'Password does not match']"
              
            ></v-text-field>
            <p class="font-weight-medium" >
              <router-link to="/register" class="link_clover">Belum punya akun?</router-link>
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
        <v-card-text v-if="messages.message" class="mt-5">
          <v-alert  type="success"  class="mb-8" outlined>{{ messages.message }}</v-alert>
          <v-layout  justify-center>
            <router-link to="/login/">
              <v-btn color="success" class="mb-5" dark>Login ke dashboard</v-btn>
            </router-link>
          </v-layout>
        </v-card-text>
        <v-card-text v-if="errors.message" class="mt-5">
          <v-alert type="error"  class="mb-8" outlined>{{ errors.message }}</v-alert>
          <v-layout justify-center>
            <router-link to="/" >
              <v-btn color="error"  class="mb-5" dark>Kembali ke halaman utama</v-btn>
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
    password: "",
    confirmPassword: "",
    passwordRules: [v => !!v || "Password is required"]
  }),
  computed: {
    hideBoxes() {
      if (this.errors.message || this.messages.message) return false;
      else return true;
    },
    ...mapState({
      messages: state => state.authsys.message,
      errors: state => state.authsys.errors,
      loading: state => state.authsys.loading
    })
  },
  methods: {
    validPassword(password, current) {
      if (password === current && password && current) return true;
    },
    ...mapActions({
      resetAction: "authsys/checkTokenReset",
      setPassword: "authsys/resetPassword",
      clear: "authsys/clear"
    }),

    resetPassword() {
      this.setPassword({
        token: this.$route.params.token,
        new_password: this.password,
        router: this.$router
      });
    }
  },
  beforeMount() {
    console.log(this.$route.params.token),
      this.resetAction({
        token: this.$route.params.token
      });
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

.link_clover {
  text-decoration: unset !important;
}

.link_clover:hover {
  color: cornflowerblue;
}
</style>