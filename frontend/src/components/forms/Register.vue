<template>
  <v-card elevation="0">
    <v-form v-model="valid">
      <v-text-field
        label="Почта"
        :rules="[rules.required, rules.isEmail]"
        v-model="email"
        validate-on-blur
      ></v-text-field>
      <v-text-field
        v-model="password"
        label="Пароль"
        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
        :rules="[rules.required]"
        :type="showPassword ? 'text' : 'password'"
        validate-on-blur
        @click:append="showPassword = !showPassword"
      ></v-text-field>
      <v-text-field
        v-model="password2"
        label="Пароль ещё раз"
        :append-icon="showPassword2 ? 'mdi-eye' : 'mdi-eye-off'"
        :rules="[rules.required, rules.matchPassword]"
        :type="showPassword2 ? 'text' : 'password'"
        @click:append="showPassword2 = !showPassword2"
      ></v-text-field>
      <v-select
        :items="roles"
        v-model="role"
        item-text="name"
        item-value="id"
        label="Роль"
      >
        <template #append-outer>
          <v-tooltip bottom color="primary">
            <template v-slot:activator="{ on, attrs }">
              <v-icon v-bind="attrs" v-on="on">mdi-information-outline</v-icon>
            </template>
            <span>На основании выбранной роли подстроятся рекомендации.</span>
          </v-tooltip>
        </template>
      </v-select>
      <v-btn @click="register" :disabled="!valid" block color="primary"
        >Зарегистрироваться</v-btn
      >
    </v-form>
  </v-card>
</template>

<script lang="ts">
import { mapActions, mapState } from "vuex";
import { required, isEmail, passwordsMatches } from "@/validators";
import Vue from "vue";

export default Vue.extend({
  data() {
    return {
      email: "",
      password: "",
      password2: "",
      showPassword: false,
      showPassword2: false,
      role: "",
      valid: false,
    };
  },
  computed: {
    ...mapState(["isAuthenticated", "roles"]),
    rules() {
      return {
        matchPassword: (v: string) => passwordsMatches(this.password, v),
        required,
        isEmail,
      };
    },
  },
  methods: {
    ...mapActions({ registerDispatch: "register" }),
    ...mapActions(["getRoles"]),
    async register() {
      await this.registerDispatch({
        email: this.email,
        password: this.password,
        role: this.role,
      });
      this.$router.replace({ name: "Profile" });
    },
  },
  async beforeMount() {
    if (this.isAuthenticated) {
      this.$router.replace({ name: "News" });
    }
    if (!this.roles.length) await this.getRoles();
  },
});
</script>

<style>
.temp {
  width: 80px;
}
</style>