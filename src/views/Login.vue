<template>
  <v-container>
    <v-layout justify-center>
      <v-card
        outlined
        max-width="500"
        width="500"
        class="card_cloverleaf mb-5 mt-10 px-5"
      >
        <v-card-title class="title_card_cloverleaf mt-7">Masuk</v-card-title>
        <v-card-subtitle class="subtitle_card_cloverleaf"
          >Informatics Festival (IFest) #8</v-card-subtitle
        >

        <v-card-text>
          <v-form ref="form" @submit.prevent="login">
            <v-text-field
              v-model="email"
              label="Email"
              type="email"
              required
              autocomplete="username"
              :rules="emailRules"
            ></v-text-field>
            <v-text-field
              v-model="password"
              label="Password"
              class="mb-3"
              type="password"
              autocomplete="current-password"
              required
              :rules="passwordRules"
            ></v-text-field>

            <p class="font-weight-medium">
              <router-link to="/reset-password" class="link_clover"
                >Lupa password?</router-link
              >
            </p>
            <p class="font-weight-medium">
              <router-link to="/register" class="link_clover"
                >Belum punya akun?</router-link
              >
            </p>
            <p class="font-weight-medium">
              <router-link to="/resend" class="link_clover"
                >Kirim ulang email aktivasi?</router-link
              >
            </p>

            <v-btn
              large
              block
              color="primary"
              type="submit"
              :loading="loading"
              :disabled="!isComplete"
              >Masuk</v-btn
            >
          </v-form>
        </v-card-text>
        <v-card-text>
          <v-alert v-if="errors.message" prominent type="error" outlined>{{
            errors.message
          }}</v-alert>
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
    password: "",
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+\..+/.test(v) || "Email harus valid"
    ],
    passwordRules: [v => !!v || "Password is required"]
  }),
  computed: {
    isComplete() {
      return this.email && this.password;
    },
    ...mapState({
      errors: state => state.authsys.errors,
      loading: state => state.authsys.loading
    })
  },
  methods: {
    ...mapActions({
      loginAction: "authsys/login",
      clear: "authsys/clear"
    }),

    login() {
      this.loginAction({
        email: this.email,
        password: this.password,
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
