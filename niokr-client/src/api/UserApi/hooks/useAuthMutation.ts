import { useMutation } from '@tanstack/vue-query';
import { userApi } from '..';

export const useAuthMutation = () => {
  return useMutation({
    mutationFn: () => userApi.auth(),
  });
};
