import handle from "../control/apihandle";

export default {
  namespaced: true,
  state: {
    competitions: [],
    isLoading: false,
    errors: [],
    messages: [],
    competitionsCount: 0,
    teams: [],
    teamsCount: 0
  },
  mutations: {
    setError(state, e) {
      state.errors = e;
    },
    resetError(state) {
      state.errors = [];
    },
    setLoading(state, load) {
      state.isLoading = load;
    },
    setCompetitions(state, m) {
      state.competitions = m;
    },
    resetCompetitions(state) {
      state.competitions = [];
    },
    setCompetitionsCount(state, c) {
      state.competitionsCount = c;
    },
    resetCompetitionsCount(state) {
      state.competitionsCount = 0;
    },
    setteamsCount(state, c) {
      state.teamsCount = c;
    },
    resetteamsCount(state) {
      state.teamsCount = 0;
    },
    setMessage(state, m) {
      state.messages = m;
    },
    resetMessage(state) {
      state.messages = [];
    },
    setTeams(state, m) {
      state.teams = m;
    },
    resetTeams(state) {
      state.teams = [];
    }
  },
  actions: {
    async addMember({commit}, {team_id, full_name, email, id_line, nomor_telepon, nomor_id, tanggal_lahir, alamat}) {
      try {
        commit("setLoading", true);
        commit("resetError");
        let response = await handle.post("hackathon/teams/member/add/", {
          team_id,
          full_name,
          email,
          id_line,
          nomor_telepon,
          nomor_id,
          tanggal_lahir,
          alamat
        });
        if (response.status === 200) {
          commit("setMessage", response.data);
          let req2 = await handle.get("/hackathon/teams/");
          commit("setTeams", req2.data);
          commit("setteamsCount", req2.data.length);
        }
      } catch (e) {
        commit("setError", e.response.data);
      } finally {
        commit("setLoading", false);
      }
    },
    async getCompetition({ commit }) {
      try {
        commit("setLoading", true);
        commit("resetCompetitionsCount");
        commit("resetError");
        let req = await handle.get("/hackathon/");
        commit("setCompetitions", req.data);
        commit("setCompetitionsCount", req.data.length);
      } catch (e) {
        commit("setError", e);
      } finally {
        commit("setLoading", false);
      }
    },
    async clear({ commit }) {
      commit("resetError");
      commit("resetMessage");
    },
    async register(
      { commit },
      {
        slug_name,
        name,
        team_institution,
        alamat_institution,
        nama_pembimbing,
        no_telp_pembimbing
      }
    ) {
      try {
        commit("setLoading", true);
        commit("resetError");
        let response = await handle.post("hackathon/register/", {
          slug_name,
          name,
          team_institution,
          alamat_institution,
          nama_pembimbing,
          no_telp_pembimbing
        });
        if (response.status == 201) {
          //console.log(response.data);
          commit("setMessage", response.data);
          let req2 = await handle.get("/hackathon/teams/");
          commit("setTeams", req2.data);
          commit("setteamsCount", req2.data.length);
        }
      } catch (e) {
        commit("setError", e.response.data);
      } finally {
        commit("setLoading", false);
      }
    },
    async joinTeam({ commit }, { token }) {
      try {
        commit("setLoading", true);
        commit("resetError");
        let response = await handle.post("hackathon/teams/join/", { token });
        //console.log(response.data);
        if (response.status == 201) {
          console.log(response.data);
          commit("setMessage", response.data);
          let req2 = await handle.get("/hackathon/teams/");
          commit("setTeams", req2.data);
          commit("setteamsCount", req2.data.length);
        }
      } catch (e) {
        commit("setError", e.response.data);
      } finally {
        commit("setLoading", false);
      }
    },
    async getTeams({ commit }) {
      try {
        commit("setLoading", true);
        commit("resetteamsCount");
        commit("resetError");
        let req = await handle.get("/hackathon/teams/");
        commit("setTeams", req.data);
        commit("setteamsCount", req.data.length);
      } catch (e) {
        commit("setError", e);
      } finally {
        commit("setLoading", false);
      }
    },
    async postTaskResponse({ commit }, { team_id, task_id, response }) {
      try {
        commit("setLoading", true);
        commit("resetError");
        let resp = await handle.post("/hackathon/teams/task/add/", {
          team_id,
          task_id,
          response
        });
        //console.log(resp.data);
        if (resp.status == 201) {
          //console.log(resp.data);
          commit("setMessage", resp.data);
          let req2 = await handle.get("/hackathon/teams/");
          commit("setTeams", req2.data);
          commit("setteamsCount", req2.data.length);
        }
      } catch (e) {
        commit("setError", e);
      } finally {
        commit("setLoading", false);
      }
    }
  }
};
