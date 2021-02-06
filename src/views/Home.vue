<template>
  <div class="body2">
    <div class="header-box">
      <img
          class="circle-top"
          src="https://dashboard.ifest-uajy.com/assets/atma_jaya5050.png"
      />
      <img
          class="circle-top"
          src="https://dashboard.ifest-uajy.com/assets/himaforka5050.png"
      />
      <img
          class="circle-top"
          src="https://dashboard.ifest-uajy.com/assets/ifest5050.png"
      />
    </div>

    <div class="columns-a">
      <div class="column-a kiri">
        <img
            class="navigator-svg"
            :src="images.welcome"
        />
      </div>
      <div class="column-a kanan">
        <h1 class="judul">
          Dashboard
          <br/>
          <span class="judul-span">Informatics Festival</span>
        </h1>
        <p class="mb-3">
          Selamat datang di Sistem Registrasi Kompetisi Informatics Festival (IFest) #9.
        </p>
        <router-link to="/register">
          <v-btn class="btn daftar">
            <span>Daftar Sekarang!</span>
          </v-btn>
        </router-link>
        <router-link to="/login">
          <v-btn class="btn login">
            <span>Masuk</span>
          </v-btn>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    this.$ga.page("/");
  },
  data() {
    return {
      colors: [
        "indigo",
        "warning",
        "pink darken-2",
        "red lighten-1",
        "deep-purple accent-4"
      ],
      slides: ["First", "Second", "Third", "Fourth", "Fifth"],
      images: {
        welcome: require('@/assets/Innovation _Monochromatic.svg')
      }
    };
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Amiri&display=swap");
@import url("https://fonts.googleapis.com/css?family=Roboto&display=swap");

.header_big {
  margin-top: 40px;
  font-size: 80pt;
}

.subheader_big {
  font-size: 60pt;
  margin-bottom: 40px;
}

.link_clover {
  font-size: 25pt;
  text-decoration: unset !important;
}

.link_clover:hover {
  color: cornflowerblue;
}

.boxed-center {
  margin: auto;
  margin-top: 80px;
  width: 700px;
}

.image-center {
  max-height: 200px;
}

.circle-top {
  margin: auto 10px;
  padding: 10px;
  height: 50px;
  width: 50px;
  background: white;
  border-radius: 100%;
}

.header-box {
  display: flex;
  background: #1b262c;
  justify-content: center;
  height: 100px;
}

.body2 {
  background-color: #0f4c75;
  min-height: 100%;
  color: #dfdbdb;
  font-family: "Roboto", sans-serif;
  clear: both;
}

.alur-pendaftaran {
  min-height: 200px;
  margin: auto;
  margin-top: 50px;
  margin-bottom: 50px;
  display: flex;
  justify-content: space-around;
  align-content: center;
  align-items: center;
  flex-wrap: wrap;
  max-width: 1000px;
}

.cara-pendaftaran {
  background-color: #263b68;
  font-family: "Amiri", serif;
  display: flex;
  padding-top: 20px;
  margin-top: 50px;
  justify-content: center;
}

.sub {
  padding: 20px;
  padding-left: 25px;
  padding-right: 25px;
  background: #fff;
  border-radius: 2px;
  display: inline-block;
  border-radius: 8px;
  margin: 1rem;
  position: relative;
  width: 300px;
  color: #1b262c;
}

.columns-a {
  margin: auto;
  height: 70vh;
  max-width: 1000px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  align-content: center;
  flex-wrap: wrap;
}

.column-a {
  padding: 10px;
}

.navigator-svg {
  margin: auto;
  max-width: 350px;
}

.kanan {
  max-width: 410px;
}

.judul {
  color: #ffffff;
  font-family: "Amiri", serif;
  line-height: 1.1em;
  font-size: 30pt;
  font-weight: 500;
}

.sub-judul {
  color: #ffffff;
  font-family: "Amiri", serif;
  line-height: 1.1em;
  font-size: 24pt;
  font-weight: 500;
  padding: 20px;
}

.judul-span {
  font-weight: 700;
}

.btn {
  margin-top: 5px;
}

.daftar {
  margin-right: 20px;
}

.link-hubungi {
  margin-top: 15px;
  font-size: 10pt;
  color: #fff !important;
}

a {
  text-decoration: none;
  color: #fff !important;
}

a:visited {
  color: #dfdfdf;
}

/* mouse over link */
a:hover {
  color: #4b83c4 !important;
}

/* selected link */
a:active {
  color: #dfdbdb;
}

@media only screen and (max-width: 600px) {
  .columns-a {
    margin: auto;
    max-width: 80vw;
    display: flex;
    justify-content: space-around;
    align-items: center;
    align-content: center;
    flex-wrap: wrap;
  }

  .kiri {
    margin-top: 120px;
  }

  .kanan {
    margin-top: 50px;
    margin-bottom: 50px;
  }

  .column-a {
    padding: 10px;
  }

  .navigator-svg {
    margin: auto;
    max-width: 350px;
  }
}

.number-sub {
  font-weight: 700;
  font-size: 20pt;
}

.container-dash {
  margin: auto;
  max-width: 900px;
}

.competition-box {
  min-height: 300px;
  background-color: white;
  box-shadow: 0 10px 20px 0 rgba(53, 64, 90, 0.2);
  outline: none;
  border: none !important;
  border-radius: 8px !important;
  max-width: 1000px;
}
</style>
