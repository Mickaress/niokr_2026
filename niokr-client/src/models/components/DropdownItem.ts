import { RouteLocationRaw } from 'vue-router';

export type DropdownItem =
  | {
      content: string;
      type: 'link';
      href?: string;
      location?: RouteLocationRaw;
    }
  | { content: string; type: 'button'; action: () => void };
