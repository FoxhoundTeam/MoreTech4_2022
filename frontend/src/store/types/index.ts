export interface InterestingTheme {
  id: number;
  name: string;
}

export interface User {
  id: number;
  email: string;
  keywords: string[];
  relevantDigestsCount: number;
  interestingThemes: InterestingTheme[];
}

export interface News {
  id: number;
  url: string;
  title: string;
  date: string;
  urlPreview?: string;
}

export interface Trend {
  id: number;
  title: string;
  topic: string[];
  date: string;
  favorite: boolean;
  news: News[];
}

export interface Digest {
  id: number;
  title: string;
  topic: string[];
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
