<template>
  <v-card :class="cardClass">
    <v-card-actions>
      <v-btn icon disabled color="warning">
        <v-icon>mdi-star-outline</v-icon>
      </v-btn>
    </v-card-actions>
    <v-skeleton-loader type="card-heading" />
    <v-card-text>
      <v-chip-group>
        <v-skeleton-loader type="chip" class="mr-2" />
        <v-skeleton-loader type="chip" class="mr-2" />
        <v-skeleton-loader type="chip" class="mr-2" />
      </v-chip-group>
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  props: {
    mostRelevant: {
      type: Boolean,
      required: false,
      default: () => false,
    },
  },
  computed: {
    cardClass(): string[] {
      let cardClass = ["mx-auto"];
      if (this.mostRelevant) {
        cardClass = [...cardClass, "border", "border-success"];
      }      
      return cardClass;
    },
  },
});
</script>

<style>
</style>