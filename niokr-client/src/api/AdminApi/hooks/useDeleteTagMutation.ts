import { useMutation } from '@tanstack/vue-query';
import { toast } from 'vue3-toastify';
import { adminApi } from '..';

export const useDeleteTagMutation = () => {
  return useMutation({
    mutationFn: (id: number) => adminApi.deleteTag(id),
    onMutate: () => {
      const toastId = toast.loading('Обработка запроса');
      return { toastId };
    },
    onSuccess: async (_, __, context) => {
      toast.remove(context?.toastId);
      toast.success('Тег удален');
    },
    onError: (_, __, context) => {
      toast.remove(context?.toastId);
      toast.error('Ошибка сервера');
    },
  });
};
