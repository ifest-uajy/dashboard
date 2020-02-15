<template>
  <div class="container">
    <div class="big-i">
      <div class="image-holder">
        <img class="navigator-svg" src="https://ifest-uajy.com/assets/undraw_Taken_if77.svg" />
      </div>
            <p class="text-center subtitle-1">Duh... Halaman yang kamu minta tidak ditemukan atau telah dipindahkan.</p>

      <center>
        <router-link to="/">
          <v-btn class="btn login" color="primary">
            <span>Kembali</span>
          </v-btn>
        </router-link>
      </center>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.container {
  margin-top: 100px;
  max-width: 100vw;
}
.big-i {
  margin: auto;
  width: 400px;
}
.navigator-svg {
  margin: auto;
  max-width: 200px; 
}
.image-holder {
  margin:auto;
  width: 200px;
  margin-top: 50px;
  margin-bottom: 35px;
}
</style>