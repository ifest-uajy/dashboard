import handle from '../control/apihandle'

export default {

    namespaced: true,
    state: {
        competitions: [],
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
        setCompetitions(state, m) {
            state.competitions = m
        },
        resetCompetitions(state) {
            state.competitions = []
        }
    },
    actions: {
        async getCompetition({ commit }) {
            try {
                commit('setLoading', true)
                commit('resetError')
                let req = await handle.get('/hackathon/')
                commit('setCompetitions', req.data)
            } catch (e) {
                commit('setError', e)
            } finally {
                commit('setLoading', false)
            }
        },
    }

}