import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Axios from "axios";
import VueCookies from "vue-cookies";
import store from "./store";
import vuetify from "./plugins/vuetify";

Vue.use(VueCookies);

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!store.state.isAuthenticated) {
      next({
        name: "Login",
        query: { redirect: to.fullPath },
      });
    } else {
      next();
    }
  } else {
    next();
  }
});
Vue.config.productionTip = false;
store.dispatch("checkAuth").then(() => {
  new Vue({
    router,
    store,
    vuetify,
    render: (h) => h(App),
  }).$mount("#app");
});
if (Axios.defaults?.headers) {
  Axios.defaults.headers["Content-Type"] = "application/json";
} else {
  Axios.defaults.headers = { "Content-Type": "application/json" };
}
