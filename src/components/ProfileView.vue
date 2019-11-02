<template>
<v-container>
      <v-card class="mx-auto"  outlined>
    <v-card-text class=text-center>
             <vue-letter-avatar class="mb-5 mt-5" :name="user.full_name" size="90" :rounded="true" />
          <p class="display-1 text--primary mb-0">{{user.full_name}}</p>
          <p class="subtitle-2 text--primary mb-0">{{user.email}}</p>
    </v-card-text>
    <v-card-actions class="justify-center">
      <v-btn text color="blue accent-4">Edit Profile</v-btn>
    </v-card-actions>
  </v-card>
</v-container>
</template>

<script>
import { mapState } from "vuex";

export default {
  data: () => ({}),
  computed: mapState({
    user: state => state.authsys.user
  })
};
</script>