<template>
  <v-container>
    <v-alert class="mx-auto" prominent outlined type="error" v-if="!user.isProfileComplete" max-width="600px">
      <p class="font-weight-bold mb-0">Profil akun kamu belum lengkap</p>
      <p
        class="black--text text--darken-2 mb-1"
      >Saat ini kamu belum bisa mendaftar kompetisi atau seminar karena data profil akun kamu belum terisi lengkap.</p>
      <v-btn outlined color="red" class="mt-2" min-width="130px">Edit Profil</v-btn>
    </v-alert>
    <transition name="fade">
      <v-alert class="mx-auto" prominent outlined type="success" v-if="messages.message && alertShow" max-width="600px">
        <p class="font-weight-bold mb-0">Profil berhasil diedit</p>
        <p
          class="black--text text--darken-2 mb-1"
        >{{messages.message}} Cheers...</p>
      </v-alert>
    </transition>
      <v-card outlined max-width="600" width="600" class="card_cloverleaf mb-5 mt-10 px-5">
      <v-card-text class="text-center">
        <vue-letter-avatar class="mb-5 mt-5" :name="user.full_name" size="90" :rounded="true" />
        <p class="display-1 text--primary mb-0">{{user.full_name}}</p>
        <p class="subtitle-2 text--primary mb-0">{{user.email}}</p>
        <p>
          Nama : {{user.full_name}} <br />
          Email : {{user.email}} <br />
          Nomor telepon : {{user.nomor_telepon}} <br />
          Is vege : {{user.is_vege}} <br />
          Alergi : {{user.alergic}} <br />
          No ID : {{user.nomor_id}} <br />
          Tanggal Lahir : {{user.tanggal_lahir}} <br />
        </p>
      </v-card-text>
      <v-card-text v-if="editing">
        <v-form @submit.prevent="update">
          <v-container>
            <v-container class="px-0 grey--text text--darken-4 title">Informasi Peserta</v-container>
            <v-text-field v-model="full_name" required :counter="50" outlined label="Nama Lengkap"></v-text-field>
            <v-text-field
              disabled
              :value="user.email"
              outlined
              required
              label="Email"
              :persistent-hint="true"
              hint="Alamat email yang didaftarkan tidak bisa diubah."
            ></v-text-field>
            <!-- <v-menu v-model="datemenu">
              <template v-slot:activator="{on}">
                <v-text-field
                  :value="date"
                  v-on="on"
                  label="Tanggal Lahir"
                  outlined
                  readonly
                  :rules="[v => !!v || 'Required']"
                ></v-text-field>
              </template>
              <v-date-picker v-model="date"></v-date-picker>
            </v-menu> -->
            <v-container class="px-0 grey--text text--darken-4 title">Kontak Peserta</v-container>
            <v-text-field v-model="id_line" :counter="50" outlined label="ID Line" required></v-text-field>
            <v-text-field
              v-model="nomor_telepon"
              outlined
              required
              :error="errors.nomor_telepon"
              :error-messages="errors.nomor_telepon"
              prefix="+62"
              label="Nomor Telepon"
              :persistent-hint="true"
              hint="Diutamakan untuk mengisi nomor telepon yang terhubung dengan WhatsApp."
            ></v-text-field>

            <v-container class="px-0 grey--text text--darken-4 title">Preferensi Konsumsi</v-container>
            <v-text-field
              v-model="alergic"
              outlined
              required
              label="Alergi"
              :persistent-hint="true"
              hint="Isikan alergi anda terutama terhadap alergi makanan."
            ></v-text-field>
            <v-switch
              color="blue"
              v-model="is_vege"
              :true-value="true"
              :false-value="false"
              required
              label="Apakah anda seorang vege?"
            ></v-switch>
          </v-container>
          
        </v-form>
      </v-card-text>
      <v-card-actions v-if="!editing" class="justify-center">
        <v-btn outlined class="mb-5" @click="editing = !editing">Edit Profile</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  data: () => ({
    editing: false,
    full_name: "",
    id_line: "",
    nomor_telepon: "",
    alergic: "",
    is_vege: false,
    alertShow: false,
    date: ""
  }),
  computed: mapState({
    user: state => state.authsys.user,
    loading: state => state.authsys.loading,
    errors: state => state.authsys.errors,
    messages: state => state.authsys.message
  }),
  beforeMount() {
    this.passStateToProps();
  },
  methods: {
    ...mapActions({
      updateProfile: "authsys/updateProfile",
      getCurrentSession: "authsys/getCurrentSession"
    }),

    passStateToProps() {
      (this.full_name = this.user.full_name),
        (this.id_line = this.user.id_line),
        (this.nomor_telepon = this.user.nomor_telepon),
        (this.alergic = this.user.alergic),
        (this.is_vege = this.user.is_vege);
    },

    update() {
      this.updateProfile({
        full_name: this.full_name,
        id_line: this.id_line,
        nomor_telepon: this.nomor_telepon,
        alergic: this.alergic,
        is_vege: this.is_vege,
        nomor_id: 0,
        tanggal_lahir: this.date
      })//,
      //this.scrollToTop(),
      //this.alertShow = true;
      //this.editing = false;
      //this.getCurrentSession();
      //setTimeout(() => (this.alertShow = false), 2000);
    },

    scrollToTop() {
      window.scrollTo(0, 0);
    }
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
</style>