import handle from '../control/apihandle'

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
        async login({ commit }, { email, password, router }) {
            try {
                console.log("HELL")
                commit('setLoading', true)
                commit('resetError')
                let response = await handle.post( '/auth/login/', { email, password })
                commit('setUser', response.data)
                let redirectTo = this.loginRedirect
                if (!redirectTo) redirectTo = { name: 'dashboard' }
                router.push(redirectTo)
            } catch (e) {
                commit('setError', e)
            } finally {
                commit('setLoading', false)
            }
        },
        async clear({ commit }) {
            commit('resetError')
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