import { FilterType } from '@/models/Filters';
import { useQuery } from '@tanstack/vue-query';
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { projectApi } from '..';
import { Status } from '@/models/Status';

export const useGetAppliedProjectListQuery = () => {
  const route = useRoute();

  const filter = computed<FilterType>(() => {
    const page =
      route.query.page && typeof route.query.page === 'string' ? Number(route.query.page) : 1;

    return {
      status: Status.Active,
      is_applied: true,
      page,
    };
  });

  return useQuery({
    queryKey: ['applied_projects', filter],
    queryFn: () => projectApi.getFilteredProjectList(filter.value),
    refetchOnWindowFocus: false,
    refetchOnMount: true,
  });
};
