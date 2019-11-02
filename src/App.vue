<template>
    <v-app>
        <v-content>
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
            title: 'Informatics Festival 8'
        }
    },
    components: {
        Footer
    }
}
</script>