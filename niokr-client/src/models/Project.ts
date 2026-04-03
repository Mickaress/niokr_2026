import { CompanyType } from './Company';
import { Status } from './Status';

export type ProjectFileType = {
  id: number;
  file: string;
  original_filename?: string;
  uploaded_at: string;
};

export interface ProjectType {
  id: number;
  name: string;
  description: string;
  period: string;
  tags: number[];
  status: Status;
  payment: boolean;
  views: number;
  skills: number[];
  company: CompanyType;
  is_applied: boolean;
  created_at: string;
  applications_count: number;
  files?: ProjectFileType[];
  employee_id?: number | null;
}

export interface ListDTO<T> {
  count: number;
  results: T[];
}

export interface ProjectFormType {
  name: string;
  description?: string;
  dateStart?: string;
  dateEnd?: string;
  tagIds: number[];
  files?: File[];
}
