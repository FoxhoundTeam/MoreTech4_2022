<template>
  <v-container>
    <h1>Новости {{ $route.name == "TrendNews" ? "тренда" : "дайджеста" }}</h1>
    <v-row v-if="loading"
      ><v-col><news-skeleton-card /></v-col
    ></v-row>
    <v-row v-for="news in localNews" :key="news.id">
      <v-col>
        <news-card :news="news" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import http from "@/http";
import { News } from "@/store/types";
import NewsCard from "@/components/cards/NewsCard.vue";
import NewsSkeletonCard from "@/components/cards/NewsSkeletonCard.vue";

const routePrefixMap = {
  TrendNews: "/api/trend/",
  DigestNews: "/api/digest/",
} as Record<string, string>;

export default Vue.extend({
  components: { NewsCard, NewsSkeletonCard },
  data() {
    return {
      localNews: [] as News[],
      loading: false,
    };
  },
  async mounted() {
    this.loading = true;
    const entityId = this.$route.params.id;
    const urlPrefix = routePrefixMap[this.$route.name as string];
    const response = await http.getList<News[]>(
      urlPrefix + `${entityId}/news/`
    );
    if (response.status == 200) this.localNews = response.data;
    this.loading = false;
  },
});
</script>

<style>
</style>