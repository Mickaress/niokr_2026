import { queryClient } from '@/api/queryClient';
import { userApi } from '@/api/UserApi';
import { NavigationGuard } from 'vue-router';

export const fetchUserData: NavigationGuard = async (_, from, next) => {
  if (!from.name) {
    await queryClient.fetchQuery({
      queryKey: ['user'],
      queryFn: () => userApi.getUserInfo(),
      staleTime: Infinity,
    });
  }

  return next();
};
