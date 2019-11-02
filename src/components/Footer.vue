<template>
  <v-footer class="font-weight-medium" justify-center>
    <v-container>
      <v-layout>
        <v-flex>
          <p class="text-center ma-0">
            Made with
            <span style="color: #c51104; font-size: 1.5em; vertical-align:middle;">❤</span>
            by
            <strong>CBIS 3.0</strong>
            © {{ new Date().getFullYear() }}
            <a
              href="https://ifest-uajy.com"
              target="_blank"
              rel="noopener noreferrer"
              class="LinkToHome"
            >
              <strong>Informatics Festival #8</strong>
            </a>
          </p>
        </v-flex>
      </v-layout>
    </v-container>
  </v-footer>
</template>


<style scoped>
.LinkToHome {
    text-decoration-line: unset
}
</style>