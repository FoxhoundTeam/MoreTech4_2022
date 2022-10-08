export interface InterestingTrend {
  id: number;
  name: string;
}

export interface User {
  id: number;
  email: string;
  keywords: string[];
  relevantTrendsCount: number;
  interestingTrends: InterestingTrend[];
}

export interface News {
  id: number;
  link: string;
  header: string;
  siteName: string;
  imageLink?: string;
}

export interface Trend {
  id: number;
  name: string;
  favorite: boolean;
  news: News[];
}

export type LoginData = {
  email: string;
  password: string;
};

export type RegisterData = {
  role: string | null;
  password2: string;
} & LoginData;

export type ChangeUserPasswordData = {
  password: string;
  password2: string;
};

export type TErrorModalContent = string | string[] | null;
export type TSnackbarColor = "warning" | "success" | "primary" | "red" | null;
export interface IShowSnackbar {
  text: string;
  color: TSnackbarColor;
}
export interface ILoginResponse {
  accessToken: string;
}

export type PaginatedResponse<T> = {
  page: number;
  items: T[];
  next?: boolean;
  total: number;
  size: number;
};

export interface Role {
  id: number | null;
  name: string;
}
