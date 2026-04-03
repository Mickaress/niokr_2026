import { axiosInstance } from '../axiosInstance';
import EmployeeApiType from './EmployeeApi.interface';

export default class EmployeeApi implements EmployeeApiType {
  async apply(projectId: number): Promise<void> {
    await axiosInstance.post(`project/${projectId}/apply`);
  }

  async withdraw(projectId: number): Promise<void> {
    await axiosInstance.delete(`project/${projectId}/apply`);
  }
}
