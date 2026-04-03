import { FilterType } from '@/models/Filters';
import { useCheckRole } from '@/hooks/useCheckRole';
import { Status } from '@/models/Status';
import { UserRole } from '@/models/User';
import { useQuery } from '@tanstack/vue-query';
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { projectApi } from '..';

export const useGetUserProjectListQuery = () => {
  const route = useRoute();
  const isEmployee = useCheckRole([UserRole.EMPLOYEE]);

  const filter = computed<FilterType>(() => {
    const status =
      route.query.status && typeof route.query.status === 'string'
        ? (route.query.status as Status)
        : Status.Active;

    const page =
      route.query.page && typeof route.query.page === 'string' ? Number(route.query.page) : 1;

    return {
      status: isEmployee ? Status.Archived : status,
      page,
    };
  });

  return useQuery({
    queryKey: ['user_projects', filter],
    queryFn: () => projectApi.getFilteredProjectList(filter.value),
    refetchOnWindowFocus: false,
    refetchOnMount: true,
  });
};
