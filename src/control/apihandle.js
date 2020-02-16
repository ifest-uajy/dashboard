import axios from "axios";
import Cookies from "js-cookie";

const handle = axios.create({
  baseURL: "/api",
  timeout: 5000,
  headers: {
    "Content-Type": "application/json", // Always use json content type for every requests
    "Cache-Control": "no-cache", // Prevent browser from using cached version of each requests
    "X-CSRFToken": Cookies.get("csrftoken") // Always provide csrf token for each POST/PUT requests
  }
});

handle.interceptors.request.use(
  function(config) {
    // Do something before request is sent
    //console.log(config)
    return config;
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

export default handle;
