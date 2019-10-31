<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">
                        Registrasi Peserta
                    </div>
                    <div class="card-body">
                        <v-form class="mt-3" @submit.prevent="login">
                        <v-text-field v-model="email" label="Email" type="email" autocomplete="email" required></v-text-field>
                        <v-text-field v-model="password" label="Password" type="password" autocomplete="current-password" required></v-text-field>
                        <v-alert v-for="error in errors" :key="error" :value="true" type="error" outline>
                            {{ error }}
                        </v-alert>
                        <v-btn
                            large
                            block
                            color="primary"
                            type="submit"
                            :loading="loading"
                            :disabled="loading"
                        >
                            Login
                        </v-btn>
                        </v-form>
                    </div>
                    <div>
                        {{output}}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    data: () => ({
        email: '',
        password: ''
    }),
    computed: {
        ...mapState({
            errors: state => state.authsys.errors,
            loading: state=> state.authsys.loading
        })
    },
    methods: {
        ...mapActions({
            loginAction: 'authsys/login',
            clear: 'authsys/clear'
        }),

        login() {
            this.loginAction({
                email: this.email,
                password: this.password,
                router: this.$router
            })
        }
    },
    beforeRouteLeave(to, from, next) {
        this.clear()
        next()
    }
}
</script>