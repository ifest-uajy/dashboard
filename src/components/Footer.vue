<template>
  <v-footer class="font-weight-medium" justify-center absolute>
    <v-container>
      <v-layout>
        <v-flex>
          <p class="text-center ma-0">
            Made with
            <span style="color: #c51104; font-size: 1.5em; vertical-align:middle;">❤</span>
            by
            <strong>CBIS 3.0</strong>
            |&nbsp;Hak Cipta © {{ new Date().getFullYear() }}
            <a
              href="https://ifest-uajy.com"
              target="_blank"
              rel="noopener noreferrer"
              class="LinkToHome"
            >
              <span class="footer-text">Informatics Festival (IFest) #8</span>
            </a>
          </p>
        </v-flex>
      </v-layout>
    </v-container>
  </v-footer>
</template>


<style scoped>
.LinkToHome {
  text-decoration-line: unset;
}
.footer-text {
  font-weight: bolder;
  color: #212121;
}
</style>