<template>
  <v-app id="main" style="background: #fff">
    <v-main class="content">
      <router-view />
    </v-main>
    <Footer />
  </v-app>
</template>

<script>
import Footer from "./components/Footer";

export default {
  name: "App",
  data() {
    return {
      title: "Informatics Festival (IFest) #9"
    };
  },
  components: {
    Footer
  }
};
</script>

<style scoped>

</style>
