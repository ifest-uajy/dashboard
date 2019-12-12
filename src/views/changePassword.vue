<template>
  <v-container>
    <v-layout justify-center>
      <v-card outlined max-width="500" width="500" class="card_cloverleaf mb-5 mt-10 px-5">
        <v-card-subtitle class="mt-5 pb-0 mb-0"><router-link to="/dashboard/profile" class="link_clover">Kembali</router-link></v-card-subtitle>
        <v-card-title class="title_card_cloverleaf">Ganti Password</v-card-title>
        <v-card-subtitle class="subtitle_card_cloverleaf">Informatics Festival (IFest) #8</v-card-subtitle>

        <v-card-text v-if="!messages.message" class="mb-7">
          <v-form ref="form" @submit.prevent="changePasswordAction">
            <v-text-field
              v-model="oldPassword"
              label="Old Password"
              type="password"
              required
              autocomplete="username"
              :rules="passwordRules"
            ></v-text-field>
            <v-text-field
              v-model="newPassword"
              label="New Password"
              type="password"
              autocomplete="current-password"
              required
              :rules="passwordRules"
            ></v-text-field>
            <v-text-field
              v-model="confirmnNewPassword"
              label="Confirm New Password"
              type="password"
              required
              :rules="[(v) => !!v || 'Confirm New Password cannot be empty', (v) => v === newPassword || 'Password does not match']"
            ></v-text-field>
            <v-btn
              large
              block
              color="primary"
              type="submit"
              :loading="loading"
              :disabled="!isComplete"
            >Ganti Password</v-btn>
          </v-form>
        </v-card-text>
        <v-card-text class="mt-5" v-if="messages.message">
          <v-alert type="success" class="mb-8" outlined prominent>{{ messages.message }}</v-alert>
          <v-layout justify-center class="mb-5">
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
    oldPassword: "",
    newPassword: "",
    confirmnNewPassword: "",
    passwordRules: [v => !!v || "Password is required"],
  }),
  computed: {
    isComplete() {
      return this.oldPassword && this.newPassword && this.confirmnNewPassword && (this.newPassword === this.confirmnNewPassword);
    },
    ...mapState({
      errors: state => state.authsys.errors,
      messages: state => state.authsys.message,
      loading: state => state.authsys.loading
    })
  },
  methods: {
    ...mapActions({
      changePassword: "authsys/changePassword",
      clear: "authsys/clear"
    }),
    sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    },
    async changePasswordAction() {
      await this.changePassword({
        password: this.oldPassword,
        new_password: this.newPassword
      });
      setTimeout(() => (location.reload(true)), 2000);
      
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