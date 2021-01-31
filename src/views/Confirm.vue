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
          >Konfirmasi Email</v-card-title
        >
        <v-card-subtitle class="subtitle_card_cloverleaf"
          >Informatics Festival (IFest) #9</v-card-subtitle
        >
        <v-card-text class="mb-5">
          <v-alert v-if="messages.message" type="success" outlined>{{
            messages.message
          }}</v-alert>
          <v-alert v-if="errors.message" type="error" outlined>{{
            errors.message
          }}</v-alert>
          <v-layout v-if="messages.message" justify-center>
            <router-link to="/login">
              <v-btn color="success" dark>Login ke dashboard</v-btn>
            </router-link>
          </v-layout>
          <v-layout v-if="errors.message" justify-center>
            <router-link to="/">
              <v-btn color="error" dark>Kembali</v-btn>
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
  data: () => ({}),
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
    })
  },
  beforeMount() {
    //console.log(this.$route.params.token),
      this.confirmToken({
        token: this.$route.params.token
      });
  },
  beforeRouteLeave(to, from, next) {
    this.clear();
    next();
  }
};
</script>

<style>
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
