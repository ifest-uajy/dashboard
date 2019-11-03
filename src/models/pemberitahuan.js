import handle from '../control/apihandle'

export default {

    namespaced: true,
    state: {
        announcements: [],
        isLoading: false,
        errors: [],
        announcementsCount: 0
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
            state.announcements = m
        },
        resetAnnouncement(state) {
            state.announcements = []
        },
        setAnnouncementCount(state, c) {
            state.announcementsCount = c
        },
        resetAnnouncementCount(state) {
            state.announcementsCount = 0
        }
    },
    actions: {
        async getPemberitahuan({ commit }) {
            try {
                commit('setLoading', true)
                commit('resetAnnouncementCount')
                commit('resetError')
                let req = await handle.get('/announcement/')
                commit('setAnnouncement', req.data)
                commit('setAnnouncementCount', req.data.length)
            } catch (e) {
                commit('setError', e)
            } finally {
                commit('setLoading', false)
            }
        },
    }

}