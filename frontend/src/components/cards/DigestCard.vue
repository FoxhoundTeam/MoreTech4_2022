<template>
  <v-card class="mx-auto border border-success">
    <v-card-title> {{ digest.title }} </v-card-title>
    <v-card-text>
      <v-chip-group>
        <v-chip v-for="topic in digest.topic" :key="`${topic}-${digest.id}`">
          {{ topic }}
        </v-chip>
      </v-chip-group>
    </v-card-text>
    <v-card-actions>
      <v-btn
        color="primary"
        text
        :to="{ name: 'DigestNews', params: { id: digest.id } }"
      >
        Перейти к новостям
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import Vue, { PropType } from "vue";
import { Digest } from "@/store/types";

export default Vue.extend({
  props: {
    digest: {
      type: Object as PropType<Digest>,
      required: true,
    },
  },
});
</script>

<style>
</style>