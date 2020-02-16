<template>
  <v-layout class="bg-img">
    <!-- /* LOGOUT BUTTON */ -->
    <div @click="logoutActions" class="logout-btn">
      <a>Logout</a>
    </div>
    <v-container justify-center class="boxed-isi">
      <v-card outlined width="1700" class="card_cloverleaf mb-5 pt-0 mt-10">
        <v-card-subtitle class="mt-5 pb-0 mb-0">
          <router-link to="/administrasi" class="link_clover"
            >Kembali</router-link
          >
        </v-card-subtitle>

        <div v-if="loading">
          <v-skeleton-loader
            class="ml-4 mt-5 mb-2"
            type="heading"
            max-width="350"
          ></v-skeleton-loader>
          <v-skeleton-loader
            class="ml-4 mt-5 mb-2"
            type="text"
            max-width="350"
          ></v-skeleton-loader>
        </div>
        <div v-else>
          <v-card-title class="title_card_cloverleaf mt-0 pb-3">{{
            slug.name
          }}</v-card-title>
          <v-card-subtitle class="subtitle_card_cloverleaf mb-5 pt-2 pb-0"
            >Informatics Festival (IFest) #8</v-card-subtitle
          >
        </div>

        <v-card-text class="mb-5">
          <v-data-table
            :headers="headers"
            :items="list"
            :items-per-page="10"
            :sort-by="['name']"
            :loading="loading"
            mobile-breakpoint="600"
            class="elevation-1"
          >
            <template v-slot:top v-if="dialog">
              <div v-if="loading2">
                <v-dialog v-model="dialog" max-width="400">
                  <v-card dark>
                    <v-card-text class="pt-2">
                      Memuat data kelompok
                      <v-progress-linear
                        indeterminate
                        color="white"
                        class="mb-0"
                      ></v-progress-linear>
                    </v-card-text>
                  </v-card>
                </v-dialog>
              </div>
              <div v-else>
                <v-dialog v-model="dialog" max-width="1200px">
                  <v-card outlined class="card_cloverleaf pt-5">
                    <v-card-title style="font-size: 20pt"
                      >Data Detail Tim</v-card-title
                    >
                    <v-card-text>
                      <!-- <v-container> -->
                      <v-row>
                        <v-col>
                          <p class="title-inner">Informasi Tim</p>
                          <span class="subtitle-inner">Nama</span>
                          <p class="subtitle-outer">{{ detail.nama }}</p>
                          <span class="subtitle-inner">Asal Institusi</span>
                          <p class="subtitle-outer">{{ detail.asal }}</p>
                          <span class="subtitle-inner">Alamat Institusi</span>
                          <p class="subtitle-outer">{{ detail.alamat }}</p>
                          <span class="subtitle-inner">Nama Ketua</span>
                          <p class="subtitle-outer">{{ detail.ketua }}</p>
                        </v-col>
                        <v-col>
                          <p class="title-inner">Informasi Pendamping</p>
                          <span class="subtitle-inner">Nama Pendaming</span>
                          <p class="subtitle-outer">
                            {{ detail.pembimbing.nama }}
                          </p>
                          <span class="subtitle-inner">Kontak Pendamping</span>
                          <p class="subtitle-outer">
                            (+62) {{ detail.pembimbing.telepon }}
                          </p>
                          <p class="title-inner">Data SI untuk Tim</p>
                          <span class="subtitle-inner">Token</span>
                          <p class="subtitle-outer">{{ detail.token }}</p>
                          <span class="subtitle-inner">Dibuat Pada</span>
                          <p class="subtitle-outer">
                            {{
                              moment(String(detail.created_at)).format(
                                "DD MMMM YYYY hh:mm A "
                              )
                            }}
                          </p>
                        </v-col>
                      </v-row>
                      <!-- </v-container> -->
                      <p class="title-inner">Informasi Anggota</p>
                      <v-simple-table>
                        <template v-slot:default>
                          <thead>
                            <tr>
                              <th class="text-left">#</th>
                              <th class="text-left">Nama</th>
                              <th class="text-center">Email</th>
                              <th class="text-left">Nomor ID</th>
                              <th class="text-left">Tanggal Lahir</th>
                              <th class="text-left">Telepon</th>
                              <th class="text-left">ID Line</th>
                              <th class="text-center">Vege?</th>
                              <th class="text-left">Alergi</th>
                              <!-- <th class="text-left">Tanggal Daftar</th> -->
                            </tr>
                          </thead>
                          <tbody>
                            <tr
                              v-for="(item, key) in detail.anggota"
                              :key="key"
                            >
                              <td>{{ key + 1 }}</td>
                              <td v-if="item.nama == detail.ketua">
                                <b>{{ item.nama }} (Ketua)</b>
                              </td>
                              <td v-else>{{ item.nama }}</td>
                              <td>{{ item.email }}</td>
                              <td>{{ item.nomor_id }}</td>
                              <td>
                                {{
                                  moment(String(item.tanggal_lahir)).format(
                                    "DD MMM YYYY"
                                  )
                                }}
                              </td>
                              <td>{{ item.nomor_telepon }}</td>
                              <td>{{ item.id_line }}</td>
                              <td class="text-center">
                                <span v-if="item.is_vege === true">
                                  <v-icon color="green"
                                    >mdi-check-circle</v-icon
                                  >
                                </span>

                                <span v-else>
                                  <v-icon color="red">mdi-close-circle</v-icon>
                                </span>
                              </td>
                              <td>{{ item.alergic }}</td>
                              <!-- <td>{{moment(String(item.date_joined)).format("DD MMMM YYYY hh:mm A ")}}</td> -->
                            </tr>
                          </tbody>
                        </template>
                      </v-simple-table>
                      <p class="title-inner">Informasi Task Lomba</p>
                      <span class="subtitle-inner">Task Saat Ini</span>
                      <p class="subtitle-outer">
                        {{ detail.current_task.name }}
                      </p>

                      <v-simple-table>
                        <template v-slot:default>
                          <thead>
                            <tr>
                              <th class="text-left">#</th>
                              <th class="text-left">Nama Task</th>
                              <th class="text-left">Status</th>
                              <th class="text-left">Respon</th>
                              <th class="text-left">Terima Respon</th>
                              <th class="text-left">Tolak Respon</th>
                              <th class="text-center">Is Verified?</th>
                              <th class="text-left">Updated at</th>
                              <!-- <th class="text-left">Tanggal Daftar</th> -->
                            </tr>
                          </thead>
                          <tbody>
                            <tr v-for="(item, key) in detail.tasks" :key="key">
                              <td>{{ key + 1 }}</td>
                              <td>{{ item.task.name }}</td>
                              <td>
                                <span v-if="item.response.status === 'selesai'"
                                  >Selesai</span
                                >
                                <span
                                  v-if="
                                    item.response.status ===
                                      'menunggu_verifikasi'
                                  "
                                  >Menunggu Verifikasi</span
                                >
                                <span v-if="item.response.status === 'ditolak'"
                                  >Ditolak</span
                                >
                                <span v-if="!item.response.status"
                                  >Belum ada respon</span
                                >
                              </td>
                              <td>
                                <span
                                  v-if="
                                    item.task.task_type !== 'pengumuman' &&
                                      item.task.id <= detail.current_task.id &&
                                      item.response.length !== 0
                                  "
                                >
                                  <a
                                    :href="
                                      `/api/file/download/` +
                                        item.response.response +
                                        `/`
                                    "
                                    class="body-link"
                                    target="_blank"
                                  >
                                    <v-btn depressed color="primary" small
                                      >Unduh Respon</v-btn
                                    >
                                  </a>
                                </span>
                                <span v-else>-</span>
                              </td>
                              <td>
                                <span
                                  v-if="
                                    item.response.status ===
                                      'menunggu_verifikasi'
                                  "
                                >
                                  <v-btn
                                    depressed
                                    @click="terima(item.response.id)"
                                    color="success"
                                    small
                                    >Terima</v-btn
                                  >
                                </span>
                                <span v-else>-</span>
                              </td>
                              <td>
                                <span
                                  v-if="
                                    item.response.status ===
                                      'menunggu_verifikasi'
                                  "
                                >
                                  <v-btn
                                    depressed
                                    @click="tolak(item.response.id)"
                                    color="error"
                                    small
                                    >Tolak</v-btn
                                  >
                                </span>
                                <span v-else>-</span>
                              </td>
                              <td class="text-center">
                                <span v-if="item.response.is_verified === true">
                                  <v-icon color="green"
                                    >mdi-check-circle</v-icon
                                  >
                                </span>

                                <span
                                  v-if="
                                    !item.response.status ||
                                      item.response.status ===
                                        'menunggu_verifikasi'
                                  "
                                >
                                  <v-icon color="warning"
                                    >mdi-help-circle</v-icon
                                  >
                                </span>

                                <span
                                  v-if="
                                    item.response.is_verified === false &&
                                      item.response.status !==
                                        'menunggu_verifikasi'
                                  "
                                >
                                  <v-icon color="red">mdi-close-circle</v-icon>
                                </span>
                              </td>
                              <td v-if="item.response.updated_at">
                                {{
                                  moment(
                                    String(item.response.updated_at)
                                  ).format("DD MMMM YYYY hh:mm A ")
                                }}
                              </td>
                              <td v-else>-</td>
                            </tr>
                          </tbody>
                        </template>
                      </v-simple-table>
                    </v-card-text>
                    <v-card-text>
                      <p class="mt-2">
                        <strong>Informasi simbol verifikasi</strong>
                      </p>
                      <p>
                        <v-icon color="green">mdi-check-circle</v-icon>Berarti
                        sudah di verifikasi baik oleh PH untuk pembayaran atau
                        Sekretariat untuk task administrasi.
                      </p>
                      <p>
                        <v-icon color="warning">mdi-help-circle</v-icon>Menunggu
                        di verifikasi atau belum ada respon dari tim.
                      </p>
                      <p>
                        <v-icon color="red">mdi-close-circle</v-icon>Task
                        ditolak oleh panitia dan menunggu tim mengupload ulang
                        atau menyerah.
                      </p>
                      <p class="mt-2">
                        <strong
                          >PH hanya bisa memverifikasi task Pembayaran
                          Registrasi. Sekretariat hanya bisa memverifikasi task
                          yang perlu diverifikasi selain Pembayaran
                          Registrasi.</strong
                        >
                      </p>
                      <p>
                        Note buat verifikator,
                        <span style="font-weight:bold; color:red;"
                          >GUNAKAN TOMBOL DENGAN BIJAK</span
                        >. There's no way back after clicking yet.
                      </p>
                    </v-card-text>
                  </v-card>
                </v-dialog>
              </div>
            </template>
            <template v-slot:item.action="{ item }">
              <v-icon small @click="detailTim(item)">mdi-magnify</v-icon>
            </template>
          </v-data-table>
        </v-card-text>
      </v-card>
    </v-container>
    <v-snackbar v-model="snackbar">{{ message.message }}</v-snackbar>
  </v-layout>
</template>

<script>
import { mapState, mapActions } from "vuex";
import moment from "moment";

export default {
  data: () => ({
    dialog: false,
    snackbar: false,
    headers: [
      {
        text: "#",
        align: "left",
        sortable: false,
        value: "id"
      },
      { text: "Nama Tim", value: "name" },
      { text: "Asal Institusi", sortable: false, value: "institution" },
      { text: "Nama Ketua", sortable: false, value: "team_leader_name" },
      // { text: "Email Ketua", sortable: false, value: "team_leader_email" },
      { text: "Detail", value: "action", sortable: false }
    ]
  }),
  computed: {
    ...mapState({
      user: state => state.authsys.user,
      list: state => state.sekret.competitionList,
      detail: state => state.sekret.competitionDetail,
      loading: state => state.sekret.loading,
      slug: state => state.sekret.slugDetail,
      loading2: state => state.sekret.loading2,
      message: state => state.sekret.message
    })
  },
  methods: {
    moment,
    ...mapActions({
      logoutActions: "authsys/logout",
      getCompetitionList: "sekret/getCompetitionList",
      getCompetitionDetail: "sekret/getCompetitionDetail",
      getSlugDetail: "sekret/getSlugDetail",
      confirmTeam: "sekret/confirmTeam",
      resetList: "sekret/clear"
    }),
    detailTim(item) {
      this.getCompetitionDetail({
        id: item.id
      });
      this.dialog = true;
    },
    async tolak(id) {
      console.log(id);
      await this.confirmTeam({
        task_res_id: id,
        tolak: true
      });
      console.log("get new detail");
      await this.getCompetitionDetail({
        id: this.detail.id
      });
      this.snackbar = true;
      await setTimeout(() => (this.snackbar = false), 3000);
    },
    async terima(id) {
      await this.confirmTeam({
        task_res_id: id,
        tolak: false
      });
      await this.getCompetitionDetail({
        id: this.detail.id
      });
      this.snackbar = true;
      await setTimeout(() => (this.snackbar = false), 3000);
    }
  },
  beforeMount() {
    this.resetList();
    if (this.user.is_staff) {
      this.getCompetitionList({
        slug_name: this.$route.params.slug
      });
      this.getSlugDetail({
        slug_name: this.$route.params.slug
      });
    } else {
      this.$router.push({ name: "dashboard" });
    }
  }
};
</script>

<style scoped>
.card_cloverleaf {
  box-shadow: 0 10px 20px 0 rgba(53, 64, 90, 0.2);
  outline: none;
  border: none !important;
  border-radius: 8px !important;
  padding-left: 20px;
  padding-right: 20px;
}

.title_card_cloverleaf {
  font-size: 20pt;
  margin-top: 10px;
}

.subtitle_card_cloverleaf {
  font-size: 15pt;
}

.subtitle-inner {
  font-size: 9pt;
  margin: 0;
  font-weight: bold;
  color: rgb(0, 11, 32);
}

.subtitle-outer {
  margin: 0;
  padding: 0;
  margin-bottom: 10px;
}

.title-inner {
  margin: 0;
  padding: 0;
  margin-bottom: 10px;
  font-size: 14pt;
  font-weight: bold;
  margin-top: 25px;
}

.logout-btn {
  position: fixed;
  top: 50px;
  right: 0px;
  padding: 0px;
  margin: 0px;
  cursor: pointer;
  width: 40px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
  height: 100px;
  background: #13355b;
  color: #adadad;
  z-index: 15;
  border-radius: 8px 0px 0px 8px;
}
.logout-btn a {
  margin: auto 10px;
  margin-top: 25px;
  writing-mode: tb-rl;
  color: rgb(119, 170, 241);
  text-decoration: none;
}
.logout-btn a:visited {
  text-decoration: none;
}
.logout-btn:hover {
  background: rgb(13, 34, 65);
}

.link_clover {
  text-decoration: unset !important;
}

.link_clover:hover {
  color: cornflowerblue;
}

.bg-img {
  width: 100%;
  background: url("https://ifest-uajy.com/assets/email/bg_top2.jpg") no-repeat;
}

.boxed-isi {
  max-width: 1000px;
}

@media (max-width: 420px) {
  .card_cloverleaf {
    padding: 0;
  }
}
</style>
