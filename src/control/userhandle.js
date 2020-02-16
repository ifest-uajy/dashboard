import store from "../store/index";
import handle from "../control/apihandle";

async function getCurSession() {
  try {
    let response = await handle.get("/auth/");
    return response.data;
  } catch (e) {
    return null;
  }
}

export async function reqLogin(to, from, next) {
  // Will redirect here if not logged in
  const redirectTo = { name: "login", replace: true };

  // If we are logged in according to the store state, allow navigation
  // (cases where the cookie is invalid even though the store state says we're logged in
  // will be handled by the API call error handler)
  if (store.getters["authsys/isLoggedIn"]) {
    next();
    return;
  }

  // If user state is empty, try checking the current session from API
  // (perhaps we still have a valid cookie?)
  let user = await getCurSession();
  if (user) {
    store.commit("authsys/setUser", user);
    next();
    return;
  }

  // We don't have a valid cookie, redirect to login
  if (to.name !== redirectTo.name) {
    store.commit("authsys/setRedirectTo", to);
  }
  next(redirectTo);
}

export async function reqAnonymous(to, from, next) {
  // Will redirect here if logged in
  const redirectTo = { name: "dashboard" };

  // If we are logged in according to store state, redirect
  if (store.getters["authsys/isLoggedIn"]) {
    next(redirectTo);
    return;
  }

  // If user state is empty, try checking the current session from API
  // (perhaps we still have a valid cookie?)
  let user = await getCurSession();
  if (user) {
    store.commit("authsys/setUser", user);
    next(redirectTo);
    return;
  }

  // We are not logged in, allow navigation
  next();
}
