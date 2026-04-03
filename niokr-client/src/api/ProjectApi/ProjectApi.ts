import type { FilterType } from '@/models/Filters';
import type { ListDTO, ProjectFormType, ProjectType } from '@/models/Project';
import { axiosInstance } from '../axiosInstance';
import type ProjectApiType from './ProjectApiType';
import { SharedUserType } from '@/models/User';

export default class ProjectApi implements ProjectApiType {
  async getFilteredProjectList(filters: FilterType): Promise<ListDTO<ProjectType>> {
    const response = await axiosInstance.get('projects', {
      params: filters,
    });

    return response.data;
  }

  async getSingleProject(id: number): Promise<ProjectType> {
    const response = await axiosInstance.get(`project/${id}`);

    return response.data;
  }

  async getProjectApplicants(id: number): Promise<Pick<SharedUserType, 'id' | 'full_name'>> {
    const response = await axiosInstance.get(`project/${id}/applicants`);

    return response.data;
  }

  async updateProject(id: number, data: Partial<ProjectType> | ProjectFormType): Promise<void> {
    await axiosInstance.patch(`project/${id}`, data);
  }
}
