import handle from '../control/apihandle'

export default {

    namespaced: true,
    state: {
        isLoading: false,
        errors: [],
        messages: [],
    },
    mutations: {
        setErrors(state, e) {
            state.errors = e
        },
        resetErrors(state) {
            state.errors = []
        },
        setLoading(state, load) {
            state.loading = load
        },
        setMessages(state, m) {
            state.messages = m
        },
        resetMessages(state) {
            state.messages = []
        },
    },
    actions: {
        async send({ commit }, {
            nama_pengirim, email_pengirim, pesan
        }) {
            try {
                commit('setLoading', true)
                commit('resetErrors')
                commit('resetMessages')
                let req = await handle.post('/message/send/',
                    {
                        nama_pengirim,
                        email_pengirim,
                        pesan
                    }
                )
                if (req.status === 200) {
                    commit('setMessages', req.data)
                }
            } catch (e) {
                commit('setErrors', e.response.data)
            } finally {
                commit('setLoading', false)
            }
        },
    }

}