import { ProjectFormType } from '@/models/Project';
import CustomerApiType from './CustomerApiType';
import { axiosInstance } from '../axiosInstance';

export default class CustomerApi implements CustomerApiType {
  async createProject(data: ProjectFormType): Promise<void> {
    const formData = new FormData();

    formData.append('name', data.name);
    if (data.description) formData.append('description', data.description);
    if (data.dateStart) formData.append('dateStart', data.dateStart);
    if (data.dateEnd) formData.append('dateEnd', data.dateEnd);
    if (data.tagIds) formData.append('tagIds', JSON.stringify(data.tagIds));
    data.files?.forEach((file) => formData.append('files', file));

    const response = await axiosInstance.post('projects', formData);

    return response.data;
  }
}
