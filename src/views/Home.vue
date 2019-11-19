<template>
  <div>
    <div class="container">
      <h1 class="header_big">RegSys v1.0.0</h1>
      <h2 class="subheader_big">Informatics Festival (IFest) #8</h2>
      <p class="font-weight-medium">
        <router-link to="/register" class="link_clover">Register</router-link>
      </p>
      <p class="font-weight-medium">
        <router-link to="/login" class="link_clover">Login</router-link>
      </p>
      <p class="font-weight-medium">
        <router-link to="/reset-password" class="link_clover">Lupa password?</router-link>
      </p>
      <p class="font-weight-medium">
        <router-link to="/contact" class="link_clover">Hubungi Kami</router-link>
      </p>
    </div>
  </div>
</template>

<style scoped>
.header_big {
  margin-top: 40px;
  font-size: 80pt;
}
.subheader_big {
  font-size: 60pt;
  margin-bottom: 40px;
}
.link_clover {
  font-size: 25pt;
  text-decoration: unset !important;
}

.link_clover:hover {
  color: cornflowerblue;
}
</style>