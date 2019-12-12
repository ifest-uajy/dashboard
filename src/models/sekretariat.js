import handle from '../control/apihandle'

export default {

    namespaced: true,
    state: {
        competitionDetail: [],
        competitionList: [],
        slugDetail: [],
        loading: false,
        loading2: false,
        message: [],
    },
    mutations: {
        setSlugDetail(state, m) {
            state.slugDetail = m
        },
        resetSlugDetail(state) {
            state.slugDetail = []
        },
        setSuccess(state) {
            state.success = true
        },
        resetSuccess(state) {
            state.success = false
        },
        setCompetitionList(state, m) {
            state.competitionList = m
        },
        setCompetitionDetail(state, m) {
            state.competitionDetail = m
        },
        resetCompetitionList(state) {
            state.competitionList = []
        },
        resetCompetitionDetail(state) {
            state.competitionDetail = []
        },
        setLoading(state, load) {
            state.loading = load
        },
        setLoading2(state, load) {
            state.loading2 = load
        },
        setMessage(state, m) {
            state.message = m
        },
        resetMessage(state) {
            state.message = ""
        }
    },
    actions: {
        async getCompetitionList( { commit }, { slug_name } ) {
            try {
                commit('setLoading', true)
                let response = await handle.get(
                    '/hackathon/admin/team/list/' + slug_name + '/'
                )
                commit('setCompetitionList', response.data)
            } catch (e) {
                
            } finally {
                commit('setLoading', false)
            }
        },
        async clear({commit}) {
            commit('resetCompetitionList')
            commit('resetCompetitionDetail')
        },
        async getCompetitionDetail( {commit}, {id} ) {
            try {
                commit('setLoading', true)
                let response = await handle.get(
                    '/hackathon/admin/detail/' + id + '/'
                )
                commit('setCompetitionDetail', response.data)
            } catch (e) {
                console.log(e)
            } finally {
                commit('setLoading', false)
            }
        },
        async getSlugDetail( {commit}, {slug_name} ) {
            try {
                commit('setLoading', true)
                let response = await handle.get(
                    '/hackathon/admin/team/slug-detail/' + slug_name + '/'
                )
                commit('setSlugDetail', response.data)
            } catch (e) {
                console.log(e)
            } finally {
                commit('setLoading', false)
            }
        },
        async confirmTeam({commit}, {task_res_id, tolak}) {
            try {
                commit('resetMessage')
                commit('setLoading2', true)
                let response = await handle.post(
                    '/hackathon/admin/task/handler/', {task_res_id, tolak}
                )
                commit('setMessage', response.data)
            } catch (e) {
                commit('setMessage', e.response.data)
            } finally {
                commit('setLoading', false)
            }
        }
    }
}