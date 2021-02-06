<template>
  <div class="container pb-5 mb-5">
    <div class="row">
      <div class="col-lg-4">
        <div class="card_cloverleaf text-center px-5 py-5" style="background-color: #1d3557; color: white !important;">
          <vue-letter-avatar
              :name="user.full_name"
              :rounded="true"
              class="mb-5 mt-2"
              size="90"
          />
          <p class="font-weight-bold mb-0" style="font-size: 16pt">{{ user.full_name }}</p>
          <p class="subtitle-2 mb-0" style="opacity: 0.8;">{{ user.email }}</p>
          <p class="font-weight-medium mt-5 mb-0">
            <router-link class="link_clover" to="profile/changepassword"
            >
              <d-btn block-level theme="light">
                Ganti Password?
              </d-btn>
            </router-link
            >
          </p>
        </div>
      </div>
      <div class="col">
        <div class="card_cloverleaf px-5 pt-5">
          <v-alert
              v-if="!user.isProfileComplete"
              class="mx-auto"
              outlined
              prominent
              type="error"
          >
            <p class="font-weight-bold mb-0">Data Peserta Belum Lengkap</p>
            <p class="black--text text--darken-2 mb-1">
              Lengkapi data peserta terlebih dahulu untuk bisa melakukan pembuatan tim atau pendaftaran acara.
            </p>
          </v-alert>
          <v-alert
              v-if="alertShow"
              class="mx-auto"
              outlined
              prominent
              type="success"
          >
            <p class="font-weight-bold mb-0">Data Peserta Berhasil Dilengkapi</p>
            <p class="black--text text--darken-2 mb-1">
              {{ messages.message }} Selamat, Data peserta kamu sudah dilengkapi. Selamat berkompetisi ataupun mengikuti
              rangkaian acara Informatics Festival (IFest) yang lain.
            </p>
          </v-alert>
          <v-form ref="form" @submit.prevent="update">
            <v-container class="px-0 grey--text text--darken-4 title pt-0 font-weight-bold"
            >
              Data Peserta
            </v-container
            >
            <div class="form-group">
              <label style="cursor: default">Nama Lengkap<span class="red--text">*</span></label>
              <d-input
                  v-model="profilUser.full_name"
                  :disabled="isEditing"
                  :state="errors.full_name ? 'invalid' : 'null'"
                  class=""
                  type="text"
              />
              <d-form-invalid-feedback>Isian ini tidak boleh kosong.</d-form-invalid-feedback>
            </div>
            <div class="form-group">
              <label style="cursor: default">Tanggal Lahir<span class="red--text">*</span></label>
              <d-input
                  v-model="profilUser.tanggal_lahir"
                  :disabled="isEditing"
                  :state="errors.tanggal_lahir ? 'invalid' : 'null'"
                  class=""
                  type="date"
              />
              <d-form-invalid-feedback>Isian ini tidak boleh kosong.</d-form-invalid-feedback>
            </div>
            <div class="form-group">
              <label style="cursor: default">Nomor Identitas<span class="red--text">*</span></label>
              <d-input
                  v-model="profilUser.nomor_id"
                  :disabled="isEditing"
                  :state="errors.nomor_id ? 'invalid' : 'null'"
                  class=""
              />
              <d-form-invalid-feedback>Isian ini tidak boleh kosong.</d-form-invalid-feedback>
              <small class="form-text text-muted mb-2 mt-0 pt-0">Kamu bisa mengisi dengan nomor kartu pelajar atau kartu
                mahasiswa.</small>
            </div>
            <label style="cursor: default">Alamat<span class="red--text">*</span></label>
            <d-form-textarea
                v-model="profilUser.alamat"
                :disabled="isEditing"
                :max-rows="3"
                :rows="2"
                :value.prop="profilUser.alamat">
            </d-form-textarea>
            <div class="row pt-3">
              <div class="col-md-6">
                <div class="form-group">
                  <label style="cursor: default">Nomor Telepon<span class="red--text">*</span></label>
                  <d-input
                      v-model="profilUser.nomor_telepon"
                      :disabled="isEditing"
                      :state="errors.nomor_telepon ? 'invalid' : 'null'"
                      class=""
                  />
                  <d-form-invalid-feedback>Isian ini tidak boleh kosong.</d-form-invalid-feedback>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <label style="cursor: default">LINE ID</label>
                  <d-input
                      v-model="profilUser.id_line"
                      :disabled="isEditing"
                      class=""
                  />
                </div>
              </div>
            </div>
          </v-form>
<!--          <div class="pb-5" > v-if="!user.isProfileComplete"-->
          <div class="pb-5" >
            <div class="pb-3" v-if="!isEditing">
            <div class="row">
              <div class="col-md-6 py-0">
                <d-btn block-level theme="secondary" @click="batalUbahProfil">Batal</d-btn>
              </div>
              <div class="col-md-6 py-0">
                <d-btn block-level @click="update">Simpan</d-btn>
              </div>
            </div>
          </div>
          <div
              v-else
          >
            <d-btn
                block-level
                @click="isEditing = false"
            >
              Perbaharui Profil
            </d-btn>
          </div>
        </div>
          </div>
      </div>
    </div>
  </div>
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
