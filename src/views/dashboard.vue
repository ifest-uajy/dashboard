<template>
  <section class="section">
    <div class="container">
      <h2 class="subtitle">Informatics Festival #8</h2>
      <h1 class="title">Selamat datang, {{user.full_name}}!</h1>
    </div>
    <div @click="logoutActions" class="logout-btn">
      <a>Logout</a>
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

<style scoped>
.logout-btn {
  position: fixed;
  top: 50px;
  right: 0px;
  padding: 0px;
  margin: 0px;
  cursor: pointer;
  width: 40px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  height: 100px;
  background: #13355B;
  color: #adadad;
  z-index: 15;
  border-radius: 8px 0px 0px 8px; }
  .logout-btn a {
    margin: auto 10px;
    margin-top: 25px;
    writing-mode: tb-rl;
    color: rgb(119, 170, 241);
    text-decoration: none; }
  .logout-btn a:visited {
    text-decoration: none; }
  .logout-btn:hover {
    background: rgb(13, 34, 65);
  }

</style>