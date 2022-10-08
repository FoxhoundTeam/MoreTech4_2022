import Vuex from "vuex";
import http from "../http";
import Vue from "vue";
import {
  LoginData,
  User,
  TErrorModalContent,
  TSnackbarColor,
  IShowSnackbar,
  ILoginResponse,
  RegisterData,
  Trend,
  InterestingTrend,
  ChangeUserPasswordData,
  PaginatedResponse,
  Role,
} from "./types";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    user: null as User | null,
    isAuthenticated: false,
    showErrorModal: false,
    errorModalContent: null as TErrorModalContent,
    snackbarColor: null as TSnackbarColor,
    showSnackbar: false,
    snackbarText: null as string | null,
    relevantTrends: [] as Trend[],
    trends: {
      page: 0,
      items: [] as Trend[],
      next: false,
    } as PaginatedResponse<Trend>,
    loadingTrends: false,
    loadingFavoriteTrends: false,
    loadingRelevantTrends: false,
    favoriteTrends: {
      page: 0,
      items: [] as Trend[],
      next: false,
    } as PaginatedResponse<Trend>,
    interestingTrends: [] as InterestingTrend[],
    roles: [] as Role[],
    settingFavoriteTrendFor: [] as number[],
  },
  getters: {},
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setAuthenticated(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
    },
    showErrorModal(state, content: TErrorModalContent) {
      state.errorModalContent = content;
      state.showErrorModal = true;
    },
    setShowErrorModal(state, value: boolean) {
      state.showErrorModal = value;
    },
    showSnackbar(state, content: IShowSnackbar) {
      state.snackbarColor = content.color || "success";
      state.snackbarText = content.text;
      state.showSnackbar = true;
    },
    setShowSnackbar(state, value: boolean) {
      state.showSnackbar = value;
    },
    setTrends(state, trends: PaginatedResponse<Trend>) {
      trends.next = trends.page * trends.size < trends.total;
      if (trends.page == 1) state.trends = trends;
      else {
        state.trends = {
          ...trends,
          items: [...state.trends.items, ...trends.items],
        };
      }
    },
    setFavoriteTrends(state, trends: PaginatedResponse<Trend>) {
      trends.next = trends.page * trends.size < trends.total;
      if (trends.page == 1) state.favoriteTrends = trends;
      else {
        state.favoriteTrends = {
          ...trends,
          items: [...state.favoriteTrends.items, ...trends.items],
        };
      }
    },
    setInterestingTrends(state, interestingTrends: InterestingTrend[]) {
      state.interestingTrends = interestingTrends;
    },
    setRelevantTrends(state, trends: Trend[]) {
      state.relevantTrends = trends;
    },
    setLoadingTrends(state, value: boolean) {
      state.loadingTrends = value;
    },
    setLoadingFavoriteTrends(state, value: boolean) {
      state.loadingFavoriteTrends = value;
    },
    setLoadingRelevantTrends(state, value: boolean) {
      state.loadingRelevantTrends = value;
    },
    setRoles(state, roles: Role[]) {
      state.roles = [{ id: null, name: "Без роли" }, ...roles];
    },
    setSettingFavoriteTrendFor(state, value: number[]) {
      state.settingFavoriteTrendFor = value;
    },
  },
  actions: {
    async updateUserInfo(context, userData: User) {
      const response = await http.partialUpdateItem<User>("User", {
        data: userData,
        showSnackbar: true,
      });
      if (response.status != 200) return;
      context.commit("setUser", response.data);
      context.commit("showSnackbar", {
        text: "Данные успешно сохранены",
      } as IShowSnackbar);
    },
    async changeUserPassword(context, content: ChangeUserPasswordData) {
      const response = await http.createItem("ChangePassword", {
        data: content,
        showSnackbar: true,
      });
      if (response.status != 200) return;
      context.commit("showSnackbar", {
        text: "Пароль успешно изменен",
      } as IShowSnackbar);
    },
    async getInterestingTrends(context) {
      const response = await http.getList<InterestingTrend[]>(
        "InterestingTrend",
        { showSnackbar: true }
      );
      context.commit("setInterestingTrends", response.data);
    },
    async getTrends(context, options?: { page?: number }) {
      const requestPage = options?.page
        ? options?.page
        : context.state.trends.page + 1;
      context.commit("setLoadingTrends", true);
      const response = await http.getList("Trend", {
        filters: {
          page: requestPage,
          exclude_ids: context.state.relevantTrends.map((v) => v.id).join(","),
          size: 10,
        },
        showSnackbar: true,
      });
      if (response.status == 200) context.commit("setTrends", response.data);
      context.commit("setLoadingTrends", false);
    },
    async getRelevantTrends(context) {
      context.commit("setLoadingRelevantTrends", true);
      const response = await http.getList<Trend[]>("RelevantTrend", {
        showSnackbar: true,
      });
      context.commit("setLoadingRelevantTrends", false);
      if (response.status != 200) return;
      context.commit("setRelevantTrends", response.data);
      await context.dispatch("getTrends", { page: 1 });
    },
    async getFavoriteTrends(context, options?: { page?: number }) {
      const requestPage = options?.page
        ? options?.page
        : context.state.favoriteTrends.page + 1;
      context.commit("setLoadingFavoriteTrends", true);
      const response = await http.getList("Trend", {
        filters: {
          page: requestPage,
          favorite: true,
          size: 10,
        },
        showSnackbar: true,
      });
      if (response.status == 200)
        context.commit("setFavoriteTrends", response.data);
      context.commit("setLoadingFavoriteTrends", false);
    },
    async getRoles(context) {
      const response = await http.getList<Role[]>("Role", {
        showSnackbar: true,
      });
      if (response.status == 200) context.commit("setRoles", response.data);
    },
    async setFavoriteTrend(context, id: number): Promise<boolean> {
      context.commit("setSettingFavoriteTrendFor", [
        ...context.state.settingFavoriteTrendFor,
        id,
      ]);
      const response = await http.createItem(`/api/trend/${id}/favorite/`, {
        showSnackbar: true,
      });
      const settingFavoriteTrendFor = [
        ...context.state.settingFavoriteTrendFor,
      ];
      settingFavoriteTrendFor.splice(
        settingFavoriteTrendFor.findIndex((v) => v == id),
        1
      );
      context.commit("setSettingFavoriteTrendFor", settingFavoriteTrendFor);
      return response.status == 200;
    },
    async login(context, credentials: LoginData) {
      const response = await http.createItem<ILoginResponse>("Login", {
        data: credentials,
        showSnackbar: true,
      });
      if (response.status == 200) {
        localStorage.setItem("accessToken", response.data.accessToken);
      }
      await context.dispatch("checkAuth");
    },
    async logout(context) {
      localStorage.removeItem("accessToken");
      context.commit("setAuthenticated", false);
      context.commit("setUser", {});
    },
    async register(context, credentials: RegisterData) {
      const response = await http.createItem<ILoginResponse>("Register", {
        data: credentials,
        showSnackbar: true,
      });
      if (response.status == 200) {
        localStorage.setItem("accessToken", response.data.accessToken);
      }
      await context.dispatch("checkAuth");
    },
    async checkAuth(context) {
      const result = await http.getItem<User>("User");
      if (result.status != 200) {
        context.commit("setUser", {});
      } else {
        context.commit("setAuthenticated", true);
        context.commit("setUser", result.data);
      }
    },
  },
});

export default store;
