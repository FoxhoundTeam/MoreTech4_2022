<template>
  <v-card class="mx-auto">
    <v-img v-if="news.urlPreview" :src="news.urlPreview" height="200px"></v-img>

    <v-card-title> {{ news.title }} </v-card-title>

    <v-card-actions>
      <v-btn color="primary" text :href="news.url"> Перейти к новости </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import Vue, { PropType } from "vue";
import { News } from "@/store/types";

export default Vue.extend({
  props: {
    news: {
      type: Object as PropType<News>,
      required: true,
    },
  },
});
</script>

<style>
</style>