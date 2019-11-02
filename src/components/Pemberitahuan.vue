<template>
  <v-container fluid>
    <v-badge class="mb-5">
      <template
        v-if="Object.keys(anouncements).length !== 0"
        v-slot:badge
      >{{Object.keys(anouncements).length}}</template>
      <h3 class="subtitle">Update Pemberitahuan</h3>
    </v-badge>
    <v-content v-for="a in anouncements" :key="a.id">
      <v-alert prominent outlined :type="(a.type)">
        <p class="font-weight-bold mb-0">{{a.title}}</p>
        <p class="black--text text--darken-2 mb-1">{{a.message}}</p>
      </v-alert>
    </v-content>
    <v-content v-if="Object.keys(anouncements).length === 0">
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
import { mapState, mapActions } from "vuex";
export default {
  computed: mapState({
    anouncements: state => state.pemberitahuan.anouncements
  }),
  methods: {
    ...mapActions({
      getAnouncement: "pemberitahuan/getPemberitahuan"
    })
  },
  beforeMount() {
    this.getAnouncement();
  }
};
</script>