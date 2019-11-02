<template>
  <v-container>
    <v-layout justify-center>
      <v-card outlined max-width="500" width="500">
        <v-card-title>Konfirmasi Email</v-card-title>
        <v-card-subtitle>Informatics Festival #8</v-card-subtitle>
        <v-card-text>
          <v-alert v-if="messages.message" type="success" outlined>{{ messages.message }}</v-alert>
          <v-alert v-if="errors.message" type="error" outlined>{{errors.message}}</v-alert>
          <v-layout v-if="messages.message" justify-center>
            <router-link to="/login"><v-btn color="success" dark>Login ke dashboard</v-btn></router-link>
          </v-layout>
          <v-layout v-if="errors.message" justify-center>
            <router-link to="/"><v-btn color="error" dark>Kembali</v-btn></router-link>
          </v-layout>
        </v-card-text>
      </v-card>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
    data: () => ({ }),
  computed: {
    ...mapState({
      errors: state => state.authsys.errors,
      messages: state => state.authsys.message,
      loading: state => state.authsys.loading
    })
  },
  methods: {
    ...mapActions({
      confirmToken: "authsys/confirm",
      clear: "authsys/clear"
    }),
  },
  beforeMount() {
      console.log(this.$route.params.token),
      this.confirmToken({
        token: this.$route.params.token,
      })
    },
    beforeRouteLeave(to, from, next) {
       this.clear()
       next()
    }
};
</script>