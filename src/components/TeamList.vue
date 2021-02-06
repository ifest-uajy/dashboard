<template>
  <v-container class="px-0 pt-0 mx-0">
    <v-container v-if="Object.keys(teams).length > 0">
      <d-card v-for="(c, k) in teams" :key="k">
        <d-card-body class="pb-0 mb-3">
          <d-badge class="font-weight-bold" theme="primary">{{ c.kompetisi.name }}</d-badge>
        </d-card-body>
        <d-card-body :subtitle="c.asal" :title="c.nama" class="pt-0 mt-0">
          <hr/>
          <div class="row">
            <div class="col-md-6  ">
              <p class="font-weight-bold mb-3">ℹ️&nbsp;️&nbsp;️&nbsp;Detail Tim</p>
              <label>Alamat Institusi Tim</label>
              <d-form-textarea
              :value.prop="c.alamat"
              readonly
              :max-rows="4"
              :rows="4">
          </d-form-textarea>
            </div>
            <div class="col-md-6">
              <p class="font-weight-bold mb-3">ℹ️&nbsp;️&nbsp;️&nbsp;Informasi Pendamping</p>
              <div>
                <label>Nama Pembimbing</label>
                <d-input
                    v-model="c.pembimbing.nama"
                    disabled=""
                />
                <label class="mt-3">Kontak Pembimbing</label>
                <d-input
                    v-model="c.pembimbing.telepon"
                    disabled=""
                />
              </div>
            </div>
          </div>
          <hr/>
          <p class="font-weight-bold mb-3">ℹ️&nbsp;️&nbsp;️&nbsp;Anggota Tim</p>
              <vs-table>
                <template #thead>
                  <vs-tr>
                    <vs-th>
                      Nomor Identitas
                    </vs-th>
                    <vs-th>
                      Nama Lengkap
                    </vs-th>
                    <vs-th>
                      Email
                    </vs-th>
                    <vs-th>
                      No Telepon
                    </vs-th>
                    <vs-th>
                      ID Line
                    </vs-th>
                    <vs-th>
                      Tanggal Lahir
                    </vs-th>
                    <vs-th>
                      Alamat
                    </vs-th>
                  </vs-tr>
                </template>
                <template #tbody>
                  <vs-tr
                      v-for="(u, k) in c.anggota"
                      :key="k"
                      :data="u"
                  >
                    <vs-td>
                      {{ u.nomor_id }}
                    </vs-td>
                    <vs-td>
                      {{ u.full_name }}
                    </vs-td>
                    <vs-td>
                      {{ u.email }}
                    </vs-td>
                    <vs-td>
                      {{ u.nomor_telepon }}
                    </vs-td>
                    <vs-td>
                      {{ u.id_line }}
                    </vs-td>
                     <vs-td>
                       {{ moment(String(u.tanggal_lahir)).format("DD MMM YYYY") }}
                    </vs-td>
                    <vs-td>
                      {{ u.alamat }}
                    </vs-td>
                  </vs-tr>
                </template>
              </vs-table>
              <d-btn :hidden="c.is_full" @click.native="handleClick" size="sm" class="mt-3">Tambah Data Anggota</d-btn>
          <hr/>
          <p class="font-weight-bold mb-3">ℹ️&nbsp;️&nbsp;️&nbsp;Task Kompetisi</p>

          <v-alert
              v-if="!c.task_permission"
              class="mb-5"
              dense
              outlined
              prominent
              type="error"
          >
            <strong>Anggota tim belum lengkap!</strong>
            <p class="mb-0 black--text caption">Kamu belum bisa mengupload berkas pendaftaran. Harap lengkapi data
              anggota kelompok terlebih dahulu.</p>
          </v-alert>

          <div class="mt-5">
            <div v-for="task in c.tasks" :key="task.task.order">
              <d-card class="mb-5">
                <d-card-header>
                  <p class="mb-0" style="font-weight: bold; font-size: 16pt">
                    {{ task.task.order }}. {{ task.task.name }}
                    <span v-if="task.response.length !== 0 &&
                          task.response.status === 'selesai'">
                    <d-badge theme="success">Selesai</d-badge>
                  </span>
                    <span v-else-if="task.task.task_type === 'pengumuman'">
                    <d-badge theme="warning">Pengumuman</d-badge>
                  </span>
                  </p>
                  <div v-if="task.task.task_type !== 'pengumuman'">
                    <p class="mt-3 mb-0 pb-0">Batas pengumpulan tugas
                      <span class="font-weight-bold">
                    {{ moment(String(task.task.deadline)).format("DD MMMM YYYY [Pukul] HH:mm") }}
                  </span>
                    </p>
                    <small
                        v-if="
                        task.response.length !== 0 &&
                          task.response.status === 'selesai'
                      "
                        class="mt-0 pb-0"
                    >
                      Berkas berhasil diunggah pada
                      <b>{{
                          moment(String(task.response.updated_at)).format(
                              "DD MMMM YYYY [Pukul] HH:mm"
                          )
                        }}</b> | <a
                        :href="
                            `/api/file/download/` + task.response.response + `/`
                          "
                        class="body-link"
                        target="_blank"
                    >Unduh berkas</a
                    >
                    </small>
                  </div>
                  <div v-else>
                    <p class="mt-3 mb-0 pb-0">
                      {{ task.task.deskripsi }}
                    </p>
                  </div>
                </d-card-header>
                <d-collapse id="accordion1" :hidden="task.task.order !== c.current_task.order || !c.task_permission" accordion="my-accordion"
                            role="tabpanel" visible>
                  <d-card-body>
                    <div v-if="!moment().isAfter(moment(task.task.deadline))">
                      <UploaderWidget
                          :hidden="
                            task.task.task_type !== 'file_uploader' &&
                              task.task.task_type !== 'payment_verification'
                          "
                          :response="task.response"
                          :task="task.task"
                          :team="c"
                      />
                    </div>
                    <div v-else>
                      <div v-if="task.task.task_type !== 'pengumuman'">
                          <span class="red--text">
                            <v-alert
                                class="mb-5"
                                dense
                                outlined
                                prominent
                                type="error"
                            >
                              <p class="font-weight-bold mb-2">
                                {{ task.task.name }} sudah melewati batas
                                pengumpulan
                              </p>
                              <p class="black--text text--darken-2 mb-1">
                                Maaf, anda tidak bisa lagi mengunggah file
                                karena batas waktu pengumpulan sudah terlewati
                                sejak
                                <b>
                                  {{
                                    moment(String(task.task.deadline)).format(
                                        "DD MMMM YYYY HH:mm")
                                  }}
                                </b>
                              </p>
                            </v-alert>
                          </span>
                      </div>
                    </div>
                  </d-card-body>
                </d-collapse>
              </d-card>
            </div>
          </div>
        </d-card-body>
        <d-modal v-if="showModal" @close="handleClose">
        <d-modal-header>
            <d-modal-title>Tambah Data Anggota</d-modal-title>
        </d-modal-header>
        <d-modal-body>
          <label>Nama</label>
            <d-input v-model="data.full_name"/>
          <label class="pt-3">Nomor Identitas</label>
            <d-input v-model="data.nomor_id"/>
          <label class="pt-3">Email</label>
            <d-input type="email" v-model="data.email"/>
          <label class="pt-3">Tanggal Lahir</label>
            <d-input type="date" class="mb-3" v-model="data.tanggal_lahir"/>
          <label>Alamat</label>
          <d-form-textarea
              v-model="data.alamat"
              :max-rows="3"
              :rows="2">
          </d-form-textarea>
          <label class="pt-3">Nomor Telepon</label>
            <d-input type="tel" v-model="data.nomor_telepon"/>
          <label class="pt-3">ID Line</label>
            <d-input v-model="data.id_line"/>
          <d-button @click="sendData(c.id)" block-level class="mt-5 mb-1">Tambah</d-button>
        </d-modal-body>
    </d-modal>
      </d-card>

    </v-container>
    <v-container v-else>
      <div class="pb-3 text-center">
        <div class="px-5 pt-5">
          <img :src="images.noTeams"/>
          <p class="font-weight-bold mb-0" style="font-size: 26pt; color: #1d3557 !important;">Whoops...</p>
          <p class="black--text text--darken-2 mb-1" style="opacity: 0.8;">Kamu belum mendaftar kompetisi apapun saat ini</p>
        </div>
      </div>
    </v-container>
  </v-container>
</template>

<script>
import {mapActions, mapState} from "vuex";
import moment from "moment";
import UploaderWidget from "./UploaderWidget.vue";

moment.locale("id");

export default {
  data: () => ({
    showModal: false,
    data: {
      team_id: "",
      full_name: "",
      email: "",
      id_line: "",
      nomor_telepon: "",
      nomor_id: "",
      tanggal_lahir: "",
      alamat: ""
    },
    images: {
        noTeams: require('@/assets/Progress _Two Color.svg')
    }
  }),
  computed: mapState({
    competitions: state => state.competition.competitions,
    teams: state => state.competition.teams
  }),
  components: {
    UploaderWidget
  },
  methods: {
    moment,
     handleClick() {
            this.showModal = true
        },
    handleClose() {
            this.showModal = false
            this.data.team_id = ""
            this.data.full_name = ""
            this.data.email = ""
            this.data.id_line = ""
            this.data.nomor_telepon = ""
            this.data.nomor_id = ""
            this.data.tanggal_lahir = ""
            this.data.alamat = ""
        },
    ...mapActions({
      addMember: "competition/addMember",
      getTeams: "competition/getTeams"
    }),
    sendData(data) {
      this.data.team_id = data
      this.addMember(this.data).then(
          this.handleClose
      ).then(
          this.getTeams
      )
    }
  }
};
</script>