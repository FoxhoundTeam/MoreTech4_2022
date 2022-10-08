<template>
  <v-app-bar app>
    <v-app-bar-title
      ><router-link
        :to="{ name: 'News' }"
        class="text-decoration-none text-dark text-no-wrap"
        >FoxDigests</router-link
      ></v-app-bar-title
    >
    <v-spacer></v-spacer>
    <v-btn
      v-if="!isAuthenticated && $route.name != 'Register'"
      class="mr-4"
      outlined
      color="primary"
      :to="{ name: 'Register' }"
      >Зарегистрироваться</v-btn
    >
    <v-btn
      v-if="!isAuthenticated && $route.name != 'Login'"
      color="primary"
      :to="{ name: 'Login' }"
      >Войти</v-btn
    >
    <div v-if="isAuthenticated">
      <v-menu open-on-hover bottom offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn text class="text-dark" dark v-bind="attrs" v-on="on"
            ><v-icon left dark> mdi-account </v-icon>
            {{ user.email }}
          </v-btn>
        </template>
        <v-list>
          <v-list-item link :to="{ name: 'Profile' }">
            <v-list-item-title>Профиль</v-list-item-title>
          </v-list-item>
          <v-list-item link :to="{ name: 'FavoriteTrends' }">
            <v-list-item-title>Избранное</v-list-item-title>
          </v-list-item>
          <v-list-item link>
            <v-list-item-title @click="logout">Выйти</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
  </v-app-bar>
</template>

<script lang="ts">
import Vue from "vue";
import { mapActions, mapState } from "vuex";

export default Vue.extend({
  data() {
    return {};
  },
  computed: {
    ...mapState(["user", "isAuthenticated"]),
  },
  methods: {
    async logout() {
      await this.logoutDispatch();
      location.reload();
    },
    ...mapActions({
      logoutDispatch: "logout",
    }),
  },
});
</script>

<style>
.v-app-bar-title__content {
  width: 200px !important;
}
</style>