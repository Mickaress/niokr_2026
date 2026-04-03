import { queryClient } from '@/api/queryClient';
import { UserRole } from '@/models/User';
import { NavigationGuard } from 'vue-router';
import { RouteNames } from '../types/routeNames';

type UserData = { role: UserRole };

export const checkUserRole: NavigationGuard = (to, _, next) => {
  const roles = to.meta.roles;

  if (!roles) {
    return next();
  }

  const userData = queryClient.getQueryData<UserData>(['user']);
  const userRole = userData?.role;

  if (userRole && roles.includes(userRole)) {
    return next();
  }

  return next({
    name: userRole ? RouteNames.NOT_FOUND : RouteNames.LOGIN,
  });
};
