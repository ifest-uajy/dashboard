<template>
  <v-container class="px-0 pt-0 mx-0">
    <v-container v-if="Object.keys(announcements).length > 0">
      <d-card v-for="a in announcements" :key="a.id" class="pb-3">
        <div class="px-5 pt-5">
          <p class="font-weight-bold mb-0" style="font-size: 16pt">{{ a.title }}</p>
          <p class="mb-1 grey--text text--darken-4 caption">
            Posted on
            {{ moment(String(a.issued_at)).format("DD MMM YYYY") }}
          </p>
          <p class="black--text text--darken-2 mb-1">{{ a.message }}</p>
        </div>
      </d-card>
    </v-container>
    <v-container v-else>
      <div class="pb-3 text-center">
        <div class="px-5 pt-5">
          <img class="image-empty" :src="images.inboxEmpty"/>
          <p class="font-weight-bold mb-0" style="font-size: 26pt; color: #1d3557 !important;">Relax...</p>
          <p class="black--text text--darken-2 mb-1" style="opacity: 0.8;">Saat ini belum ada pengumuman yang di rilis oleh Panitia Informatics Festival (IFest)</p>
        </div>
      </div>
    </v-container>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
import moment from "moment";

moment.locale("id");

export default {
  data() {
    return {
      images: {
        inboxEmpty: require('@/assets/Empty Inbox _Two Color.svg')
      }
    }
  },
  computed: mapState({
    announcements: state => state.pemberitahuan.announcements
  }),
  methods: {
    moment
  }
};
</script>

<style scoped>
.image-empty {
  max-width: 50vw;
}
</style>
