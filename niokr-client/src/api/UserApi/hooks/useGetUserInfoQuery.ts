import { useQuery } from '@tanstack/vue-query';
import { userApi } from '..';

export const useGetUserInfoQuery = () => {
  return useQuery({
    queryKey: ['user'],
    queryFn: () => userApi.getUserInfo(),
    refetchOnWindowFocus: false,
    refetchOnMount: false,
    staleTime: Infinity,
  });
};
