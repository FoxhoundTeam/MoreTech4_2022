<template>
  <v-card class="mx-auto border border-success">
    <v-skeleton-loader type="card-heading" />
    <v-card-text>
      <v-chip-group>
        <v-skeleton-loader type="chip" class="mr-2" />
        <v-skeleton-loader type="chip" class="mr-2" />
        <v-skeleton-loader type="chip" class="mr-2" />
      </v-chip-group>
    </v-card-text>
    <v-card-actions>
      <v-skeleton-loader type="button" />
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({});
</script>

<style>
</style>