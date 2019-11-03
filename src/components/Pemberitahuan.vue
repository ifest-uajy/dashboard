<template>
  <v-container fluid>
    <!--<v-badge class="mb-5">
      <template
        v-if="Object.keys(anouncements).length !== 0"
        v-slot:badge
      >{{Object.keys(anouncements).length}}</template>
      <h3 class="subtitle">Update Pemberitahuan</h3>
    </v-badge>
    -->
    <v-content v-for="a in announcements" :key="a.id">
      <v-alert prominent outlined :type="(a.type)">
        <p class="font-weight-bold mb-0 ">{{a.title}}</p>
        <p class="mb-1 grey--text text--darken-4 caption">Issued by {{a.issuer}} on {{moment(String(a.issued_at)).format("DD MMMM YYYY hh:mm A ")}}</p>
        <p class="black--text text--darken-2 mb-1">{{a.message}}</p>
      </v-alert>
    </v-content>
    <v-content v-if="Object.keys(announcements).length === 0">
      <v-alert prominent outlined>
        <p class="font-weight-bold mb-0">You're clear</p>
        <p
          class="black--text text--darken-2 mb-1"
        >Tidak ada info pemberitahuan dari panitia saat ini.</p>
      </v-alert>
    </v-content>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
import moment from "moment";
export default {
  computed: mapState({
    announcements: state => state.pemberitahuan.announcements
  }),
  methods: {
    moment
  },
};
</script>