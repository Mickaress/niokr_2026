import { NavigationGuard } from 'vue-router';
import { RouteNames } from '../types/routeNames';
import { queryClient } from '@/api/queryClient';

export const requiresGuest: NavigationGuard = (to, _, next) => {
  const userData = queryClient.getQueryData(['user']);

  if (to.meta.requiresGuest && userData) {
    return next({
      name: RouteNames.USER_INFO,
    });
  }

  return next();
};
