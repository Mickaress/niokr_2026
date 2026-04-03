import { CompanyType } from './Company';

export enum UserRole {
  CUSTOMER = 'customer',
  EMPLOYEE = 'employee',
  ADMIN = 'admin',
}

export interface SharedUserType {
  id: number;
  full_name: string;
  email: string;
  phone: string;
  role: UserRole;
}

export interface CustomerType extends SharedUserType {
  company: CompanyType;
}

export interface EmployeeType extends SharedUserType {
  tags: number[];
  competencies: string;
}

export interface AdminType extends SharedUserType {}

export interface UserFormType {
  full_name?: string;
  email?: string;
  phone?: string;
  company_name?: string;
  company_address?: string;
  company_description?: string;
  tags?: number[];
}
