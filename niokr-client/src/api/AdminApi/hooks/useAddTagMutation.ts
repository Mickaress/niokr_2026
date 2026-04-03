import { useMutation } from '@tanstack/vue-query';
import { toast } from 'vue3-toastify';
import { adminApi } from '..';

export const useAddTagMutation = () => {
  return useMutation({
    mutationFn: (name: string) => adminApi.addTag(name),
    onMutate: () => {
      const toastId = toast.loading('Обработка запроса');
      return { toastId };
    },
    onSuccess: async (_, __, context) => {
      toast.remove(context?.toastId);
      toast.success('Тег добавлен');
    },
    onError: (_, __, context) => {
      toast.remove(context?.toastId);
      toast.error('Ошибка сервера');
    },
  });
};
