<template>
  <div class="container pb-5 mb-5">
    <div class="row">
      <div class="col-lg-4">
        <div class="card_cloverleaf py-5" style="background-color: #ffffff;">
          <p class="font-weight-bold mb-3 px-5" style="font-size: 16pt">Pesan Bantuan</p>
          <div class="p-3 px-5 black--text message-card">
            <div class="row no-gutters mb-2 small">
              <div class="col">
                <d-badge class="font-weight-bold" theme="warning">Dalam Proses</d-badge>
              </div>
              <div class="col-auto">
                Yesterday
              </div>
            </div>
            Update data peserta
            <p class="small mb-0">ID <span class="font-weight-bold">000002</span></p>
          </div>
          <div class="p-3 px-5 black--text message-card">
            <div class="row no-gutters mb-2 small">
              <div class="col">
                <d-badge class="font-weight-bold" theme="light">Selesai</d-badge>
              </div>
              <div class="col-auto">
                29 Jan
              </div>
            </div>
            Pembayaran tidak dikonfirmasi
            <p class="small mb-0">ID <span class="font-weight-bold">000001</span></p>
          </div>
          <router-link class="link_clover" to="profile/changepassword">
            <div class="px-5">
              <d-btn block-level theme="primary" class="mt-4">
              Buat Tiket Baru
            </d-btn>
            </div>
          </router-link>
        </div>
      </div>
      <div class="col">
        <div class="card_cloverleaf px-5 py-5">
          <div class="px-5 pt-5 text-center mb-5 pb-5">
            <img :src="images.inboxEmpty"/>
            <p class="font-weight-bold mb-0" style="font-size: 26pt; color: #1d3557 !important;">Halo...</p>
            <p class="black--text text--darken-2 mb-1" style="opacity: 0.8;">Silahkan pilih pesan dalam tab disamping untuk melihat jawaban</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelpDesk",
  data() {
      return {
        images: {
          inboxEmpty: require('@/assets/Empty Inbox _Two Color.svg')
        }
      }
    }
  }
</script>

<style scoped>
.message-card {
  background-color: white;
  transition: 0.3s ease;
}
.message-card:hover {
  background-color: #f5f5f5;
  transition: 0.3s ease;
  cursor: pointer;
}
</style>