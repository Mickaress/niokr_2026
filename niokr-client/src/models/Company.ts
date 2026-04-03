import { CustomerType } from './User';

export type CompanyType = {
  name: string;
  address: string;
  description: string;
  customer: Pick<CustomerType, 'full_name' | 'email' | 'phone'>;
};
