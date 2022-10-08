<template>
  <v-container>
    <v-row class="mt-5">
      <v-col cols="12"><h1>FoxNews</h1></v-col>
    </v-row>
    <v-row>
      <v-col class="my-1" sm="7" order-sm="1" order="12">
        <v-img class="w-50" :src="hackLogo"></v-img>
        <h3 class="mt-2">Агрегатор новостей</h3></v-col
      >
      <v-col class="my-1" order-sm="12" order="1" sm="5">
        <login v-if="$route.name == 'Login'" />
        <register v-if="$route.name == 'Register'" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Register from "@/components/forms/Register.vue";
import Login from "@/components/forms/Login.vue";
import Vue from "vue";
export default Vue.extend({
  components: { Register, Login },
  data() {
    return {
      hackLogo: require("@/assets/hackLogo.jpg"),
    };
  },
});
</script>

<style>
.temp {
  width: 80px;
}
</style>