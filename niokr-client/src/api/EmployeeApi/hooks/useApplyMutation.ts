import { useMutation, useQueryClient } from '@tanstack/vue-query';
import { toast } from 'vue3-toastify';
import { employeeApi } from '..';

export const useApplyMutation = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (projectId: number) => employeeApi.apply(projectId),
    onMutate: () => {
      const toastId = toast.loading('Обработка запроса');

      return { toastId };
    },
    onSuccess: async (_, __, context) => {
      await queryClient.invalidateQueries();

      toast.remove(context?.toastId);
      toast.success('Вы откликнулись на проект');
    },
    onError: (_, __, context) => {
      toast.remove(context?.toastId);
      toast.error('Ошибка сервера');
    },
  });
};
