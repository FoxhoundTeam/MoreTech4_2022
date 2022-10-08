<template>
  <v-card elevation="0">
    <v-card-title>Настройки рекомендаций</v-card-title>
    <v-container fluid>
      <v-form v-model="valid">
        <v-text-field
          type="number"
          label="Количество релевантных новостей"
          v-model="relevantTrendsCount"
          :rules="[rules.required, rules.relevantTrendsCountValidator]"
        />
        <v-autocomplete
          v-model="userInterestingTrends"
          :items="interestingTrends"
          label="Темы"
          multiple
          chips
          deletable-chips
          item-text="name"
          return-object
        ></v-autocomplete>
        <v-combobox
          v-model="keywords"
          label="Ключевые слова"
          multiple
          chips
          deletable-chips
        ></v-combobox>
        <v-btn
          :loading="loading"
          @click="save"
          :disabled="!valid"
          block
          color="primary"
          >Сохранить</v-btn
        >
      </v-form>
    </v-container>
  </v-card>
</template>

<script lang="ts">
import Vue from "vue";
import { mapActions, mapState } from "vuex";
import { required, relevantTrendsCountValidator } from "@/validators";

export default Vue.extend({
  data() {
    return {
      keywords: [],
      userInterestingTrends: [],
      relevantTrendsCount: 0,
      loading: false,
      valid: false,
      rules: { required, relevantTrendsCountValidator },
    };
  },
  computed: {
    ...mapState(["user", "interestingTrends"]),
  },
  async beforeMount() {
    if (!this.interestingTrends.length) await this.getInterestingTrends();
    this.keywords = [...this.user.keywords] as never[];
    this.userInterestingTrends = [...this.user.interestingTrends] as never[];
    this.relevantTrendsCount = this.user.relevantTrendsCount;
  },
  methods: {
    ...mapActions(["updateUserInfo", "getInterestingTrends"]),
    async save(): Promise<void> {
      this.loading = true;
      await this.updateUserInfo({
        keywords: this.keywords,
        interestingTrends: this.userInterestingTrends,
        relevantTrendsCount: this.relevantTrendsCount,
      });
      this.loading = false;
      this.$emit("onSave");
    },
  },
});
</script>

<style>
</style>