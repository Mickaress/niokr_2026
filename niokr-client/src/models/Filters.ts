import { Status } from './Status';

export type FilterType = {
  name?: string;
  tags?: number[];
  status?: Status;
  is_applied?: boolean;
  page: number;
};

export type TagType = {
  id: number;
  name: string;
};
