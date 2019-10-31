<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">
                        Registrasi Peserta
                    </div>
                  {{errors}}
                    
                    <div class="card-body">
                        <form v-on:submit.prevent="login">

                        <strong>Name:</strong>

                        <input type="text" class="form-control" v-model="email">
                        <input type="text" class="form-control" v-model="password">
    

                        <button class="btn btn-success">Submit</button>

                        </form>
                    </div>
                    <div>
                            
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
    //beforeRouteLeave(to, from, next) {
       // this.clear()
       // next()
    //}
}
</script>