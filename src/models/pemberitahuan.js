import handle from '../control/apihandle'

export default {

    namespaced: true,
    state: {
        anouncements: [],
        isLoading: false,
        errors: []
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
        setAnnouncement(state, m) {
            state.anouncements = m
        },
        resetAnnouncement(state) {
            state.anouncements = []
        }
    },
    actions: {
        async getPemberitahuan({ commit }) {
            try {
                commit('setLoading', true)
                commit('resetError')
                let req = await handle.get('/announcement/')
                commit('setAnnouncement', req.data)
            } catch (e) {
                commit('setError', e)
            } finally {
                commit('setLoading', false)
            }
        },
    }

}