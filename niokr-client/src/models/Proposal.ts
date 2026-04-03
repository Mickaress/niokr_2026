import { ProjectType } from './Project';
import { StatusType } from './Status';
import { EmployeeType } from './User';

export const enum FilterProposalsBy {
  Review = 'review',
  Approved = 'approved',
  Rejected = 'rejected',
}

export type ResponseType = {
  id: number;
  employee: EmployeeType;
  project: ProjectType;
  date: string;
  comment: string;
};

export type ResponseListType = {
  responses: ResponseType[];
  quantity: number;
};

export type SkillOfferType = {
  id: number;
  status: StatusType;
  name: string;
};

export type SkillOfferListType = {
  skills: SkillOfferType[];
  quantity: number;
};

export type VacancyOfferListType = {
  vacancies: ProjectType[];
  quantity: number;
};
