import { FilterType } from '@/models/Filters';
import { useQuery } from '@tanstack/vue-query';
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { projectApi } from '..';
import { Status } from '@/models/Status';

export const useGetActiveProjectListQuery = () => {
  const route = useRoute();

  const filter = computed<FilterType>(() => {
    const name = route.query.name && typeof route.query.name === 'string' ? route.query.name : '';

    const tags = route.query.tags
      ? typeof route.query.tags === 'string'
        ? [Number(route.query.tags)]
        : route.query.tags.map((tag) => Number(tag))
      : [];

    const page =
      route.query.page && typeof route.query.page === 'string' ? Number(route.query.page) : 1;

    return {
      name,
      tags,
      status: Status.Active,
      page,
    };
  });

  return useQuery({
    queryKey: ['projects', filter],
    queryFn: () => projectApi.getFilteredProjectList(filter.value),
    refetchOnWindowFocus: false,
    refetchOnMount: true,
  });
};
