import { FilterType } from '@/models/Filters';
import { debounce } from 'lodash';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

export const useFilters = () => {
  const route = useRoute();
  const router = useRouter();

  const defaultFilters: FilterType = {
    title: '',
    tags: [],
    page: 1,
  };
  const filters = ref<FilterType>({ ...defaultFilters });

  if (route.query.title) {
    filters.value.title = route.query.title as string;
  }

  if (route.query.tags) {
    if (typeof route.query.tags === 'string') {
      filters.value.tags = [Number(route.query.tags)];
    } else {
      filters.value.tags = route.query.tags.map((tag) => Number(tag));
    }
  }

  if (route.query.page) {
    filters.value.page = Number(route.query.page);
  }

  function filter() {
    router.replace({
      ...route,
      query: {
        ...filters.value,
        page: 1,
      },
    });
  }

  function clearFilter() {
    filters.value = { ...defaultFilters };
    router.replace({ ...route, query: defaultFilters });
  }

  const debouncedInput = debounce(filter, 1000);

  return {
    filter,
    clearFilter,
    filters,
    debouncedInput,
  };
};
