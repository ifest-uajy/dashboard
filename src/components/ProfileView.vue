<template>
  <v-container>
    <v-alert
        v-if="!user.isProfileComplete"
        class="mx-auto"
        max-width="600px"
        outlined
        prominent
        type="error"
    >
      <p class="font-weight-bold mb-0">Profil akun kamu belum lengkap</p>
      <p class="black--text text--darken-2 mb-1">
        Saat ini kamu belum bisa mendaftar kompetisi atau seminar karena data
        profil akun kamu belum terisi lengkap.
      </p>
    </v-alert>

    <v-alert
        v-if="alertShow"
        class="mx-auto"
        max-width="600px"
        outlined
        prominent
        type="success"
    >
      <p class="font-weight-bold mb-0">Profil kamu berhasil di perbaharui</p>
      <p class="black--text text--darken-2 mb-1">
        {{ messages.message }} Cheers...
      </p>
    </v-alert>

    <v-card
        class="card_cloverleaf mb-5 mt-10 px-5 mr-auto ml-auto"
        max-width="600"
        outlined
    >
      <v-card-text class="text-center">
        <vue-letter-avatar
            :name="user.full_name"
            :rounded="true"
            class="mb-5 mt-5"
            size="90"
        />
        <p class="display-1 text--primary mb-0">{{ user.full_name }}</p>
        <p class="subtitle-2 text--primary mb-0">{{ user.email }}</p>
        <p class="font-weight-medium mt-2 mb-0">
          <router-link class="link_clover" to="profile/changepassword"
          >Ganti Password?
          </router-link
          >
        </p>
      </v-card-text>
      <v-card-text class="pb-10">
        <v-form ref="form" @submit.prevent="update">
          <v-container class="px-0 grey--text text--darken-4 title"
          >Informasi Peserta
          </v-container
          >
          <div class="form-group">
            <label>Nama Lengkap</label>
            <d-input
                v-model="profilUser.full_name"
                :state="errors.full_name ? 'invalid' : 'null'"
                class=""
                :disabled="isEditing"
                type="text"
            />
            <d-form-invalid-feedback>Isian ini tidak boleh kosong.</d-form-invalid-feedback>
          </div>
          <div class="form-group">
            <label>Tanggal Lahir</label>
            <d-input
                v-model="profilUser.tanggal_lahir"
                :state="errors.tanggal_lahir ? 'invalid' : 'null'"
                class=""
                :disabled="isEditing"
                type="date"
            />
            <d-form-invalid-feedback>Isian ini tidak boleh kosong.</d-form-invalid-feedback>
          </div>
          <div class="form-group">
            <label>Nomor Identitas</label>
            <d-input
                v-model="profilUser.nomor_id"
                :state="errors.nomor_id ? 'invalid' : 'null'"
                :disabled="isEditing"
                class=""
            />
            <d-form-invalid-feedback>Isian ini tidak boleh kosong.</d-form-invalid-feedback>
            <small class="form-text text-muted mb-2 mt-0 pt-0">Kamu bisa mengisi dengan nomor kartu pelajar atau kartu
              mahasiswa.</small>
          </div>
          <label>Alamat Rumah</label>
          <d-form-textarea
              v-model="profilUser.alamat"
              :value.prop="profilUser.alamat"
              :disabled="isEditing"
              :max-rows="3"
              :rows="2">
          </d-form-textarea>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label>LINE ID</label>
                <d-input
                    v-model="profilUser.id_line"
                    :disabled="isEditing"
                    class=""
                />
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label>Nomor Telepon</label>
                <d-input
                    v-model="profilUser.nomor_telepon"
                    :disabled="isEditing"
                    :state="errors.nomor_telepon ? 'invalid' : 'null'"
                    class=""
                />
                <d-form-invalid-feedback>Isian ini tidak boleh kosong.</d-form-invalid-feedback>
              </div>
            </div>
          </div>
        </v-form>
        <div v-if="!isEditing">
          <div class="row">
          <div class="col-md-6 py-0">
            <d-btn block-level theme="secondary" @click="batalUbahProfil">Batal</d-btn>
          </div>
          <div class="col-md-6 py-0">
            <d-btn block-level @click="update">Simpan</d-btn>
          </div>
        </div>
        </div>
        <div v-else>
          <d-btn block-level @click="isEditing = false">Perbaharui Profil</d-btn>
        </div>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import {mapActions, mapState} from "vuex";
import moment from "moment";

moment.locale("id");

export default {
  data: () => ({
    moment: moment,
    editing: false,
    isEditing: true,
    nama_lengkap: "",
    vege: false,
    alergi: "",
    id_line: "",
    nomor_telepon: "",
    nomor_id: "",
    fromDateMenu: false,
    fromDateVal: null,
    alertShow: false,
    profilUser: {
      full_name: "",
      tanggal_lahir: "",
      nomor_id: "",
      alamat: "",
      nomor_telepon: "",
      id_line: ""
    }
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

    editProfilUser() {
      this.isEditing = true
    },

    passStateToProps() {
      this.profilUser.full_name = this.user.full_name
      this.profilUser.tanggal_lahir = this.user.tanggal_lahir
      this.profilUser.nomor_id = this.user.nomor_id
      this.profilUser.alamat = this.user.alamat
      this.profilUser.nomor_telepon = this.user.nomor_telepon
      this.profilUser.id_line = this.user.id_line
    },

    batalUbahProfil() {
      this.passStateToProps()
      this.isEditing = true
    },

    async update() {
      this.clear();
      await this.updateProfile(this.profilUser);
      this.scrollToTop();
      if (!this.success) {
        //console.log("A");
        this.isEditing = false;
      } else {
        //console.log("B");
        this.alertShow = true;
        this.isEditing = true;
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

.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
{
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
