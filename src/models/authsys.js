import handle from '../control/apihandle'

export default {

    namespaced: true,
    state: {
        user: null,
        errors: [],
        loading: false,
        redirectTo: null,
        message: [],
    },
    getters: {
        isLoggedIn(state) {
            return !!state.user
        }
    },
    mutations: {
        setError(state, e) {
            state.errors = e
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
        },
        setMessage(state, m) {
            state.message = m
        },
        resetMessage(state) {
            state.message = ""
        }
    },
    actions: {
        async login({ commit }, { email, password, router }) {
            try {
                //console.log("HELL")
                commit('setLoading', true)
                commit('resetError')
                let response = await handle.post( '/auth/login/', { email, password })
                commit('setUser', response.data)
                let redirectTo = this.loginRedirect
                if (!redirectTo) redirectTo = { name: 'dashboard' }
                router.push(redirectTo)
            } catch (e) {
                if(e.response.data.message) {
                    console.log(e.response.data)
                    commit('setError', e.response.data)
                } else {
                    commit('setError', e)
                }
            } finally {
                commit('setLoading', false)
            }
        },
        async clear({ commit }) {
            commit('resetError')
            commit('resetMessage')
        },
        async register({commit}, {full_name, email, password}) {
            try {
                commit('setLoading', true)
                commit('resetError')
                commit('resetMessage')
                let response = await handle.post('/auth/register/', {full_name, email, password})
                if(response.status == 201) {
                    console.log(response.data)
                    commit('setMessage', response.data)
                }
            } catch (e) {
                if(e.response.data) {
                    console.log(e.response.data)
                    commit('setError', e.response.data)
                } else {
                    commit('setError', e)
                }
            } finally {
                commit('setLoading', false)
            }
        },
        async logout({ commit }) {
            try {
                commit('setLoading', true)
                commit('resetError')
                await handle.post('/auth/logout/', null)
                commit('setUser', null)
                location.reload(true)
            } catch (e) {
                commit('setError', e)
            } finally {
                commit('setLoading', false)
            }
        }
    }

}