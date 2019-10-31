<template>
  <div id="dashboard">
    <h1>Selamat Datang</h1>
    <p>Halaman dashboard {{user.full_name}}</p>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  data: () => ({
    name: "Dev"
  }),
  computed: mapState({
    user: state => state.authsys.user
  }),
};
</script>