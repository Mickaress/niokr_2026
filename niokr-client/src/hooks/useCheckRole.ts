import { queryClient } from '@/api/queryClient';
import { UserRole } from '@/models/User';

type RoleType = {
  role: UserRole;
};

export const useCheckRole = (roles: UserRole[] = []): boolean => {
  const userData = queryClient.getQueryData<RoleType>(['user']);
  const userRole = userData?.role;

  if (userRole && roles.includes(userRole)) {
    return true;
  }
  return false;
};
