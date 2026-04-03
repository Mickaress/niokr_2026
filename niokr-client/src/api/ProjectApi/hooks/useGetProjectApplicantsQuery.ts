import { useQuery } from '@tanstack/vue-query';
import { computed, type Ref, unref } from 'vue';
import { projectApi } from '..';

export const useGetProjectApplicantsQuery = (
  id: Ref<number | null>,
  isOpen: Ref<boolean>,
  isAdmin: boolean | Ref<boolean>,
) => {
  return useQuery({
    queryKey: ['project_applicants', id],
    queryFn: () => projectApi.getProjectApplicants(id.value!),
    enabled: computed(() => unref(isAdmin) && isOpen.value && id.value !== null),
  });
};
