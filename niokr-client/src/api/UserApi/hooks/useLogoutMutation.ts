import { useMutation } from '@tanstack/vue-query';
import { userApi } from '..';

export const useLogoutMutation = () => {
  return useMutation({
    mutationFn: () => userApi.logout(),
  });
};
