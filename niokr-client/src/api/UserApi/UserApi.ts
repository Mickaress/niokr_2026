import { AdminType, CustomerType, EmployeeType, UserFormType } from '@/models/User';
import { axiosInstance } from '../axiosInstance';
import UserApiType from './UserApiType';
import { askForUserRole } from './utils/mockCookie';

export default class UserApi implements UserApiType {
  async auth(): Promise<void> {
    const external_id = askForUserRole();

    if (!external_id) return;

    await axiosInstance.post('login', {
      external_id: external_id,
    });

    window.location.reload();
  }

  async logout(): Promise<void> {
    await axiosInstance.post('logout');

    window.location.reload();
  }

  async getUserInfo(): Promise<CustomerType | EmployeeType | AdminType | null> {
    try {
      const response = await axiosInstance.get('me');

      return response.data;
    } catch (error) {
      return null;
    }
  }

  async updateUserInfo(userInfo: UserFormType): Promise<void> {
    await axiosInstance.patch('me', userInfo);
  }
}
