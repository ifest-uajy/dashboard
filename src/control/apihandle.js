import axios from 'axios'
import Cookies from 'js-cookie'

const handle = axios.create({
    baseURL: '/api',
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': Cookies.get('csrftoken')
    }
})

handle.interceptors.request.use(function (config) {
    // Do something before request is sent
    //console.log(config)
    return config;
}, function (error) {
    // Do something with request error
    return Promise.reject(error);
});

export default handle;