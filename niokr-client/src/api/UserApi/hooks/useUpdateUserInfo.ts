import { useMutation, useQueryClient } from '@tanstack/vue-query';
import { userApi } from '..';
import { toast } from 'vue3-toastify';
import { RouteNames } from '@/router/types/routeNames';
import { useRouter } from 'vue-router';
import { UserFormType } from '@/models/User';

export const useUpdateUserInfo = () => {
  const queryClient = useQueryClient();
  const router = useRouter();

  return useMutation({
    mutationFn: (userInfo: UserFormType) => userApi.updateUserInfo(userInfo),
    onMutate: () => {
      const toastId = toast.loading('Обработка запроса');

      return { toastId };
    },
    onSuccess: async (_, __, context) => {
      await queryClient.invalidateQueries();

      toast.remove(context?.toastId);
      toast.success('Информация обновлена');

      router.replace({ name: RouteNames.USER_INFO });
    },
    onError: (_, __, context) => {
      toast.remove(context?.toastId);
      toast.error('Ошибка сервера');
    },
  });
};
