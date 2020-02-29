<template>
  <v-container>
    <v-alert
      class="mx-auto"
      prominent
      outlined
      type="error"
      v-if="!user.isProfileComplete"
      max-width="600px"
    >
      <p class="font-weight-bold mb-0">Profil akun kamu belum lengkap</p>
      <p class="black--text text--darken-2 mb-1">
        Saat ini kamu belum bisa mendaftar kompetisi atau seminar karena data
        profil akun kamu belum terisi lengkap.
      </p>
    </v-alert>

    <v-alert
      class="mx-auto"
      prominent
      outlined
      type="success"
      v-if="alertShow"
      max-width="600px"
    >
      <p class="font-weight-bold mb-0">Profil kamu berhasil di perbaharui</p>
      <p class="black--text text--darken-2 mb-1">
        {{ messages.message }} Cheers...
      </p>
    </v-alert>

    <v-card
      outlined
      max-width="600"
      class="card_cloverleaf mb-5 mt-10 px-5 mr-auto ml-auto"
    >
      <v-card-text class="text-center">
        <vue-letter-avatar
          class="mb-5 mt-5"
          :name="user.full_name"
          size="90"
          :rounded="true"
        />
        <p class="display-1 text--primary mb-0">{{ user.full_name }}</p>
        <p class="subtitle-2 text--primary mb-0">{{ user.email }}</p>
        <p class="font-weight-medium mt-2 mb-0">
          <router-link to="profile/changepassword" class="link_clover"
            >Ganti Password?</router-link
          >
        </p>
      </v-card-text>
      <v-card-text>
        <div class="columns-e">
          <div class="column-e">
            <p class="span-info">Informasi Umum</p>
            <span class="entity-name">Nama Lengkap</span>
            <br />
            {{ user.full_name }}
            <br />
            <span class="entity-name">Email</span>
            <br />
            {{ user.email }}
            <br />
            <span class="entity-name">Tanggal Lahir</span>
            <br />
            {{ moment(String(user.tanggal_lahir)).format("DD MMMM YYYY") }}
            <br />
            <span class="entity-name">Nomor Kartu Pelajar/KTM</span>
            <br />
            {{ user.nomor_id }}
            <br />
            <br />
          </div>
          <div class="column-e">
            <p class="span-info">Kontak</p>
            <span class="entity-name">Nomor Telepon</span>
            <br />
            +62 {{ user.nomor_telepon }}
            <br />
            <span class="entity-name">ID Line</span>
            <br />
            {{ user.id_line }}
            <br />
            <br />
            <p class="span-info">Preferensi Konsumsi</p>
            <span class="entity-name">Vege</span>
            <br />
            <span v-if="user.is_vege === true">Iya</span>
            <span v-else>Tidak</span>
            <br />
            <span class="entity-name">Alergi</span>
            <br />
            {{ user.alergic }}
            <br />
          </div>
        </div>
      </v-card-text>
      <v-card-text v-if="editing" class="pb-10">
        <v-form ref="form" @submit.prevent="update">
          <v-container class="px-0 grey--text text--darken-4 title"
            >Informasi Peserta</v-container
          >

          <v-text-field
            v-model="nama_lengkap"
            label="Nama Lengkap"
            :error="errors.full_name"
            :error-messages="errors.full_name"
            hint="Gunakan nama dengan singkatan seminimal mungkin."
            required
          ></v-text-field>
          <v-menu
            v-model="fromDateMenu"
            :close-on-content-click="false"
            :nudge-right="40"
            transition="scale-transition"
            max-width="290px"
            min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field
                :error="errors.tanggal_lahir"
                :error-messages="errors.tanggal_lahir"
                label="Tanggal Lahir"
                readonly
                :value="fromDateDisp"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="fromDateVal"
              no-title
              @input="fromDateMenu = false"
            ></v-date-picker>
          </v-menu>
          <v-text-field
            :error="errors.nomor_id"
            v-model="nomor_id"
            :error-messages="errors.nomor_id"
            :counter="50"
            label="Nomor Kartu Pelajar/KTM"
          ></v-text-field>
          <v-container class="px-0 grey--text text--darken-4 title"
            >Kontak Peserta</v-container
          >
          <v-text-field
            v-model="user.email"
            label="Email"
            type="email"
            disabled
            :persistent-hint="true"
            hint="Email yang sudah didaftarkan tidak dapat diganti."
          ></v-text-field>
          <v-text-field
            v-model="id_line"
            :counter="50"
            label="ID Line"
          ></v-text-field>
          <v-text-field
            v-model="nomor_telepon"
            :error="errors.nomor_telepon"
            :error-messages="errors.nomor_telepon"
            prefix="+62"
            label="Nomor Telepon"
            :persistent-hint="true"
            hint="Diutamakan untuk mengisi nomor telepon yang terhubung dengan WhatsApp."
          ></v-text-field>
          <v-container class="px-0 grey--text text--darken-4 title"
            >Preferensi Konsumsi Peserta</v-container
          >
          <v-text-field
            v-model="alergi"
            label="Alergi terhadap makanan"
            hint="Isilah field ini dengan informasi alergi anda terhadap makanan."
          ></v-text-field>
          <v-switch
            color="blue"
            v-model="is_vege"
            :true-value="true"
            :false-value="false"
            required
            label="Apakah anda seorang vege?"
          ></v-switch>
          <center>
            <v-btn
              large
              color="primary"
              type="submit"
              outlined
              class="mt-5 mr-5"
              :loading="loading"
              :disabled="loading"
              >Perbaharui Profil</v-btn
            >
            <v-btn
              large
              @click="editing = !editing"
              outlined
              v-if="!loading"
              class="mt-5"
              >Batal</v-btn
            >
          </center>
        </v-form>
      </v-card-text>
      <v-card-actions v-if="!editing" class="justify-center">
        <v-btn outlined class="mb-5" @click="editing = !editing"
          >Ubah Profil</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import moment from "moment";

moment.locale("id");

export default {
  data: () => ({
    moment: moment,
    editing: false,
    nama_lengkap: "",
    vege: false,
    alergi: "",
    id_line: "",
    nomor_telepon: "",
    nomor_id: "",
    fromDateMenu: false,
    fromDateVal: null,
    alertShow: false
  }),
  computed: {
    ...mapState({
      user: state => state.authsys.user,
      errors: state => state.authsys.errors,
      messages: state => state.authsys.message,
      loading: state => state.authsys.loading,
      success: state => state.authsys.success
    }),
    fromDateDisp() {
      let a = "";
      if (this.fromDateVal) {
        a = moment(this.fromDateVal, "YYYY-MM-DD");
        return moment(a).format("D MMMM YYYY");
      } else {
        return "Silahkan pilih tanggal.";
      }
    }
  },
  beforeMount() {
    this.clear();
    this.passStateToProps();
  },
  methods: {
    ...mapActions({
      updateProfile: "authsys/updateProfile",
      getCurrentSession: "authsys/getCurrentSession",
      clear: "authsys/clear"
    }),

    passStateToProps() {
      (this.nama_lengkap = this.user.full_name),
        (this.id_line = this.user.id_line),
        (this.nomor_telepon = this.user.nomor_telepon),
        (this.alergi = this.user.alergic),
        (this.nomor_id = this.user.nomor_id),
        (this.fromDateVal = this.user.tanggal_lahir),
        (this.is_vege = this.user.is_vege);
    },

    async update() {
      this.clear();
      await this.updateProfile({
        full_name: this.nama_lengkap,
        id_line: this.id_line,
        nomor_telepon: this.nomor_telepon,
        alergic: this.alergi,
        is_vege: this.is_vege,
        nomor_id: this.nomor_id,
        tanggal_lahir: this.fromDateVal
      }); //,
      //
      this.scrollToTop();
      if (!this.success) {
        //console.log("A");
        this.editing = true;
      } else {
        //console.log("B");
        this.alertShow = true;
        this.editing = false;
        await setTimeout(() => (this.alertShow = false), 2000);
        this.clear();
      }
    },

    scrollToTop() {
      window.scrollTo(0, 0);
    }
  },
  beforeRouteLeave(to, from, next) {
    this.clear();
    next();
  }
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}

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

.span-info {
  font-weight: bold;
  font-size: 1.2em;
  color: #0f4c75;
}

.link_clover:hover {
  color: cornflowerblue;
}

.entity-name {
  font-size: 0.8em;
  color: black;
}

.columns-e {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.column-e {
  min-width: 250px;
}
</style>
