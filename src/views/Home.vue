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
          src="https://ifest-uajy.com/assets/undraw_navigator_a479.svg"
        />
      </div>
      <div class="column-a kanan">
        <h1 class="judul">
          Dashboard
          <br />
          <span class="judul-span">Informatics Festival #8</span>
        </h1>
        <p class="mb-3">
          Selamat datang di Sistem Registrasi Kompetisi Informatics Festival #8.
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
        <p class="link-hubungi">
          <router-link to="/reset-password">
            <span class="lupa-password">Lupa Password?</span>
          </router-link>
          <br />
          <router-link to="/contact">
            <span class="hubungi-kami">Punya pertanyaan?</span>
          </router-link>
        </p>
      </div>
    </div>
<!-- 
    <v-container class="container-dash mt-12">
      <v-row align="center">
        <v-col cols="12" sm="6">
          <h1>Apa itu Informatics Festival?</h1>
          <p>
            IFest adalah Informatics Festival. Merupakan festival tahunan yang
            diselenggarakan oleh Himpunan Mahasiswa Informatika (HIMAFORKA)
            Universitas Atma Jaya Yogyakarta.
          </p>
        </v-col>
        <v-col cols="12" sm="6">
          <v-carousel
            cycle
            height="250"
            hide-delimiter-background
            show-arrows-on-hover
          >
            <v-carousel-item v-for="(slide, i) in slides" :key="i">
              <v-sheet :color="colors[i]" height="100%">
                <v-row class="fill-height" align="center" justify="center">
                  <div class="display-3">{{ slide }} Slide</div>
                </v-row>
              </v-sheet>
            </v-carousel-item>
          </v-carousel>
        </v-col>
      </v-row>
    </v-container>

    <v-container class="competition-box mt-12 px-10 pb-10 mb-10">
      <h2 class="pt-5 pb-5 grey--text text--darken-4">Kompetisi tahun ini</h2>
      <v-card class="" max-width="344">
        <v-card-text>

          <p class="display-1 text--primary">
            Competition Name
          </p>
          <p>Pendaftaran: </p>
          <div class="text--primary">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          </div>
        </v-card-text>
        <v-card-actions>
          <v-btn text color="deep-purple accent-4">
            Learn More
          </v-btn>
        </v-card-actions>
      </v-card>p
    </v-container>

    <v-container class="container-dash mt-12">
      <v-row align="center">
        <v-col cols="12" sm="6">
             <v-carousel
            cycle
            height="250"
            hide-delimiter-background
            show-arrows-on-hover
          >
            <v-carousel-item v-for="(slide, i) in slides" :key="i">
              <v-sheet :color="colors[i]" height="100%">
                <v-row class="fill-height" align="center" justify="center">
                  <div class="display-3">{{ slide }} Slide</div>
                </v-row>
              </v-sheet>
            </v-carousel-item>
          </v-carousel>
        </v-col>
        <v-col cols="12" sm="6">
       <h1>Gimana cara mendaftar kompetisi IFest?</h1>
          <p>
            IFest adalah Informatics Festival. Merupakan festival tahunan yang
            diselenggarakan oleh Himpunan Mahasiswa Informatika (HIMAFORKA)
            Universitas Atma Jaya Yogyakarta.
          </p>
        </v-col>
      </v-row>
    </v-container>

    <v-container class="container-dash mt-12">
      <h2>Tertarik dengan Informatics Festival (IFest)? </h2>
      <p>Masukkan alamat email kamu melalui form dibawah ini untuk menerima informasi lomba berikutnya.</p>
      <p>Kami hanya akan menghubungi anda jika ada kompetisi baru.</p>
    </v-container> -->

    <!-- <div class="cara-pendaftaran">
      <p class="sub-judul">Gimana sih cara daftar kompetisi <b>Informatics Festival #8</b>?</p>
    </div>
    <div class="alur-pendaftaran">
      <div class="sub sub-1"><span class="number-sub">1.<br /></span> Buat akun kamu di dashboard <b>Informatics Festival #8</b></div>
      <div class="sub sub-2"><span class="number-sub">2.<br /></span> Lengkapi profil akun dalam tab profil</div>
      <div
        class="sub sub-3"
      ><span class="number-sub">3.<br /></span> Buat atau join tim dengan token di tab kompetisi</div>
      <div class="sub sub-4"><span class="number-sub">4.<br /></span> Selesaikan task dalam setiap kompetisi yang didaftarkan</div>
    </div> -->
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
      slides: ["First", "Second", "Third", "Fourth", "Fifth"]
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
