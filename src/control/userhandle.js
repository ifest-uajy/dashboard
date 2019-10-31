import store from '../store/index'
import handle from '../control/apihandle'

async function getCurSession() {
    try {
        let response = await handle.get('/auth/')
        return response.data
    } catch (e) {
        return null
    }
}

export async function reqLogin(to, from, next) {
    const redirectTo = {
        name: 'login',
        replace: true
    }

    if(store.getters['authsys/isLoggedIn']) {
        next()
        return
    }

    let user  = await getCurSession()
    if(user) {
        store.commit('authsys/setUser', user)
        next()
        return
    }
}