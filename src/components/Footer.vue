<template>
  <v-footer class="font-weight-medium" justify-center absolute app>
    <v-container bg fill-height grid-list-md text-xs-center>
      <v-layout row wrap align-center>
        <v-flex>
          <p class="text-center ma-0 footer-font">
            Made with
            <span style="color: #ff4757; font-size: 1.5em; vertical-align:middle;"><img style="height:1em; margin:auto;" 
            src="data:image/svg+xml;base64,
PHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJDYXBhXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy
8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9
IjBweCIgeT0iMHB4IiB2aWV3Qm94PSIwIDAgNDkyLjcxOSA0OTIuNzE5IiBzdHlsZT0iZW5hYm
xlLWJhY2tncm91bmQ6bmV3IDAgMCA0OTIuNzE5IDQ5Mi43MTk7IiB4bWw6c3BhY2U9InByZXNl
cnZlIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgY2xhc3M9IiI+PGc+PGc+Cgk8ZyBpZD0iSW
NvbnNfMThfIj4KCQk8cGF0aCBkPSJNNDkyLjcxOSwxNjYuMDA4YzAtNzMuNDg2LTU5LjU3My0x
MzMuMDU2LTEzMy4wNTktMTMzLjA1NmMtNDcuOTg1LDAtODkuODkxLDI1LjQ4NC0xMTMuMzAyLD
YzLjU2OSAgICBjLTIzLjQwOC0zOC4wODUtNjUuMzMyLTYzLjU2OS0xMTMuMzE2LTYzLjU2OUM1
OS41NTYsMzIuOTUyLDAsOTIuNTIyLDAsMTY2LjAwOGMwLDQwLjAwOSwxNy43MjksNzUuODAzLD
Q1LjY3MSwxMDAuMTc4ICAgIGwxODguNTQ1LDE4OC41NTNjMy4yMiwzLjIyLDcuNTg3LDUuMDI5
LDEyLjE0Miw1LjAyOWM0LjU1NSwwLDguOTIyLTEuODA5LDEyLjE0Mi01LjAyOWwxODguNTQ1LT
E4OC41NTMgICAgQzQ3NC45ODgsMjQxLjgxMSw0OTIuNzE5LDIwNi4wMTcsNDkyLjcxOSwxNjYu
MDA4eiIgZGF0YS1vcmlnaW5hbD0iIzAwMDAwMCIgY2xhc3M9ImFjdGl2ZS1wYXRoIiBzdHlsZT0
iZmlsbDojRkY0NzU3IiBkYXRhLW9sZF9jb2xvcj0iIzAwMDAwMCI+PC9wYXRoPgoJPC9nPgo8L2c+PC9nPiA8L3N2Zz4=" /></span>
            by
            <strong>SI IFest</strong>
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
  color: #747d8c;
  transition: ease .2s;
}

.footer-text:hover {
color: #57606f;
transition: ease .2s;
}

.footer-font {
  color: #57606f;
}
</style>