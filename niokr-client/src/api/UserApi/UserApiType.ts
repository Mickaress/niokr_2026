import { AdminType, CustomerType, EmployeeType } from '@/models/User';

export default interface UserApiType {
  auth(): Promise<void>;
  logout(): Promise<void>;
  getUserInfo(): Promise<CustomerType | EmployeeType | AdminType | null>;
  updateUserInfo(userInfo: Partial<CustomerType | EmployeeType | AdminType>): Promise<void>;
}
