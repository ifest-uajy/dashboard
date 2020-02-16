<template>
  <v-layout pt-12 class="bg-img">
    <!-- /* LOGOUT BUTTON */ -->
    <div @click="logoutActions" class="logout-btn">
      <a>Keluar</a>
    </div>

    <v-container >
      <div class="header-box">
      <img class="circle-top" src="https://dashboard.ifest-uajy.com/assets/atma_jaya5050.png" />
      <img class="circle-top" src="https://dashboard.ifest-uajy.com/assets/himaforka5050.png" />
      <img class="circle-top" src="https://dashboard.ifest-uajy.com/assets/ifest5050.png" />
    </div>
      <v-container>
        <h2 class="judul">Dashboard IFest #8</h2>
        <h1 class="title sub-judul">
          Selamat datang,
          <span class="font-weight-bold">{{user.full_name}}</span>!
        </h1>
      </v-container>
      <div v-if="!isMobile()">
        <v-tabs grow :show-arrows="true">
          <v-tab to="/dashboard">
            <div class="pr-5">
              <v-badge class="mt-2">
                <template v-if="anouncementsCount !== 0" v-slot:badge>{{anouncementsCount}}</template>
                Pengumuman
              </v-badge>
            </div>
          </v-tab>
          <v-tab to="/dashboard/competition">
            <div class="pr-5">
              <v-badge class="mt-2">
                <template v-if="competitionsCount !== 0" v-slot:badge>{{competitionsCount}}</template>
                Kompetisi
              </v-badge>
            </div>
          </v-tab>
          <v-tab to="/dashboard/teams">
            <div class="pr-5">
              <v-badge class="mt-2">
                <template v-if="teamsCount !== 0" v-slot:badge>{{teamsCount}}</template>
                Tim
              </v-badge>
            </div>
          </v-tab>
          <v-tab to="/dashboard/profile">
            <div class="pr-5">
              <v-badge class="mt-2" color="red">
                <template v-if="user.isProfileComplete !== true" v-slot:badge>!</template>
                Profil
              </v-badge>
            </div>
          </v-tab>
        </v-tabs>
      </div>
      <div v-else>
        <div class="bottom-bar">
          <v-bottom-navigation v-model="bottomNav" dark height=75>
            <v-btn to="/dashboard">
              <span>Pengumuman</span>
              <v-icon>mdi-flag</v-icon>
            </v-btn>

            <v-btn to="/dashboard/competition">
              <span>Kompetisi</span>
              <v-icon>mdi-playlist-check</v-icon>
            </v-btn>

            <v-btn to="/dashboard/teams">
              <span>Tim</span>
              <v-icon>mdi-account-group</v-icon>
            </v-btn>

            <v-btn to="/dashboard/profile">
              <span>Profil</span>
              <v-icon>mdi-account</v-icon>
            </v-btn>
          </v-bottom-navigation>
        </div>
      </div>

      <router-view class=""></router-view>
    </v-container>
  </v-layout>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  data: () => ({}),
  beforeMount() {
    if (this.user.is_staff) {
      this.$router.push({ name: "sekret-view" });
    } else {
      console.log("Damn");
      this.getAnouncement();
      this.getCompetition();
      this.getTeams();
    }
  },
  computed: {
    ...mapState({
      user: state => state.authsys.user,
      competitionsCount: state => state.competition.competitionsCount,
      anouncementsCount: state => state.pemberitahuan.announcementsCount,
      teamsCount: state => state.competition.teamsCount
    })
  },

  methods: {
    ...mapActions({
      logoutActions: "authsys/logout",
      getCompetition: "competition/getCompetition",
      getAnouncement: "pemberitahuan/getPemberitahuan",
      getTeams: "competition/getTeams",
      clear: "authsys/clear"
    }),
    isMobile: function() {
      var check = false;
      (function(a) {
        if (
          /(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(
            a
          ) ||
          /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(
            a.substr(0, 4)
          )
        )
          check = true;
      })(navigator.userAgent || navigator.vendor || window.opera);
      return check;
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Amiri&display=swap");
@import url("https://fonts.googleapis.com/css?family=Roboto&display=swap");
.logout-btn {
  position: fixed;
  top: 50px;
  right: 0px;
  padding: 0px;
  margin: 0px;
  cursor: pointer;
  width: 40px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
  height: 100px;
  background: #13355b;
  color: #adadad;
  z-index: 15;
  border-radius: 8px 0px 0px 8px;
}
.logout-btn a {
  margin: auto 10px;
  margin-top: 25px;
  writing-mode: tb-rl;
  color: rgb(119, 170, 241);
  text-decoration: none;
}
.logout-btn a:visited {
  text-decoration: none;
}
.logout-btn:hover {
  background: rgb(13, 34, 65);
}
.bottom-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 75px;
  z-index: 99;
}

.circle-top {
  margin: auto 10px;
  /* padding: 10px; */
  height: 50px;
  width: 50px;
  background: white;
  border-radius: 100%;
}

.judul {
  font-family: "Roboto", sans-serif;  line-height: 1.1em;
  font-size: 30pt;
  color: #0f4c75;
  font-weight: 500;
}

.sub-judul {
font-family: "Roboto", sans-serif;  line-height: 1.1em;
  font-size: 24pt;
  font-weight: 500;
  margin-bottom: 20px;
}

.bg-img {
  width: 100%;
  background: url('https://ifest-uajy.com/assets/email/bg_top2.jpg') no-repeat;
}
</style>