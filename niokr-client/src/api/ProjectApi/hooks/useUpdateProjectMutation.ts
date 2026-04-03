import { useMutation, useQueryClient } from '@tanstack/vue-query';
import { toast } from 'vue3-toastify';
import { projectApi } from '..';
import { ProjectFormType, ProjectType } from '@/models/Project';

export const useUpdateProjectMutation = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, data }: { id: number; data: Partial<ProjectType> | ProjectFormType }) =>
      projectApi.updateProject(id, data),
    onMutate: () => {
      const toastId = toast.loading('Обработка запроса');

      return { toastId };
    },
    onSuccess: async (_, __, context) => {
      await queryClient.invalidateQueries();

      toast.remove(context?.toastId);
      toast.success('Проект обновлен');
    },
    onError: (_, __, context) => {
      toast.remove(context?.toastId);
      toast.error('Ошибка сервера');
    },
  });
};
