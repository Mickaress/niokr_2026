import { ProjectFormType } from '@/models/Project';
import { RouteNames } from '@/router/types/routeNames';
import { useMutation } from '@tanstack/vue-query';
import { useRouter } from 'vue-router';
import { toast } from 'vue3-toastify';
import { customerApi } from '..';

export const useCreateProjectMutation = () => {
  const router = useRouter();

  return useMutation({
    mutationFn: (projectData: ProjectFormType) => customerApi.createProject(projectData),
    onMutate: () => {
      const toastId = toast.loading('Обработка запроса');
      return { toastId };
    },
    onSuccess: async (_, __, context) => {
      router.replace({
        name: RouteNames.USER_PROJECTS,
      });

      toast.remove(context?.toastId);
      toast.success('Проект создан');
    },
    onError: (_, __, context) => {
      toast.remove(context?.toastId);
      toast.error('Ошибка сервера');
    },
  });
};
