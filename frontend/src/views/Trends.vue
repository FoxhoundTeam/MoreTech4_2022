<template>
  <v-container fluid>
    <v-row>
      <v-col cols="4">
        <recommendation-settings @onSave="getRelevantTrends" />
      </v-col>
      <v-col cols="6">
        <div v-if="loadingRelevantTrends">
          <v-row
            ><v-col><trend-skeleton-card :mostRelevant="true" /></v-col
          ></v-row>
          <v-row
            ><v-col><trend-skeleton-card :mostRelevant="true" /></v-col
          ></v-row>
        </div>

        <v-row
          v-for="relevantTrend in relevantTrends"
          :key="`relevantTrend-${relevantTrend.id}`"
          ><v-col>
            <trend-card :trend="relevantTrend" :mostRelevant="true" /></v-col
        ></v-row>
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
import TrendSkeletonCard from "@/components/cards/TrendSkeletonCard.vue";
import RecommendationSettings from "@/components/forms/RecommendationSettings.vue";
import Vue from "vue";
import { mapActions, mapState } from "vuex";
export default Vue.extend({
  components: { RecommendationSettings, TrendSkeletonCard, TrendCard },
  computed: {
    ...mapState([
      "relevantTrends",
      "trends",
      "loadingRelevantTrends",
      "loadingTrends",
    ]),
  },
  methods: {
    ...mapActions(["getTrends", "getRelevantTrends"]),
  },
  async mounted() {
    if (!this.relevantTrends.length) await this.getRelevantTrends();
  },
});
</script>
<style>
</style>