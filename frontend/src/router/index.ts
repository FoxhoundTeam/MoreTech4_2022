import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const opts = {
  routes: [
    {
      path: "/",
      name: "News",
      component: () => import('../views/Trends.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/login",
      name: "Login",
      component: () => import('../views/LoginRegister.vue'),
      meta: {
        requiresAuth: false
      }
    },
    {
      path: "/register",
      name: "Register",
      component: () => import('../views/LoginRegister.vue'),
      meta: {
        requiresAuth: false
      }
    },
    {
      path: "/profile",
      name: "Profile",
      component: () => import('../views/Profile.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/favorites",
      name: "FavoriteTrends",
      component: () => import('../views/FavoriteTrends.vue'),
      meta: {
        requiresAuth: true
      }
    },
  ],
  linkExactActiveClass: 'active'
};
const router = new VueRouter(opts);

export default router
