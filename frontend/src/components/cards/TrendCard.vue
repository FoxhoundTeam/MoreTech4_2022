<template>
  <v-card :class="cardClass">
    <v-card-actions>
      <v-btn
        icon
        color="warning"
        @click="favoriteTrend"
        :loading="settingFavoriteTrendFor.includes(trend.id)"
      >
        <v-icon>{{ trend.favorite ? "mdi-star" : "mdi-star-outline" }}</v-icon>
      </v-btn>
    </v-card-actions>
    <v-card-title> {{ trend.name }} </v-card-title>
    <v-card-text>
      <v-chip-group>
        <v-chip v-for="link in trend.links" :key="link.id" :href="link.link">
          {{ link.siteName }}
        </v-chip>
      </v-chip-group>
    </v-card-text>
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
    mostRelevant: {
      type: Boolean,
      required: false,
      default: () => false,
    },
  },
  computed: {
    ...mapState(["settingFavoriteTrendFor"]),
    cardClass(): string[] {
      let cardClass = ["mx-auto"];
      if (this.mostRelevant) {
        cardClass = [...cardClass, "border", "border-success"];
      }
      return cardClass;
    },
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