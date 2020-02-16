<template>
    <v-app id="main" style="background: #fff">
        <v-content class="content">
            <router-view />
        </v-content>
        <Footer />
    </v-app>
</template>

<script>
import Footer from "./components/Footer";

export default {
    name: 'App',
    data () {
        return {
            title: 'Informatics Festival (IFest) #8'
        }
    },
    components: {
        Footer
    }
}
</script>

<style scoped>
#main {
    clear: both;
}
</style>