import handle from '../control/apihandle'

export default {

    namespaced: true,
    state: {
        competitions: [],
        isLoading: false,
        errors: [],
        competitionsCount: 0
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
        },
        setCompetitionsCount(state, c) {
            state.competitionsCount = c
        },
        resetCompetitionsCount(state) {
            state.competitionsCount = 0
        }
    },
    actions: {
        async getCompetition({ commit }) {
            try {
                commit('setLoading', true)
                commit('resetCompetitionsCount')
                commit('resetError')
                let req = await handle.get('/hackathon/')
                commit('setCompetitions', req.data)
                commit('setCompetitionsCount', req.data.length)
            } catch (e) {
                commit('setError', e)
            } finally {
                commit('setLoading', false)
            }
        },
    }

}