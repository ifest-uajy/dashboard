<template>
  <section class="section">
    <div class="container">
      <h2 class="subtitle">Informatics Festival #8</h2>
      <h1 class="title">Selamat datang, {{user.full_name}}!</h1>
      <v-btn @click="logoutActions">Logout</v-btn>
    </div>
  </section>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  data: () => ({}),
  computed: mapState({
    user: state => state.authsys.user
  }),
  methods: {
    ...mapActions({
      logoutActions: "authsys/logout",
      clear: "authsys/clear"
    })
  }
};
</script>