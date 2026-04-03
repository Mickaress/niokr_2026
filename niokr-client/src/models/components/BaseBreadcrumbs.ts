import { RouteLocationRaw } from 'vue-router';

export type Breadcrumb = {
  to?: RouteLocationRaw;
  title: string;
};
