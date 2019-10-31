<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">
                        Registrasi Peserta
                    </div>
                    <div class="card-body">
                        <form @submit="formSubmit">
                            <strong>Nama :</strong>
                            <input type="text" class="form-control" v-model="full_name">
                            <strong>Alamat email :</strong>
                            <input type="text" class="form-control" v-model="email">
                            <strong>Password :</strong>
                            <input type="password" class="form-control" v-model="password">
                            <button class="btn btn-success">Submit</button>
                        </form>
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
export default {
        name: 'Registration',
        mounted() {
            console.log('Component mounted.')
        },
        data() {
            return {
                full_name: '',
                email: '',
                password: '',
                output: ''
            };
        },
        methods: {
            formSubmit(e) {
                e.preventDefault();
                let curObj = this;
                this.axios.post(
                    '/api/auth/register/',
                    {
                        full_name: this.full_name,
                        email: this.email,
                        password: this.password
                    }
                )
                .then(function (response) {
                    curObj.output = response.data;
                })
                .catch(function (error) {
                    curObj.output = error;
                })
            }
        }
    }
</script>