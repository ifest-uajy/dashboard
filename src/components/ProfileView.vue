<template>
  <v-container>
    <v-alert prominent outlined type="error" v-if="!user.isProfileComplete">
      <p class="font-weight-bold mb-0">Profil akun kamu belum lengkap</p>
      <p
        class="black--text text--darken-2 mb-1"
      >Saat ini kamu belum bisa mendaftar kompetisi atau seminar karena data profil akun kamu belum terisi lengkap.</p>
      <v-btn outlined color="red" class="mt-2" min-width="130px">Edit Profil</v-btn>
    </v-alert>
    <v-card class="mx-auto" outlined>
      <v-card-text class="text-center">
        <vue-letter-avatar class="mb-5 mt-5" :name="user.full_name" size="90" :rounded="true" />
        <p class="display-1 text--primary mb-0">{{user.full_name}}</p>
        <p class="subtitle-2 text--primary mb-0">{{user.email}}</p>
      </v-card-text>
      <v-card-text v-if="editing">
        <v-form v-model="valid">
          <v-container>
            <v-container class="px-0 grey--text text--darken-4 title">Informasi Peserta</v-container>
            <v-text-field
              :value="user.full_name"
              :counter="50"
              outlined
              label="Nama Lengkap"
              required
            ></v-text-field>
            <v-text-field
              disabled
              :value="user.email"
              outlined
              label="Email"
              persistent-hint="true"
              hint="Alamat email yang didaftarkan tidak bisa diubah."
            ></v-text-field>
            <v-container class="px-0 grey--text text--darken-4 title">Kontak Peserta</v-container>
            <v-text-field :value="user.id_line" :counter="50" outlined label="ID Line" required></v-text-field>
            <v-text-field
              :value="user.nomor_telepon"
              outlined
              prefix="+62"
              label="Nomor Telepon"
              persistent-hint="true"
              hint="Diutamakan untuk mengisi nomor telepon yang terhubung dengan WhatsApp."
            ></v-text-field>
            <v-container class="px-0 grey--text text--darken-4 title">Preferensi Konsumsi</v-container>
            <v-text-field
              :value="user.alergic"
              outlined
              label="Alergi"
              persistent-hint="true"
              hint="Isikan alergi anda terutama terhadap alergi makanan."
            ></v-text-field>
            <v-switch :value="user.is_vege" label="Apakah anda seorang vege?"></v-switch>
          </v-container>
        </v-form>
      </v-card-text>
      <v-card-actions v-if="!editing" class="justify-center">
        <v-btn outlined class="mb-5" @click="editing = !editing">Edit Profile</v-btn>
      </v-card-actions>
      <v-card-actions v-if="editing" class="justify-center">
        <v-btn outlined color="green" class="mb-5" @click="editing = !editing">Save</v-btn>
        <v-btn outlined color="red" class="mb-5" @click="editing = !editing">Cancel</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import { mapState } from "vuex";

export default {
  data: () => ({
    editing: false
  }),
  computed: mapState({
    user: state => state.authsys.user
  })
};
</script>