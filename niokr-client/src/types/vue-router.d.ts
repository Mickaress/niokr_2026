import 'vue-router';
import { UserRole } from '@/models/User';
import { NavType } from '@/router/types/navTypes';

declare module 'vue-router' {
  interface RouteMeta {
    title?: string;
    roles?: UserRole[];
    type?: NavType;
    order?: number;
    requiresGuest?: boolean;
  }
}
