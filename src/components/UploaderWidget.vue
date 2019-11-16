<template>
  <v-flex>
    <v-form @submit.prevent="sumbitFile">
      <v-flex class="mb-5">
        <vue-dropzone
          ref="dropzone"
          id="dropzone"
          :options="dropOptions"
        />
        <span v-for="resp in task_response_list" :key="resp.task_id">

          {{resp.task.name}}
          {{resp.status}}

        </span>
        <v-alert v-if="dropzoneError" :value="true" type="error" outline>{{ dropzoneError }}</v-alert>
      </v-flex>
    </v-form>
  </v-flex>
</template>

<script>
import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
export default {
  props: ['task', 'task_response_list'],
  components: {
    vueDropzone: vue2Dropzone
  },
      data: function () {
      return {
        dropOptions: {
          url: 'https://httpbin.org/post',
          maxFiles: 1,
          maxFilesize: 10,
          addRemoveLinks: true,
          dictDefaultMessage: "<i class='fa fa-cloud-upload'></i> Upload File"
        },
        dropzoneError: null,
      }
    },
}
</script>

<style>
@import url("https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css");
</style>