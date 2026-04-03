import { useRouter } from 'vue-router';
import { useCheckRole } from './useCheckRole';
import { NavType } from '@/router/types/navTypes';

export const useMainNavigationRoutes = () => {
  const router = useRouter();

  return router
    .getRoutes()
    .filter((route) => route.meta.type === NavType.MAIN_NAV && useCheckRole(route.meta.roles))
    .sort((a, b) => (a.meta.order || 0) - (b.meta.order || 0));
};

export const useUserNavigationRoutes = () => {
  const router = useRouter();

  return router
    .getRoutes()
    .filter((route) => {
      return route.meta.type === NavType.USER_NAV && useCheckRole(route.meta.roles);
    })
    .sort((a, b) => (a.meta.order || 0) - (b.meta.order || 0));
};
