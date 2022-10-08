<template>
  <v-container fluid>
    <v-row>
      <v-col cols="4">
        <recommendation-settings @onSave="getDigests" />
        <v-slider v-model="day" step="3" min="0" max="30"></v-slider>
      </v-col>
      <v-col cols="6">
        <h2>Дайджесты</h2>
        <v-divider />
        <div v-if="loadingDigests">
          <v-row
            ><v-col><digest-skeleton-card /></v-col
          ></v-row>
          <v-row
            ><v-col><digest-skeleton-card /></v-col
          ></v-row>
        </div>
        <v-row v-for="digest in digests" :key="`digest-${digest.id}`"
          ><v-col> <digest-card :digest="digest" /></v-col
        ></v-row>
        <h2 class="mt-5">Тренды</h2>
        <v-divider />
        <v-row v-for="trend in trends.items" :key="`trend-${trend.id}`"
          ><v-col> <trend-card :trend="trend" /></v-col
        ></v-row>
        <div v-if="trends.next" v-intersect="getTrends">
          <v-row
            ><v-col><trend-skeleton-card /></v-col
          ></v-row>
          <v-row
            ><v-col><trend-skeleton-card /></v-col
          ></v-row>
          <v-row
            ><v-col><trend-skeleton-card /></v-col
          ></v-row>
        </div>
      </v-col>
      <v-col cols="2">&nbsp;</v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import TrendCard from "@/components/cards/TrendCard.vue";
import DigestCard from "@/components/cards/DigestCard.vue";
import TrendSkeletonCard from "@/components/cards/TrendSkeletonCard.vue";
import DigestSkeletonCard from "@/components/cards/DigestSkeletonCard.vue";
import RecommendationSettings from "@/components/forms/RecommendationSettings.vue";
import Vue from "vue";
import { mapActions, mapState } from "vuex";
export default Vue.extend({
  components: {
    RecommendationSettings,
    TrendSkeletonCard,
    DigestSkeletonCard,
    TrendCard,
    DigestCard,
  },
  data() {
    return {
      day: 0,
    };
  },
  computed: {
    ...mapState(["digests", "trends", "loadingDigests", "loadingTrends"]),
  },
  methods: {
    ...mapActions(["getTrends", "getDigests"]),
  },
  watch: {
    async day() {
      await this.getTrends({ page: 1, day: this.day });
    },
  },
  async mounted() {
    if (!this.digests.length) await this.getDigests();
    if (!this.trends.items.length) await this.getTrends();
  },
});
</script>
<style>
</style>