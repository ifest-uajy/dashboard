<template>
  <div class="onboarding-dialog" v-bind:class="[isShown ? 'onboarding-dialog--shown' : 'onboarding-dialog--hidden']">
    <div class="onboarding-modal text-center">
      <div class="onboarding-container--1" :hidden="slideOne">
        <h2 class="onboarding-modal-title pt-5">Selamat Datang! 👋</h2>
        <p class="text-center">Sebelum dapat melakukan pendaftaran perlombaan atau kompetisi kamu harus melengkapi data
          diri terlebih dahulu.</p>
        <d-btn class="text-center" @click="toSlideTwo()">Mulai →</d-btn>
        <a @click="isShown = false">
          <p class="mt-3 caption indigo--text darken-4">Lain kali saja</p>
        </a>
      </div>
      <div class="onboarding-container--1" :hidden="slideTwo">
        Container 2
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "OnboardingDialog",
  data: function () {
    return {
      isShown: true,
      slideOne: false,
      slideTwo: true,
    }
  },
  methods: {
    toSlideTwo() {
      this.slideOne =  true
      this.slideTwo = false
    }
  }
}
</script>

<style lang="scss" scoped>
/*Onboarding Modal Style*/

.onboarding-dialog {
  position: fixed;
  left: 0;
  top: 0;
  width: 100vw;
  height: 100vh;
  z-index: 99;
  background-color: rgba(0, 0, 0, 0.5);
  transition: all 0.3s linear;

  &--hidden {
    opacity: 0;
    visibility: hidden;
  }

  &--shown {
    opacity: 100;
    visibility: visible;
  }
}

.onboarding-modal {
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  padding: 2rem 6rem 2rem;
  width: 50rem;
  border-radius: 0.5rem;
  transition: all 0.3s linear;

  &-title {
    font-family: 'Lato', sans-serif;
    text-align: center;
  }

}
</style>