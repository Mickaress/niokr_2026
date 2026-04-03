import { axiosInstance } from '../axiosInstance';
import AdminApiType from './AdminApiType';

export default class AdminApi implements AdminApiType {
  async addTag(name: string): Promise<void> {
    await axiosInstance.post(`tags`, { name });
  }

  async deleteTag(id: number): Promise<void> {
    await axiosInstance.delete(`tag/${id}`);
  }
}
