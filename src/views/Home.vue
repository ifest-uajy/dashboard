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
          <d-btn class="mr-3">
            Buat Akun
          </d-btn>
        </router-link>
        <router-link to="/login">
          <d-btn theme="secondary">
            Masuk
          </d-btn>
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

.circle-top {
  margin: auto 10px;
  padding: 10px;
  height: 50px;
  width: 50px;
  background: #ffffff;
  border-radius: 100%;
}

.header-box {
  display: flex;
  background: #01497c;
  justify-content: center;
  height: 100px;
}

.body2 {
  background-color: #f7f7ff;
  min-height: 100%;
  color: #323232;
  font-family: "Roboto", sans-serif;
  clear: both;
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
  color: #1d1d1d;
  font-family: "Amiri", serif;
  line-height: 1.1em;
  font-size: 30pt;
  font-weight: 500;
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
</style>
