<template>
  <v-card class="mx-auto">
    <v-card-title> {{ trend.title }} </v-card-title>
    <v-card-subtitle> {{ trend.date }}</v-card-subtitle>
    <v-card-actions>
      <v-btn
        color="primary"
        text
        :to="{ name: 'TrendNews', params: { id: trend.id } }"
      >
        Перейти к новостям
      </v-btn>
      <v-spacer />
      <v-btn
        icon
        color="warning"
        @click="favoriteTrend"
        :loading="settingFavoriteTrendFor.includes(trend.id)"
      >
        <v-icon>{{ trend.favorite ? "mdi-star" : "mdi-star-outline" }}</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import Vue, { PropType } from "vue";
import { Trend } from "@/store/types";
import { mapActions, mapState } from "vuex";

export default Vue.extend({
  props: {
    trend: {
      type: Object as PropType<Trend>,
      required: true,
    },
  },
  computed: {
    ...mapState(["settingFavoriteTrendFor"]),
  },
  methods: {
    ...mapActions(["setFavoriteTrend"]),
    async favoriteTrend() {
      const result = await this.setFavoriteTrend(this.trend.id);
      if (result) this.trend.favorite = !this.trend.favorite;
    },
  },
});
</script>

<style>
</style>