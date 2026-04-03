import { useQuery } from '@tanstack/vue-query';
import { projectApi } from '..';

export const useGetSingleProjectQuery = (id: number) => {
  return useQuery({
    queryKey: ['project', id],
    queryFn: () => projectApi.getSingleProject(id),
    refetchOnWindowFocus: false,
    refetchOnMount: true,
  });
};
