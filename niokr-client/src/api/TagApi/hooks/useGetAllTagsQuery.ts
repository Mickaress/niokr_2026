import { useQuery } from '@tanstack/vue-query';
import { tagApi } from '..';
import { useRoute } from 'vue-router';
import { computed } from 'vue';
import { FilterType } from '@/models/Filters';

export const useGetAllTagsQuery = (isFilter = false) => {
  const route = useRoute();

  const filter = computed<Pick<FilterType, 'page'>>(() => {
    const page =
      route.query.page && typeof route.query.page === 'string' ? Number(route.query.page) : 1;

    return {
      page,
    };
  });

  return useQuery({
    queryKey: ['tags', filter],
    queryFn: () => tagApi.getAllTags(isFilter ? filter.value : undefined),
    refetchOnWindowFocus: false,
    refetchOnMount: true,
  });
};
