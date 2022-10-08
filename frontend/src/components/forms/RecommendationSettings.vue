<template>
  <v-card elevation="0">
    <v-card-title>Настройки рекомендаций</v-card-title>
    <v-container fluid>
      <v-form v-model="valid">
        <v-text-field
          type="number"
          label="Количество релевантных дайджестов"
          v-model="relevantDigestsCount"
          :rules="[rules.required, rules.relevantDigestsCountValidator]"
        />
        <v-autocomplete
          v-model="userInterestingThemes"
          :items="interestingThemes"
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
import { required, relevantDigestsCountValidator } from "@/validators";

export default Vue.extend({
  data() {
    return {
      keywords: [],
      userInterestingThemes: [],
      relevantDigestsCount: 0,
      loading: false,
      valid: false,
      rules: { required, relevantDigestsCountValidator },
    };
  },
  computed: {
    ...mapState(["user", "interestingThemes"]),
  },
  async beforeMount() {
    if (!this.interestingThemes.length) await this.getInterestingThemes();
    this.keywords = [...this.user.keywords] as never[];
    this.userInterestingThemes = [...this.user.interestingThemes] as never[];
    this.relevantDigestsCount = this.user.relevantDigestsCount;
  },
  methods: {
    ...mapActions(["updateUserInfo", "getInterestingThemes"]),
    async save(): Promise<void> {
      this.loading = true;
      await this.updateUserInfo({
        keywords: this.keywords,
        interestingThemes: this.userInterestingThemes,
        relevantDigestsCount: this.relevantDigestsCount,
      });
      this.loading = false;
      this.$emit("onSave");
    },
  },
});
</script>

<style>
</style>