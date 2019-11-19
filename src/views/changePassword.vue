<template>
  <v-container>
    <v-layout justify-center>
      <v-card outlined max-width="500" width="500">
        <v-card-title>Ganti Password</v-card-title>

        <v-card-text>
          <v-form ref="form" @submit.prevent="changePasswordAction">
            <v-text-field
              v-model="oldPassword"
              label="Old Password"
              type="password"
              required
              autocomplete="username"
              :rules="passwordRules"
              outlined
            ></v-text-field>
            <v-text-field
              v-model="newPassword"
              label="New Password"
              type="password"
              autocomplete="current-password"
              required
              outlined
              :rules="passwordRules"
            ></v-text-field>
            <v-text-field
              v-model="confirmnNewPassword"
              label="Confirm New Password"
              type="password"
              required
              :rules="[(v) => !!v || 'Confirm New Password cannot be empty', (v) => v === newPassword || 'Password does not match']"
              outlined
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
        <v-card-text>
          <v-alert v-if="messages.message" type="success" outlined>{{ messages.message }}</v-alert>
          <v-alert v-if="errors.message" type="error" outlined>{{ errors.message }}</v-alert>
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
      this.changePassword({
        password: this.oldPassword,
        new_password: this.newPassword
      });

      await sleep(5000);

      location.reload(true);

    }
  },
  beforeRouteLeave(to, from, next) {
    this.clear();
    next();
  }
};
</script>