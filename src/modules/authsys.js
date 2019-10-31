export default {

    namespaced: true,
    state: {
        user: null,
        errors: [],
        loading: false,
        redirectTo: null
    },
    getters: {
        isLoggedIn(state) {
            return !!state.user
        }
    },
    mutations: {
        setError(state, e) {
            state.errors.push(e + '')
        },
        resetError(state) {
            state.errors = []
        },
        setLoading(state, load) {
            state.loading = load
        },
        setUser(state, user) {
            state.user = user
        },
        setRedirectTo(state, redirectTo) {
            state.redirectTo = redirectTo
        }
    },
    actions: {
        async login({commit}, {email, password, router}) {
            try {
                commit('setLoading', true)
                commit('resetError')
                let response = await this.axios.post(
                    'localhost:8000/api/auth/login/',
                    {
                        email: this.email,
                        password: this.password
                    }
                )
                commit('setUser', response.data)

            } catch (e) {
                if(e.response.data) {
                    commit('setError', e.response.data)
                } else {
                    commit('setError', e)
                }
            } finally {
                commit('setLoading', false)
            }
        },
        async clear({commit}) {
            commit('resetError')
        }
    }

}