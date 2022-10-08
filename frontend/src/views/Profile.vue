<template>
  <v-card title="Профиль">
    <v-card-title>Профиль</v-card-title>
    <v-container fluid>
      <v-row>
        <v-col cols="6"><profile-settings /></v-col>
        <v-col cols="6"><recommendation-settings /></v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import ProfileSettings from "@/components/forms/ProfileSettings.vue";
import RecommendationSettings from "@/components/forms/RecommendationSettings.vue";
import Vue from "vue";
export default Vue.extend({
  components: { RecommendationSettings, ProfileSettings },
});
</script>

<style>
</style>