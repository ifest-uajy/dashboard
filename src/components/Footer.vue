<template>
  <div class="font-weight-medium ifest-footer">
    <div class="container my-4">
      <div class="row align-items-center">
        <div class="col">
          <p class="mb-0">&copy; 2019-{{new Date().getFullYear()}} <strong>Informatics Festival (IFest)</strong>. Hak Cipta Dilindungi.</p>
        </div>
        <div class="col text-right">
          <div>
            <font-awesome-icon class="ifest-icon" :icon="['fab', 'facebook']" />
            <font-awesome-icon class="ifest-icon" :icon="['fab', 'instagram']" />
            <font-awesome-icon class="ifest-icon" :icon="['fab', 'line']" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.ifest-footer {
  background-color: #1d3557 !important;
  color: #FFFFFF !important;
  font-size: 10pt;
}
.ifest-icon {
  height: 30px;
  width: 30px;
  background-color: #152844;
  padding: 4px;
  border-radius: 4px;
  color: #5d7eb5;
  margin-left: 8px;
}
</style>
