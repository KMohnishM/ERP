import { useQuery } from '@tanstack/react-query';
import apiClient from '../api-client';

export const useEmployees = () => {
  return useQuery({
    queryKey: ['employees'],
    queryFn: async () => {
      const { data } = await apiClient.get('/hrms/employees/');
      return data;
    },
  });
};

