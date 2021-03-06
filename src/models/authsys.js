import handle from "../control/apihandle";

export default {
  namespaced: true,
  state: {
    user: null,
    errors: [],
    loading: false,
    redirectTo: null,
    message: [],
    success: false
  },
  getters: {
    isLoggedIn(state) {
      return !!state.user;
    }
  },
  mutations: {
    setSuccess(state) {
      state.success = true;
    },
    resetSuccess(state) {
      state.success = false;
    },
    setError(state, e) {
      state.errors = e;
    },
    resetError(state) {
      state.errors = [];
    },
    setLoading(state, load) {
      state.loading = load;
    },
    setUser(state, user) {
      state.user = user;
    },
    setRedirectTo(state, redirectTo) {
      state.redirectTo = redirectTo;
    },
    setMessage(state, m) {
      state.message = m;
    },
    resetMessage(state) {
      state.message = "";
    }
  },
  actions: {
    async login({ commit }, { email, password, router }) {
      try {
        commit("setLoading", true);
        commit("resetError");
        let response = await handle.post("/auth/login/", { email, password });
        commit("setUser", response.data);
        let redirectTo = this.loginRedirect;
        if (!redirectTo) redirectTo = { name: "dashboard" };
        router.push(redirectTo);
        location.reload(true);
      } catch (e) {
        if (e.response.data.message) {
          console.log(e.response.data);
          commit("setError", e.response.data);
        } else {
          commit("setError", e);
        }
      } finally {
        commit("setLoading", false);
      }
    },
    async clear({ commit }) {
      commit("resetError");
      commit("resetMessage");
    },
    async getCurrentSession({ commit }) {
      let response = await handle.get("/auth/");
      commit("setUser", response.data);
    },
    async register({ commit }, { full_name, email, password }) {
      try {
        commit("setLoading", true);
        commit("resetError");
        commit("resetMessage");
        let response = await handle.post("/auth/register/", {
          full_name,
          email,
          password
        });
        if (response.status == 201) {
          console.log(response.data);
          commit("setMessage", response.data);
        }
      } catch (e) {
        if (e.response.data) {
          console.log(e.response.data);
          commit("setError", e.response.data);
        } else {
          commit("setError", e);
        }
      } finally {
        commit("setLoading", false);
      }
    },
    async logout({ commit }) {
      try {
        commit("setLoading", true);
        commit("resetError");
        await handle.post("/auth/logout/", null);
        commit("setUser", null);
        location.reload(true);
      } catch (e) {
        commit("setError", e);
      } finally {
        commit("setLoading", false);
      }
    },
    async confirm({ commit }, { token }) {
      try {
        commit("setLoading", true);
        commit("resetError");
        commit("resetMessage");
        let response = await handle.post("/auth/confirm/", { token });
        if (response.status == 202) {
          console.log(response.data);
          commit("setMessage", response.data);
        }
      } catch (e) {
        if (e.response.data) {
          console.log(e.response.data);
          commit("setError", e.response.data);
        } else {
          commit("setError", e);
        }
      } finally {
        commit("setLoading", false);
      }
    },
    async reset({ commit }, { email }) {
      try {
        commit("setLoading", true);
        console.log("BABAA");
        commit("resetError");
        commit("resetMessage");
        let response = await handle.post("/auth/reset/", { email });
        if (response.status == 200) {
          console.log(response.data);
          commit("setMessage", response.data);
        }
      } catch (e) {
        if (e.response.data) {
          console.log(e.response.data);
          commit("setError", e.response.data);
        } else {
          commit("setError", e);
        }
      } finally {
        commit("setLoading", false);
      }
    },
    async checkTokenReset({ commit }, { token }) {
      try {
        commit("setLoading", true);
        console.log("BABAA");
        commit("resetError");
        commit("resetMessage");
        let response = await handle.post("/auth/reset/check/", { token });
        if (response.status == 200) {
          console.log(response.data);
          //commit('setMessage', response.data)
        }
      } catch (e) {
        if (e.response.data) {
          console.log(e.response.data);
          commit("setError", e.response.data);
        } else {
          commit("setError", e);
        }
      } finally {
        commit("setLoading", false);
      }
    },
    async resetPassword({ commit }, { token, new_password }) {
      try {
        commit("setLoading", true);
        commit("resetError");
        commit("resetMessage");
        let response = await handle.post("/auth/reset/confirm/", {
          token,
          new_password
        });
        if (response.status == 200) {
          console.log(response.data);
          commit("setMessage", response.data);
        }
      } catch (e) {
        if (e.response.data) {
          console.log(e.response.data);
          commit("setError", e.response.data);
        } else {
          commit("setError", e);
        }
      } finally {
        commit("setLoading", false);
      }
    },
    async updateProfile(
      { commit },
      {
        full_name,
        id_line,
        nomor_telepon,
        alamat,
        nomor_id,
        tanggal_lahir
      }
    ) {
      try {
        commit("setLoading", true);
        commit("resetError");
        commit("resetSuccess");
        commit("resetMessage");
        let response = await handle.post("/auth/profile/update/", {
          full_name,
          id_line,
          nomor_telepon,
          alamat,
          nomor_id,
          tanggal_lahir
        });
        if (response.status == 200) {
          commit("setSuccess");
          commit("setMessage", response.data);
          let response2 = await handle.get("/auth/");
          commit("setUser", response2.data);
        }
      } catch (e) {
        if (e.response.data) {
          commit("setError", e.response.data);
        } else {
          commit("setError", e);
        }
      } finally {
        commit("setLoading", false);
      }
    },
    async resend({ commit }, { email }) {
      try {
        commit("setLoading", true);
        commit("resetError");
        commit("resetMessage");
        let response = await handle.post("/auth/confirm/resend/", { email });
        if (response.status == 200) {
          //console.log(response.data);
          commit("setMessage", response.data);
        }
      } catch (e) {
        if (e.response.data) {
          //console.log(e.response.data);
          commit("setError", e.response.data);
        } else {
          commit("setError", e);
        }
      } finally {
        commit("setLoading", false);
      }
    },
    async changePassword({ commit }, { password, new_password }) {
      try {
        commit("setLoading", true);
        commit("resetError");
        commit("resetMessage");
        let response = await handle.post("/auth/change-password/", {
          password,
          new_password
        });
        commit("setMessage", response.data);
      } catch (e) {
        if (e.response.data) {
          commit("setError", e.response.data);
        } else {
          commit("setError", e);
        }
      } finally {
        commit("setLoading", false);
      }
    }
  }
};
